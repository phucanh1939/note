---
title: Texture Mapping
---

# Texture Mapping

## What is Texture Mapping

**Texture mapping** is the process of applying a 2D image (texture) onto a 3D surface to add visual detail without increasing geometric complexity.

Instead of modeling every small detail with geometry, detail is stored in textures and sampled during rendering.

---

## Position in the Graphics Pipeline

To understand texture mapping, it helps to see **when and how textures are actually used** during rendering.

Let’s walk through the pipeline step by step, following the data as it flows through the GPU.

1. **Model Data**

   A 3D model is made of vertices. Each vertex does not only store its position, but also extra information needed for shading:

   * Position `(x, y, z)` defines the shape
   * Normal defines surface orientation
   * Texture coordinates `(u, v)` define *where on the texture this vertex maps to*

2. **Vertex Shader**

   The vertex shader processes vertices one by one.

   * It transforms vertex positions from model space to clip space
   * It does **not** sample textures
   * Texture coordinates `(u, v)` are simply passed forward to the next stage

3. **Rasterization**

   Rasterization converts triangles into screen-space fragments.

   * For each fragment, `(u, v)` values are **interpolated** from the triangle’s vertices
   * At this point, every screen pixel has its own texture coordinate

4. **Fragment Shader**

   This is where texture mapping actually happens.

   * The fragment shader uses `(u, v)` to sample the texture
   * The sampled value contributes to the final pixel color

At the end of this stage, the GPU knows what color each pixel on the screen should be.

---

## UV Mapping

Before a texture can be sampled, we must answer a simple question:

> For a given point on a 3D surface, **which part of the 2D image should be used?**

This is exactly what **UV mapping** solves.

Each vertex stores a pair of texture coordinates:

* `u ∈ [0,1]` represents the horizontal axis of the texture
* `v ∈ [0,1]` represents the vertical axis

Think of UVs as *instructions* that tell the GPU how to "wrap" a flat image around a 3D shape.

During rasterization, the GPU interpolates `(u, v)` across the triangle. As a result, every fragment knows **where it lies on the texture**, even though the texture itself is only 2D.

---

## Filters — Which Texture Value to Use for a Screen Pixel

Once UV mapping is done, every fragment has an `(u, v)` coordinate. However, this raises another problem.

Textures are made of **discrete texels**, but `(u, v)` is **continuous**. Most of the time, `(u, v)` does not land exactly on the center of a texel.

So the GPU must decide:

> Given this `(u, v)`, **which texel value should we use?**

This decision process is called **texture filtering**.

A filter defines:

* Which texels are sampled
* How their values are combined to produce the final color

Different filters trade visual quality for performance, and each solves a different class of problems.

---

### Nearest Neighbor Sampling

The simplest possible filter is **nearest neighbor sampling**.

The idea is straightforward:

* Find the texel closest to `(u, v)`
* Use its value directly

There is no averaging and no smoothing.

**Pros**

* Extremely fast
* Preserves sharp pixel edges (useful for pixel art)

**Cons**

* Produces blocky results
* Causes strong shimmering when objects move

---

### Bilinear Filtering

Nearest neighbor sampling is fast, but often too harsh. A natural improvement is **bilinear filtering**.

Instead of choosing a single texel, bilinear filtering:

* Samples the four texels surrounding `(u, v)`
* Linearly interpolates between them

This smooths out hard transitions between texels.

**Pros**

* Visually smoother than nearest neighbor
* Still relatively cheap

**Cons**

* Blurs fine details
* Does not fully solve aliasing, especially at distance

---

## Mipmapping

Texture aliasing often occurs when a single screen pixel covers **many texels** (e.g. when the object is far from the camera).

If we sample only the texel at the center of the pixel, we effectively pick a **random representative value** from a large texture region, which causes aliasing and shimmering.

The ideal solution is to sample the **average value** of all texels covered by the pixel, but computing this at runtime is too expensive.

### Key Idea

Instead of computing averages at runtime:

* Precompute them once
* Store them in advance
* Look them up during rendering

Since we cannot precompute averages for every possible size, we approximate by generating textures at progressively lower resolutions:

```
128×128 → 64×64 → 32×32 → … → 1×1
```

These precomputed textures are called **mipmaps**.

> **Mipmapping** = precomputed lower-resolution versions of a texture.

---

### Mipmap Level Selection (LOD)

At runtime, for each fragment with texture coordinates `(u, v)`, the GPU selects the mipmap level that best matches the **screen-space size** of the texture footprint.

This process is called **Level-of-Detail (LOD) selection**.

**How LOD is chosen**

The GPU estimates how fast `(u, v)` changes across neighboring screen pixels using screen-space derivatives:

* `∂u/∂x`, `∂u/∂y`
* `∂v/∂x`, `∂v/∂y`

From these values, it estimates how many texels are covered by one screen pixel.

The resulting value is the **mipmap level** `λ` (lambda).

**Pros**

* Reduces aliasing
* Faster texture sampling
* More stable visuals

**Cons**

* Extra memory usage (~33%)
* Can appear blurry

---

## Trilinear Filtering

**Trilinear filtering** combines:

* **Bilinear filtering** within each mip level
* **Linear interpolation between two adjacent mip levels**

Instead of sampling from a single mipmap level, the GPU blends samples from **two mip levels** based on the computed LOD.

---

### Why Mipmapping Alone Is Not Enough

With basic mipmapping:

* Each fragment samples **only one mip level**
* When LOD crosses a boundary, the selected mip level changes abruptly

This causes:

* Visible banding
* Mipmap **popping** when the camera moves
* Sudden changes in sharpness

---

### What Trilinear Filtering Fixes

Trilinear filtering:

* Smoothly blends between mip levels `L` and `L + 1`
* Removes hard transitions
* Produces continuous detail change with distance

Result:

* Stable visuals
* No visible mip boundaries

---

### Cost and Limitations

**Pros**

* Smooth mip transitions
* Eliminates mipmap popping
* Common default in modern engines

**Cons**

* Samples from two mip levels
* Slightly higher memory bandwidth and shader cost

**Limitations**

* Does not handle steep viewing angles well → **Anisotropic filtering** is required

> **Summary:** Mipmapping reduces aliasing; **trilinear filtering removes mip-level popping**.

---

## Anisotropic Filtering

Improves texture quality when surfaces are viewed at steep angles.

**Pros**

* Very sharp results
* Ideal for floors, roads, and ground surfaces

**Cons**

* Higher GPU cost
* Limited by hardware capabilities

---

## Special-Purpose Texture Maps

Texture mapping is not limited to color.

Common maps:

* **Albedo** – base color
* **Normal Map** – surface detail illusion
* **Roughness** – micro-surface control
* **Metallic** – material behavior
* **Ambient Occlusion** – local shadowing
* **Height / Parallax** – depth illusion

**Trade-offs**

* Higher realism
* Increased memory usage
* More texture fetches

---

## Performance Challenges and Trade-offs

### Memory vs Quality

* Higher resolution improves clarity
* Increases VRAM usage

### Bandwidth vs Speed

* Many texture reads slow shaders
* Cache locality matters

### Flexibility vs Simplicity

* Atlases are fast but fragile
* Arrays are clean but rigid

### Quality vs Cost

* Advanced filtering improves visuals
* Increases GPU workload

---

## Key Takeaways

* Texture mapping is fundamentally a **sampling problem**

  * `(u, v)` is continuous
  * Texels are discrete
  * One screen pixel ≠ one texel
* UVs define **where** to sample
* Filtering defines **how** to sample
* Mipmapping is essential for stability
* Advanced techniques trade performance for quality
* Real engines combine multiple approaches

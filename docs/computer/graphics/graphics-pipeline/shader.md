---
title: Shader
---

# Shaders in the Graphics Pipeline

## What Is a Shader?

A **shader** is a small program that runs on the **GPU**.

Its job is simple:

* Take some input data
* Perform calculations
* Output transformed data or colors

In the graphics pipeline, shaders are the **programmable stages**.
Everything else in the pipeline is mostly fixed-function.

You can think of shaders as:

> “Custom logic you plug into specific points of the pipeline.”

---

## Why Shaders Exist

Early graphics pipelines were fully fixed:

* No custom lighting
* No special effects
* Very limited visuals

Shaders were introduced to let developers:

* Control how geometry is transformed
* Control how pixels are colored
* Create unique visual styles and effects

Almost all modern visual quality in games comes from shaders.

---

## Main Types of Shaders (Game-Focused)

In practice, games mostly care about **three core shader stages**.

---

## 1. Vertex Shader

### Where is it in the Pipeline

* It is the Vertex Processing stage itself - apply transformation to convert vertex from object space to clip space

### What It Operates On

* **One vertex at a time**

### What It Usually Does

* Transform vertex positions:

  * Object space → World → View → Clip space
* Pass data forward:

  * Normals
  * UVs
  * Colors

### Important Note

* The **vertex shader is where the world/view/projection transforms are actually applied** ()
* In modern engines (Unity, Godot, Unreal), these transforms are **usually handled automatically by the engine’s built-in vertex shader**, so you rarely write this yourself unless creating custom effects.

### Simple Game Example

**Moving a 3D character**

* Engine’s vertex shader applies model + view + projection matrices automatically
* Character moves and rotates correctly in the world
* Custom vertex shaders may modify these transforms for special effects (e.g., waving flags)


## 2. Fragment Shader (Pixel Shader) (Customizable)

### Where is it in the Pipeline

* It is the Fragment Processing stage itself - sample texture on the fragment, apply lighting or material logic

### What It Operates On

* **One fragment at a time**
* Interpolated data from vertices (UVs, normals, colors)

### What It Usually Does

* Sample textures (using UVs)
* Apply lighting calculations
* Decide the final pixel color
* Can include custom effects written by the developer (e.g., tint, outline, glow)

### Override Note

When writing your own fragment shader:

* The engine does not automatically run its default fragment shader.
* You must manually sample textures and calculate the final color if you want to preserve the base look.
* Your shader code completely controls the pixel output, so you can add effects after sampling the base color.
* To achieve lighting, outlines, or other effects, you need to **understand the math behind these effects** and implement it in the shader.

### Example: Simple Diffuse Lighting in Fragment Shader

```glsl
// Inputs from vertex shader
in vec3 v_normal;
in vec2 v_uv;
uniform sampler2D u_texture;
uniform vec3 u_lightDir;
out vec4 fragColor;

void main() {
    vec4 baseColor = texture(u_texture, v_uv);
    float diffuse = max(dot(normalize(v_normal), normalize(u_lightDir)), 0.0);
    fragColor = baseColor * diffuse;
}
```

* `v_normal` comes from the mesh vertices
* `u_lightDir` is the direction of the light in view space
* `baseColor` is sampled from the texture
* The final color is computed per-pixel using the **math of diffuse lighting**

### Simple Game Example (Custom Shader Override)

**Textured object with lighting plus edge effect**

* Sample the sprite or mesh texture
* Apply lighting or color modifications
* Add custom effect, like an outline or tint
* Output the final pixel color

This is the stage where most visual detail and custom pixel effects are implemented.

## 3. Geometry Shader (Optional)

### Where It Runs

* **After vertex shader**
* **Before rasterization**

### What It Operates On

* A **whole primitive** (point, line, triangle)

### What It Usually Does

* Create or remove geometry
* Modify primitives dynamically

### Common Usage

* Particle billboards
* Grass generation
* Wireframe effects

### Note

Many modern engines avoid geometry shaders due to performance cost.

---

## Other Shader Stages (Advanced)

You may see these in modern APIs:

* **Tessellation Control / Evaluation**: dynamic mesh subdivision
* **Compute Shader**: general GPU computation (not tied to rendering)

They are powerful but not required to understand the basic pipeline.

---

## Shader Placement in the Pipeline

```
Vertex Data
    |
    v
[ Vertex Shader ]  <-- applies world/view/projection transforms (often automatically by engine)
    |
    v
Projection / Clipping
    |
    v
Rasterization
    |
    v
[ Fragment Shader ]
    |
    v
Depth Test / Blending
    |
    v
Framebuffer
```

Optional stages (like Geometry or Tessellation shaders) sit between vertex processing and rasterization.

---

## Simple End-to-End Game Example

**A basic 3D character in a game:**

1. **Vertex Shader**

   * Transforms character mesh into clip space
   * Engine typically handles this automatically
   * Passes UVs and normals forward

2. **Rasterization**

   * Converts triangles into fragments

3. **Fragment Shader**

   * Samples texture (skin, clothes)
   * Applies lighting
   * Outputs pixel color

4. **Output**

   * Character appears correctly lit and textured on screen

---

## Key Takeaway

* A **shader** is a GPU program running at a specific pipeline stage
* Different shader types exist for different responsibilities
* The **vertex shader is where geometry transforms happen**, but engines usually handle it automatically
* Games mainly rely on:

  * **Vertex shaders** for geometry
  * **Fragment shaders** for appearance

If you understand *where* a shader runs and *what data it touches*,
you already understand most real-world game rendering.

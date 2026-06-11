---
title: Graphics Pipeline
---

# General Rasterization Pipeline

Let’s slow this down and think like the GPU.

A rasterization pipeline is **not magic**. It is a **carefully staged data-processing factory**. Each stage does *one simple job*, then hands the result to the next stage. The power comes from doing this **millions of times in parallel**.

Input:
- List of vertex (3D position)
- List of triangle from these vertecies (e.g triangle 1: v1, v2, v3)
- UV coordinate position, Normal (of each vertex)
- Texture Map (texture image)
- Camera transform matrix
- Projection matrix
- Frame buffer size: Width x Height (output image size)

Output:
- Image on frame buffer (pixels values)

```
Vertex Data
    |
    v
[ Vertex Processing / Vertex Shader ]
    |
    v
Projection / Clipping
    |
    v
Rasterization
    |
    v
[ Fragment Processing / Fragment Shader ]
    |
    v
Depth Test / Blending
    |
    v
Framebuffer
```

| Stage               | Runs per          |
| ------------------- | ------------------|
| Input Assembly      | Vertex            |
| Vertex Processing   | Vertex            |
| Clipping            | Triangle          |
| Perspective Divide  | Vertex            |
| Viewport Transform  | Vertex            |
| Triangle Setup      | Triangle          |
| Rasterization       | Triangle - sample |
| Fragment Processing | Triangle - sample |
| Depth / Stencil     | Triangle - sample |
| Blending            | Triangle - sample |



---

## 1. Input Assembly — “What geometry are we drawing?”

### What comes in

* Vertex buffer: positions, UVs, normals, colors
* Index buffer: how vertices form triangles

#### Vertex buffer example

```
Index | Position     | UV       | Normal
-----------------------------------------
0     | (0, 0, 0)    | (0, 0)   | (0, 0, 1)
1     | (1, 0, 0)    | (1, 0)   | (0, 0, 1)
2     | (1, 1, 0)    | (1, 1)   | (0, 0, 1)
3     | (0, 1, 0)    | (0, 1)   | (0, 0, 1)
```

#### Index buffer example

```
[0, 1, 2,   0, 2, 3]
```

Interpretation:

* Triangle 1 → vertices (0, 1, 2)
* Triangle 2 → vertices (0, 2, 3)

Visually:

```
3 ---- 2
|    / |
|   /  |
|  /   |
| /    |
0 ---- 1
```

### What this stage really does

This stage **does no math at all**.

Its only job is to:

* Read raw vertex data from memory
* Use the index buffer to assemble **triangles**

Think of it like following a recipe: the ingredients are vertices, the steps are indices.

### What goes out

* A stream of triangles
* Each triangle still lives in **model (object) space**

---

## 2. Vertex Processing

### What comes in

* One vertex at a time
* Its attributes (position, UV, normal)
* Global data (Model, View, Projection matrices)

### The core idea

A vertex starts life in **object-local coordinates**.
The GPU must answer:

> If this object is here, and the camera is there, where does this vertex end up?

So we apply transforms:

```
clipPos = Projection × View × Model × position
```

Important detail:

* This runs **fully in parallel**
* Each vertex is independent
* No vertex knows about any other vertex

### What goes out

* Vertex position in **clip space** `(x, y, z, w)`
* Attributes passed along (UVs, colors, etc.)

### Small example

```
Model space: (1, 0, 0, 1)
Clip space:  (2, 1, 0.5, 1)
```

---

## 3. Clipping — “What part of this triangle is actually visible?”

### Why this stage exists

After projection, triangles can:

* Be fully on screen
* Be fully outside the camera
* Cross the edge of the view

The GPU must avoid drawing things the camera can never see.

### What comes in

* Triangles in **clip space**

### How clipping works

The visible region is defined by:

```
-w ≤ x, y, z ≤ w
```

Each triangle is tested against these planes:

* Fully outside → dropped
* Fully inside → kept
* Partially inside → **cut into smaller triangles**

This is classic **plane–polygon intersection**.

### What goes out

* Zero, one, or multiple triangles
* All guaranteed to be inside the view volume

---

## 4. Perspective Divide — “Turn 4D math into usable 3D”

### The problem

After projection, vertices live in **clip space** as `(x, y, z, w)`.

- `w` exists only to make **perspective projection** work
- But the rest of the pipeline does not want 4D math
- Rasterization needs normal **3D positions**

So we must remove `w` without breaking perspective.

### What comes in

- **Clip-space vertices** `(x, y, z, w)`
- This stage runs **per vertex**, fully in parallel

### What happens

Each vertex is divided by its own `w` value:

```
ndc = (x/w, y/w, z/w)
```

This converts:
- 4D clip space → **3D Normalized Device Coordinates (NDC)**
- Perspective math → actual spatial positions

### What the result really means

After this step:
- `x, y` → where the vertex lies on screen (before pixel mapping)
- `z` → **depth information**, kept for visibility and depth testing

Important:
- The output is **still 3D**, not 2D
- `z` is required later for depth interpolation and the depth buffer

### What goes out

- 3D NDC positions in range `[-1, 1]`

```
(x_ndc, y_ndc, z_ndc)
```

### Example

```
Clip: (2, 1, 0.5, 2)
NDC:  (1, 0.5, 0.25)
```

The vertex is **not 2D yet** — that happens in the viewport transform.


## 5. Viewport Transform — “Map math space to screen space”

### What comes in

* NDC coordinates
* Screen size `(W, H)`

### The idea

NDC is abstract math space.
We now decide **which 2D position** this corresponds to.

### How it’s done

```
For each vertex:
x_screen = (ndc.x * 0.5 + 0.5) * W
y_screen = (ndc.y * 0.5 + 0.5) * H
```

### What goes out

* 2D screen-space triangles

---

## 6. Triangle Setup — “Prepare for heavy pixel work”

### Why this stage exists

Rasterization will touch **many pixels per triangle**.
Anything reusable should be computed once.

### What comes in

* Screen-space triangle

### What is prepared

* Edge equations
* Triangle area
* Data for attribute interpolation

### What goes out

* A triangle optimized for fast rasterization

---

## 7. Rasterization — “Which pixels does this triangle cover?”

### The core question

For each pixel (or sample):

> Is this point inside the triangle?

Rasterization is about **coverage and geometry**, not color.


### What comes in

- Prepared screen-space triangle
- Sample points (each pixel can sampled into multiple sample point - super sampling)


### How it works

For each triangle, Check all the sample points, for each sample point:

- **Edge-function tests**  
  Check whether a sample point lies inside the triangle

- **Barycentric coordinates**  
  If inside, compute weights describing *where* the point lies relative to the triangle’s vertices

Important:
- At this stage, the GPU computes **interpolation weights**, not final values
  `“This fragment is X% vertex A, Y% vertex B, Z% vertex C.”`

### What goes out

- **Fragments**
- One fragment is generated for **each covered sample**

Each fragment contains:
- Sample position
- **Interpolation data (barycentric weights)**

A fragment is **not a pixel yet**.  
It is a *potential pixel/sample contribution*.

Final attribute values (UVs, colors, depth) are computed **later**, using these weights during fragment processing.

## 8. Fragment Processing — “What color is this pixel?”

### What comes in

- Fragment position
- **Interpolation data** (barycentric weights from rasterization)
- Per-vertex attributes (UVs, colors, normals)
- Per-vertex `w` values

At this point, **final attribute values do not exist yet** — only the data needed to compute them.

---

### Critical detail

Interpolation must be **perspective-correct**.

This is why:
- `w` was generated in vertex processing
- preserved through clipping
- and carried all the way to this stage

---

### What happens

- Perform **perspective-correct interpolation** using weights and `w`
- Compute final per-fragment attributes (UV, normal, color)
- Sample textures using interpolated UVs
- Apply lighting or material logic

---

### Example

```
(interpolated UV) → texture lookup → color
```

### What goes out

- Fragment color
- Fragment depth

---

## 9. Depth & Stencil Test — “Is this fragment visible?”

### Why this exists

Many fragments may map to the same pixel (or sample).
The GPU must decide **which one is actually visible**.

This decision is made **per sample**, after fragment color and depth are known.

### What comes in

- Fragment depth (from perspective-correct interpolation)
- Fragment color (computed in fragment processing)
- Current depth value stored in the **depth buffer** (z-buffer)

### What happens

1. **Depth comparison**
   - Compare fragment depth with the depth buffer value
   - Typical test: *is the fragment closer to the camera?*

2. **If the test fails**
   - No color write
   - No depth update

3. **If the test passes**
   - **Depth buffer is updated** with the fragment’s depth
   - Fragment proceeds to blending
   - Color buffer will be updated (after blending)

Stencil tests, if enabled, are evaluated here as well.

### What goes out

- Visible fragments only
- Updated depth buffer entries for passing samples

### IMPORTANT NOTE — Depth Test vs Transparency

In the **simple opaque-only case**:

- Any fragment that **fails the depth test** is immediately discarded
- Depth test **and** depth write are both enabled
- Draw order does not matter

This works because opaque geometry fully blocks what is behind it.

For scenes that include **transparent geometry**, the pipeline must change:

#### 1. Render opaque objects first
- Depth test: **ON**
- Depth write: **ON**
- Blending: **OFF**
- Draw order: **any**

This fills the depth buffer with the nearest opaque surfaces.

#### 2. Render transparent objects
- Depth test: **ON** (still discard fragments behind opaque geometry)
- Depth write: **OFF** (do not block other transparent fragments)
- Blending: **ON**
- Draw order: **back → front**

Transparent objects must be **sorted by depth** so blending produces correct results.
Sorting is usually:
- per object (common, fast)
- sometimes per triangle (more correct, more expensive)

### Key clarification

- Transparent fragments **still fail the depth test** if they are behind existing depth
- They are **not kept** just because they are transparent
- What changes is **depth writing**, not depth testing

### Where sorting happens

- Sorting is performed on the **CPU / engine side**
- The GPU rasterization pipeline does **not** automatically sort fragments by depth

### One-line takeaway

> Depth testing removes invisible fragments; sorting controls how visible fragments blend.

## 10. Blending & Framebuffer Write — “Combine with what’s already there”

### Why this stage exists

By this point, a fragment:
- Has a final color
- Has passed depth and stencil tests
- Represents a visible contribution to the image

But the framebuffer may **already contain a color** at this pixel/sample.
Blending defines **how the new fragment interacts with what’s there**.

This stage runs **per sample**, just like depth testing.

---

### What comes in

- Fragment color (source color)
- Fragment alpha
- Existing framebuffer color (destination color)
- Blending state (blend mode, factors)

---

### What happens

The GPU combines source and destination colors using a configured equation.

Common alpha blending:

```
C_result = C_src * α + C_dst * (1 − α)
```

### What goes out

- Final color value written to the **color buffer**
- Write happens only for:
- Samples that passed depth/stencil tests

### Important notes

- Opaque objects often disable blending
- Transparent objects rely on blending and usually require correct draw order
- Blending does **not** change depth (depth was already written earlier)

### Final output

- Color buffer updated
- After all samples are resolved (MSAA resolve), the framebuffer holds the final image


## Final Result — The Big Picture

After processing all triangles (in massive parallel):

* The framebuffer holds the final image `(W × H)`

Mental model:

```
Vertices → Triangles → Fragments → Pixels
```


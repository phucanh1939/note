---
title: Rasterization
---


# Rasterization

**Rasterization** is the process of converting **2D triangles into pixels**.

For each pixel, we need to know:
- Which triangles cover this pixel, and **how much** they cover it
- Among those triangles, **which one is visible** (closest to the camera)

## Rasterization as a Sampling Problem

Rasterization is solved using **sampling**.

- **Sampling**: converting a **continuous signal** into **discrete values** by taking samples at fixed points (sample rate)
- **Reconstruction**: rebuilding a signal from those discrete samples
- **Aliasing**: reconstructed signal is too different with original signal - happens when the sample rate is too low compared to the signal’s frequency, causing visible errors

The **rasterization problem can be treated as a sampling problem**.

- A triangle defines a **continuous coverage function** in 2D space
- This function answers: *is a point covered by the triangle or not?*

Because pixels are **discrete**, we cannot evaluate the coverage everywhere.  
Instead, we **sample the coverage function** at specific points.

Examples:
- Sample at the **pixel center** (single-sample rasterization)
- Sample at **multiple points per pixel** (MSAA / supersampling)

From these samples:
- We **approximate pixel coverage**
- More samples → better approximation
- Fewer samples → more aliasing, Low sample rate causes **jagged edges and artifacts**

So:
- **Triangle coverage** = continuous signal
- **Pixels** = discrete samples
- **Rasterization** = sampling the coverage function

## Coverage Function

For a 2D triangle, the **coverage function**:
- Takes a point `(x, y)`
- Returns:
  - `1` if the point is **inside** the triangle
  - `0` if the point is **outside**

By sampling this function:
- At the **pixel center** (simple rasterization)
- Or at **multiple points per pixel** (better quality)

We can **approximate how much of a pixel is covered** by the triangle.

---

## Point Inside Triangle Test (The Coverage function)

To check if a point **P** is inside a triangle:

1. For each edge of the triangle:
   - Check which side of the edge the **remaining vertex** is on
   - Check which side of the same edge **point P** is on
2. If P is on the **same side** as the remaining vertex for **all 3 edges**:
   - P is **inside** the triangle
3. Otherwise:
   - P is **outside**

---

## Using Cross Product (2D)

To know which side of an edge a point is on, we use the **cross product**.

- In **3D**, the cross product of two vectors gives a vector **perpendicular** to both
- The **direction** depends on the order of the vectors

For **2D**:
- Treat vectors as `(x, y, 0)`
- The cross product result points along the **z-axis**
- The **sign of the z value** indicates the side:
  - `z > 0` → left side
  - `z < 0` → right side
  - `z = 0` → on the line

This allows us to test whether point **P** is on the correct side of each triangle edge.

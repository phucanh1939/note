---
title: Spatial Transformation
---

# Spatial Transformation

A **Spatial Transformation** is a map that sends a point to a new location in space:

f: ℝⁿ → ℝⁿ

In graphics, transformations describe how geometry moves, rotates, scales, or is projected in space.

---

## Invariants of Transformations

A transformation can be characterized by what it **preserves (invariants)**.

| Transformation | Invariants |
|---------------|------------|
| Translation   | Differences between pairs of points |
| Scaling       | Lines through the origin, vector directions |
| Rotation      | Origin, distances between points, orientation |
| Reflection    | Distances, but flips orientation |
| Shear         | Parallel lines |

---

## Matrix Representation

A transformation can be encoded as a **matrix**.

To apply a transformation to a point:
```
p' = M · p
```

Where:
- `p` is the original point vector
- `M` is the transformation matrix
- `p'` is the transformed point

This allows transformations to be efficiently computed and composed.

---

## Composing Transformations

Multiple transformations can be combined by **matrix multiplication**:

    ```
    M = M₃ · M₂ · M₁
    p' = M · p
    ```

Important:
- **Order matters**
- Matrix multiplication is **not commutative**

Example:
- Rotate then translate ≠ translate then rotate

---

## Decomposing Transformations

A transformation matrix can be decomposed into:
- Translation
- Rotation
- Scaling (and sometimes shear)

Uses:
- Interpolating transformations
- Creating smooth animations
- Editing transforms intuitively

---

## Transformation in the Graphics Pipeline

The scene data consists of:
- **Static mesh data** (3D triangles in local/object space)
- **Object transforms**
- **Camera transform**

Pipeline flow:
1. Mesh vertices start in **local space**
2. GPU applies:
   - Local transform
   - Object (world) transform
   - Camera (view) transform
3. Vertices are now in **view space**
4. A **perspective transformation** projects 3D vertices into **2D screen space**
5. Rasterization converts 2D triangles into pixels

---

## Basic Transformations

### Linear Transformations

A **linear transformation**:
- Preserves the origin
- Preserves straight lines
- Can be represented by a matrix multiplication

Common linear transformations:

#### Rotation
- Rotates points around an axis
- Preserves distances and angles

**Rotation around X axis**
```
| 1   0        0  |
| 0  cosθ   -sinθ |
| 0  sinθ    cosθ |
```

**Rotation around Y axis**
```
|  cosθ  0  sinθ |
|   0    1   0   |
| -sinθ  0  cosθ |
```

**Rotation around Z axis**
```
| cosθ  -sinθ   0 |
| sinθ   cosθ   0 |
|  0       0    1 |
```

#### Reflection
- Mirrors points across a line or plane
- Flips orientation

### Reflection (XY plane)
```
| 1  0   0 |
| 0  1   0 |
| 0  0  -1 |
```

#### Scaling
- Changes size along one or more axes
- Preserves directions (uniform scaling)

```
| sx  0   0 |
| 0  sy   0 |
| 0   0  sz |
```

#### Shear
- Skews shapes
- Preserves parallel lines

```
| 1  sh_xy  sh_xz |
| 0    1      0   |
| 0    0      1   |
```
---

## Nonlinear / Affine Transformations

Affine transformations do **not** preserve the origin but still preserve straight lines.

### Translation
- Moves points by a fixed offset
- Does not preserve the origin

### Perspective Transformation
- Objects farther away appear smaller
- Lines may converge (vanishing points)
- Used to simulate human vision

---

## Homogeneous Coordinates

Translation and perspective cannot be represented by 3×3 linear matrices alone.

Solution: **homogeneous coordinates**

- Represent 3D points as 4D vectors `(x, y, z, w)`
- Use **4×4 matrices** to represent transformation

(Just like use 3D shear to represent 2D translation)

**Translation**
```
| 1  0  0  tx |
| 0  1  0  ty |
| 0  0  1  tz |
| 0  0  0  1  |
```

**Perspective Transformation**
```
| 1   0    0      0 |
| 0   1    0      0 |
| 0   0    1      0 |
| 0   0  1/d     0 |
```

**Rotation (Z axis)**
```
| cosθ  -sinθ  0  0 |
| sinθ   cosθ  0  0 |
|  0       0    1  0 |
|  0       0    0  1 |
```

**Scaling**
```
| sx  0   0   0 |
| 0  sy   0   0 |
| 0   0  sz   0 |
| 0   0   0   1 |
```

**Shear**
```
| 1  sh_xy  sh_xz  0 |
| 0    1    sh_yz  0 |
| 0    0      1    0 |
| 0    0      0    1 |
```

**After division by w:**
(x, y, z, w) → (x/w, y/w, z/w)

**Benefits:**
- Translation becomes a matrix multiplication
- Perspective projection becomes a linear operation in 4D
- Linear and affine transformations are unified and can represent by 4x4 matrix, which make the implement more simple and efficiency

### Point vs vector in Homogeneous coordinates

Homogeneous coordinates distinguish **points** and **vectors** using the `w` component.

- **Point**: `(x, y, z, 1)`: A point has a location in space → translation affects it
- **Vector (direction)**: `(x, y, z, 0)` : A vector encode a direction and magnitude → translation makes no sense

---

## Scene Graphs

A **scene graph** is a hierarchical structure for organizing transformations.

Key ideas:
- Each node has a **local transformation**
- A child’s final transform is:
    ```
    WorldTransform = ParentWorldTransform · LocalTransform
    ```
- Changing a parent affects all children
- Local transforms remain unchanged

Advantages:
- Natural hierarchy (e.g. character → arm → hand)
- Efficient updates (children local transform unchanged when change the parent transforma)
- Cached transformations multiplication (of local transforms) improve performance

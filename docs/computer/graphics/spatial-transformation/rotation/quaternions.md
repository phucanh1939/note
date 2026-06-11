---
title: Quaternions
---

# Quaternions

Quaternions represent rotation as **one single mathematical object**, not a sequence of axis rotations (lik Eucler Rotation) 
This avoids gimbal lock and allows smooth interpolation.

To understand why this works, we start from **Euler’s formula** and complex numbers.

## 2D Foundation: Euler Formula & Complex Numbers

Before quaternions, consider **complex numbers** for 2D rotation.

### Vector as complex number
```
v = x + y·i
```

### Euler Formula

Euler’s formula links angles to complex numbers:
```
e^(iθ) = cosθ + i·sinθ
```

This single expression encodes:
- **Direction** → angle θ
- **Rotation** → multiplication

### Length + Angle (Polar Form)

Any 2D vector can be written as:
```
v = (x, y)
```

Using polar coordinates:
```
|v| = r
angle = φ
```

As a complex number:
```
v = r·(cosφ + i·sinφ)
```

Using Euler’s formula:
```
v = r·e^(iφ) (encode rotation(φ) and scale (r))
```

So a complex number stores:
- **Length** → r
- **Angle** → φ

---

### Rotation as Multiplication

A rotation by angle θ is:
```
r = e^(iθ) (Just remove the scale/length factor)
```

Apply rotation:
```
v′ = r · v
    = e^(iθ) · r·e^(iφ)
    = r·e^(i(φ + θ))
```

Result:
- Length unchanged
- Angle increased by θ

➡️ Rotation becomes **angle addition**, not matrix math.

➡️ Quaternions extend this idea to 3D.

---

## Quaternion Definition

A quaternion has four components:
```
q = w + x·i + y·j + z·k
```

- **w** : scalar part  s
- **(x, y, z)** : vector part  

Often written as:
```
q = (x, y, z, w)
```

---

## Axis–Angle Representation

Any 3D rotation can be described by:
- A **unit axis** `u = (ux, uy, uz)`
- A **rotation angle** `θ`

### Quaternion formula
```
q = cos(θ/2) + u·sin(θ/2)
```

Expanded form:
```
q = (
  ux·sin(θ/2),
  uy·sin(θ/2),
  uz·sin(θ/2),
  cos(θ/2)
)
```

Why half-angle?
- Quaternion multiplication doubles the angle internally
- Ensures correct rotation behavior

---

## Unit Quaternion

For rotation, quaternions must be **normalized**:
```
|q| = 1
```

This guarantees:
- No scaling
- Pure rotation only

---

## Rotation Representation
```
v′ = q · v · q⁻¹
```

Same idea as:
```
v′ = r · v   (complex numbers)
```

But extended to 3D.

---

## Applying Quaternion Rotation

### Step 1: Vector as pure quaternion
```
v = (vx, vy, vz, 0)
```

### Step 2: Conjugate (inverse for unit quaternion)
```
q⁻¹ = (-x, -y, -z, w)
```

### Step 3: Rotate
```
v′ = q · v · q⁻¹
```

This rotates the vector in 3D space.

---

## Example: Quaternion Rotation

Rotate vector:
```
v = (1, 0, 0)
```

Around axis:
```
u = (0, 1, 0)   // Y axis
```

Angle:
```
θ = 90°
```

---

### Step 1: Build quaternion

```
sin(θ/2) = sin(45°) ≈ 0.707
cos(θ/2) = cos(45°) ≈ 0.707
```

```
q = (0, 0.707, 0, 0.707)
```

---

### Step 2: Rotate

```
v = (1, 0, 0, 0)
q⁻¹ = (0, -0.707, 0, 0.707)
```

```
v′ = q · v · q⁻¹
```

Result:
```
v′ = (0, 0, -1)
```

Same result as Euler or matrix rotation, but without gimbal lock.

---

## Engine-Optimized Rotation Formula

Game engines rarely compute `q · v · q⁻¹` directly.

Let:
- `q_vec = (x, y, z)`
- `w` = scalar part

Optimized form:
```
v′ = v
   + 2w · (q_vec × v)
   + 2 · (q_vec × (q_vec × v))
```

Benefits:
- Faster
- No temporary quaternions
- Same mathematical result

---

## Why Quaternions Are Better

### Compared to Euler angles
- No gimbal lock
- Order-independent (because it represent rotation as a single object)
- Stable under continuous rotation

### Compared to matrices
- Fewer parameters (4 vs 9)
- Easier normalization
- Better interpolation (SLERP)

---

## Summary

- Euler angles → easy to edit, unsafe
- Matrices → explicit, heavy
- **Quaternions → compact, stable, optimal for 3D rotation**

> Same rotation, different representations.  
> Quaternions are the most robust choice.

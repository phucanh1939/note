---
title: Eucler Rotation
---

# Euler Rotation

Euler rotation represents orientation as a sequence of rotations around fixed axes.  
It is intuitive and easy to edit, which is why it is commonly used in editors and UI.

---

## 2D Euler Rotation

In 2D, rotation happens around the origin by an angle **θ**.

### Basis vectors

Original basis:
- **e₁** = (1, 0)
- **e₂** = (0, 1)

After rotating by angle **θ**:
- **e₁′** = (cosθ, sinθ)
- **e₂′** = (−sinθ, cosθ)

---

### Vector rotation

Any vector **u** can be written as:
```
u = a·e₁ + b·e₂
```

Because rotation is a **linear transformation**, rotating **u** is equivalent to rotating the basis:
```
u′ = a·e₁′ + b·e₂′
```

---

### Rotation matrix (2D)

```
R(θ) =
[ cosθ  -sinθ ]
[ sinθ   cosθ ]
```

```
u′ = R(θ) · u
```

---

### Example (2D)

```
v = (1, 0)
θ = 90° = π/2
```

```
R =
[ 0  -1 ]
[ 1   0 ]
```

```
v′ = R · v = (0, 1)
```

---

## 3D Euler Rotation

In 3D, rotation is represented as a sequence of rotations around the **X**, **Y**, and **Z** axes.

---

### Axis rotation matrices

**X axis**
```
Rx(θ) =
[ 1   0        0 ]
[ 0  cosθ  -sinθ ]
[ 0  sinθ   cosθ ]
```

**Y axis**
```
Ry(θ) =
[ cosθ   0  sinθ ]
[ 0        1   0 ]
[ -sinθ  0  cosθ ]
```

**Z axis**
```
Rz(θ) =
[ cosθ  -sinθ  0 ]
[ sinθ   cosθ  0 ]
[ 0         0  1 ]
```

---

### Composition order

```
R = Ry · Rx · Rz
```

Order matters.

---

### Example (3D)

```
v = (1, 0, 0)
θ = 90° = π/2
```

```
Ry =
[ 0  0  1 ]
[ 0  1  0 ]
[ -1 0  0 ]
```

```
v′ = Ry · v = (0, 0, -1)
```

---

## Problems with Euler Angles

- Gimbal lock  
- Order dependent  
- Poor interpolation  

### Gimbal Lock

**Gimbal lock** occurs in Euler rotations when two rotation axes become aligned, causing the loss of one degree of freedom.

#### Why it happens
- Euler rotation uses three sequential axis rotations (X, Y, Z)
- At certain angles (commonly ±90°)
- Two axes overlap
- One rotation becomes indistinguishable from another

#### What goes wrong
- You effectively go from **3 DOF → 2 DOF** (Degrees of Freedom)
- One direction of rotation is lost
- Small input can cause large, unexpected motion

#### Example
- Rotate 90° around X
- Y and Z axes align
- Rotating around Y now behaves like rotating around Z

---

## Summary

- Simple and intuitive
- Good for editors
- Weak for animation and interpolation
- Often converted to quaternions internally

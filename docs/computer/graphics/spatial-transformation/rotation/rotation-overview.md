---
title: Rotation Overview
---

# Rotation Overview

## What is a rotation

A rotation is a transformation that satisfies:

- Length is preserved  
- Angles are preserved  
- Orientation is preserved (no mirroring)  
- Origin is preserved  

---

## Rotation in 2D vs 3D

### 2D
Rotations commute.

Example:
- Rotate 30°, then 60° = rotate 60°, then 30°

Reason: only one rotation axis exists.

---

### 3D
Rotations do NOT commute.

Example:
- Rotate 90° around Y, then Z
- ≠ Rotate 90° around Z, then Y

Reason: each rotation changes the axes used by the next rotation.

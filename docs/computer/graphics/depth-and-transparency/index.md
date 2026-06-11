---
title: Depth And Transparency
---

# Depth and Transparency — How They Actually Fit into the Pipeline

This section focuses on **where depth and transparency live inside the pipeline**,  
and **why they are tightly coupled but fundamentally conflicting**.

---

## First: What the Pipeline *Wants* to Do

The rasterization pipeline is designed around this assumption:

> For each sample:
> - Compute color
> - Compare depth
> - Keep **one winner**
> - Write final color

This works perfectly for **opaque geometry**.

Why?
- Opaque means **no contribution from what’s behind**
- Depth test can safely discard everything farther away

So for opaque objects, the pipeline is:
```
Triangle → Fragments → Shade (Sample Texture) → Depth Test → Write Color
```

---

## Where Transparency Enters the Picture

Transparency changes the question.

Instead of:
> “Which fragment wins?”

The question becomes:
> “How much does this fragment contribute?”

That means:
- You **cannot discard** what’s behind
- You need **both colors**
- You must **combine** them

---

## The Core Conflict: Depth Test vs Transparency

Depth testing wants to discard early.  
Transparency needs late information.

Depth test logic:
```
if fragment_depth < depth_buffer:
    write color
    write depth
else:
    discard fragment
```

Transparency blending:
```
final_color = blend(src_color, dst_color)
```

If the destination was discarded earlier, blending breaks.

---

## Why Depth Write Is the Real Problem

Depth **testing** is fine for transparent objects.  
Depth **writing** is not.

If a transparent fragment writes depth:
- It blocks everything behind it
- Even though it’s see-through

So the pipeline splits behavior:

| Object type | Depth Test | Depth Write |
|------------|-----------|-------------|
| Opaque | ON | ON |
| Transparent | ON | OFF |

---

## Pipeline Order in Practice

### 1. Render opaque objects first
- Depth test: **ON**
- Depth write: **ON**
- Blending: **OFF**
- Draw order: **any**

This fills the depth buffer with the nearest opaque surfaces.

### 2. Render transparent objects
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

### Why Draw Order Matters

Blending is **not commutative**:
```
A over B ≠ B over A
```

Transparent objects must be drawn:
```
Back → Front
```

## Alpha in the Pipeline

Alpha is interpreted **only during blending**, not during depth test.

No blending = alpha has no effect.

---

## Non-Premultiplied Alpha

Output from shader:
```
(RGB, α)
```

Blend equation:
```
C = RGB * α + dst * (1 − α)
```

Issues:
- Filtering artifacts
- Edge halos
- Sensitive to draw order errors

---

## Premultiplied Alpha

Output from shader:
```
(RGB * α, α)
```

Blend equation:
```
C = RGB + dst * (1 − α)
```

Benefits:
- Correct filtering
- Simpler math
- More stable accumulation

---

## Why Transparency Is Still Hard

The pipeline stores:
- One depth per sample
- One color per sample

Transparency wants **multiple layers**.

This mismatch leads to advanced techniques like:
- Depth peeling
- Weighted blended OIT
- Per-pixel linked lists

---

## Mental Summary

- Depth answers **visibility**
- Transparency answers **contribution**
- The pipeline is optimized for visibility
- Transparency conflicts with that design

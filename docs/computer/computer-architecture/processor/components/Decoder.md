---
title: Decoder
---

# Decoder

A decoder is a **[combinational circuit]** that converts binary inputs into a unique activated output

It can be used to create more complex circuits: **[multiplexer]**, **[RAM]**, **[Memory Controller Unit]** etc.

## How a Decoder works
- Takes **n** binary inputs and produces **2ⁿ** outputs.
- Only **one output** is active (HIGH) at a time based on the input combination.

Example: A 2-to-4 decoder takes 2 input (A, B) and produces 4 outputs (Y0, Y1, Y2, Y3)

| A | B | Y0 | Y1 | Y2 | Y3 |
|---|---|----|----|----|----|
| 0 | 0 |  1 |  0 |  0 |  0 |
| 0 | 1 |  0 |  1 |  0 |  0 |
| 1 | 0 |  0 |  0 |  1 |  0 |
| 1 | 1 |  0 |  0 |  0 |  1 |

## How to Make a Decoder

Just like any other **[combinational circuit]**:
- First, Describe the circuit in a **[truth table]**
- Then, Create **[logical function]** represent the **[truth table]**
- Finnally, Form the circuit using [**logic gates**]

### Example: Create 2-to-4 Decoder

A 2-to-4 decoder takes **2 inputs (A, B)** and produces **4 outputs (Y0, Y1, Y2, Y3)** using AND, NOT gates.

#### Truth Table:

| A | B | Y0 | Y1 | Y2 | Y3 |
|---|---|----|----|----|----|
| 0 | 0 |  1 |  0 |  0 |  0 |
| 0 | 1 |  0 |  1 |  0 |  0 |
| 1 | 0 |  0 |  0 |  1 |  0 |
| 1 | 1 |  0 |  0 |  0 |  1 |

#### Logic Equations:
```
Y0 = NOT(A) AND NOT(B)
Y1 = NOT(A) AND B
Y2 = A AND NOT(B)
Y3 = A AND B
```

[multiplexer]: ./Multiplexer
[RAM]: ../../Memory/Memory
[Memory Controller Unit]: ./MemoryController
[combinational circuit]: ./Circuit
[logic gates]: ./LogicGate
[logical function]: ../../../../../Math/BooleanAlgebra/BooleanAlgebra
[truth table]: ../../../../../Math/BooleanAlgebra/BooleanAlgebra


---
title: Boolean Algebra
---

# Boolean Algebra

## What is Boolean Algebra

Boolean algebra is a mathematical theory - a branch of algebra that deals with binary variables (true/false, 1/0) and logical operations. 
It provides the foundation for digital circuits and computer logic.

**Example:** AAND, OR, and NOT logic gates are built to represent basic operations in Boolean Algebra. These gates are then used to form complex circuits such as ALUs, multiplexers, flip-flops, and registers.    

### Basic Operations

- **AND** (`A · B` or `A ∧ B`): Output is true if both inputs are true.
- **OR** (`A + B` or `A ∨ B`): Output is true if at least one input is true.
- **NOT** (`A'` or `¬A`): Inverts the input (true becomes false, and vice versa).

### Key Laws:

#### 1. Identity Laws
- **AND Identity:** `A · 1 = A`
- **OR Identity:** `A + 0 = A`

#### 2. Domination Laws
- **AND Domination:** `A · 0 = 0`
- **OR Domination:** `A + 1 = 1`

#### 3. Idempotent Laws
- `A + A = A`
- `A · A = A`

#### 4. Complement Laws
- `A + A' = 1`
- `A · A' = 0`

#### 5. Double Negation
- `A'' = A`

#### 6. Commutative Laws
- **AND Commutative:** `A · B = B · A`
- **OR Commutative:** `A + B = B + A`

#### 7. Associative Laws
- **AND Associative:** `(A · B) · C = A · (B · C)`
- **OR Associative:** `(A + B) + C = A + (B + C)`

#### 8. Distributive Laws
- **AND over OR:** `A · (B + C) = (A · B) + (A · C)`
- **OR over AND:** `A + (B · C) = (A + B) · (A + C)`

#### 9. Absorption Laws
- `A + (A · B) = A`
- `A · (A + B) = A`

#### 10. De Morgan’s Theorems
- `(A · B)' = A' + B'`
- `(A + B)' = A' · B'`

## How Boolean Algebra helps to built logic blocks (circuits)

Logic blocks are categorized as one of two types, depending on whether they contain memory.
- Blocks without memory are called `combinational`; the output of a combinational block depends only on the current input. 
- Blocks with memory are called `sequential`: the outputs can depend on both the inputs and the value stored in memory, which is called the `state` of the logic block

### Combinational Logic Circuit

### Combinational Logic Circuit

With basic operations (AND, OR, NOT), a **logic function** that represents any given truth table can be formed. The logic function serves as a blueprint for combinational logic circuits. By connecting logic gates according to the logic function, we can build a combinational logic circuit.

#### Example

| A | B | C | Output (F) |
|---|---|---|------------|
| 0 | 0 | 0 | 0          |
| 0 | 0 | 1 | 0          |
| 0 | 1 | 0 | 0          |
| 0 | 1 | 1 | 1          |
| 1 | 0 | 0 | 0          |
| 1 | 0 | 1 | 1          |
| 1 | 1 | 0 | 1          |
| 1 | 1 | 1 | 1          |

- The corresponding logic function: `F = (A · B · C) + (A · B) + (A · C)`
- The circuit consists of **AND** and **OR** gates combined to implement the function.
### Sequential Logic Circuit

Boolean Algebra helps to build `flip-flops` by defining the logical relationships needed to store and update binary states. Flip-flops are constructed using logic gates (AND, OR, NOT, NAND, NOR) arranged based on Boolean equations.

`Flip-flops` are used to form complex sequential logic circuits (register, RAM, etc.) or used to synchronize execution stages in the processor pipeline by working with the clock signal and detecting rising or falling edges.

#### Example: D Flip-Flop
A **D Flip-Flop** stores the value of the `D` input when a clock pulse occurs.
- When the clock signal is high, `D` is stored in the flip-flop.
- The stored value is available at the output `Q`.

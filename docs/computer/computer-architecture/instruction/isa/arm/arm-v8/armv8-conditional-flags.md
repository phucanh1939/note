---
title: ARMv8 Conditional Flags
---

### Condition Flags in ARMv8

When an arithmetic or logical instruction is executed with the `s` suffix, the following condition flags in the **Program Status Register (CPSR)** are updated based on the result of the operation:

- **N (Negative)**: Set if the result is negative (most significant bit is 1 in two's complement representation).
- **Z (Zero)**: Set if the result is zero.
- **C (Carry)**: Set based on carry (for addition) or borrow (for subtraction).
- **V (Overflow)**: Set if there was a signed overflow or underflow.

### How Flags Are Set Based on Operations:

| Flag | Addition (`adds`) | Subtraction (`subs`) | Logical AND (`ands`) | Logical OR (`orrs`) | Logical XOR (`eors`) |
|------|-------------------|----------------------|----------------------|---------------------|----------------------|
| **N (Negative)** | Set if result is negative | Set if result is negative | Set if result is negative | Set if result is negative | Set if result is negative |
| **Z (Zero)** | Set if result is zero | Set if result is zero | Set if result is zero | Set if result is zero | Set if result is zero |
| **C (Carry)** | Set if there is a carry | Set if no borrow (operand1 >= operand2) | Unchanged | Unchanged | Unchanged |
| **V (Overflow)** | Set if signed overflow | Set if signed overflow | Unchanged | Unchanged | Unchanged |


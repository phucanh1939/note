---
title: ARMv8 Registers
---

# ARMv8 Registers

## General-Purpose Registers
These are 64-bit registers used for computation and data storage.

| Register Name | Alias | Purpose                                                                                           |
|---------------|-------|---------------------------------------------------------------------------------------------------|
| x0 - x7       |       | Pass the first 8 function arguments and hold return values (x0 for single return value).          |
| x8            | IP0   | Intra-Procedure Call Scratch Register (may also be used for passing arguments).                   |
| x9            | IP1   | Intra-Procedure Call Scratch Register (temporary usage within functions).                         |
| x10 - x15     |       | Temporary registers for intermediate calculations (caller-saved).                                 |
| x16           | IP0   | Typically used for procedure linkage or system calls (Inter-Procedure Call).                      |
| x17           | IP1   | Another inter-procedure call register (e.g., for trampolines or calls into PLT).                  |
| x18           |       | Platform Register (used as thread pointer in some systems).                                       |
| x19 - x28     |       | Callee-saved registers (preserved across function calls).                                         |
| x29           | FP    | Frame Pointer: Points to the base of the current stack frame.                                     |
| x30           | LR    | Link Register: Holds the return address after a function call.                                    |

## Special-Purpose Registers

| Register Name | Alias | Purpose                                                                                           |
|---------------|-------|---------------------------------------------------------------------------------------------------|
| xzr           | ZR    | Zero Register: Always holds the value 0 (used as a source or destination in some instructions).   |
| sp            | SP    | Stack Pointer: Points to the current top of the stack.                                            |
| pc            | PC    | Program Counter: Holds the address of the next instruction to execute.                            |
| nzcv          |       | Flags Register: Holds condition flags (Negative, Zero, Carry, Overflow).                          |
| v0 - v31      |       | Vector Registers: 128-bit SIMD registers used for vector and floating-point operations.           |

## System Control Registers

| Register Name | Purpose                                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------|
| spsr          | Saved Program Status Register: Holds the state of the program status before an exception.                 |
| elr           | Exception Link Register: Holds the return address for exception handlers.                                 |
| far           | Fault Address Register: Holds the address of a fault during exception handling.                           |
| ttbr0/1       | Translation Table Base Register: Points to the base of the page tables for address translation.           |
| mair0/1       | Memory Attribute Indirection Register: Controls memory attributes for different types of memory.          |

## Floating-Point/NEON Registers

| Register Name | Alias    | Purpose                                                                        |
|---------------|----------|--------------------------------------------------------------------------------|
| q0 - q31      |          | 128-bit registers used for SIMD (Single Instruction, Multiple Data) operations.|
| d0 - d31      |          | 64-bit registers for floating-point operations.                                |

## Control Registers

| Register Name | Purpose                                                                |
|---------------|------------------------------------------------------------------------|
| cpsr          | Current Program Status Register: Holds flags and status bits.          |
| spsr          | Saved Program Status Register: Saved version of CPSR before exceptions.|

------------------------------------------------------------------------------------------------------------

## Notes

### w0-w31 & wzr

The `w0 - w31` registers are the lower 32-bits of the corresponding `x0 - x31` registers.

The `wzr` is the lower 32-bites of `xzr`

### Difference between CPSR and NZCV

| Feature            | **CPSR**                          | **NZCV**                         |
|--------------------|-----------------------------------|----------------------------------|
| **Content**        | Contains condition flags (N, Z, C, V), control flags (I, F, T), and interrupt status. | Only contains the **N, Z, C, V** flags from the CPSR (the condition flags). |
| **Size**           | 32 bits (for AArch32) or 64 bits (for AArch64, in a different register set). | 4 bits (just for **N, Z, C, V** flags). |
| **Purpose**        | Manages processor status, condition flags, interrupt control, and mode flags. | Represents only the condition flags (N, Z, C, V) from the CPSR, typically used in conditional instruction execution. |
| **Access**         | The full CPSR is typically accessed to control interrupts, check processor status, and handle exceptions. | The NZCV flags are often used in conditional execution to check the status of the last arithmetic/logical operation. |

### Flags

#### Condition flags
- N (Negative)  : Set if the result of the last operation was negative.
- Z (Zero)      : Set if the result of the last operation was zero.
- C (Carry)     : Set if the last operation generated a carry (for addition) or borrow (for subtraction).
- V (Overflow)  : Set if the last operation caused an overflow.

#### Control flags:
- I: Interrupt disable
- F: Fast interrupt disable
- T: Thumb instruction set indicator

### Caller-saved registers

`Caller-saved` registers are typically saved by the caller before calling another function, and restored after the function call

```s
foo:
    stp x10, x11, [sp, #-16]!    ; Save caller-saved registers (x10, x11) to stack
    bl bar                     ; Call the function bar
    ldp x10, x11, [sp], #16      ; Restore x10, x11 from stack after bar returns
    ; Continue using x10, x11 here

bar:
    ; Function body, caller-saved registers (x0, x1) can be used or modified
    ret                         ; Return to foo
```

### Callee-saved registers

`Callee-saved` registers are registers that the called function (callee) is responsible for preserving. If a function (the callee) uses a callee-saved register, it must save the value of that register at the beginning of the function and restore it before returning to the caller.

```s
foo:
    bl bar                         ; Call bar

bar:
    stp x19, x20, [sp, #-16]!      ; Save callee-saved registers
    ; Do work, modifying x19, x20
    ldp x19, x20, [sp], #16        ; Restore callee-saved registers
    ret                            ; Return to foo

```

## References

https://developer.arm.com/documentation/ddi0601/2024-12/AArch64-Registers/
---
title: ARMv8 Instructions
---

# ARMv8 Instruction Set

The ARMv8-A instruction set is designed for 64-bit processors, supporting both 64-bit and backward-compatible 32-bit applications.

In ARMv8, each instruction is encoded in a 32-bit word (AArch32) or 64-bit word (AArch64) depending on the mode. The instructions are categorized into various types based on their functions, such as data processing, memory access, branching, etc. Each instruction can also have specific conditions for conditional execution based on flags set by previous operations.

## 1. Data Processing Instructions
These instructions perform operations on registers or immediate values.

Arithmetic and logical and instructions have an `s` suffix that makes the instruction update the condition flags in the Program Status Register (CPSR) and (NZCV)

- **Arithmetic Operations**:
  - `add <Xd>, <Xn>, <Xm>`: Add the values in registers `Xn` and `Xm` and store the result in `Xd`.
  - `sub <Xd>, <Xn>, <Xm>`: Subtract the value in register `Xm` from `Xn` and store the result in `Xd`.
  - `mul <Xd>, <Xn>, <Xm>`: Multiply the values in registers `Xn` and `Xm` and store the result in `Xd`.
  - `sdiv <Xd>, <Xn>, <Xm>`: Signed divide the value in register `Xn` by the value in `Xm` and store the result in `Xd`.
  - `udiv <Xd>, <Xn>, <Xm>`: Unsigned divide the value in register `Xn` by the value in `Xm` and store the result in `Xd`.
  - `neg <Xd>, <Xn>`: Negate the value in register `Xn` and store the result in `Xd`.

- **Logical Operations**:
  - `and <Xd>, <Xn>, <Xm>`: Bitwise AND between the values in registers `Xn` and `Xm`, store result in `Xd`.
  - `orr <Xd>, <Xn>, <Xm>`: Bitwise OR between the values in registers `Xn` and `Xm`, store result in `Xd`.
  - `eor <Xd>, <Xn>, <Xm>`: Bitwise XOR between the values in registers `Xn` and `Xm`, store result in `Xd`.
  - `bic <Xd>, <Xn>, <Xm>`: Bitwise AND between `Xn` and the negation of `Xm`, store result in `Xd`.
  - `lsl <Xd>, <Xn>, <Xm>`: Logical shift left the value in `Xn` by the number of bits specified in `Xm`, store result in `Xd`.
  - `lsr <Xd>, <Xn>, <Xm>`: Logical shift right the value in `Xn` by the number of bits specified in `Xm`, store result in `Xd`.
  - `asr <Xd>, <Xn>, <Xm>`: Arithmetic shift right the value in `Xn` by the number of bits specified in `Xm`, store result in `Xd`.
  - `ror <Xd>, <Xn>, <Xm>`: Rotate right the value in `Xn` by the number of bits specified in `Xm`, store result in `Xd`.

- **Comparison and Test**:
  - `cmp <Xn>, <Xm>`: Compare registers `Xn` and `Xm` (sets flags).
  - `tst <Xn>, <Xm>`: Bitwise AND between `Xn` and `Xm`, sets flags but doesn't store result.
  - `ccmn <Xn>, <Xm>, <imm>, <cond>`: Compare `Xn` and `Xm` with immediate, and update flags based on condition.
  - `csel <Xd>, <Xn>, <Xm>, <cond>`: Conditional select between `Xn` and `Xm`, store in `Xd` based on the condition.

## 2. Conditional Data Processing Instructions

- `cset <Xd>, <cond>`: Conditionally set register `Xd` to `1` if condition `cond` is true, otherwise set it to `0`.
- `cmp <Xn>, <Xm>`: Compare registers `Xn` and `Xm` (perform `Xn - Xm`), update flags, but do not store the result.
- `cmn <Xn>, <Xm>`: Compare registers `Xn` and `Xm` (perform `Xn + Xm`), update flags, but do not store the result.
- `tst <Xn>, <Xm>`: Perform a bitwise AND between registers `Xn` and `Xm`, update flags, but do not store the result.
- `teq <Xn>, <Xm>`: Perform a bitwise XOR between registers `Xn` and `Xm`, update flags, but do not store the result.
- `mvn <Xd>, <Xm>`: Move the bitwise negation of `Xm` into register `Xd`.
- `mov <Xd>, <Xm>`: Move the value of `Xm` into register `Xd`.
- `adr <Xd>, <label>`: Load the address of `label` into register `Xd`.

## Condition Codes
- **`eq`**: Equal (Zero flag set).
- **`ne`**: Not equal (Zero flag clear).
- **`gt`**: Greater than (Zero flag clear, Negative flag equals Overflow flag).
- **`lt`**: Less than (Negative flag not equal to Overflow flag).
- **`ge`**: Greater than or equal (Negative flag equals Overflow flag).
- **`le`**: Less than or equal (Zero flag set, or Negative flag not equal to Overflow flag).
- **`mi`**: Negative (Negative flag set).
- **`pl`**: Positive (Negative flag clear).
- **`vs`**: Overflow (Overflow flag set).
- **`vc`**: No overflow (Overflow flag clear).
- **`hs`**: Higher or same (Carry flag set).
- **`lo`**: Lower (Carry flag clear).

## 3. Memory Access Instructions
These instructions are used for reading from or writing to memory.

- **Load/Store**:
  - `ldr <Xd>, [<Xn>, #<imm>]`: Load a value from memory at the address calculated by `Xn + imm` into `Xd`.
  - `str <Xd>, [<Xn>, #<imm>]`: Store the value in `Xd` into memory at the address `Xn + imm`.
  - `ldrsb <Xd>, [<Xn>, #<imm>]`: Load a signed byte from memory into `Xd`, sign-extend it.
  - `ldrsw <Xd>, [<Xn>, #<imm>]`: Load a signed word from memory into `Xd`, sign-extend it.
  - `ldrb <Xd>, [<Xn>, #<imm>]`: Load a byte from memory into `Xd`.
  - `ldrh <Xd>, [<Xn>, #<imm>]`: Load a half-word from memory into `Xd`.
  - `stp <Xd>, <Xm>, [<Xn>, #<imm>]`: Store the values in `Xd` and `Xm` at the address `Xn + imm` (pair of registers).
  - `ldp <Xd>, <Xm>, [<Xn>, #<imm>]`: Load the values from memory at the address `Xn + imm` into `Xd` and `Xm`.
  - `stur <Xd>, [<Xn>, #<imm>]`: Store the value in `Xd` at the unscaled address `Xn + imm`.
  - `ldur <Xd>, [<Xn>, #<imm>]`: Load the value from memory at the unscaled address `Xn + imm` into `Xd`.

- **Special Load/Store**:
  - `ldp <Xd>, <Xm>, [<Xn>]`: Load a pair of registers from memory at the address in `Xn`.
  - `stp <Xd>, <Xm>, [<Xn>]`: Store a pair of registers to memory at the address in `Xn`.

## 4. Branch and Control Flow
These instructions control the flow of the program.

- **Branching**:
  - `b <label>`: Unconditional branch to the specified label.
  - `bl <label>`: Branch with link (stores the return address in `X30`).
  - `br <Xn>`: Branch to the address stored in `Xn`.
  - `blr <Xn>`: Branch with link to the address stored in `Xn`.

- **Conditional Branching**:
  - `cbnz <Xn>, <label>`: Conditional branch if `Xn` is not zero.
  - `cbz <Xn>, <label>`: Conditional branch if `Xn` is zero.
  - `tbnz <Xn>, #<bit>, <label>`: Conditional branch if bit `<bit>` of register `Xn` is **set** (non-zero).
  - `tbz <Xn>, #<bit>, <label>`: Conditional branch if bit `<bit>` of register `Xn` is **clear** (zero).

- **Procedure Call**:
  - `bl <label>`: Branch with link, storing the return address in `X30`.
  - `ret`: Return from function (branch to the address stored in `X30`).

- **Exception and Control**:
  - `svc #<imm>`: Supervisor call (system call, with immediate argument).
  - `hlt`: Halt the processor (used for debugging).
  - `mrs <Xd>, <SysReg>`: Move value from a system register (e.g., program status register) into `Xd`.
  - `msr <SysReg>, <Xd>`: Move value from `Xd` into a system register.

## 5. SIMD and Floating Point Operations
ARMv8 supports SIMD (Single Instruction Multiple Data) and floating-point instructions.

- **SIMD (Neon)**:
  - `fmla <Vd>, <Vm>, <Vn>`: Multiply-accumulate the vectors `Vm` and `Vn`, store the result in `Vd`.
  - `fadd <Vd>, <Vn>, <Vm>`: Floating-point addition between `Vn` and `Vm`, store result in `Vd`.
  - `fsub <Vd>, <Vn>, <Vm>`: Floating-point subtraction between `Vn` and `Vm`, store result in `Vd`.
  - `fmul <Vd>, <Vn>, <Vm>`: Floating-point multiplication between `Vn` and `Vm`, store result in `Vd`.
  
- **Floating-point (FP)**:
  - `fmov <Xd>, <Xm>`: Move the floating-point value in `Xm` to `Xd`.
  - `fdiv <Xd>, <Xn>, <Xm>`: Divide the floating-point value in `Xn` by `Xm`, store the result in `Xd`.
  - `fsqrt <Xd>, <Xn>`: Compute the square root of `Xn`, store result in `Xd`.
  - `fcmp <Xn>, <Xm>`: Compare the floating-point values in `Xn` and `Xm`.

## 6. System Control Instructions
These instructions allow control over the system state, status registers, and enable or disable certain features.

- **Control Register Access**:
  - `mrs <Xd>, <SysReg>`: Move from a system register (e.g., program status register) into `Xd`.
  - `msr <SysReg>, <Xd>`: Move value from `Xd` into a system register.

- **Memory Barrier**:
  - `dmb`: Data memory barrier (ensures memory ordering).
  - `dsb`: Data synchronization barrier.
  - `isb`: Instruction synchronization barrier.

- **Exception Handling**:
  - `svc #<imm>`: Supervisor call (system call, with an immediate argument).
  - `hvc #<imm>`: Hypervisor call (for virtualization).
  - `smc #<imm>`: Secure monitor call (for ARM's TrustZone).

## 7. Conditional Execution
ARMv8 uses a conditional execution model that allows you to execute instructions based on certain flags (like Zero, Negative, Carry, and Overflow flags).

- **Conditional Instructions**:
  - Most ARMv8 instructions can be executed conditionally based on the status of flags. For example:
    - `eq`: Execute if equal.
    - `ne`: Execute if not equal.
    - `lt`: Execute if less than.
    - `gt`: Execute if greater than.
  
  You can suffix instructions with a condition (e.g., `addeq` to add if equal).

## 8. Miscellaneous Instructions
These include special instructions for specific needs.

- **NOP**: No operation (used for timing or debugging).
- **CLZ**: Count leading zeros (counts how many leading zeros in a register's value).
- **REV**: Reverse the byte order in a register.
- **SEL**: Conditional select between two registers.

---

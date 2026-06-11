---
title: Instruction
---

# Instruction

## What is an Instruction?

An instruction is a (binary) command that can executed by computer processor

**Types of Instructions**:
- Data Transfer Instructions: Move data between memory, registers (LOAD, STORE, MOV)
- [Arithmetic] Instructions: Perform [arithmetic] operations. (AD-D, SUB, MUL, DIV)
- Logical Instructions: Perform bitwise operations. (AND, OR, NOT. XOR)
- Control Instructions: Alter the flow of execution (JUMP, CALL, RET, BRANCH)
- Comparison Instructions: Compare values and set flags/register value based on the result. (CMP, TEST)
- I/O Instructions: Facilitate communication with input/output devices. (IN, OUT)

## Instruction Structure

An instruction typically consists of the following fields:
- Opcode (Operation Code): Specifies the operation to be performed (e.g., ADD, SUB, LOAD).
- Operands: 
  - Source Operands: Data or addresses required for the operation.
  - Destination Operand: Where the result is stored.

Example (in a 32-bit R-type instruction in MIPS):
opcode (6 bits) | rs (5 bits) | rt (5 bits) | rd (5 bits) | shamt (5 bits) | funct (6 bits)

## Some common problem about Instruction

- Large address or immediate value is not fit in fields used in an instruction (example 32 bit address not fit in 23 bits in jump instruction in MIPS). So we need some how to:
  - [Handle Large Immediate](./ImmediateValue)
  - [Represent address in fewer bits in instruction (by combine with other data like PC, register value, etc.)](./AddressingMode)
- We may need some kinds of [instructions that support synchornization for parallelism execution](./SupportParallelism) (example, We may need instructions that support lock memory when process and writing to avoid another program override the value during the execution)

[arithmetic]: ../../General/Arithmetics/Arithmetics
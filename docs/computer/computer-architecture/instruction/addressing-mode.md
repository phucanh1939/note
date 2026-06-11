---
title: Addressing Mode
---

# Addressing Mode

Address may require more than number of bits used in instruction to represent them, so we need a way to use less bits to represent more addresses (by combine these bits with other data like current program pointer PC, or with a value from a register, ...)

Addressing modes are different ways to represent address in instructions:

- Immediate Addressing: Address is a immediate value. Ex: `j 242424 # Jump to the address 242424`
- Register Addressing: The address is the value stored in a register. Ex: `lw $t0, 0($t1) # Load word from memory address stored in $t1 into $t0`
- Base or Displacement Addressing: The address is the sum of a register's value and a constant (displacement). Ex: `lw $t0, 4($t1) # Load word from the memory address ($t1 + 4) into $t0`
- PC-Relative Addressing: The address is calculated by adding a constant to the current program counter (PC). Ex: `beq $t0, $t1, 100 # Branch to (PC + 1 + 100)th word/instruction if $t0 equals $t1`
- etc.

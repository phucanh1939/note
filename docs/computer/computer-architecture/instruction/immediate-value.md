---
title: Immediate Value
---

# Handle Large Immediate

Instructions are limited to a fixed length (ex. 32 bit). However, some operands, such as immediate values or addresses, require more than number of bits used in instruction to represent these value (ex. 16 bits of 32 bits used for immediate value, but some value need more than 16bit to represent)

To handle large immediate values, breaks them into smaller parts and reassembles them into registers.

Example:
```asm
# Load `0000 0000 0011 1101 0000 1001 0000 0000` into register `$s0`
lui $s0, 61 # Load upper 16 bits: 0000 0000 0011 1101
ori $s0, $s0, 2304 # Insert lower 16 bits: 0000 1001 0000 0000
```
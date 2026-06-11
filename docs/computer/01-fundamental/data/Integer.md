---
title: Integer
---

# Integer

An **integer** is a whole number (positive, negative, or zero) that does not have a fractional or decimal point.

Example: 0, 124, -30, etc.

## How to Represent an Integer in Binary

### Unsigned Integer

**Unsigned integer** is represented in binary form using **positional notation**, where each bit (binary digit) represents a power of 2.

#### Convert from Decimal to Binary
To convert an **unsigned integer** from **decimal** to **binary**: use repeated division by 2.

##### Example: Convert **157** to Binary
1. 157 \div 2 = 78 remainder **1**
2. 78 \div 2 = 39 remainder **0**
3. 39 \div 2 = 19 remainder **1**
4. 19 \div 2 = 9 remainder **1**
5. 9 \div 2 = 4 remainder **1**
6. 4 \div 2 = 2 remainder **0**
7. 2 \div 2 = 1 remainder **0**
8. 1 \div 2 = 0 remainder **1**

**Read from bottom to top:**  
`157 = 1001 1101`

#### Convert from Binary to Decimal
To convert an **unsigned integer** from **binary** to **decimal**: use `Positional Notation`

For **n-bit** unsigned integer:

`Decimal` = `bit[n-1] * 2^(n-1) + bit[n-2] * 2^(n-2) + ... + bit[0] * 2^0`

= `Sum(bit[i-1] * 2^(i-1))` *with* `i` *from* `n-1` *to* `0`

##### Example: Convert unsigned integer `1011` to decimal
The binary number `1011` is: `1x2^3 + 0x2^2 + 1x2^1 + 1x2^0 = 11 (in base 10 - Decimal)`

### Signed Integer

**Singed integer** are commonly represented using **two's complement** encoding:
1. Flip all the bits of the number (1's complement).
2. Add 1 to the result.

#### Why `-X = flip_all_bit(X) + 1`
```c
we have: X + flip_all_bit(X) = -1 // all bits are 1
=>      -X = flip_all_bit(X) + 1
```

#### Why Two's Complement

**Two's Complement** representation simplifies [arithmetic] operations (see [here][arithemetic]) and ensures there is only one representation for zero

#### Convert from Decimal to Binary

1. **Convert the absolute value** of the number to binary (as an unsigned int).

2. **If the number is negative**, take the two’s complement:
   - Invert all bits.
   - Add 1 to the result.

##### Example Convert `-99` to 8-bit Two’s Complement

1. Convert **99₁₀** to binary (unsigned):  
   - `99 = 0110 0011`

2. Take the **two’s complement**:
   - Invert bits: **1001 1100**
   - Add 1: **1001 1101**

Thus, **-99 = 1001 1101** in **two’s complement** (8-bit representation).

#### Convert from Binary to Decimal

To convert an **signed integer** from **binary** to **decimal**: use `Positional Notation` with sign for **leftmost bit** (**MSB** - **Most Significant Bit**)

For **n-bit** unsigned integer:

`Decimal` = `sign * bit[n-1] * 2^(n-1) + bit[n-2] * 2^(n-2) + ... + bit[0] * 2^0`

= `sign * bit[n-1] * 2^(n-1) + Sum(bit[i-1] * 2^(i-1))` *with* `i` *from* `n-2` *to* `0`

Decimal = 

##### Example: Convert `1001 1101` to Deciaml

`1001 1101` = `-2^7 + 2^4 + 2^3 + 2^2 + 2^0` = `-99`

##### Example: Convert `0001 0001` to Deciaml

`0001 0001` = `2^4 + 2^0` = `17`

## History of Integer

See [Number History](Number)

[arithemetic]: ../../ComputerArchitecture/Arithmetics/Arithmetics
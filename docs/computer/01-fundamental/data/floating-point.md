---
title: Floating Point
---

# Floating Point

Floating-point numbers are approximately representation of **[real number][real-numbers]**.

Why *approximately*: 
- Computer used a limited bits to represent a number, but **[real number][real-numbers]** can have infinity digits

## How to Represent Floating-point Number in Binary

Floating-point numbers (e.g., 3.14) are represented using the **IEEE 754 standard**, which divides the binary representation into three parts:
1. **Sign bit**: 1 for negative, 0 for positive.
2. **Exponent**: Encodes the range or scale (stored with a bias - to make it > 0 and simplify when check condition between 2 floating point numbers).
3. **Mantissa** (or significand): Encodes the precision.

| **Field**          | **Single Precision (32-bit)** | **Double Precision (64-bit)** |
|--------------------|-------------------------------|-------------------------------|
| **Sign Bit**       | 1 bit                         | 1 bit                         |
| **Exponent**       | 8 bits                        | 11 bits                       |
| **Mantissa**       | 23 bits                       | 52 bits                       |
| **Bias**           | 127                           | 1023                          |
| **Total Size**     | 32 bits                       | 64 bits                       |


With `k` is the number of exponent bits: `Bias` = 2^(k-1) - 1

### Special Values

| Value     | Binary Representation              | Explanation                                                            |
|-----------|------------------------------------|------------------------------------------------------------------------|
| +0        | `00000000000000000000000000000000` | **Sign bit** = 0, **exponent** = 0, **mantissa** = 0.                  |
| -0        | `10000000000000000000000000000000` | **Sign bit** = 1, **exponent** = 0, **mantissa** = 0.                  |
| +infinity | `01111111100000000000000000000000` | **Sign bit** = 0, **exponent** = all 1s, **mantissa** = 0.             |
| -infinity | `11111111100000000000000000000000` | **Sign bit** = 1, **exponent** = all 1s, **mantissa** = 0.             |
| NaN       | `01111111100000000000000000000001` | **Sign bit** can be 0 or 1, **exponent** = all 1s, **mantissa** != 0.  |

### Convert from Decimal to Binary

1. Get the `sign` bit
2. Convert integer part and fractional part to binary
3. Normalize the binary to get the `exponent` & `fraction`
4. Bias the `exponent` found in step #3
5. Form the binay: `sign|fraction|exponent`

#### Example 1: Representing ` -6.75 ` in IEEE 754 (32-bit Single Precision)

1. Sign bit: 1 (negative)

2. Convert `6.75` to binary:  
- The integer part `6` is `110` in binary.  
- The fractional part `0.75` is `0.11` in binary.  
Thus, `6.75` is `110.11` in binary.

3. Normalize the binary number:  
- Move the decimal point to the right of the first 1: `1.1011 x 2^2`.  
  - **Mantissa**: `1011` (excluding the leading 1, which is implicit).  
  - **Exponent**: `2`.  

4. Bias the exponent:  
- IEEE 754 single precision uses a bias of `127`.  
- `2 + 127 = 129`, which is `10000001` in binary.  

5. Assemble the parts: `1 10000001 10110000000000000000000` (32 bits)

#### Example 2: Representing `10.3562` in IEEE 754 (32-bit Single Precision)

1. Sign bit: 0

2. Convert to binary format
- Step 1: Convert the integer part (10) to binary: 10 (decimal) = 1010 (binary)
- Step 2: Convert the fractional part (0.3562) to binary
For the fractional part, multiply by 2 and record the integer part at each step. Repeat the process until the fractional part becomes 0 or you reach the desired precision.
0.3562 × 2 = 0.7124 → integer part = 0
0.7124 × 2 = 1.4248 → integer part = 1
0.4248 × 2 = 0.8496 → integer part = 0
0.8496 × 2 = 1.6992 → integer part = 1
0.6992 × 2 = 1.3984 → integer part = 1
0.3984 × 2 = 0.7968 → integer part = 0
.... 
0.3562 (decimal) ≈ .01011001100110011001101 (binary)
=> 10.3562 (decimal) ≈ 1010.01011001100110011001101 (binary)

3. Normalize the Binary Number
1010.010110 = 1.01001011001100110011001101 × 2^3 (2 ^ exponent)

4. Bias the exponent
exponent = 3 + 127 = 130 = 1000001

5. Form the binary
`10.3562`= `0 10000010 01001011001100110011001`

### Convert from Binary to Decimal
1. Extract `sign`, `exponent`, and `fraction` from the binary
2. Compute the decimal value using the formula: `(-1)^sign * (1 + fraction) * 2^(exponent - bias)`

#### Example conver `0 10000010 01001011001100110011001` to floating point

1. Extract the sign, exponent, and mantissa.
  - sign = 0
  - exponent = 10000010 = 130
  - mantissa: `01001011001100110011001` = 0/2^1 + 1/2^2 + 0/2^3 +... ≈ 0.28125

2. Compute the decimal value using the formula: `(-1)^sign * (1 + mantissa) * 2^(exponent - bias)`
  value = -1 ^ 0 * (1 + 0.28125) * 2 ^ (130-127) = 10.25

## Floating-point History

Before computers, approximations of real numbers is needed because: In general, many real-world quantities (like lengths, areas, or volumes) have infinite precision make it impossible to calculate.

## 1. Early Beginnings  
- **Ancient Civilizations**: Early estimates of real-world values (like astronomical data) used approximations but lacked precise representation of decimals.

## 2. 17th Century  
- **Napier's Logs (1614)**: John Napier introduced **logarithms**, which helped with multiplication and division by converting them to addition and subtraction.

## 3. 19th Century  
- **Charles Babbage**: The **Analytical Engine** (1837) was designed to use floating-point arithmetic for calculations, though it was never fully built.

## 4. 20th Century  
- **IEEE Standardization (1985)**: The **IEEE 754 standard** was introduced to provide a standardized format for floating-point representation, ensuring consistency across computers.
- **Early Computing**: In the 1940s, computers like the **ENIAC** used floating-point arithmetic for scientific and engineering calculations.
  
[real-numbers]: Number
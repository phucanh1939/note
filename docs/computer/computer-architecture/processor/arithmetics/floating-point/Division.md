---
title: Division
---

# Floating Point Division

## Steps for Floating Point Division:

1. **Divide the Mantissas:**
   - Divide the mantissas (fractional parts) of the two numbers.
   - The result may need normalization after the division.

2. **Subtract the Exponents:**
   - Subtract the exponent of the divisor from the exponent of the dividend. This is because when dividing powers of 2, we subtract the exponents.

3. **Normalize the Result:**
   - After division, normalize the result so that the leading 1 is placed before the decimal point (unless the result is subnormal).
   - Adjust the exponent accordingly to reflect any shifts in the mantissa.

4. **Handle Rounding:**
   - Round the mantissa to the desired precision. If needed, adjust the exponent to maintain normalization after rounding.

5. **Final Result:**
   - The result will include:
     - **Sign**: Positive if both signs are the same, negative if they differ.
     - **Exponent**: The difference between the exponents of the dividend and divisor.
     - **Mantissa**: The normalized and rounded result of the division.

---

### Example: Dividing 3.5 by 1.25 (IEEE 754 Single Precision)

1. **Convert to Binary (Normalized Form):**
   - `3.5 = 1.11000000000000000000000 x 2^1`
   - `1.25 = 1.01000000000000000000000 x 2^0`

2. **Divide the Mantissas:**
   - Divide:
     ```
     1.11000000000000000000000 ÷ 1.01000000000000000000000
     = 
     1.10000000000000000000000
     ```

3. **Subtract the Exponents:**
   - Subtract exponents: `1 - 0 = 1`

4. **Normalize the Result:**
   - The result is already normalized: `1.10000000000000000000000 x 2^1`

5. **Handle Rounding:**
   - Round the mantissa if needed (no rounding needed in this case).

6. **Final Result:**
   - The quotient is `1.1000 x 2^1`, which equals **2.5** in decimal.

-----


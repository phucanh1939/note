---
title: Multiplication
---

# Floating Point Multiplication

### Steps for Floating Point Multiplication:

1. **Multiply the Mantissas:**
   - Multiply the mantissas (fractional parts) of the two numbers.
   - The result may need normalization after multiplication.

2. **Add the Exponents:**
   - Add the exponents of the two numbers. The exponent is adjusted based on the rule: when multiplying powers of 2, you add the exponents.

3. **Normalize the Result:**
   - After multiplication, normalize the result so that the leading 1 is placed before the decimal point (unless the result is subnormal).
   - Adjust the exponent accordingly to reflect any shifts in the mantissa.

4. **Handle Rounding:**
   - Round the mantissa to the desired precision. If needed, adjust the exponent to maintain normalization after rounding.

5. **Final Result:**
   - The result will include:
     - **Sign**: Positive if both signs are the same, negative if they differ.
     - **Exponent**: The sum of the exponents of the two numbers.
     - **Mantissa**: The normalized and rounded product of the mantissas.

---

### Example: Multiplying 1.25 and 3.5 (IEEE 754 Single Precision)

1. **Convert to Binary (Normalized Form):**
   - `1.25 = 1.01000000000000000000000 x 2^0`
   - `3.5 = 1.11000000000000000000000 x 2^1`

2. **Multiply the Mantissas:**
   - Multiply:
     ```
     1.01000000000000000000000
     * 
     1.11000000000000000000000
     = 
     1.11010000000000000000000
     ```

3. **Add the Exponents:**
   - Add exponents: `0 + 1 = 1`

4. **Normalize the Result:**
   - The result is already normalized: `1.11010000000000000000000 x 2^1`

5. **Handle Rounding:**
   - Round the mantissa if needed (no rounding needed in this case).

6. **Final Result:**
   - The product is `1.1101 x 2^2`, which equals **5.5** in decimal.

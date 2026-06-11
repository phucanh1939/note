---
title: Addition And Substraction
---

# Floating Point Addition and Substraction

## Steps for Floating Point Addition:

1. **Align the Exponents:**
   - Compare the exponents of the two numbers.
   - Shift the smaller exponent’s mantissa to the right until the exponents are equal.
   - Adjust the exponent of the smaller number accordingly.

2. **Add or Subtract Mantissas:**
   - Add the mantissas if the numbers have the same sign.
   - Subtract the mantissas if the numbers have opposite signs.
   - The result’s sign depends on the larger (absolute) mantissa.

3. **Normalize the Result:**
   - After addition or subtraction, normalize the result so that the leading 1 is placed before the decimal point (unless subnormal).
   - Adjust the exponent if necessary to reflect any shifts in the mantissa.

4. **Round the Result:**
   - Round the mantissa to the nearest representable value based on the precision of the floating point format.

5. **Final Result:**
   - The final result includes:
     - The sign of the sum.
     - The adjusted exponent.
     - The rounded and normalized mantissa.

---

### Example: Adding 1.25 and 3.5 (IEEE 754 Single Precision)

1. **Convert to Binary (Normalized Form):**
   - `1.25 = 1.01000000000000000000000 x 2^0`
   - `3.5 = 1.11000000000000000000000 x 2^1`

2. **Align Exponents:**
   - Shift 1.25 to match the exponent of 3.5: `0.10100000000000000000000 x 2^1`
   - Both exponents are now 1.

3. **Add Mantissas:**
   - Add the mantissas: 
     ```
     0.10100000000000000000000 
     + 
     1.11000000000000000000000 
     = 
     10.01100000000000000000000
     ```

4. **Normalize:**
   - Normalize the result: `1.00110000000000000000000 x 2^2`
   - Exponent is adjusted to 2.

5. **Handle Rounding:**
   - Round the mantissa (if needed) to the desired precision.

6. **Final Result:**
   - The sum is `1.0011 x 2^2`, or **4.75** in decimal.

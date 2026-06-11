---
title: Rounding
---

# Floating Point Rounding

In floating-point arithmetic, when a result exceeds the precision limits of the mantissa, rounding is necessary. 
There are two methods of rounding:
1. **Normal Rounding** (without guard, round, and sticky bits)
2. **Rounding with Guard, Round, and Sticky Bits** (using additional bits for better accuracy)

## Normal Rounding (Without Guard, Round, and Sticky Bits):
- **Normal rounding** involves simply truncating the extra bits after the desired precision and rounding the last bit based on the value of the next bit.
- Typically, **round half-up** is used:
  - **If the next bit is 5 or greater**, round up the last retained bit.
  - **If the next bit is less than 5**, leave the last retained bit unchanged.

### Rounding with Guard, Round, and Sticky Bits:
The **guard bit (G)**, **round bit (R)**, and **sticky bit (S)** improve the accuracy of rounding by using extra bits for more precise rounding decisions.

- **Guard Bit (G)**: The first bit after the last mantissa bit that is kept temporarily for rounding.
- **Round Bit (R)**: The second bit after the guard bit, used for refining the rounding decision.
- **Sticky Bit (S)**: A bit that records if any non-zero bits exist beyond the round bit.

## Rounding Rules (With Guard, Round, and Sticky Bits):

1. **Examine the bits (G, R, S)**.
2. **Rounding Decisions:**
   - **If Sticky Bit (S) = 1**: Always round up.
   - **If Sticky Bit (S) = 0**:
     - **If Guard Bit (G) = 1**: Round up.
     - **If Round Bit (R) = 1**: Round up.
     - **If G = 0 and R = 0**: No rounding (keep the value as is).

## Final Rounding Logic:
- **Round Up**:
  - If G = 1, or if R = 1 and S = 1.
  - If S = 1 (sticky bit is set), always round up.
- **No Rounding**:
  - If G = 0 and R = 0, keep the value as is.

### Example:

Let's round `3.14159265358979` (approximately) to a precision of 4 decimal places.

- **Normal Rounding**:
  - Truncate to 4 decimal places: `3.1415`
  - Next bit is `9`, so we round up to `3.1416`.

- **Rounding with Guard, Round, and Sticky Bits**:
  - Original number in binary (for the sake of simplicity, we'll only consider a few bits):
    ```
    11.0010010000111111011010101000010001000010110100011111...
    or
    1.10010010000111111011010101000010001000010110100011111... x 2 ^ 1
    ```
    
  - We want to round to the 4th decimal place, so we look at the **Guard**, **Round**, and **Sticky** bits.
  - The number has the following bits beyond the 4th decimal place:
    - **Guard bit (G)** = `1` (last bit of 1.1001)
    - **Round bit (R)** = `0` (next to G bit)
    - **Sticky bit (S)** = `1` (since there are still non-zero bits beyond the round bit).

  - **Rounding decision**:
    - Since the **Sticky bit (S)** = `1`, we always round up.
    - The rounded result is `3.1416`.

## Comparison: Normal Rounding vs Guard-Round-Sticky Rounding:

| Rounding Method        | Condition                                    | Action                         |
|------------------------|----------------------------------------------|--------------------------------|
| **Normal Rounding**    | If next bit ≥ 5                              | Round up                       |
|                        | If next bit < 5                              | Leave as is                    |
| **Guard-Round-Sticky** | If Sticky Bit (S) = 1                        | Always round up                |
|                        | If Sticky Bit (S) = 0 and Guard Bit (G) = 1  | Round up                       |
|                        | If Sticky Bit (S) = 0 and Guard Bit (G) = 1  | Round up                       |
|                        | If Sticky Bit (S) = 0 and Round Bit (R) = 1  | Round up                       |
|                        | If Sticky Bit (S) = 0 and Round Bit (R) = 1  | Round up                       |
|                        | If Sticky Bit (S) = 0, G = 0, and R = 0      | No rounding                    |

## Benefits of Guard-Round-Sticky Rounding:
- **More accurate**: By keeping track of the bits beyond the mantissa, this method ensures that rounding decisions are based on more data, making it less prone to errors caused by truncation.
- **Prevents significant errors**: Especially important in repeated calculations, where small rounding errors can accumulate.

### Final Thoughts:
- **Normal rounding** is simple and quick, but it may result in less accurate results, especially for numbers that are close to rounding thresholds.
- **Guard, round, and sticky bit rounding** is more precise and prevents small errors from accumulating in floating-point operations.

---
title: Addtion And Substraction
---

# Integer Addition and Substraction

`Addition`: digits are added bit by bit from right to left, with carries passed to the next digit to the left, just as you would do by hand

`Subtraction` uses addition: the appropriate operand is simply negated before being added

Example: 7 + 6

```
    0000 0111 ( 7)
  + 0000 0110 ( 6)
  ---------------
         1101 (13)
```

Example: 7 - 6 = 7 + -6

```
    0000 0111 ( 7)
  + 1111 1010 (-6)
  ---------------
    0000 0001 (13)
```

## Overflow

Overflow occurs when the result from an operation cannot be represented with the available hardware.
Overlow in addition and subtraction can be detect using the sign of result and operands.

- Adding 2 positive number, result is negative => Overflow
- Adding 2 negative number, result is positive => Overflow

Example: Adding 4-bits integers: 0111 (15) + 0001 (1) = 1000 (-16) => Overflow


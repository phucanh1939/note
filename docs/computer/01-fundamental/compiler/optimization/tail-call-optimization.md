---
title: Tail Call Optimization
---

# Tail Call Optimization (TCO)

Tail Call Optimization (TCO) is an optimization technique used by compilers to improve the performance of recursive functions.
Normally, each recursive call adds a new frame to the call stack.
With tail call optimization, the compiler reuses the current function’s stack frame for the recursive call instead of creating a new one, making the recursion constant in space

## How it work

In a tail call, the recursive function call is the last operation in the function.
Once the function call is made, no further computation is required in the current function.
The result of the recursive call is immediately returned as the final result.

## Example

### Without TCO

If the recursive function is not tail call, compiler can NOT apply the optimization, stack frames will be created over recursive calls

```c
int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);  // Not a tail call
}
```

```asm
factorial:
    # Function prologue
    addi    $sp, $sp, -8         # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Allocate space on stack - NEW STACK FRAME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sw      $ra, 4($sp)          # Save return address
    sw      $a0, 0($sp)          # Save argument n

    # Check if n == 0
    beq     $a0, $zero, .L1       # If n == 0, go to base case

    # Recursive call: n * factorial(n-1)
    addi    $a0, $a0, -1         # Decrement n by 1
    jal     factorial            # Recursive call

    # After return from recursion, multiply result by n
    lw      $a0, 0($sp)          # Load original n
    mul     $v0, $a0, $v0        # Multiply result of factorial(n-1) with n

    # Return
    j       .L2                  # Jump to function epilogue

.L1:   
    # Base case: return 1
    li      $v0, 1               # Return 1 if n == 0

.L2:
    # Function epilogue
    lw      $ra, 4($sp)          # Restore return address
    addi    $sp, $sp, 8          # Deallocate space from stack
    jr      $ra                  # Return
```

### With TCO

If the recursive function is tail call, compiler will apply the optimiazation, no stack frame needed for recursive calls

```c
int factorial_helper(int n, int acc) {
    if (n == 0) return acc;
    return factorial_helper(n - 1, n * acc);  // Tail call
}

int factorial(int n) {
    return factorial_helper(n, 1);
}
```

```asm
factorial_helper:
    # Check if n == 0
    beq     $a0, $zero, .L1      # If n == 0, go to base case

    # Tail recursive call: factorial_helper(n-1, n*acc)
    addi    $a0, $a0, -1         # Decrement n by 1
    mul     $a1, $a0, $a1        # Multiply acc by n
    jal     factorial_helper     # Tail call with new arguments (n-1, n*acc)
    jr      $ra                  # Return (after tail call, no more instructions)

.L1:
    # Base case: return acc
    move    $v0, $a1             # Return acc when n == 0
    jr      $ra                  # Return

factorial:
    # Initial call to factorial_helper with (n, 1)
    move    $a1, $zero           # Set accumulator (acc) to 1
    jal     factorial_helper     # Call factorial_helper(n, 1)
    jr      $ra                  # Return
```
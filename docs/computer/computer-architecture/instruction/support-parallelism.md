---
title: Support Parallelism
---

# Support Parallelism Instructions

To ensure parallelism tasks cooperate without interference, synchronization mechanisms are typically implemented using hardware primitives that allow for atomic operations, meaning that a read and write to a memory location happen without interruption.

This ensures that no other task can modify the data between the read and write operations.

### Atomic Exchange and Synchronization Primitives

One basic synchronization operation is the atomic exchange (swap), where a value in a register is exchanged with a value in memory. This operation helps to manage locks in parallel systems, where a value of 0 indicates that a lock is free and 1 indicates the lock is unavailable.

Example of Atomic Exchange:
- A processor tries to claim a lock by exchanging a 1 from a register with the lock in memory.
- If the lock was already set (1), the processor will see the old value and know it failed to acquire the lock.
- If the lock was free (0), the processor sets it to 1 and acquires the lock, preventing other processors from simultaneously acquiring it.
- Simultaneous attempts to acquire the lock by multiple processors are handled atomically, ensuring that only one processor successfully acquires the lock.

### Hardware Primitives in MIPS for Synchronization

In MIPS architecture, the load linked (ll) and store conditional (sc) instructions are used together to create atomic operations

- Load Linked (ll): Loads the value from memory to register and marks the memory location as "linked" to track changes (set the value of Linked Register to the address).
- Store Conditional (sc): Attempts to store a new value from register to the same memory location. It succeeds only if the memory content has not changed since the ll instruction (still linked). If it succeeds, the value in the register is updated (the linked mark is removed); if it fails, the operation must be retried.

```asm
again:
    ; Load value at memory address (stored in $s1) into $t1, mark this address "linked"
    ll $t1, 0($s1)

    ; Do some calculation of the value t1 = t1 + 1
    addi $t1, $t1, 1

    ; Try to store value from t1 the the same memory, 
    ; if this memory address is still linked (not changed), then store value and set t1 to 1, orther wise t1 will be 0
    sc $t1, 0($s1) 
    
    ; If sc failed, try again
    beq $t1, $zero, again   ; If sc fails (lock already set), retry

    ; sc success, continue the program
    add $s4, $zero, $t1     
```

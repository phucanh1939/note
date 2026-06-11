---
title: Function
---

# Function / Proceture

Function or procedure are higher-level construct/concept in programming that encapsulate reusable code.

At their core, they are a set of instructions with a specific address or label in memory.
These instructions are loaded into memory when the program starts running and can be invoked using a jump instruction to their address.

## **How Functions Work in Low-Level Implementation**

1. **Save the Return Address**:  
   The program saves the address of the instruction immediately after the function call into a specific register (e.g., `$ra`, the return address register) or onto the stack.

2. **Pass Function Parameters**:  
   Function parameters are pushed into a location where the function can access them, such as:  
   - **Function Parameter Registers** (e.g., `$a0, $a1` in MIPS).  
   - **The Stack**, when there are more param needed then number of param registers

3. **Save the Current Register State**:  
   The current values of registers are saved (typically onto the stack) to preserve their state before the function modifies them.

4. **Execute the function instructions**:  
   Executing its instructions.

5. **Store the Result (Return Value)**:  
   After executing the function, the result is stored in specific registers designated for return values (e.g., `$v0`, `$v1` in MIPS).

6. **Restore Registers**:  
   Registers modified during the function are restored to their original state (from the stack) to ensure continuity in the calling program.

7. **Return to the Caller**:  
   A jump instruction is used to transfer control back to the return address stored in `$ra` or retrieved from the stack.

## Example

```asm
# Main Program
MOVE $a0, 5         # Pass first parameter
MOVE $a1, 3         # Pass second parameter
JAL MyFunction      # Jump and link to MyFunction ($ra will store address of the instruction right after the function call - the instruction MOVE below)

# Use the return value from MyFunction
MOVE $t0, $v0       # Store the result in $t0 for further processing
MUL $t1, $t0, 2     # Multiply the result by 2 and store it in $t1

MyFunction:
PUSH $s0-$s7, $ra   # Save callee-saved registers
ADD $v0, $a0, $a1   # Execute the function, store result in $v0
POP $s0-$s7, $ra    # Restore callee-saved registers
JR $ra              # Jump back to return address
```


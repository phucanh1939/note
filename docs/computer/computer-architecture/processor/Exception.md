---
title: Exception
---

# Exception Handling

Exceptions and interrupts are events that alter the normal execution flow of a program. These events can be triggered by software or hardware and require the processor to take appropriate actions to handle them.

## Types of Exceptions

### 1. **Synchronous Exceptions**
Synchronous exceptions occur as a direct result of executing an instruction. These exceptions are predictable and happen at the same point every time the instruction executes.

#### Examples:
- **Arithmetic Exception**: Division by zero, overflow, or underflow.
- **Illegal Instruction**: Executing an invalid or unimplemented instruction.
- **Page Fault**: Accessing a memory page that is not currently mapped.
- **System Calls**: User programs request services from the operating system.

### 2. **Asynchronous Exceptions (Interrupts)**
Asynchronous exceptions occur due to external events and are not related to the execution of a specific instruction.

#### Examples:
- **Hardware Interrupts**: Triggered by external devices (e.g., keyboard, mouse, network, disk I/O).
- **Timer Interrupts**: Generated periodically to allow multitasking.
- **Power Failure**: Emergency handling for sudden power loss.

## Exception Handling Process
When an exception occurs, the processor follows these steps to handle it:

1. **Detect the Exception**: The processor identifies the exception and classifies it.
2. **Save Execution State**: The current program counter (PC) and processor state are saved to allow resumption later.
3. **Jump to Exception Handler**: The processor transfers control to a predefined exception handler in the operating system or firmware.
4. **Execute Exception Handler**: The handler determines the cause of the exception and takes the appropriate action (e.g., terminate the program, retry the instruction, allocate memory, etc.).
5. **Resume or Terminate Execution**: After handling the exception, the processor either resumes execution from the saved state or terminates the program if recovery is not possible.

## Exception Handling Mechanisms
- **Polling**: The processor periodically checks for exceptions (inefficient for real-time processing).
- **Vectored Interrupts**: The processor jumps directly to the appropriate interrupt handler based on an interrupt vector table.
- **Priority Handling**: When multiple exceptions occur, the processor prioritizes them based on predefined levels.
- **Nested Exceptions**: Some systems allow exceptions to be interrupted by higher-priority exceptions.

Efficient exception handling is crucial for system stability and performance, ensuring smooth execution even in the presence of unexpected events.


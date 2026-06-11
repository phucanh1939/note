---
title: Program
---

# Program

## What is a Program

A **program** is a set of instructions (defines a task) that a computer can execute.

## How does a Program is created

- Programmer writes the source code in a high-level programming language (C, Java, Python, etc.).
- The source code is converted into machine code by a **[compiler]** and a *linker*

## How does computer execute a program?

### Executable program

- 1. **Loading**:
   - The operating system (OS) loads the program's executable file into memory.
   - Necessary resources (e.g., shared libraries, data) are also loaded into memory.
- 2. **Linking**
   - If the program uses dynamic linking, unresolved references to shared libraries are resolved at this stage.
   - This is sometimes called **runtime linking**.
- 3. **Initialization**:
   - The runtime environment prepares the program for execution:
     - Sets up the execution context (e.g., stack, heap, global variables).
     - Allocates resources needed by the program.
   - Control is handed over to the program’s entry point (e.g., `main()` in C/C++).
- 4. **Execution**:
   - The CPU begins executing the instructions loaded into memory.
   - The program performs its intended tasks until completion.

### Bytecode program

Bytecode program need a runtime to run on

1. **Class Loading**:
  - The run-time reads the bytecode files and metadata to locate the entry point (the main method or other designated starting point) and its dependencies.
  - A loader (a run-time component) then loads all the necessary bytecodes into memory.

2. **Bytecode Execution**:
  - The runtime begins executing bytecode instructions one by one from the entry point function.
  - A **Just-In-Time (JIT) Compiler** is used to convert bytecode instruction to machine code and execute it.
  - Additional, machine code may be cached for faster execution latter.

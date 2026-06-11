---
title: Dynamic Linking
---

# Dynamic Linking

In dynamic linking, external libraries are not included in the executable. References to functions or variables in shared libraries are resolved at runtime when the program is executed.

## Start-time linking

Early implementations of dynamic libraries would load the entire library into memory and resolve all symbols at startup. This was inefficient because:
  - Large libraries with many unused functions would waste memory.
  - Startup times were significantly longer.

## Run-time linking (lazy binding)

Lazy binding solves start-time linking issue issues by only load the needed functions/routines when required.

When a program is running and a call to a routine in a dynamic library occurs, the process is as follows:

1. **Initial Jump to a Stub (PLT Stub):**
   - The program does **not** directly jump to the actual code of the dynamic library routine because the library has not been loaded into memory yet.
   - Instead, the jump instruction points to a *stub* or *dummy entry point* (typically in the **Procedure Linkage Table (PLT)**).
   - This stub contains code to handle the dynamic routine call indirectly.

2. **Stub Prepares the Call:**
   - The stub typically:
     - Saves a unique identifier (e.g., an offset or index) in a register or on the stack. This identifier indicates which dynamic library routine is needed.
     - Transfers control to the **dynamic linker/loader**.

3. **Dynamic Linker/Loader Resolves the Address:**
   - The dynamic linker/loader reads the identifier to determine the required routine.
   - It performs the following steps:
     - If the library is not yet loaded, it maps the dynamic library into memory.
     - Resolves the function symbol to its actual address in the library.
     - If necessary, performs **relocation** to ensure the function can be called directly.

4. **Relocation of the Jump Instruction:**
   - After resolving the address of the function, the dynamic linker/loader modifies the stub (or jump instruction `X`) to directly point to the resolved address of the function.
   - This ensures that subsequent calls bypass the stub and jump directly to the function.

5. **Subsequent Calls:**
   - Once the relocation is done, the actual address of needed dynamic routine is updated in PLT.
   - This means that **indirect jumps only happen once**, during the first call.

6. **Benefits of Lazy Binding:**
   - This process is known as **lazy binding**, where functions are resolved only when called for the first time. This improves:
     - **Startup time** by deferring the resolution of unused symbols.
     - **Memory usage** by not loading the entire library unnecessarily.
   - After the first call, there is no additional overhead since all calls go directly to the resolved function.

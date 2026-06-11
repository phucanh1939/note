---
title: Object File
---

# Object file

An object file is output of compiler after compile a source file.
This file stores machine language instructions, data and information needed to place instructions properly in memory.

## General Structure

Different system (OS) have different object file format, below is the gerenal parts may found in an object file.

The must-have info in object file includes: header(info how to read the file), binary instructions, relocation info, symbols table, data/constant (if any)

### 1. Header
- Provides basic information about the file.
- Includes:
  - File format/type (e.g., ELF, Mach-O, PE/COFF).
  - Machine architecture (e.g., x86, ARM).
  - Endianness.
  - Versioning.
  - High-level structural metadata (e.g., offsets to tables like the symbol table, relocation sections).

### 2. Segments
- High-level groups of **sections**.
- Represent logical regions such as:
  - Code.
  - Data.
  - Dynamic linking information.
- Examples:
  - In **ELF**, segments are defined in the **program header table**.
  - In **Mach-O**, segments are defined in **load commands** (this is a part of the object file come after the header).

### 3. Sections
- Contain the actual data (e.g., binary instructions, variables, constants).
- Examples:
  - `.text` → Code (binary instructions).
  - `.data` → Initialized global variables.
  - `.bss` → Uninitialized global variables.
  - `.rodata` → Read-only data.

### 4. Relocation Entries
- Defined in a special section **relocation sections** (e.g., `.rel.text` in ELF).
- Specify what needs to be adjusted (e.g., symbol addresses, offsets).
- Guide the linker on address adjustments when combining object files.

### 5. Symbol Table
- Lists all symbols in the file, including: Functions. Global variables. External references.
- Used by the linker to resolve references between object files.
- Typically stored in a dedicated section (e.g., `.symtab` in ELF or the COFF symbol table).

### 6. The debugging information 
- Contains a concise description of how the modules were compiled so that a debugger can associate machine instructions with C source files and make data structures readable

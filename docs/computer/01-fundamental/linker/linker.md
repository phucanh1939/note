---
title: Linker
---

# Linker

## What is linker
The **linker** combines object files to create an executable program.

Types of linking:
- [Static Linking]: All the code and data from external libraries are included directly in the executable at compile time
- [Dynamic Linking]: References to functions or variables in shared libraries are resolved at runtime

## How does linker link object files

The linking proces:
- Combine Instructions: merges machine instructions and data from multiple object files into a single binary.
- Resolve Symbols: Matches and resolves references to symbols (e.g., functions, variables) across object files.
- Relocate Addresses: Adjusts symbol addresses and offsets to map correctly into the program's **virtual address space** (This virtual address space is where the operating system loads the program during execution).

[Static Linking]:   ./StaticLinking
[Dynamic Linking]: ./DynamicLinking

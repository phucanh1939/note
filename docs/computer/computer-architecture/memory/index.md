---
title: Memory
---

# Memory

Computer memory is used to store program instructions and data — including input, output, and data used during execution.

## Building Blocks

At the hardware level, memory is built from basic digital circuits:

- **Latch**: A simple circuit that can store 1 bit of data using feedback loops (level-triggered)
- **Flip-Flop**: A more stable version of a latch, stores 1 bit and changes state on clock edge (edge-triggered)
- **Memory Cell**: A circuit (often built from latches or transistors) that stores a bit in RAM

## Memory Hierarchy

Processor speed is much faster than memory access speed. To bridge this gap, memory is organized into a hierarchy:

| Level             | Speed     | Size     | Cost            | Proximity to CPU |
|------------------|-----------|----------|-----------------|------------------|
| Register          | Fastest   | Smallest | Most Expensive  | Closest          |
| L1 Cache          | Very Fast | Very Small | High          | On-chip          |
| L2 / L3 Cache     | Fast      | Small    | Medium          | On-chip/near     |
| Main Memory (RAM) | Moderate  | Large    | Moderate        | Off-chip         |
| Disk (HDD/SSD)    | Slowest   | Largest  | Cheapest        | Farthest         |

> **Note**: Smaller, faster memory is placed closer to the CPU. Frequently accessed data is kept in faster memory to improve performance.

## Virtual Memory

Virtual memory is a memory management technique that enables:

- Programs to use more memory than physically available (by using disk as extra memory)
- Multiple programs to safely share the same physical memory

### How it Works

- Each program has its **own virtual address space**
- The **compiler** uses virtual addresses in the binary
- At runtime, the **Memory Management Unit (MMU)** translates virtual addresses into **physical addresses**
- The **Operating System (OS)**:
  - Allocates memory in **pages** (fixed-size blocks)
  - Swaps pages in/out between **RAM** and **disk** as needed (paging)

This system ensures:
- Isolation between programs
- Efficient use of RAM
- Execution of programs larger than available RAM

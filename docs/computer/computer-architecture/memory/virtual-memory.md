---
title: Virtual Memory
---

# Virtual Memory

## What is Virtual Memory?
Virtual memory is a memory management technique that provides an abstraction of physical memory, allowing programs to use a larger address space than what is physically available. The operating system (OS) manages virtual memory by mapping virtual addresses to physical memory locations using a process called **paging**.

More importantly, virtual memory supports sharing of the main memory among multiple, simultaneously active processes, in a protected manner

## Why Was Virtual Memory Created?
Virtual memory was introduced to address the following challenges:

- **Programs requiring more memory than available:**
  - Large-scale applications (e.g., video editing, 3D rendering, big data processing)
  - High-performance games and scientific simulations
  - Web browsers with multiple open tabs consuming large amounts of memory
  - Virtual machines and containers running multiple instances simultaneously

- **Efficient multi-programming:**
  - Allows multiple programs to run simultaneously without memory conflicts
  - Prevents system crashes due to memory shortages

## How Virtual Memory Works

### Compiler Assumptions
When a program is compiled, the compiler assumes that the program has a **continuous block of memory**. It generates **virtual memory addresses** based on this assumption.

### OS Memory Setup with Pages
When a program starts, the OS:
1. Allocates memory in **pages** (fixed-size blocks, typically 4KB or more).
2. Loads the program's instructions into memory in pages.
3. Creates a **Page Table** for each process, mapping virtual addresses to physical addresses.
   - Since Page Tables can be large, techniques like multi-level paging and inverted Page Tables help reduce their size.
4. Allocates a space on disk (swap space) for pages that may need to be stored temporarily when RAM is full.

### Runtime Memory Access
When a program accesses memory, it does so using a **virtual address**. The following steps occur:

1. **Address Translation:**
   - The **Memory Management Unit (MMU)** converts the virtual address into a physical address using the **Page Table**.
   - Since the Page Table is stored in RAM, accessing it directly is slow. To speed up address translation, the **Translation Lookaside Buffer (TLB)** (a small cache) stores recently used Page Table entries.

2. **Fetching Data:**
   - Once the physical address is obtained, the CPU first checks if the data is in the **cache**.
   - If **cache hit**, data is retrieved quickly.
   - If **cache miss**, data is fetched from RAM.
   - If the data is not in RAM (i.e., a **page fault** occurs), the OS loads the required page from disk and choose a page on RAM to replace if needed

### Page Faults and Swapping
A **page fault** happens when a program accesses a page that is not currently in RAM. The OS then:
1. Loads the missing page from disk into RAM.
2. If RAM is full, it selects a page to **evict** (swap out to disk) using a **page replacement algorithm**.

#### Page Replacement Algorithms
Common strategies include:
- **Least Recently Used (LRU):** Replaces the page that has not been used for the longest time.
- **First-In-First-Out (FIFO):** Replaces the oldest loaded page.
- **Optimal Page Replacement:** Replaces the page that will not be used for the longest future period (requires future knowledge).

#### Writting Operation
Writes to secondary memory are expensive, so virtual memory uses a write-back scheme and also tracks whether a page is unchanged (using a dirty bit) to avoid writing unchanged pages

## Performance Considerations
- **Page faults are slow:** Accessing data from disk is much slower than from RAM.
- **Thrashing:** Excessive page faults lead to **thrashing**, where the system spends more time swapping pages than executing processes, significantly degrading performance.
- **Optimizations:**
  - **Demand Paging:** Loads pages only when needed.
  - **Prefetching:** Anticipates and loads pages before they are needed.
  - **Increasing RAM:** Reduces the need for swapping and improves performance.

## Summary
Virtual memory enables efficient and flexible memory management, allowing modern operating systems to run complex applications without being limited by physical memory constraints.


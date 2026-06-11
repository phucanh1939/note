---
title: Memory Allocation
---

# **Memory Allocation in Runtime**

## **Types of Memory Allocation**
1. **Static Allocation** → Global/static variables, allocated at compile-time.
2. **Stack Allocation** → Local variables, function calls.
3. **Heap Allocation** → Dynamic memory (`malloc()`, `new`).

## **How `malloc()` Works?**
1. **Program calls `malloc(size)`.**
2. **Memory Manager (glibc) checks available space in heap.**
3. **If not enough space, OS is asked for more memory.**
   - Uses `brk()` to expand the heap.
   - Uses `mmap()` for large allocations.
4. **OS allocates memory and updates the process memory map.**
5. **`malloc()` returns a pointer to the allocated memory.**

## **Memory Fragmentation**
- **Internal fragmentation** → Small gaps inside allocated blocks.
- **External fragmentation** → Free memory is split into non-contiguous blocks.

## **Garbage Collection & Freeing Memory**
- **Manual** → `free(ptr)`, `delete ptr`.
- **Automatic** (in languages like Python, Java).
- **Memory Leaks** → When allocated memory is never freed.

## **Memory Management System Calls**
- **Linux:** `brk()`, `mmap()`, `munmap()`, `sbrk()`.
- **Windows:** `VirtualAlloc()`, `HeapAlloc()`, `GlobalAlloc()`. 

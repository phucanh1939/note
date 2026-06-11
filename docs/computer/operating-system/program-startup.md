---
title: Program Startup
---

# **Program Startup**

## **How a Program Starts?**
1. **User Requests Execution**
    - CLI (e.g., `./a.out`)
    - GUI (double-click an icon)
2. **OS Creates a Process**
    - Loads the executable file.
    - Assigns **at least one thread**.
    - Allocates memory for code, stack, heap, and data.
3. **OS Initializes Execution**
    - Sets up **program counter (PC)**.
    - Loads **shared libraries (if needed)**.
4. **Process Starts Running**
    - OS scheduler selects the process.
    - CPU executes the instructions.

## **Program Memory Layout**
| Segment | Description |
|---------|------------|
| **Code** | Executable instructions |
| **Data** | Global/static variables |
| **Heap** | Dynamically allocated memory (malloc/new) |
| **Stack** | Function calls, local variables (**each thread gets its own stack**) |

## **How a Process Ends?**
- **Normal exit** (`return 0;`, `exit()`, `_exit()`).
- **Exception/crash** (segfault, illegal instruction).
- **Killed by OS (`kill PID`) or another process.**
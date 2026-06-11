---
title: Process
---

# **Process**

## **What is a Process?**
A process is an independent execution unit with its own memory space.

## **Key Characteristics**
- Has its own **memory space (heap, data, code).**
- Can have multiple **threads**.
- Managed by the **OS process scheduler**.
- Can communicate with other processes using **IPC (Inter-Process Communication)**.
- **Processes do not have a single unified stack**; instead, each thread within a process has its own stack.

## **Process Lifecycle**
1. **New** → Process is created.
2. **Ready** → Waiting to be assigned to a CPU.
3. **Running** → Currently executing.
4. **Waiting** → Blocked, waiting for I/O.
5. **Terminated** → Process execution completed.

## **Process Creation (System Calls)**
A program can create a new process and execute code in it at runtime using system calls.
- **Linux:** `fork()`, `exec()`, `waitpid()`
- **Windows:** `CreateProcess()`

## **Process vs. Thread**
| Feature  | Process | Thread |
|----------|---------|--------|
| Memory Isolation | Yes | No (shares memory) |
| Communication | IPC (slow) | Shared memory (fast) |
| Creation Overhead | High | Low |
| Context Switch Cost | High | Low |

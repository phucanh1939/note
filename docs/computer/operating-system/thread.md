---
title: Thread
---

# **Thread**

## **What is a Thread?**
A thread is the smallest unit of execution within a process. Multiple threads share the same process memory but execute independently.

## **Key Characteristics**
- Each thread has its own **stack**, **program counter**, and **registers**.
- Threads **share memory and resources** within the same process.
- Threads are managed by the OS **scheduler**.
- Threads can run in **parallel** on multi-core CPUs.

## **Types of Threads**
1. **User Threads** → Managed by libraries (e.g., pthreads in Linux).
2. **Kernel Threads** → Managed directly by the OS.

## **Thread Lifecycle**
1. **New** → Created but not started.
2. **Runnable** → Ready to run.
3. **Running** → Actively executing on a CPU.
4. **Blocked/Waiting** → Waiting for resources.
5. **Terminated** → Execution finished.

## **Thread Scheduling**
- OS dynamically assigns threads to CPU cores.
- Uses **preemptive scheduling** (interrupt-based).
- Threads can be moved between cores by the OS.

## **Thread Synchronization**
- **Mutexes** → Prevent race conditions.
- **Semaphores** → Control resource access.
- **Condition Variables** → Manage thread communication.

## **Threads and CPU Cores**
- **Single-threaded Core:** Only one thread runs at a time per core.
- **Multi-threaded Core (Hyper-Threading / SMT):** One core can run multiple threads simultaneously by sharing execution resources.
- **Modern CPUs:** Most modern processors use **multi-threaded cores** (e.g., Intel Hyper-Threading, AMD SMT) to improve performance.

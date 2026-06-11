---
title: Parallelism
---

# Parallelism Processing

## Data-Level Parallelism (DLP)

### What is DLP?
- Performing the **same operation** on **multiple data elements** at once.
- Key idea: **parallelism in data**, not instructions.

### Example Use Cases
- Image processing (e.g. apply filter to pixels)
- Audio processing (e.g. mix multiple samples)
- Physics simulations (e.g. apply gravity to many objects)

### How It's Achieved
- **SIMD (Single Instruction, Multiple Data)**:
  - One instruction handles multiple data values.
  - E.g., Add two 4-element vectors in one operation.
- **Vector Processors**:
  - Specialized for operations on arrays/vectors.
- **GPUs**:
  - Highly optimized for massive DLP (e.g., thousands of threads doing the same math).

### Hardware Support
- CPU SIMD Extensions: **SSE**, **AVX**, **NEON**, etc.
- GPUs: Designed for **massive data-parallel workloads**.

### Benefits
- Great for **bulk processing** (arrays, matrices, pixels).
- High throughput with less control logic.

### Challenges
- Requires **data alignment** and **uniform operations**.
- Less useful if data is highly irregular or control flow varies.

---
title: Instruction Level Parallelism
---

## Instruction Level Parallelism (ILP)

Instruction Level Parallelism (ILP) refers to the ability of a processor to execute multiple instructions simultaneously. The goal is to increase performance by overlapping instruction execution.

There are two primary methods for increasing the potential amount of instruction-level parallelism:

1. **Deep Pipelining** - Increasing the depth of the pipeline to allow more instructions to overlap in execution.
2. **Multiple Issue** - Replicating internal components of the processor to enable multiple instructions to be issued in every pipeline stage.

### Deep pipelining

Increasing the depth of the pipeline to allow more instructions to overlap in execution

### Multiple Issue

#### Static Multiple Issue

Static multiple issue, also known as **VLIW (Very Long Instruction Word)**, relies on the compiler to determine which instructions can be issued in parallel. The compiler schedules instructions at compile time to avoid hazards and maximize parallel execution.

Characteristics of Static Multiple Issue:
- The compiler handles instruction scheduling.
- No hardware-based dynamic scheduling.
- Simpler control logic, but requires sophisticated compiler techniques.
- Works best with predictable instruction dependencies.

#### Dynamic Multiple Issue

Dynamic multiple issue, also known as **Superscalar Execution**, allows the processor to decide at runtime which instructions can be issued simultaneously. The hardware dynamically schedules instruction execution, reducing the burden on the compiler.

Characteristics of Dynamic Multiple Issue:
- The processor determines instruction scheduling dynamically.
- More complex control logic, requiring mechanisms like register renaming and dependency checking.
- Better performance in unpredictable workloads compared to static multiple issue.

##### Dynamic Pipeline Scheduling

Dynamic pipeline scheduling is a key feature of dynamic multiple issue processors. It allows out-of-order execution, where instructions can be reordered to maximize parallelism while maintaining program correctness.

Key Components of Dynamic Pipeline Scheduling:
- **Instruction Window**: Holds a set of instructions waiting to be scheduled.
- **Reorder Buffer (ROB)**: Ensures instructions commit in program order to maintain correctness.
- **Reservation Stations**: Store instructions waiting for operands, allowing execution as soon as dependencies are resolved.
- **Register Renaming**: Eliminates false dependencies (write-after-read and write-after-write hazards).

## Data Level vs Instruction Level Parallelism

| Feature | DLP (Data-Level) | ILP (Instruction-Level) |
|--------|------------------|--------------------------|
| What? | Same operation on multiple data | Multiple instructions executed in parallel |
| Example | Add 4 floats at once | Add + Multiply at same time |
| Hardware | SIMD units, GPUs | Superscalar CPUs |

## Writting program to use parallelism hardware

### 1. Task Decomposition
- Hard to split some problems into independent parts.
- Not all tasks are parallelizable.

### 2. Load Balancing
- Uneven workload causes bottlenecks.
- All threads/cores must stay busy for efficiency.

### 3. Data Sharing & Synchronization
- Shared data needs careful handling.
- Risk of race conditions, deadlocks, and data corruption.
- Requires locks, mutexes, or atomic operations.


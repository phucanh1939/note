---
title: Memory Hierarchy
---

# Memory Hierarchy

## What is Memory Hierarchy

Memory hierarchy is the structure that organizes computer memory into levels based on speed, cost, and size to keep pace with faster processor (memory access is too slow compare to processor calculations). It helps balance performance and cost by using fast, expensive memory close to the CPU and slower, cheaper memory further away.

### Why it matters:
Using fast memory for frequently accessed data improves performance while keeping costs down by using slower memory for less critical data.

### From fastest (smallest) to slowest (largest):
- Registers – inside the CPU, extremely fast, very small.
- L1 Cache – fastest cache, closest to CPU, each core.
- L2 Cache – larger, slower than L1, each core.
- L3 Cache – larger, slower than L2, share between cores.
- RAM (Main Memory) – larger, slower than cache.
- SSD/HDD (Storage) – very large, much slower.
- Cloud/Network Storage – slowest, used for backup or remote data.

## How does Memory Hierarchy work
In general, memory hierarchy works by keeping the most frequently accessed data in the fastest, smallest memory levels, and moving less-used data to slower, larger memory. The principle of locality is used to predict which data will be accessed soon, so the system can keep that data in the faster memory levels

Key idea: Faster memory is more expensive and smaller, so we use it wisely by storing only what’s likely needed soon.

### Common Framework for Memory Hierachy

These policies are four questions that apply between any two levels of a memory hierarchy

#### Where Can a Block Be Placed (Structure)

Blocks are placed in **sets**. The way blocks are mapped to sets determines the cache structure:

| Type              | Blocks per Set | Access Speed       | Miss Rate     | Common Usage                   |
|-------------------|----------------|---------------------|----------------|--------------------------------|
| Direct Mapped     | 1              | Fast (index only)   | High           | Simple, small caches           |
| Set Associative   | 2–16           | Moderate (tag check)| Medium         | General-purpose CPU caches     |
| Fully Associative | All in one set | Slow (all tags check)| Low            | TLBs, small specialized caches |

#### How Is a Block Found

| Type               | How Location Is Determined                         | Number of Comparisons           |
|--------------------|----------------------------------------------------|----------------------------------|
| **Direct Mapped**     | Use index to directly locate the block              | 1 comparison                     |
| **Set Associative**   | Use index to find the set, then search tags         | Equal to **associativity** level |
| **Fully Associative** (incl. Page Table) | Search all tags or use a lookup table (e.g., Page Table) | Equal to **number of blocks** or lookup-based (0) |

#### Which Block Should Be Replaced on a Cache Miss? 
Common strategies include:
- Random: randomly select a block
- **Least Recently Used (LRU):** Replaces the block that has not been used for the longest time.
- **First-In-First-Out (FIFO):** Replaces the oldest loaded block.
- **Optimal Page Replacement:** Replaces the block that will not be used for the longest future period (requires future knowledge).

#### What Happens on a Write (Write Policy)?

| Write Policy     | Description                                                         | Common Use                                      |
|------------------|---------------------------------------------------------------------|--------------------------------------------------|
| **Write Through** | Writes data to both **cache** and **main memory** immediately       | cache                                        |
| **Write Back**    | Writes data only to **cache** first; updates main memory **later**  | cache, paged memory (must be write back) |

### Memory Access Process

### Compiler Assumptions

When a program is compiled, the compiler assumes that the program has a **continuous block of memory**. It generates **virtual memory addresses** based on this assumption.

### OS Memory Setup with Pages

When a program starts, the OS:

1. Allocates memory in **pages** (fixed-size blocks, typically 4KB).
2. Loads the program’s instructions and data into memory using pages.
3. Creates a **Page Table** for each process to map virtual addresses to physical addresses.
   - Page Tables can be large, so techniques like **multi-level paging** or **inverted Page Tables** are used to reduce memory overhead.
4. Reserves **swap space** on disk for pages that may be evicted from RAM when memory is full.

### Runtime Memory Access

When a program accesses memory, it does so using a **virtual address**. The following steps occur:

#### 1. Address Translation

- The **Memory Management Unit (MMU)** converts the virtual address into a physical address using the **Page Table**.
- To speed up this process, a **Translation Lookaside Buffer (TLB)** caches recently used Page Table entries.
- If the virtual page number is **not in the TLB** (**TLB miss**):
  - The Page Table in RAM is checked.
    - If found: copy the page entry into TLB and return the physical address.
    - If **not found** (**page fault**):
      - Load the page from disk into RAM.
      - Choose a page to replace in RAM if needed.
      - Update the Page Table and TLB with the new entry.

#### 2. Fetching Data

- With the physical address:
  - **Check cache**:
    - If **cache hit** → return data quickly.
    - If **cache miss** → fetch data from **RAM**.
  - If data is **not in RAM** (another **page fault**):
    - OS loads the data from **disk into RAM**.
    - Replaces an existing page in RAM if needed.


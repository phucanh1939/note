---
title: Cache
---

# Cache Memory

## What is a Cache?
A cache is a small, high-speed memory located inside the CPU that stores frequently accessed data and instructions. It helps reduce the time needed to fetch data from the slower main memory (RAM).

### Inputs and Outputs:
- **Inputs:** Address from the CPU, Read/Write control signals, Data (for writes)
- **Outputs:** Data (for reads), Hit/Miss signal (indicates if data is in cache)

## Why Was Cache Created?
Caches were created to bridge the speed gap between the CPU and RAM. CPUs operate much faster than RAM, so frequent memory access would slow down execution. Cache reduces this latency by storing frequently used data closer to the CPU, improving performance significantly.

**The only problem cache solves is reducing the memory access time!**

## How Does Cache Work?
### Structure
A cache is typically organized into multiple levels:
- **L1 Cache:** Smallest, fastest, closest to the CPU core (focuses on reducing access time when cache hit)
- **L2 Cache:** Larger, slower than L1, may be shared between cores (focuses on reducing cache miss rate)
- **L3 Cache:** Largest, slowest, shared across all CPU cores (focuses on reducing cache miss rate)

**Why not 4, 5, or more levels of cache instead of 3?**
- Balances **miss rate** and **miss penalty**.
- 3 is practical choice, more levels can increase access time with diminishing returns.

### Cache Block Organization
Each cache is divided into sets, and each set contains multiple blocks. A block consists of:
- **Tag:** Upper part of an actual memory address used to identify the memory address range.
- **Data:** A chunk of memory fetched from RAM (not just the requested word, but an entire block for spatial locality).
- **Valid Bit:** Indicates whether the data in the block is valid.
- **Dirty Bit:** Used in write-back caches to track modified data that needs to be written to RAM.

### Address Breakdown
When accessing data, the memory address is divided into:
- **Index:** Used to locate a specific set in the cache.
- **Tag:** Compared against the tags stored in the blocks within the selected set.
- **Offset:** Specifies the exact byte/word inside the block.

#### Example:
Assume:
- A **32-bit** memory address
- A **4 KB (4096 B) cache** with **64-byte blocks**
- **Direct-mapped cache**

##### Address Breakdown:
1. **Offset (6 bits):** Since each block is 64 bytes, we need `log2(64) = 6` bits.
2. **Index (6 bits):** 4 KB cache / 64 B per block = `4096 / 64 = 64` blocks → `log2(64) = 6` bits.
3. **Tag (20 bits):** The remaining `32 - (6 + 6) = 20` bits.

##### Memory Address Example:
```
0xA3B4C8D2  (Binary: 1010 0011 1011 0100 1100 1000 1101 0010)
```
- **Tag:** `1010 0011 1011 0100 11` (20 bits)
- **Index:** `0010 0011` (6 bits)
- **Offset:** `010010` (6 bits)

## Read/Write Operations and CPU Interaction
### Cache Lookup Process
1. **CPU Generates a Memory Request**
2. **Index Lookup**
3. **Tag Comparison**
4. **Hit or Miss:**
   - **Cache hit:** The requested data is retrieved.
   - **Cache miss:** A block is fetched from RAM and stored in the cache (A miss occurs when the requested memory address is not found in the cache, whether for a read or a write.)

### Read Operation:
1. **Cache Hit:** Data is retrieved from the cache.
2. **Cache Miss:** Data is fetched from RAM and stored in cache before use.

### Write Operation:
1. **Write Hit:**
   - **Write-Through:** Data is immediately written to RAM.
   - **Write-Back:** Data is marked dirty and written later.
2. **Write Miss:** Data is written to RAM and may be loaded into the cache.

## Cache Replacement Policies
When a cache miss occurs and the cache set is full, a block must be replaced. Common policies include:
1. **Least Recently Used (LRU)**
2. **First-In, First-Out (FIFO)**
3. **Random Replacement**
4. **Least Frequently Used (LFU)**

## Challenges in Optimizing Cache
- **Increasing cache size** reduces miss rate but increases miss penalty and lookup time.
- **Using direct-mapped cache** reduces lookup time but increases miss rate.

## Challenges in Writing Cache-Optimized Programs
Memory hierarchy varies between architectures. **Autotuning** dynamically searches for optimal parameters to maximize cache efficiency.

## Q&A
### What happens to the processor pipeline during a cache miss?
- **Simple CPUs:** Stall until data is available.
- **Modern CPUs:** Use **out-of-order execution** to keep executing independent instructions while waiting.

### What is a write miss?
A miss occurs when the requested memory address is not found in the cache, whether for a read or a write.

### How does a cache track the least recently used (LRU) block?
- **Full LRU (Counter-based)** → Uses a log₂(N)-bit counter per block.
- **LRU Stack (Shift Register)** → Reorders blocks on access.
- **Approximate LRU (2-bit per block)** → Simple & space-efficient.
- **Pseudo-LRU (Tree-based)** → Best for large caches (8-way, 16-way).

### Why are there 3 levels of cache instead of 1?
It is a pratical numbers:
- **Single large cache** is too slow.
- **3 levels balance speed & efficiency:**
  - L1 → **Small, very fast** (low hit time)
  - L2 → **Medium-sized**, balances speed & size
  - L3 → **Large**, reduces main memory accesses
- **More than 3 levels?** → Diminishing returns.

## How to Write Cache-Optimized Programs
### Strategy:
1. **Load data into cache.**
2. **Process it repeatedly before replacing it.**
3. **Minimize unnecessary memory accesses to reduce cache misses.**

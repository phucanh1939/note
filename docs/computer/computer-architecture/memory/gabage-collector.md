---
title: Gabage Collector
---

# Garbage Collector (GC)

## What is a GC
Garbage Collection (GC) is an automatic memory management process that reclaims unused memory to prevent memory leaks and optimize performance.

## GC Structure/Architecture
- **Heap Memory**: Divided into generations (Young, Old, and sometimes Permanent/Metaspace).
- **GC Roots**: Special references (e.g., global/static variables) used to track live objects.
- **Collectors**: Different algorithms (e.g., Mark-and-Sweep, Generational GC) for managing memory.

## How does it work
1. **Mark**: Identify live objects by tracing from GC roots.
2. **Sweep**: Remove unreferenced objects from memory.
3. **Compact (optional)**: Defragment memory to optimize space.
4. **Optimize**: Use generational collection to manage short-lived and long-lived objects efficiently.

--

## Downsides of Garbage Collection (GC)

### 1. GC Overhead (CPU & Memory Usage)
- GC consumes extra **CPU cycles** for tracking and cleaning objects.  
- Requires **more memory** for metadata and efficient operation.  
- **Example:** A manually managed app may run in 100MB, while a GC-based app needs 150MB+.  

### 2. GC Pauses (Stop-the-World Events)
- The entire application **pauses** when GC runs.  
- **More memory pressure → more frequent pauses**.  
- **Example:** A 10ms GC pause can disrupt real-time trading or cause frame drops in games.  

### 3. Unpredictable Performance
- GC runs **at unpredictable times**, leading to performance spikes.  
- High object churn → **frequent minor GCs** → slowdowns.  
- **Example:** Java applications experience **random latency spikes** due to GC activity.  

### 4. Increased Memory Consumption
- **GC needs extra heap space** to manage allocations efficiently.  
- If the heap is too small → **frequent GCs**, if too large → **wasted memory**.  
- **Example:** A GC-based app may require **2× more memory** than a manually managed one.  

### 5. GC Tuning Complexity
- Requires **fine-tuning heap size, GC strategy, and pause times**.  
- Misconfiguration can lead to **high CPU usage or long pauses**.  
- **Example:** Java apps may need options like:  
```
-XX:+UseG1GC -XX:MaxGCPauseMillis=100 -XX:InitiatingHeapOccupancyPercent=45
```

### 6. Memory Leaks Still Happen (GC ≠ Leak-Free)
- **Holding unnecessary references** prevents GC from freeing objects.  
- Causes: **Static variables, unclosed resources, reference cycles**.  
- **Example:** A **HashMap cache** that never clears can cause **OutOfMemory errors**.  

### 7. Poor Fit for Real-Time Systems
- GC **introduces unpredictable delays**, making it unsuitable for real-time applications.  
- **Example:** Game engines like **Unreal Engine** avoid GC to maintain **smooth frame rates**.  

### When to Use & Avoid GC
| Aspect                 | GC-Based (Java, Go, C#) | Manual Memory (C, C++) |
|------------------------|------------------------|------------------------|
| **Ease of Use**        | ✅ Automatic | ❌ Requires manual tracking |
| **Performance Stability** | ❌ Unpredictable | ✅ Fully controlled |
| **Memory Efficiency**  | ❌ Higher overhead | ✅ More compact |
| **Real-Time Suitability** | ❌ Bad for strict deadlines | ✅ Best for real-time |
| **Memory Leak Risk**   | ❌ Still possible | ❌ Possible (if `free` is forgotten) |

### Conclusion
- **GC is great** for web apps, enterprise software, and general-purpose applications.  
- **GC is bad** for real-time systems, games, and low-latency applications.  

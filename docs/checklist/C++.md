## Section 1: Value Categories & Resource Ownership

*This section ensures you aren’t accidentally duplicating massive assets in memory.*

* [ ] **Understanding exactly what `std::move` does:** (Hint: It’s just a cast; it copies nothing. How does it change a variable's value category from an lvalue to an rvalue?)
* [ ] **Understanding Reference Collapsing and Perfect Forwarding (`std::forward`):** How do you write a template function that preserves whether an argument was passed as a temporary or a permanent object?
* [ ] **Understanding the Rule of 5:** When you write a custom game component, do you know exactly how to implement the copy constructor, move constructor, copy assignment, move assignment, and destructor?
* [ ] **Understanding Smart Pointer Overhead:** What is the physical memory difference between a `std::unique_ptr` (zero overhead) and a `std::shared_ptr` (allocates a heap control block for reference counting)?
* [ ] **Understanding RVO and NRVO (Return Value Optimization):** How does the compiler completely eliminate copies when returning objects from functions, and why does adding `std::move()` to a return statement actually slow it down?

---

## Section 2: Hardware-Aware Memory Layout

*This section is where 90% of game performance comes from. It teaches you how to design data for the CPU cache.*

* [ ] **Understanding Padding and Alignment (`alignas` / `alignof`):** How does the compiler insert invisible bytes into your `struct` to align data for the CPU? How do you reorder variables to minimize memory waste?
* [ ] **Understanding Cache Line Mechanics with Vector vs List:** Why does iterating through a contiguous `std::vector` fetch data perfectly into the 64-byte CPU cache line, while a pointer-heavy node container like `std::list` causes massive performance stalls?
* [ ] **Understanding Small String Optimization (SSO):** At what exact character length does your compiler stop storing a string inside the object stack and silently trigger an expensive heap allocation?
* [ ] **Understanding Polymorphic Memory Allocators (PMR):** How do C++17 PMR containers allow you to swap out standard heap allocations for lightning-fast stack allocations or pre-allocated "Arena" buffers?

---

## Section 3: The Cost of Language Abstractions

*This section teaches you when to use C++ features and when they cost too much runtime performance.*

* [ ] **Understanding the Layout of a `vtable` (Virtual Table):** What does a class look like in memory the moment you add a `virtual` function? How many pointer indirections happen during a virtual method call?
* [ ] **Understanding Static vs. Dynamic Dispatch:** When should you use templates (compile-time polymorphism) versus inheritance (runtime polymorphism) in a game engine loop?
* [ ] **Understanding why Exceptions are Banned:** Why is standard `try/catch/throw` forbidden in real-time execution blocks, and how do `std::optional` or `std::expected` (C++23) replace them?
* [ ] **Understanding Cast Overhead:** What is the runtime performance difference between a free `static_cast`/`reinterpret_cast` and an expensive, type-checking `dynamic_cast`?

---

## Section 4: Compile-Time Baking (Metaprogramming)

*This section teaches you how to shift heavy computations from the player’s device to your compilation stage.*

* [ ] **Understanding `constexpr` vs `consteval` (C++20):** How do you force the compiler to pre-calculate mathematical look-up tables, quaternion math, or string hashes before the game executable even runs?
* [ ] **Understanding C++20 Concepts:** How do you replace old, unreadable template code (`std::enable_if`) with modern constraints to ensure generic engine systems only accept types that match your strict requirements?
* [ ] **Understanding Template Bloat:** How does extensive template utilization impact the final size of your game binary and affect the CPU's Instruction Cache (I-Cache)?

---

## Section 5: Zero-Allocation Views

*This section focuses on writing safe, modern code without copying data structures.*

* [ ] **Understanding `std::string_view` (C++17):** How do you pass string data around your asset pipeline as a simple pointer + length pair without ever allocating memory on the heap?
* [ ] **Understanding `std::span` (C++20):** How do you pass raw pointer arrays, `std::vector`s, or `std::array`s into rendering or physics subsystems using a single, unified, non-owning interface?

---

## Section 6: Real-Time Concurrency

*This section covers how to safely scale your code across multiple CPU cores without causing frame stutter.*

* [ ] **Understanding `std::atomic` and Memory Ordering:** How do you update a variable safely across two threads using hardware-level CPU instructions without using a heavy lock?
* [ ] **Understanding Data Races vs. Race Conditions:** What is the physical hardware difference between two threads writing to the same memory address versus a logic error in thread execution order?
* [ ] **Understanding C++20 Coroutines:** How does the compiler transform a function into a heap-allocated state machine that can pause its execution and resume later (essential for asynchronous gameplay scripting and asset streaming)?

---


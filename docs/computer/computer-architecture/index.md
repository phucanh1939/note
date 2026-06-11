---
title: Computer Architecture
---

# Computer Architecture

**Computer Architecture** is the study of how computer systems are designed and organized.  
It focuses on the structure and behavior of a computer system—especially the **Processor (CPU)** and **Memory**, which are the main components responsible for processing data (transforming data from one form to another).

## Topics in Computer Architecture

### [Instruction & Instruction Set Architecture (ISA)](./Instruction/Instruction.md)
Defines the commands a computer can execute (data transformations). 

Sections:
  - Structure of an instruction (opcode, operands, etc.)  
  - Types of instructions: arithmetic, logic, control, memory access  
  - How ISAs are designed to balance performance, complexity, and compatibility  

### Processor
The hardware implementation of the ISA.  

Sections:
  - Basic building blocks (logic gates, logic circuit)
  - Internal design of the CPU
  - How it fetches, decodes, and executes instructions  

### Memory
How data and instructions are stored for processing.

Sections:
- How memory components are built: flip-flops, SRAM, DRAM, and storage technologies  
- Different types of memory in a computer
- **Memory hierarchy**: Organizing memory types to execute data faster  

### Parallelism
Designing hardware to execute data transformations in parallel for better performance and energy efficiency.

Sections
  - Why energy efficiency matters and why the shift to multicore processors occurred 
  - Challenges in design parallelism hardware/sofware
  - **Instruction-level parallelism**: Executing multiple instructions at once  
  - **Data-level parallelism**: Executing the same instruction on multiple data  
  - The need to shift from sequential to multi-core programming to take full advantage of multicore processors (and how to do it in basic form)

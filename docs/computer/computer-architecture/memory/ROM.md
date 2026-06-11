---
title: Rom
---

# Read Only Memory (ROM)

## What is ROM?

ROM is **Non-volatile memory** that retains data even without power. It stores **firmware, bootloaders, and embedded system code**.  

ROM can be seen as a **combinational logic circuit**: **Input** = Address, **Output** = Stored data at that address.  

### Types of ROM
- **Masked ROM (MROM)** – Pre-programmed at manufacturing, cannot be changed.  
- **PROM** – Programmable once using special hardware.  
- **EPROM** – Erasable with **UV light**, then reprogrammable.  
- **EEPROM** – Electrically erasable and reprogrammable.  
- **Flash Memory** – A faster form of EEPROM (used in SSDs, USB drives).  

## How does ROM Work?

### Internal Structure
- Organized as a **matrix of word lines (rows) and bit lines (columns)**.  
- Uses a **decoder** to select a row based on the input address.  
- Each intersection has a **predefined logic state (0 or 1)**.  
- Each ROM cell is built using **diodes, fuses, or floating-gate transistors**, **not flip-flops** like RAM.  
    - **MROM:** Uses **diodes/transistors** at fixed locations to store data. 
        - **1** = Connection exists (diode/transistor present).  
        - **0** = No connection.  
    - **PROM:** Uses **fuses** that are selectively burned. 
        - **1** = Intact fuse (connection exists).  
        - **0** = Blown fuse (no connection). 
    - **EPROM/EEPROM/Flash:** Uses **floating-gate transistors** to trap charge.  
        - **1** = No charge in the floating gate (transistor conducts).  
        - **0** = Charge trapped in the floating gate (transistor blocks current).  

### Writing Data (During Chip Manufacturing)
#### **For Masked ROM (MROM):**  
- Data is **hardwired** during fabrication using photolithography.  
- The circuit layout defines **permanent 0s and 1s**.  

#### For Programmable ROMs (PROM, EPROM, EEPROM, Flash):
- **PROM**: Uses **fuses** that are selectively burned to store data.  
- **EPROM**: Uses **floating-gate transistors**, programmed with high voltage.  
- **EEPROM/Flash**: Uses **electrical signals** to trap/remove charge in floating gates.  

### Reading Data Process
1. **Input Address** → Sent to the **address decoder**.  
2. **Decoder selects a row** (word line) in the memory array.  
3. The **corresponding bits** are read from the selected row.  
4. Data appears instantly at the **output** (no need for a clock).  

## Key Properties
- ROM behaves like a **combinational logic circuit** (Address → Output).  
- **No need for refresh cycles** (unlike RAM).  
- **Read-only (mostly)** – Cannot be easily modified after manufacturing.  

## How to Create a ROM (From Scratch)

- Define the **logic function** with a **truth table** (Address → Data).
- Implement a cell using **diodes, fuses, or floating-gate transistors**
- Implement a **decoder** to select rows and store data in a **word/bit line matrix**.
- Connect & layout cells follow the logic functions

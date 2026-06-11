---
title: Storage
---

# Secondary Storage 

## What is Secondary Storage 

**Secondary Storage** is **non-volatile memory** used to store data permanently, even when the computer is powered off. It is slower than primary storage (RAM) but has much higher capacity and is essential for long-term data retention.

### Types of Secondary Storage:
| Storage Type   | Element Structure                | How Each Cell Stores 1 Bit       | Speed                | Cost per GB |
|---------------|--------------------------------|--------------------------------|----------------------|------------|
| **Hard Disk Drive (HDD)**       | Magnetic platter with sectors & tracks | Magnetic domains (1 = magnetized in one direction, 0 = opposite direction) | 80-250 MB/s (SATA)  | Low ($0.02-$0.05) |
| **Solid-State Drive (SSD)**       | NAND Flash cells (floating-gate transistors) | Electrical charge in floating-gate (1 = charged, 0 = no charge) | 500-7000 MB/s (NVMe) | Moderate ($0.10-$0.25) |
| **Magnetic Tape** | Long strip of magnetized material | Magnetic particles aligned in a specific direction (1 or 0) | 100-400 MB/s (sequential) | Very Low ($0.005-$0.01) |

## How does Secondary Storage Work?

### How is Data Stored in a Secondary Storage?

Different type of Secondary Storage has different way to store data
- HDD: Store data using: Magnetic domains (1 = magnetized in one direction, 0 = opposite direction)
- SSD: Store data using: Electrical charge in floating-gate (1 = charged, 0 = no charge)
- Magnetic Tape: Data is written in linear tracks along the tape, with magnetic particles aligned in one direction (1) or the opposite direction (0).

### Structure of a Secondary Storage

#### **1. Physical Storage Medium**  
- **HDD**: Magnetic platters divided into sectors and tracks.  
- **SSD**: NAND flash memory cells arranged in blocks and pages.  
- **Magnetic Tape**: Long magnetic strip storing data sequentially.  

#### **2. Storage Controller**  
- Manages read/write operations and error correction.  
- Contains firmware (embedded software) to control the device.  
- In SSDs, it handles **wear leveling** and **garbage collection**.  

#### **3. Cache / Buffer Memory**  
- Temporary high-speed memory for frequently accessed data.  
- HDDs have a small DRAM cache (e.g., 8MB-256MB).  
- SSDs use DRAM or SLC cache for faster access.  

#### **4. Interface / Connection to Computer**  
- Allows communication between the storage device and the computer.  
- **Common Interfaces:**  
  - **SATA (Serial ATA)** – Used in HDDs & SATA SSDs, ~600 MB/s max.  
  - **NVMe (Non-Volatile Memory Express)** – High-speed SSD interface using PCIe lanes, ~7000 MB/s.  
  - **USB (Universal Serial Bus)** – Used for external drives (USB 3.0, 3.1, 3.2, or 4.0).  
  - **SAS (Serial Attached SCSI)** – Used in enterprise HDDs & SSDs, faster than SATA.  
  - **FC (Fibre Channel)** – High-speed interface for data centers.  

#### **5. Power Supply**  
- **Internal Drives** (HDDs, SSDs) use **SATA power** or **PCIe power** (for NVMe SSDs).  
- **External Drives** (USB HDDs/SSDs) get power from the **USB port** or external adapters.  

```
+-------------------------------------------------+
|            Secondary Storage Device             |
+-------------------------------------------------+
| 1. Physical Storage Medium (Magnetic/NAND)      |
| 2. Storage Controller (Manages read/write)      |
| 3. Cache Memory (Temporary high-speed data)     |
| 4. Interface (SATA, NVMe, USB, etc.)            |
| 5. Power Supply (SATA Power, PCIe, USB)         |
+-------------------------------------------------+
       │
       │  Interface (SATA, PCIe, USB, etc.)
       ▼
+-------------------------------------------------+
|      Computer System (CPU, RAM, Motherboard)   |
+-------------------------------------------------+
```

### Reading Data Process

#### **1. Request Initiation**  
- CPU requests data via the OS.  
- OS checks the file system for the storage location and converts it to **Logical Block Address (LBA)**.
- The OS calls the **storage controller** with an input address (LBA - Logical Block Address) to read data

#### **2. Address Translation**  
- Converts logical block address (LBA) to physical location.  
  - **HDD**: Maps LBA to tracks & sectors.  
  - **SSD**: Uses a flash translation layer (FTL).  
  - **Magnetic Tape**: Finds the correct tape position.  

#### **3. Positioning the Read Mechanism**  
- Moves to the correct data location.  
  - **HDD**: Actuator arm moves the read head; platter spins.  
  - **SSD**: No movement; direct NAND access.  
  - **Magnetic Tape**: Fast-forwards or rewinds the tape.  

#### **4. Data Retrieval**  
- Reads stored data using different methods:  
  - **HDD**: Detects magnetic field changes.  
  - **SSD**: Reads electrical charge in NAND cells.  
  - **Magnetic Tape**: Reads magnetic polarity shifts.  

#### **5. Error Detection & Correction**  
- Verifies data integrity using built-in error correction (ECC).  

#### **6. Data Transfer to CPU**  
- Sends data via interface SATA, NVMe, USB, or other interfaces. 

### Writing Data Process

#### **1. Request Initiation**  
- CPU requests data write via the OS.  
- OS determines file system location and converts it to **Logical Block Address (LBA)**.  
- The OS calls the **storage controller** with an input address (LBA - Logical Block Address) and data to write

### **2. Address Translation**  
- Storage controller maps **LBA → physical location**:  
  - **HDD**: Finds correct **track & sector**.  
  - **SSD**: Uses **Flash Translation Layer (FTL)** to map LBA to NAND memory.  
  - **Magnetic Tape**: Moves tape to the correct position.  

### **3. Move to the correct physic locationm**  
- Moves to the correct location before writing:  
  - **HDD**: Read/write head moves to the right track.  
  - **SSD**: No movement; controller prepares NAND cells.  
  - **Magnetic Tape**: Fast-forwards or rewinds tape.  

### **4. Data Writing**  
- **HDD**: Magnetic head **alters the polarity** on the platter.  
- **SSD**: NAND **charges/discharges floating-gate transistors**.  
- **Magnetic Tape**: Magnetizes the tape surface.  

### **5. Error Checking & Verification**  
- Storage controller performs **error correction (ECC)**.  
- **HDD/SSD**: May rewrite or use spare sectors/pages for reliability.  

### **6. Data is Committed**  
- The write is finalized, and the OS is notified of success.  
- **SSDs** may use **wear leveling** to prevent excessive writes to the same memory cells.  

### **7. Cache & Buffer Management** *(Optional, for performance)*  
- **HDDs/SSDs** may temporarily store data in cache before writing.  
- Some SSDs use **DRAM or SLC cache** to speed up writes. 

### Deleting Data Process

#### **1. Request Initiation**  
- CPU requests file deletion via the OS.  
- OS marks the file as deleted in the **file system metadata**.  

#### **2. Handling by Storage Type**  

##### **HDD (Hard Disk Drive)**  
- Data is **not immediately erased**; only the reference to it is removed.  
- The space is marked as **free**, allowing new data to overwrite it.  
- Secure deletion requires **overwriting with zeros/random data**.  

##### **SSD (Solid-State Drive)**  
- OS sends a **TRIM command** to mark data as invalid.  
- Data is **not immediately erased**, but flagged for **garbage collection**.  
- During garbage collection, invalid data is erased to free up blocks.  

##### **Magnetic Tape**  
- No direct delete operation.  
- Data remains until the tape is **rewritten or reformatted**.  

#### **3. Data Removal Confirmation**  
- File is no longer accessible by the OS.  
- **HDDs & SSDs**: Data may still be recoverable unless securely erased.  
- **Magnetic Tape**: Requires manual overwriting to fully remove data.

## **How to Create a Secondary Storage (From Scratch)**  

### **1. Choose a Storage Type**  
- **HDD** – Uses magnetic platters for data storage.  
- **SSD** – Uses NAND flash memory for fast access.  
- **Magnetic Tape** – Uses sequential magnetic recording.  

### **2. Define & Implement Each Component**  

#### **Storage Medium (Data Storage Layer)**  
- **HDD**: Magnetic platters store bits using magnetized domains.  
- **SSD**: NAND flash cells store charge to represent bits.  
- **Tape**: Magnetic tape stores data sequentially.  

#### **Read/Write Mechanism**  
- **HDD**: Read/write heads change or detect magnetic states.  
- **SSD**: Electrical charge levels define data states.  
- **Tape**: Magnetizes tape surface for storage.  

#### **Storage Controller**  
- Translates **LBA ↔ Physical Address**.  
- Manages **error correction, caching, wear leveling (SSD)**.  
- Interfaces: **SATA, NVMe, PCIe, SAS, USB**.  

#### **Firmware & File System Support**  
- Controls data flow and manages memory.  
- Supports file systems **(NTFS, FAT32, ext4, etc.)**.  
- Optimizes speed, reliability, and power usage.  

### **3. Assemble & Test**  
- Integrate all components.  
- Perform **read/write speed, reliability, and compatibility tests**.  

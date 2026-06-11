---
title: Raid
---

# RAID (Redundant Array of Independent Disks)

RAID is a technology that **combines multiple disks** to improve **performance**, **redundancy**, or both. Each RAID level (type) defines a different way to combine the disks for specific purposes.

| **RAID Level** | **Purpose**          | **How it Works**                                              | **Pros**                                             | **Cons**                                           |
|----------------|----------------------|---------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------|
| **RAID 0**     | Speed                | Data is split across multiple disks (striping).               | Faster read/write speeds.                           | No redundancy. If one disk fails, all data is lost.|
| **RAID 1**     | Redundancy           | Data is mirrored on two or more disks (duplicate).             | Data protection. One disk failure doesn’t cause data loss. | Storage space is halved.                         |
| **RAID 5**     | Performance + Fault Tolerance | Data is striped across multiple disks with parity (error correction). | Good balance of speed and data protection. Can tolerate one disk failure. | Slower write speeds due to parity calculation.    |
| **RAID 10**    | High performance + Redundancy | Combines mirroring (RAID 1) and striping (RAID 0).            | High speed and redundancy.                         | Requires at least 4 disks; 50% storage efficiency. |

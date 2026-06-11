---
title: Tcp
---

# TCP (Transmission Control Protocol)

**Definition:** A protocol at the transport layer that sender and receiver agree to use for reliably packing, sending, and reassembling data segments.

**Purpose / Problem Solved:** Ensures that data sent from the sender arrives at the receiver **in order, complete, and without errors** (when send it to application layer)

**Layer:** Transport Layer

**How it works:**
- Sender splits data into **segments**, adds sequence numbers and checksums
- Receiver checks sequence and checksum, reorders segments, requests retransmission if needed
- Both sides acknowledge received segments
- Guarantees reliable, ordered delivery

**Example (simplified TCP segment structure):**

Data segment follow this format:

| Source Port | Destination Port | Sequence Number | Ack Number | Flags | Payload |

- **Sender:** fills all fields and sends payload  
- **Receiver:** reads ports to know which app, checks sequence & flags, validates checksum, reassembles payload

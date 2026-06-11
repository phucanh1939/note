---
title: Ethernet
---

# Ethernet

**Definition:**  
A data link & physical layer protocol that sender and receiver agree to use for formatting frames and transmitting them over a wired LAN.

**Purpose / Problem Solved:**  
Defines how devices on the same network deliver data frames reliably over a physical medium.

**Layer:** Data Link Layer + Physical Layer

**How it works:**
- Sender wraps IP packet into a frame with **source/destination MAC** and CRC.
- Receiver validates CRC, extracts packet.

**Example Ethernet frame structure:**

Data frame follow this format:

| Destination MAC | Source MAC | EtherType | Payload (IP Packet) | CRC |

- **Sender:** fills MAC addresses, sends frame  
- **Receiver:** checks CRC, reads EtherType, extracts IP packet

---
title: Udp
---

# UDP (User Datagram Protocol)

**Definition:** A protocol at the transport layer that sender and receiver agree to use for sending data as single, independent messages without guaranteeing delivery or order.

**Purpose / Problem Solved:** Allows **fast, low-latency communication** where occasional loss is acceptable.

**Layer:** Transport Layer

**How it works:**
- Sender wraps application data into **datagrams** with port numbers
- Receiver delivers datagrams to the application based on port
- No retransmission or ordering; fast and simple

**Example (simplified UDP datagram structure):**

datagrams follow this format:

| Source Port | Destination Port | Length | Checksum | Payload |

- **Sender:** fills all fields and sends data  
- **Receiver:** checks port to find the application, optionally validates checksum

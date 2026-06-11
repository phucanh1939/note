---
title: Ip
---

# IP (Internet Protocol)

**Definition:** A protocol at the network layer that sender and receiver (and also routers, switchs on the way) agree to use for addressing and routing packets across networks.

**Purpose / Problem Solved:** Ensures data can travel from source device to destination device across multiple networks.

**Layer:** Network Layer

**How it works:**
- Adds **source and destination IP addresses**
- Routers read IP to determine the next hop toward the destination
- Each router forwards the packet until it reaches the correct network

**Example (simplified IPv4 packet structure):**

Data packet follow this format:

| Version | Header Length | Source IP | Destination IP | Payload (TCP/UDP segment) |

- **Sender:** fills source/dest IP, passes TCP/UDP segment as payload  
- **Receiver:** checks destination IP, extracts transport layer segment

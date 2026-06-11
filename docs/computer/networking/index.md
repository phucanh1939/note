---
title: Networking
---

# Computer Network Foundation

## What is a network
A network is a group of devices connected by wires or wireless links so they can exchange data.

## How data is transferred
Data travels through layers.  
Each layer remove/adds the information needed for the next part of the journey.

---

# Sender Side

### 1. Application Layer
- Creates the raw data (message, request, file).
**Output:** Data

### 2. Transport Layer (TCP/UDP) - Software in Kernel
- Adds **ports**
- Splits data into **segments**
- Adds reliability info (TCP: order, checksum, ACK)
**Output:** Segments

### 3. Network Layer (IP) - Software in Kernel
- Adds **source IP** and **destination IP**
- Decides which network the data goes to
**Output:** Packet (each segment converted to 1 packet)

### 4. Data Link Layer (Ethernet/Wi-Fi)
- Software driver + NIC (Network Interface Card)
- Adds **source MAC** and **destination MAC**
- Destination MAC = **first router (gateway)**
- Wraps packet into a **frame**
**Output:** Frame

### 5. Physical Layer / NIC
- Converts the frame into **signals**
- Sends signals to the **switch**

---

# Network Path

### Switch
- Reads **MAC**
- Sends frame toward the **local router** (no modify the frame)

### Router (each hop)
1. Receives a frame → extracts the packet  
2. Reads **destination IP**  
3. Looks up **next-hop IP** in routing table  
4. Uses **ARP** to get next-hop **MAC**  
5. Builds a new frame:
   - Dest MAC = next router
   - Src MAC = its own NIC  
6. Sends the frame to the next router

Repeat until the packet reaches the final router.

---

# Receiver Side

### Final Router
- Sees the destination IP is on its LAN
- Builds a frame with the **destination device’s MAC**
- Sends it to the switch

### Switch
- Forwards the frame to the device (using MAC)

### Destination Device
- **Data Link:** validates + removes frame/MAC  
- **Network:** validates + removes IP  
- **Transport:** reassembles segments, checks order + checksum, sends ACK (TCP)  
- **Application:** receives the complete data


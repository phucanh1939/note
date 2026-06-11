---
title: Network Protocol
---

# **Network Protocol**

## **What is a protocol**

The sender and receiver must **agree on the data format** so it can be packed and parsed correctly.  

A **protocol** is a set of rules that define how devices communicate.

It specifies:

- **Format**: structure of data  
- **Timing / behavior**: when and how to send/receive  
- **Error handling**: how to detect or correct problems  
- **Semantics**: meaning of messages  

Protocols exist at **every layer** of the network.

---

## **Example: HTTP**
- **Format**: request line + headers + body  
- **Behavior**: client sends request → server responds  
- **Error handling**: status codes like 404, 500  
- **Semantics**: GET = retrieve data, POST = send data  

---

## **Application Layer Protocols (assumed by the receiver)**
- The receiver application **assumes** all data it receives on a specific port follows the expected protocol.  
- **No protocol type information** is explicitly included in the packet payload.  
- The **port number** in the transport layer segment tells the OS which application to deliver the data to.  

**Example:**
- HTTP server listens on TCP port 80  
- Any segment arriving on port 80 is parsed as HTTP  
- Random or malformed data → server fails to parse → error/exception  

---

## **Other Layer Protocols (known by the layer)**
- Lower layers (Transport, Network, Data Link) **know which protocol to use** because the information is included in the segment or packet header.  
- The receiver’s layer reads the header to determine how to parse the payload.  
- Examples:  
  - **Transport Layer:** TCP vs UDP (port numbers + flags in segment header)  
  - **Network Layer:** IP version (IPv4/IPv6) in packet header  
  - **Data Link Layer:** Ethernet frame type (EtherType)  

**Key idea:**  
- Protocols at these layers are **explicitly indicated in headers**, unlike application layer protocols which rely on the receiving application to assume the protocol.  

---

## **Key idea**
- **Sender:** formats data according to the protocol the receiver expects  
- **Receiver application:** assumes data follows the protocol and parses it accordingly  
- **Receiver layers:** read headers to determine the correct protocol and parse payload  
- **OS/Transport Layer:** delivers application payload to the correct application via port

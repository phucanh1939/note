---
title: Https
---

# HTTPS (HTTP Secure)

**Definition:** An application layer protocol that sender and receiver agree to use for secure web communication over encrypted channels.

**Purpose / Problem Solved:** Ensures confidentiality, integrity, and authentication of HTTP data in transit.

**Layer:** Application Layer

**How it works:**
- Uses TLS handshake to agree on encryption keys
- Client and server encrypt/decrypt HTTP messages
- Server processes HTTP requests as usual, now over secure channel

**Example (simplified workflow):**

1. TLS handshake: agree on keys
2. Encrypted HTTP Request: 
   | Encrypted Payload |
3. Encrypted HTTP Response: 
   | Encrypted Payload |

- **Sender:** encrypts and sends HTTP request  
- **Receiver:** decrypts, parses, responds

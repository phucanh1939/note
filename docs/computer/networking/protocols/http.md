---
title: Http
---

# HTTP (HyperText Transfer Protocol)

**Definition:** An application layer protocol that sender and receiver applications agree to use for formatting and interpreting web requests and responses.

**Purpose / Problem Solved:** Standardizes communication between web clients and servers so that both sides can understand requests and responses.

**Layer:** Application Layer

**How it works:**
- Client formats request (start line, headers, body) according to HTTP rules
- Server parses request, processes it, and formats a response
- Both sides assume the other follows HTTP rules

**Example HTTP request/response (simplified):**

Http request/resposne (created by the application) must follow this format:

```
Request:
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Browser

Response:
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html>...</html> ```
```

- Sender (client): formats request like above
- Receiver (server): parses request, responds in same format

# C++ Notes: Literals

## What is a Literal?

A **literal** is a value written directly in the source code.

It represents a fixed value that does not need to be computed.

Examples:

```cpp
42
3.14
'A'
true
"Hello"
nullptr
```

Each of these is a literal.

---

# Literal vs Variable

```cpp
int x = 42;
```

```text
x      → variable
42     → integer literal
```

The variable stores a value.

The literal *is* the value written in the program.

---

# Common Types of Literals

## Integer Literals

```cpp
0
13
123
1000000
```

Different bases:

```cpp
42      // Decimal
052     // Octal (8)
0x2A    // Hexadecimal (16)
0b101010 // Binary (C++14)
```

---

## Floating-point Literals

```cpp
3.14
0.5
2.
.25
```

Scientific notation:

```cpp
3.14159E0
1E3
2.5E-2
```

Meaning:

```text
3.14159E0
=
3.14159 × 10^0
=
3.14159
```

```text
1E3
=
1 × 10^3
=
1000
```

```text
2.5E-2
=
2.5 × 10^-2
=
0.025
```

> `E` (or `e`) means **"multiply by 10 raised to the exponent."**

---

## Character Literals

```cpp
'A'
'0'
'\n'
```

---

## String Literals

```cpp
"Hello"
"World"
"ABC"
```

---

## Boolean Literals

```cpp
true
false
```

---

## Pointer Literal

```cpp
nullptr
```

Represents the null pointer value.

---

# Important: Negative Numbers

This is one of the most misunderstood topics.

Consider:

```cpp
-13
```

Many people think:

> "`-13` is one literal."

**It is not.**

It is parsed as:

```text
Unary minus operator
        │
        ▼
      13
```

The literal is:

```cpp
13
```

The `-` is the **unary minus operator**.

It performs negation on the literal.

Conceptually:

```cpp
-(13)
```

not

```cpp
(-13)
```

---

## Example

```cpp
int x = -13;
```

The compiler parses this as

```text
Assignment
    │
    └── Unary Minus
            │
            └── Integer Literal (13)
```

---

## Another Example

```cpp
-3.14
```

This is

```cpp
-(3.14)
```

The literal is

```cpp
3.14
```

The minus sign is an operator.

---

## Why is this important?

Consider:

```cpp
int x = -5 * 2;
```

The compiler sees

```cpp
(-5) * 2
```

which is actually

```cpp
(-(5)) * 2
```

The unary minus operator is applied to the literal `5`.

---

# Unary Minus is an Operator

Operators perform computations on operands.

Examples:

```cpp
-13
```

```text
Unary minus
    │
    └── 13
```

```cpp
!true
```

```text
Logical NOT
    │
    └── true
```

```cpp
~5
```

```text
Bitwise NOT
    │
    └── 5
```

These operators are **not part of the literal**.

---

# Expression Example

```cpp
-13 + 4
```

Parse tree:

```text
        +
      /   \
    (-)    4
     |
    13
```

Notice:

* `13` is a literal.
* `4` is a literal.
* `-` is the unary minus operator.
* `+` is the binary addition operator.

---

# Summary Table

| Code      | Literal(s) | Operator(s)           |
| --------- | ---------- | --------------------- |
| `42`      | `42`       | None                  |
| `3.14`    | `3.14`     | None                  |
| `true`    | `true`     | None                  |
| `nullptr` | `nullptr`  | None                  |
| `-13`     | `13`       | Unary `-`             |
| `-3.14`   | `3.14`     | Unary `-`             |
| `5 + 2`   | `5`, `2`   | Binary `+`            |
| `-5 + 2`  | `5`, `2`   | Unary `-`, Binary `+` |
| `!true`   | `true`     | Unary `!`             |

---

# Key Takeaways

* A **literal** is a fixed value written directly in source code.
* Literals include integers, floating-point numbers, characters, strings, booleans, and `nullptr`.
* Scientific notation uses `E` or `e` to mean **× 10ⁿ**.
* **`-13` is not a negative integer literal.**

  * `13` is the integer literal.
  * `-` is the unary minus operator.
* The compiler parses `-13` as:

```cpp
-(13)
```

not as a single literal.

> **Rule to remember:** A literal is the value itself. Any sign (`-`) or other symbol (`!`, `~`, etc.) before it is an operator applied to that literal, not part of the literal.

# Expressions vs. Statements

## Expression

### Definition

An **expression** is a piece of code that **evaluates to a value**.

Every expression has:

* A **value**
* A **type**

Examples:

```cpp
42                  // int
3.14                // double
a                    // value of variable a
a + b               // sum of a and b
foo()               // function return value
x = 5               // assignment expression that produce the value is the reference of x
```

Example:

```cpp
int a = 3;
int b = 4;

int c = a + b;
```

Expression:

```cpp
a + b
```

Produces:

```
Value: 7
Type: int
```

---

## Statement

### Definition

A **statement** is a complete instruction executed by the program.

Statements perform actions such as:

* Executing an expression
* Controlling program flow
* Declaring variables
* Returning from functions

Examples:

```cpp
a = 5;
return a;
if (a > b) { }
while (x--) { }
for (...) { }
```

---

## Expression Statement

An **expression statement** is simply:

```
expression ;
```

The semicolon tells the compiler:

> Evaluate this expression, then discard its result (unless the expression itself has side effects).

Example:

```cpp
a + b;
```

The program computes the value but immediately throws it away.

Another example:

```cpp
x = a + b;
```

The assignment expression is evaluated, updating `x`.

---

## Assignment is an Expression

Unlike many languages, C++ treats assignment as an expression.

```cpp
x = 5
```

This expression:

* Assigns `5` to `x`
* Produces the assigned value (technically, a reference to `x`)

That's why this works:

```cpp
a = b = c = 5;
```

Evaluation order:

```cpp
a = (b = (c = 5));
```

---

## Relationship

```text
Expression
    ↓
Produces a value

Statement
    ↓
Performs an action
```

Example:

```cpp
a + b;
```

```
Expression:
    a + b

Statement:
    evaluate a + b
```

---

## Parse Tree Example

```cpp
x = a + b;
```

```
Expression Statement
│
└── Assignment Expression (=)
    ├── Left
    │   └── x
    │
    └── Right
        └── Additive Expression (+)
            ├── a
            └── b
```

---

## Examples

| Code          |        Expression?       |       Statement?       |
| ------------- | :----------------------: | :--------------------: |
| `42`          |             ✅            |            ❌           |
| `a`           |             ✅            |            ❌           |
| `a + b`       |             ✅            |            ❌           |
| `foo()`       |             ✅            |            ❌           |
| `x = 5`       |             ✅            |            ❌           |
| `a + b;`      |        ✅ (inside)        |            ✅           |
| `x = a + b;`  |        ✅ (inside)        |            ✅           |
| `return x;`   |             ❌            |            ✅           |
| `if (x > 0)`  | `x > 0` is an expression |   `if` is a statement  |
| `while (x--)` |  `x--` is an expression  | `while` is a statement |

---

# Mental Model

### Expression

Ask:

> **"What value does this produce?"**

Examples:

```cpp
5
```

Answer:

```
5
```

---

```cpp
a + b
```

Answer:

```
sum of a and b
```

---

### Statement

Ask:

> **"What action should the program perform?"**

Examples:

```cpp
return x;
```

Action:

```
Return x to the caller.
```

---

```cpp
if (x > 0)
```

Action:

```
Execute the following block only if x > 0.
```

---

# Key Takeaways

* An **expression** produces a value.
* A **statement** performs an action.
* Every expression has a type and a value.
* An **expression statement** is an expression followed by a semicolon.
* In C++, assignment (`=`) is an expression.
* Statements often contain expressions (e.g., `if`, `while`, `return`).

---

# One-Sentence Summary

> **Expressions answer "What value?" while statements answer "What should the program do?"**

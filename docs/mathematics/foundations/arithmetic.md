---
title: Arithmetic
---

# Arithmetic - Number Systems and Number Theory

Number systems and number theory form a **core foundation of mathematics**, providing formal definitions of numbers, their relationships, and arithmetic properties.  
In set-theoretic terms, each number system can be defined as a **set**, building from simpler to more complex numbers.

---

## 1. Number Systems (Construction with Sets)

### 1.1 Natural Numbers (ℕ)
- **Definition (set-theoretic):**  
  `ℕ = {0, 1, 2, 3, …}  `
- **Von Neumann Construction using sets:**  
  - `0 = ∅`  
  - `1 = {0} = {∅} ` 
  - `2 = {0,1} = {∅, {∅}} ` 
  - `3 = {0,1,2} = {∅, {∅}, {∅,{∅}}}`
  - …  
- **Key concepts:** Addition, multiplication, order, induction principle.  
- **Use:** Counting, sequences, combinatorics, proofs by induction.

### 1.2 Integers (ℤ)
- **Definition (set-theoretic):**  
  `ℤ = {…, -3, -2, -1, 0, 1, 2, 3, …}` 
- **Construction from ℕ:**  
  - Integers are defined as **equivalence classes of ordered pairs of natural numbers**:  
    - a - b ↔ (a, b) where a, b ∈ ℕ  
    - Two pairs (a, b) and (c, d) are equivalent if a + d = b + c  
  - **Example:** (3,1) represents 2, (1,3) represents -2  
- **Key concepts:** Addition, subtraction, multiplication, divisibility.  
- **Use:** Solving equations, algebra, number theory.

### 1.3 Rational Numbers (ℚ)
- **Definition (set-theoretic):**  
  `ℚ = { p/q | p ∈ ℤ, q ∈ ℤ\{0} }`
- **Construction from ℤ:**  
  - Rational numbers are **equivalence classes of integer pairs** (p, q) with q ≠ 0.  
  - Two pairs (p,q) and (r,s) are equivalent if p × s = r × q.  
  - **Example:** (1,2) ~ (2,4) represents 1/2  
- **Key concepts:** Addition, multiplication, order, equivalence of fractions.  
- **Use:** Fractions, ratios, algebra, probability.

### 1.4 Real Numbers (ℝ)
- **Definition (set-theoretic, simplified):**  
  ℝ = all numbers that can be represented on the **number line**, including both **rationals (Q) and irrationals (√2, π, etc.)**.  
- **Set-theoretic construction (Dedekind cut idea):**  
  - A real number can be represented as a **set of rationals less than it**.  
  - **Example:** `√2 = { r ∈ ℚ | r² < 2 }`  
    - This set contains all rationals whose square is less than 2.  
    - This “set” now represents the real number √2.  
- **Key concepts:** Completeness, order, arithmetic operations.  
- **Use:** Analysis, calculus, measurement, geometry.
- 
### 1.5 Complex Numbers (ℂ) (Optional / Advanced)
- **Definition (set-theoretic):**  
  `ℂ = { a + bi | a, b ∈ ℝ, i² = -1 }`
- **Key concepts:** Arithmetic of complex numbers, conjugation, magnitude.  
- **Use:** Advanced analysis, algebra, signal processing, physics.

---

## 2. Number Theory and Properties of Numbers

**Number Theory** is the branch of mathematics that studies the **properties and relationships of numbers**, especially integers.  
It focuses on concepts like divisibility, primes, and arithmetic structures, forming the foundation for algebra, cryptography, and proofs.

### 2.1 Prime Numbers
- **Definition:** Numbers greater than 1 with no positive divisors other than 1 and itself.  
- **Examples:** 2, 3, 5, 7, 11…  
- **Importance:** Primes are the **building blocks of integers**; every integer >1 can be factored into primes (Fundamental Theorem of Arithmetic).
```
Example:
60 = 2 × 30
   = 2 × 2 × 15
   = 2 × 2 × 3 × 5
```

### 2.2 Divisibility
- **Definition:** An integer `a` is divisible by `b` (denoted `b | a`) if `a = b × k` for some integer `k`.  
- **Examples:** 12 divisible by 3 because 12 = 3 × 4.  
- **Importance:** Underpins concepts like GCD, LCM, modular arithmetic, and fraction simplification.

### 2.3 Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
- **GCD(a, b):** Largest integer dividing both a and b (e.g., GCD(12,18)=6)  
- **LCM(a, b):** Smallest integer divisible by both a and b (e.g., LCM(12,18)=36)  
- **Importance:** Useful for solving equations, finding common periods, and fraction simplification.

### 2.4 Modular Arithmetic
- **Definition:** Arithmetic where numbers **wrap around** a fixed modulus `n`.  
- **Notation:** `a ≡ b (mod n)` means `a` and `b` have the same remainder when divided by `n`.  
- **Examples:** 17 ≡ 5 (mod 12), 23 ≡ 3 (mod 10)  
- **Importance:** Used in cryptography, clock arithmetic, coding theory, and cyclic patterns.

### 2.5 Other Number Properties
- **Even / Odd numbers:** Classification based on divisibility by 2.  
- **Arithmetic laws:** Commutative, associative, distributive.  
- **Importance:** Ensures that arithmetic operations behave **predictably**, which is crucial for proofs and calculations.

### 2.6 How These Subtopics Connect
- Number theory studies the **structure and behavior of numbers**, especially integers.  
- Concepts like primes, divisibility, GCD/LCM, and modular arithmetic provide **tools for factorization, solving equations, and understanding arithmetic patterns**.  
- These tools are used in algebra, cryptography, coding theory, and formal proofs.

---

## 3. Why Number Systems and Number Theory Are Foundational
1. **Formalizes numbers:** Ensures consistent counting, measurement, and calculation.  
2. **Supports other areas:** Used in algebra, analysis, probability, and more.  
3. **Enables rigorous proofs:** Induction, divisibility, modular reasoning, and factorization are essential for mathematics.

---

## 4. Summary
- **Number systems (as sets):** ℕ, ℤ, ℚ, ℝ, (ℂ)  
- **Number theory / number properties:** Primes, divisibility, GCD/LCM, modular arithmetic, even/odd, arithmetic laws  
- **Foundational role:** Numbers and their properties are the **core building blocks** of mathematics.

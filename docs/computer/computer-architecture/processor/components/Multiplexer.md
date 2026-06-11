---
title: Multiplexer
---

# Multiplexer (MUX)

## What is a Multiplexer?

**Multiplexer** is a **[combinational logic circuit]** that selects one of multiple input signals and forwards it to a single output based on control signals (select lines).

## How does a Multiplexer Work?

**Multiplexer** takes n data inputs and use a `log2(n)-to-n` **[decoder]** to choose the output.

### Example
A **4-to-1 MUX** take 4 data inputs and use a 2-to-4 **[decoder]** to choose one of 4 data inputs
- 4 data inputs: I0, I1, I2, I3 - the signals to choose from
- 2 select input: S0, S1 - Decide which data input appears at the output
The output is:
- I0 if S = 00
- I1 if S = 01
- I2 if S = 10
- I3 if S = 11

![4-to-1 MUX](./images/4-to-1_MUX.jpg)

## How to Build a Multiplexer?

A `n-to-1` **multiplexer** is built using a `log2(n)-to-n` **[decoder]** to choose the output.

![4-to-1 MUX](./images/4-to-1_MUX.jpg)

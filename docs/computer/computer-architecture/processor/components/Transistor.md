---
title: Transistor
---

# Transistor

## What is a Transistor?
A **transistor** is a semiconductor device that acts as an electronic switch or amplifier.
A transistor modifies the **amplitude** (**voltage level**) and sometimes the **current** of the input signal. Depending on its mode of operation, a transistor can:
- Act as a switch – It turns the output on (high voltage) or off (low voltage) based on the input signal.
- Amplify the signal – It increases the power of the input signal by controlling a larger current with a smaller input signal.

It is the fundamental building block of modern computers, replacing vacuum tubes due to its small size, low power consumption, and high speed

Transistors form logic gates (AND, OR, NOT, etc.), which combine to create complex circuits (act as components of a computer): ALU, register, RAM, Flip-Flop, Multiplexer, Decoder, etc.

## How a Transistor works
There are 2 types of transistor: BJT and MOSFET

### Bipolar Junction Transistor (BJT) - Current Controlled

BJT is "current-controlled" → A small Base current controls a larger Collector-Emitter current.

A BJT works by controlling a large current (Collector → Emitter) using a small current at the Base.
- If Base voltage (V_BE) > threshold (~0.7V for silicon BJT) → Transistor turns ON (current flows).
- If Base voltage < threshold → Transistor is OFF (no current).

### MOSFET - Voltage Controlled (Used in Computers)
MOSFET is "voltage-controlled" → No Gate current is needed, just voltage.

A MOSFET works by controlling the flow of current (Drain → Source) using voltage at the Gate:
- If Gate voltage (V_GS) > threshold (~1-3V for MOSFETs) → Transistor turns ON (current flows).
- If Gate voltage < threshold → Transistor is OFF (no current).

### How to Make a Transistor

Transistors are not manufactured individually but  are fabricated collectively as part of a semiconductor chip

## **1. Silicon Extraction & Wafer Preparation**
- **Silicon Purification:** Extracted from sand (SiO₂) and purified to form high-purity silicon ingots.
- **Wafer Formation:** Ingots are sliced into thin wafers and polished for processing.

## **2. Oxidation & Doping**
- **Oxidation:** A thin layer of Silicon Dioxide (SiO₂) is grown to insulate the transistor gate.
- **Doping:** Phosphorus (N-type) or Boron (P-type) is added to create Source, Drain, and Channel regions.

## **3. Photolithography & Etching**
- **Photolithography:** UV light projects a circuit pattern onto a photoresist-coated wafer.
- **Etching:** Unwanted material is removed to shape transistor features.

## **4. Deposition & Metallization**
- **Thin Film Deposition:** Layers of conductive materials (polysilicon, metal) are added.
- **Interconnections:** Metal layers form electrical connections between transistors.

## **5. Testing & Packaging**
- **Electrical Testing:** Wafers are tested for defects.
- **Dicing & Packaging:** Functional chips are cut, packaged, and integrated into CPUs, GPUs, and memory.

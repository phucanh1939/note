## 2. Project Architecture: The Malenia-Level Boss Fight

This vertical slice is specifically designed to showcase your enterprise-grade software architecture, cache line optimization, and memory virtualization.

```
                      ┌───────────────────────────────┐
                      │    CORE SYSTEMS CONTROLLER    │
                      └───────────────┬───────────────┘
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         ▼                            ▼                            ▼
[ Async Asset Manager ]     [ Attribute Modifier Stack ]     [ Combat Broker Pool ]
 • TSoftObjectPtr references  • Contiguous memory structs     • Array of pre-allocated hits
 • Pre-cache Phase 2 in vRAM  • Bitwise flags for statuses    • Sweep shape multi-casts

```

### The 4 Crucial Engineering Subsystems

### 1. The Async Asset Memory Manager (Phase 2 Transition)

* **The Mechanics:** Do not hard-reference Phase 2 textures, animations, or VFX inside the Boss Actor at boot time, as it permanently blares console VRAM.
* **The Engineering:** Keep all Phase 2 assets wrapped in **Soft Object References (`TSoftObjectPtr<T>`)**. Use a C++ manager hooked to Unreal's `FStreamableManager` to asynchronously stream those assets into memory *in the background* during the Phase 1 death cinematic.

### 2. Event-Driven Attribute & Status Modifier Stack (Lifesteal & Rot)

* **The Mechanics:** Tracks player health, poise, lifesteal metrics, and elemental status build-ups without running expensive frame-by-frame tick loops.
* **The Engineering:** Store core gameplay stats inside data-aligned, lightweight C++ structs (`FAttribute`). Track active crowd control or damage-over-time variables using **C++ Bitwise Flags (Bitmasks)** to keep validation operations running in tiny fractions of a CPU clock cycle.

### 3. Object-Pooled Combat Broker (Waterfowl Flurry Hitboxes)

* **The Mechanics:** Safely handles high-frequency multi-hit frame data (like Malenia's iconic flurry attack) without tanking the frame rate on target hardware.
* **The Engineering:** Leverage **Animation Notifies (AnimNotifies)** in C++ to drive active threat windows. Run performance-optimized collision sweeps (`SweepMultiByChannel`) using a pre-allocated array (object pool) of spatial query structs to completely avoid runtime heap allocation fragmentation.

### 4. Hierarchical C++ AI Decision Tree (Input Reading & Spacing)

* **The Mechanics:** Recreates intelligent, ultra-responsive boss behavior (such as lunging forward immediately when detecting a player healing action) without creating a messy nesting of `if/else` statements.
* **The Engineering:** Build a decoupled **Hierarchical Finite State Machine (HFSM)** in C++ where distinct behaviors live in isolated classes. Bind the boss to an event-driven **Player Observer Pattern** that listens directly for player input broadcasts to trigger instant, logical counter-attacks.

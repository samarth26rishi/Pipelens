# Pipelens
Instruction pipeline simulator that models execution cycles, detects data/control hazards, and analyzes performance bottlenecks using trace-driven inputs.

**CPU Pipeline Simulator & Hazard Analysis Framework**

---

##  Overview

PipelineScope is a Python-based simulation framework that models instruction-level execution in a pipelined processor. It enables users to visualize how instructions flow through pipeline stages, detect hazards, and analyze performance bottlenecks.

The project is designed for **computer architecture learning**, **performance analysis**, and **academic experimentation**, with a strong focus on clarity and extensibility.

---

##  Features

-  **Pipeline Simulation**
  - Models multi-stage CPU pipelines (e.g., IF, ID, EX, MEM, WB)
  - Simulates instruction flow cycle-by-cycle

- **Hazard Detection**
  - Data hazards (RAW, WAR, WAW)
  - Control hazards (branch-related)
  - Structural hazards (resource conflicts)

- **Cycle Tracking**
  - Tracks pipeline stalls and delays
  - Provides detailed timing analysis

- **Performance Metrics**
  - CPI (Cycles Per Instruction)
  - Total execution cycles
  - Stall count and distribution

-  **Bottleneck Analysis**
  - Identifies slow stages and inefficiencies
  - Helps understand pipeline limitations

-  **Trace-Driven Simulation**
  - Accepts structured instruction input files
  - Enables reproducible experiments

---

##  Pipeline Model

The simulator uses a standard 5-stage pipeline:

1. **IF** – Instruction Fetch  
2. **ID** – Instruction Decode  
3. **EX** – Execute  
4. **MEM** – Memory Access  
5. **WB** – Write Back  

Each instruction progresses through these stages unless stalled due to hazards.

---

##  Input Format

The simulator takes an **instruction trace file** as input.

### Supported Instruction Types
- Arithmetic: `ADD`, `SUB`, `MUL`, `DIV`
- Memory: `LOAD`, `STORE`
- Control: `BRANCH`, `JUMP`

---


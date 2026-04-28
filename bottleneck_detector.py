def detect_bottleneck(hazards):
    raw = hazards.get("RAW Stall Cycles", 0)
    mem = hazards.get("Memory Stall Cycles", 0)

    if mem > raw:
        return "Memory Bound"
    elif raw > mem:
        return "Data Dependency"
    else:
        return "Balanced / Compute Bound"
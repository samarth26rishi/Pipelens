def analyze_hazards(sim_result):
    return {
        "RAW Stall Cycles": sim_result.get("raw_stalls", 0),
        "Memory Stall Cycles": sim_result.get("mem_stalls", 0),
        "Branch Penalty Cycles": 0,  # explicitly zero now
        "WAR Hazards": sim_result.get("war_count", 0),
        "WAW Hazards": sim_result.get("waw_count", 0)
    }
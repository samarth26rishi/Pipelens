def compute_ideal_cycles(instructions, latency_fn):
    if not instructions:
        return 0

    completion_times = []

    for i, inst in enumerate(instructions):
        issue_time = i
        latency = latency_fn(inst["opcode"])
        complete_time = issue_time + latency
        completion_times.append(complete_time)

    return max(completion_times)

def compute_efficiency(ideal, actual):
    if actual == 0:
        return 0
    return (ideal / actual) * 100
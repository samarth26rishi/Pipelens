LATENCY = {
    "ADD": 1, "SUB": 1,
    "MUL": 3, "DIV": 3,
    "LOAD": 5, "STORE": 5,
    "BRANCH": 2, "JUMP": 2
}

def get_latency(opcode):
    return LATENCY.get(opcode, 1)
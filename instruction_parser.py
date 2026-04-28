def parse_instruction(line):
    parts = line.strip().split()
    
    opcode = parts[0]
    dest = parts[1] if len(parts) > 1 else None
    src1 = parts[2] if len(parts) > 2 else None
    src2 = parts[3] if len(parts) > 3 else None
    
    return {
        "opcode": opcode,
        "dest": dest,
        "src": [src1, src2]
    }

def parse_trace(trace_lines):
    return [parse_instruction(line) for line in trace_lines if line.strip()]
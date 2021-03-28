# This script contains the implementation of instructions
# And mapping ints to instruction names
# As well as the get_theo function, which evaluates the result of
# an instruction based on the opcode in the "unord" dict

unord = {0: "addr",
1: "addi",
2: "mulr",
3: "muli",
4: "banr",
5: "bani",
6: "borr",
7: "bori",
8: "setr",
9: "seti",
10: "gtir",
11: "gtri",
12: "gtrr",
13: "eqir",
14: "eqri",
15: "eqrr"}

def addr(reg, a, b):
    return reg[a] + reg[b]

def addi(reg, a, b):
    return reg[a] + b

def mulr(reg, a, b):
    return reg[a] * reg[b]

def muli(reg, a, b):
    return reg[a] * b

def banr(reg, a, b):
    return reg[a] & reg[b]

def bani(reg, a, b):
    return reg[a] & b

def borr(reg, a, b):
    return reg[a] | reg[b]

def bori(reg, a, b):
    return reg[a] | b

def setr(reg, a, b):
    return reg[a]

def seti(reg, a, b):
    return a

def gtir(reg, a, b):
    return int(a > reg[b])

def gtri(reg, a, b):
    return int(reg[a] > b)

def gtrr(reg, a, b):
    return int(reg[a] > reg[b])

def eqir(reg, a, b):
    return int(a == reg[b])

def eqri(reg, a, b):
    return int(reg[a] == b)

def eqrr(reg, a, b):
    return int(reg[a] == reg[b])

def get_theo(op, reg, instr):
    a = instr[1]
    b = instr[2]
    codename = unord[op]
	
    if codename == "addr":
        return addr(reg, a, b)
    elif codename == "addi":
        return addi(reg, a, b)
    elif codename == "mulr":
        return mulr(reg, a, b)
    elif codename == "muli":
        return muli(reg, a, b)
    elif codename == "banr":
        return banr(reg, a, b)
    elif codename == "bani":
        return bani(reg, a, b)
    elif codename == "borr":
        return borr(reg, a, b)
    elif codename == "bori":
        return bori(reg, a, b)
    elif codename == "setr":
        return setr(reg, a, b)
    elif codename == "seti":
        return seti(reg, a, b)
    elif codename == "gtir":
        return gtir(reg, a, b)
    elif codename == "gtri":
        return gtri(reg, a, b)
    elif codename == "gtrr":
        return gtrr(reg, a, b)
    elif codename == "eqir":
        return eqir(reg, a, b)
    elif codename == "eqri":
        return eqri(reg, a, b)
    elif codename == "eqrr":
        return eqrr(reg, a, b)

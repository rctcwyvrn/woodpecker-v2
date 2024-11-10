import sys 

inc = "INC"
inv = "INV"
load = "LOAD"
cdec = "CDEC"

def one_bit_xor():
    program = [
        [inc, inc, inc, inc], # addr = 4
        inv,
        [load, cdec, cdec, cdec, cdec], # addr = 0
        [inc, load, cdec], # addr = 0 if b else addr = 1
        inv, # addr = 0 a xor b, addr 1 maybe garbage
        [inc, inc, inc], # addr = 3 if b else addr = 4
        [load, cdec], # addr = 3
        [inv, load, cdec, cdec, cdec], # reg = 1, addr = 0
        load, # reg = a xor b
        [inc, inc, inc, cdec, inv] # addr 2 = a xor b
    ]
    return program

class Compiler:
    def __init__(self):
        pass

    def unnest(self, xs):
        res = []
        for part in xs:
            if isinstance(part, list) or isinstance(part, tuple):
                res.extend(self.unnest(part))
            else:
                res.append(part)
        return res

    def assemble(self, program):
        lines = self.unnest(program)
        return "\n".join(lines)


c = Compiler()
with open(sys.argv[1], "w") as f:
    f.write(c.assemble(one_bit_xor()))    
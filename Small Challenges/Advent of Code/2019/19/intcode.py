class Program:    
    def __init__(self, fileName):
        file = open(fileName)
        self.program = [int(val) for val in file.read().strip().split(',')]
        file.close()

        self.create_func_map()

        self.pos = 0
        self.base = 0
        self.inputs = []
        self.last_output = None
        self.outputs = []

    def split_opcode(self, code):
        return (((code // 100) % 10),
                ((code // 1000) % 10),
                ((code // 10000) % 10))

    def op_1(self, mode):
        self.program[self.posmode(mode[2], self.pos + 3)] = (
            self.valmode(mode[1], self.pos + 2) +
            self.valmode(mode[0], self.pos + 1))

        self.pos += 4

    def op_2(self, mode):
        self.program[self.posmode(mode[2], self.pos + 3)] = (
            self.valmode(mode[1], self.pos + 2) *
            self.valmode(mode[0], self.pos + 1))
        self.pos += 4

    def op_3(self, mode):
        self.program[self.posmode(mode[0], self.pos + 1)] = (
            int(input("Input: ").strip())
            if (len(self.inputs) == 0) else self.inputs.pop(0))
        self.pos += 2

    def add_input(self, num):
        self.inputs.append(num)

    def op_4(self, mode):
        self.last_output = self.valmode(mode[0], self.pos + 1)
        self.outputs.append(self.last_output)
        self.pos += 2

    def get_outputs(self):
        output_lst = self.outputs
        self.last_output = None
        self.outputs = []
        return output_lst

    def op_5(self, mode):
        if self.valmode(mode[0], self.pos + 1) != 0:
            self.pos = self.valmode(mode[1], self.pos + 2)
        else:
            self.pos += 3

    def op_6(self, mode):
        if self.valmode(mode[0], self.pos + 1) == 0:
            self.pos = self.valmode(mode[1], self.pos + 2)
        else:
            self.pos += 3

    def op_7(self, mode):
        self.program[self.posmode(mode[2], self.pos + 3)] = int(
            self.valmode(mode[0], self.pos + 1) <
            self.valmode(mode[1], self.pos + 2))
        self.pos += 4

    def op_8(self, mode):
        self.program[self.posmode(mode[2], self.pos + 3)] = int(
            self.valmode(mode[0], self.pos + 1) ==
            self.valmode(mode[1], self.pos + 2))
        self.pos += 4

    def op_9(self, mode):
        self.base += self.valmode(mode[0], self.pos + 1)
        self.pos += 2

    def create_func_map(self):
        self.fmap = [self.op_1, self.op_2, self.op_3, self.op_4,
                     self.op_5, self.op_6, self.op_7, self.op_8,
                     self.op_9]

    def posmode(self, mode, pos):
        outpos = None
        self.extend_prog(pos)
        if mode == 2:
            outpos = self.program[pos] + self.base
        elif mode == 0:
            outpos = self.program[pos]
        else:
            return None

        self.extend_prog(outpos)
        return outpos
        
    def valmode(self, mode, pos):
        outpos = None
        if mode == 2:
            self.extend_prog(pos)
            outpos = self.program[pos] + self.base
        elif mode == 1:
            outpos = pos
        elif mode == 0:
            self.extend_prog(pos)
            outpos = self.program[pos]
        else:
            return None

        self.extend_prog(outpos)
        return self.program[outpos]
            

    def extend_prog(self, pos):
        if (pos >= len(self.program)):
            self.program.extend([0 for x in range(pos - len(self.program) + 1)])
    
    def run(self, stop = 99):
        while self.program[self.pos] != stop and self.program[self.pos] != 99:
            try:
                self.fmap[(self.program[self.pos] % 100) - 1](
                    self.split_opcode(self.program[self.pos]))
            except IndexError:
                raise IndexError("Unknown operation: " + str((self.program[self.pos])))

            #self.extend_prog(self.pos + 4)\
    def get_state(self):
        return (self.pos, self.base, self.program[:])

if __name__ == "__main__":
    print("Please create an instance of this class and use .run()")

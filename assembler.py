import sys

def twos(x):
    if x[0] == "-":
        temp = x[1:]
        x = temp
    else:
        return x
    
    two = []
    for i in x:
        if i == "0":
            two.append("1")
        else:
            two.append("0")
    
    oneAdd = True
    pos = -1
    while(oneAdd):
        
        if two[pos] == "0":
            two[pos] = "1"
            oneAdd = False
        else:
            two[pos] = "0"
            pos -=1
    return "".join(two)
    

## R type
class add:
    opcode = "000"
    def __init__(self,inst):
        self.regA = "{0:b}".format(int(inst[0])).zfill(3)
        self.regB = "{0:b}".format(int(inst[1])).zfill(3)
        self.destReg =  "{0:b}".format(int(inst[2])).zfill(3)

    def print(self):
        return int(self.opcode+self.regA+self.regB+"0"*13+self.destReg,2)
class nand:
    opcode = "001"
    def __init__(self,inst):
        self.regA = "{0:b}".format(int(inst[0])).zfill(3)
        self.regB = "{0:b}".format(int(inst[1])).zfill(3)
        self.destReg =  "{0:b}".format(int(inst[2])).zfill(3)
    def print(self):
        return int(self.opcode+self.regA+self.regB+"0"*13+self.destReg,2)

## I type
class lw:
    opcode = "010"
    def __init__(self,inst):
        self.regA = "{0:b}".format(int(inst[0])).zfill(3)
        self.regB = "{0:b}".format(int(inst[1])).zfill(3)
        self.offsetField =  twos("{0:b}".format(int(inst[2]))).zfill(16)
    def print(self):
        return int(self.opcode+self.regA+self.regB+self.offsetField,2)

class sw:
    opcode = "011"
    def __init__(self,inst):
        self.regA = "{0:b}".format(int(inst[0])).zfill(3)
        self.regB = "{0:b}".format(int(inst[1])).zfill(3)
        self.offsetField =  twos("{0:b}".format(int(inst[2]))).zfill(16)
    def print(self):
        return int(self.opcode+self.regA+self.regB+self.offsetField,2)
class beq:
    opcode = "100"
    def __init__(self,inst):
        self.regA = "{0:b}".format(int(inst[0])).zfill(3)
        self.regB = "{0:b}".format(int(inst[1])).zfill(3)
        self.offsetField =  twos("{0:b}".format(int(inst[2]))).zfill(16)
    def print(self):
        return int(self.opcode+self.regA+self.regB+self.offsetField,2)
## J type
class jalr:
    opcode = "101"
    def __init__(self,inst):
        self.regA = "{0:b}".format(int(inst[0])).zfill(3)
        self.regB = "{0:b}".format(int(inst[1])).zfill(3)
    def print(self):
        return int(self.opcode+self.regA+self.regB+"0"*16)
        
        
## O type
class halt:
    opcode = "110"
    def __init__(self,v):
        pass
    def print(self):
        return int(self.opcode+"0"*22,2)

class noop:
    opcode = "111"
    def __init__(self,v):
        pass
    def print(self):
        return int(self.opcode+"0"*22,2)

class fill:
    def __init__(self,v):
        self.value = v
    def print(self):
        return int(self.value)
instructions = {"add":add,"nand":nand,"lw":lw,
                "sw":sw,"beq":beq,"jalr":jalr}
smallInts = {"halt":halt,"noop":noop,".fill":fill}

if __name__ == "__main__":
    whiteSpaces = ['\t',' ']

    if len(sys.argv) != 3:
        print("incorrect input")
        exit(1)

    assembleCode = open(sys.argv[1]).readlines()
    
    symbolicAddress = {}
    inst = []
    order = []
    ## first pass
    for i,line in enumerate(assembleCode, 0):
        temp = line.split("\t")
        if temp[0] != "":
            if temp[0] in symbolicAddress:
                
                exit(1)
            else:
                symbolicAddress[temp[0]] = i
        if len(temp)>=4:
            inst.append(temp[1:-1])
        else:
            inst.append(temp[1:])

    ## need to add check for offsets
    for line in inst:
        if line[0][-1] == '\n':
            line[0] = line[0][:-1]
        if line[0] in instructions:
            vals = []
            for i in line[1:]:
                if i.isnumeric():
                    vals.append(i)
                elif i in symbolicAddress:
                    vals.append(symbolicAddress[i])
                else:
                    ## unidentified label
                    print(i)
                    exit(1)
            order.append(instructions[line[0]](vals))
        elif line[0] in smallInts: 
            val = 0

            if len(line) > 1 and line[1] in symbolicAddress:
               val = symbolicAddress[line[1]]
            elif len(line)>1:
                val = line[1]
            order.append(smallInts[line[0]](val))
        else:
            print(line)
            exit(1)
            
    for i in order:
        print(i.print())


        






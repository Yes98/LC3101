import simulate as sim

def untwos(x):
    if x[0] == '0':
        return int(x,2)
    two = ['1' if x == '0' else '0' for x in x]
    oneAdd = True
    pos = -1
    while(oneAdd):
        
        if two[pos] == "0":
            two[pos] = "1"
            oneAdd = False
        else:
            two[pos] = "0"
            pos -=1
    return -1*int(''.join(two),2)


def twos(x):
    if(int(x,2) >32767 or int(x,2) < -327678 ):
        print(x)
        exit(1)
    if x[0] == "-":
        temp = x[1:]
        x = temp
    else:
        return x.zfill(16)
   
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
    ret = "".join(two)
    
    return "1"*(16-len(ret)) + ret

## R type
class add:
    opcode = "000"
    def __init__(self,inst,dec=0):
        if(dec):
            self.regA = int(inst[:3],2)
            self.regB = int(inst[3:6],2)
            self.destReg = int(inst[-3:],2)
        else:
            self.regA = "{0:b}".format(int(inst[0])).zfill(3)
            self.regB = "{0:b}".format(int(inst[1])).zfill(3)
            self.destReg =  "{0:b}".format(int(inst[2])).zfill(3)
    def print(self):
        return int("0"*7+self.opcode+self.regA+self.regB+"0"*13+self.destReg,2)
    def execute(self,state):
        state.pc+=1
        state.reg[self.destReg] = state.reg[self.regA] + state.reg[self.regB]
        return True
    
class nand:
    opcode = "001"
    def __init__(self,inst,dec=0):
        if(dec):
            self.regA = int(inst[:3],2)
            self.regB = int(inst[3:6],2)
            self.destReg = int(inst[-3:],2)
        else:
            self.regA = "{0:b}".format(int(inst[0])).zfill(3)
            self.regB = "{0:b}".format(int(inst[1])).zfill(3)
            self.destReg =  "{0:b}".format(int(inst[2])).zfill(3)
    def print(self):
        return int("0"*7+self.opcode+self.regA+self.regB+"0"*13+self.destReg,2)
    def execute(self,state):
        state.pc+=1
        #### this may be an issue
        state.reg[self.destReg] = ~(state.reg[self.regA] & state.reg[self.regB])
        return True
## I type
class lw:
    opcode = "010"
    def __init__(self,inst,dec=0):
        if(dec):
            self.regA = int(inst[:3],2)
            self.regB = int(inst[3:6],2)

            ## need to change this to handle twos compliment
            self.offsetField = untwos(inst[6:])
        else:
            self.regA = "{0:b}".format(int(inst[0])).zfill(3)
            self.regB = "{0:b}".format(int(inst[1])).zfill(3)
            self.offsetField =  twos("{0:b}".format(int(inst[2]))).zfill(16)
    def print(self):
        return int("0"*7+self.opcode+self.regA+self.regB+self.offsetField,2)
    def execute (self,state):
        state.pc+=1
        print(self.offsetField + state.reg[self.regA])
        state.reg[self.regB] = state.mem[self.offsetField + state.reg[self.regA]]
        return True

class sw:
    opcode = "011"
    def __init__(self,inst,dec=0):
        if(dec):
            self.regA = int(inst[:3],2)
            self.regB = int(inst[3:6],2)
            self.offsetField = untwos(inst[6:])
        else:
            self.regA = "{0:b}".format(int(inst[0])).zfill(3)
            self.regB = "{0:b}".format(int(inst[1])).zfill(3)
            self.offsetField =  twos("{0:b}".format(int(inst[2]))).zfill(16)
    def print(self):
        return int("0"*7+self.opcode+self.regA+self.regB+self.offsetField,2)
    def execute(self,state):
        state.pc+=1
        state.mem[self.regA + self.offsetField] = state.reg[self.regB]
        return True

class beq:
    opcode = "100"
    def __init__(self,inst,dec=0):
        if(dec):
            
            self.regA = int(inst[:3],2)
            self.regB = int(inst[3:6],2)
            self.offsetField = untwos(inst[6:])
        else:
            self.regA = "{0:b}".format(int(inst[0])).zfill(3)
            self.regB = "{0:b}".format(int(inst[1])).zfill(3)
            self.offsetField =  twos("{0:b}".format(int(inst[2])))
    def print(self):
        
        return int("0"*7+self.opcode+self.regA+self.regB+self.offsetField,2)
    def execute(self,state):
        
        if(state.reg[self.regA] == state.reg[self.regB]):
            print(self.offsetField)
            state.pc = state.pc+1+ self.offsetField
        else:
            state.pc +=1
        return True

## J type
class jalr:
    opcode = "101"
    def __init__(self,inst,dec=1):
        if(dec):
            
            self.regA = int(inst[:3],2)
            self.regB = int(inst[3:6],2)
        else:
            self.regA = "{0:b}".format(int(inst[0])).zfill(3)
            self.regB = "{0:b}".format(int(inst[1])).zfill(3)
    def print(self):
        return int("0"*7+self.opcode+self.regA+self.regB+"0"*16)
    def execute(self,state):
        self.regB = state.pc +1
        state.pc = self.regA
        return True
        
## O type
class halt:
    opcode = "110"
    def __init__(self,v,dec=0):
        pass
    def print(self):
        return int("0"*7+self.opcode+"0"*22,2)
    def execute(self,state):
        state.pc +=1
        return False



class noop:
    opcode = "111"
    def __init__(self,v,dec=0):
        pass
    def print(self):
        return int("0"*7+self.opcode+"0"*22,2)
    def execute(self,state):
        state.pc +=1
        return True

class fill:
    opcode = ""
    def __init__(self,v):
        self.value = v
    def print(self):
        return int(self.value)

opcodes = {"000":add,"001":nand,"010":lw,
          "011":sw,"100":beq,"101":jalr,
          "110":halt,"111":noop}
instructions = {"add":add,"nand":nand,"lw":lw,
                "sw":sw,"beq":beq,"jalr":jalr}
smallInts = {"halt":halt,"noop":noop,".fill":fill}
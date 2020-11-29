import instructions as inst
import sys 
numRegs = 8
class stateStruct:
    def __init__(self, nm):
        self.pc = 0
        self.mem =[0]*65536
        self.reg = [0]*8
        self.numMemory = nm
        self.IFID ={"instr":inst.noop(),"pcPlus1":0}
        self.IDEX = {"instr":inst.noop(),"pcPlus1": 0, "readRegA":0, "readRegB": 0, "offset": 0}
        self.EXMEM = {"instr":inst.noop(), "branchTarget":0, "aluResult": 0, "readRegB":0 }
        self.MEMWB = {"instr": inst.noop(), "writeData":0}
        self.WBEND = {"instr": inst.noop(), "writeData": 0}
        self.cycles = 0




def printState(state):
    print(f"\n@@@\nstate before cycle {state.cycles} starts")
    print(f"\tpc state.pc")

    print(f"\tdata memory:")
    for i in range(state.numMemory):
        print(f"\t\tdataMem[ {i} ] {state.mem[i]}")

    print("\tregisters:")
    for i in range(numRegs):
        print(f"\t\treg[ {i} ] {state.reg[i]}")
    
    print("\tIFID:")
    print(f"\t\tinstruction {state.IFID["instr"].instrPrint()}")
    print(f"\t\tpcPlus1 {state.IFID["pcPlus1"]}")

    print(f"\tIDEX:")
    print(f"\t\tinstruction {state.IDEX["instr"].instrPrint()}")
    print(f"\t\tpcPlus1 {state.IDEX["pcPlus1"]}")
    print(f"\t\treadRegA {state.IDEX["readRegA"]}")
    print(f"\t\treadRegB {state.IDEX["readRegB"]}")
    print(f"\t\toffset {state.IDEX["offset"]}")

    print(f"\tEXMEM:")
    print(f"\t\tinstruction {state.EXMEM["instr"].instrPrint()}")
    print(f"\t\tbranchTarget {state.EXMEM["branchTarget"]}")
    print(f"\t\taluResult {state.EXMEM["aluResult"]}")
    print(f"\t\treadRegB {state.EXMEM["readRegB"]}")

    print(f"\tMEMWB:")    
    print(f"\t\tinstruction {state.MEMWB["instr"].instrPrint()}")
    print(f"\t\twriteData {state.MEMWB["writeData"]}")

    print(f"\tWBEND:")
    print(f"\t\tinstruction {state.WBEND["instr"].instrPrint()}")
    print(f"\t\twriteData {state.WBEND["writeData"]}")


def execute(state):
    memVal = "{:032b}".format(state.mem[state.pc])[7:]
    currentInst = inst.opcodes[memVal[:3]](memVal[3:],1)
    
    return currentInst.execute(state)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("incorrect input")
        exit(1)

    machineCode = open(sys.argv[1]).readlines()
    state = stateStruct(len(machineCode))

    for i in range(len(machineCode)):
        state.mem[i] = int(machineCode[i])
        ##print("{:032b}".format(state.mem[i])[7:])
    
    ##for i in range(state.numMemory):
    t = 1
    printState(state)
    while(1):
        printState(state)

        if(state.MEMWB["instr"] == "halt"):
            print("machine halted")
            print(f"total of {state.cycles} executed")
        t+=1

        newState = state
        newState.cycles+=1

        ## ---------------- IF Stage -----------------
        memVal = "{:032b}".format(state.mem[state.pc])[7:]
        newState.IFID["instr"] = inst.opcodes[memVal[:3]](memVal[3:],1)
        newState.IFID["pcPlust1"] = state.pc +1


        ## ---------------- ID Stage -----------------
        newState.IDEX["instr"] = state.IFID["instr"]


        state = newState

    
    print("end state")
    print("machine halted")
    print(f"total of {t} instructions executed")
    print("final state of machine: ")
    printState(state)
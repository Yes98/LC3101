import instructions as inst
import sys 




class stateStruct:
    def __init__(self, nm):
        self.pc = 0
        self.mem =[0]*65536
        self.reg = [0]*8
        self.numMemory = nm
      




def printState(state):
    print("\n@@@\nstate:")
    print(f"\tpc {state.pc}")
    print("\tmemory:")

    for i in range(state.numMemory):
        print(f"\t\tmem[ {i} ] {state.mem[i]}")

    print("\tregisters:")

    for i in range(len(state.reg)):
        print(f"\t\treg[ {i} ] {state.reg[i]}")

    print("end state")

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
    while(execute(state)):
        if(state.pc > len(machineCode)):
            break
        printState(state)
        t+=1

    
    print("end state")
    print("machine halted")
    print(f"total of {t} instructions executed")
    print("final state of machine: ")
    printState(state)
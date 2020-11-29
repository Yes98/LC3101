import sys
import instructions 
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


if __name__ == "__main__":
    whiteSpaces = ['\t',' ']

    if len(sys.argv) != 3:
        print("incorrect input")
        exit(1)

    assembleCode = open(sys.argv[1]).readlines()
    outputCode = open(sys.argv[2],'w')
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
    ## fix symbolic address
    memlock = 0
    for line in inst:
       ## print(line)
        if line[0][-1] == '\n':
            line[0] = line[0][:-1]
        if line[0] in instructions.instructions:
            vals = []
            for i in line[1:]:
                try:
                    int(i)
                    dig = True
                except:
                    dig = False
                if dig:
                    vals.append(i)
                elif i in symbolicAddress:
                    if line[0] == "beq" or line[0] == "jalr":
                        vals.append(symbolicAddress[i]-memlock-1)
                        
                    else:
                        vals.append(symbolicAddress[i])
                    
                else:
                    ## unidentified label
                    outputCode.write(i+'\n')
                    print(line)
                    print(i+"SDS")
                    exit(1)
           
            print(line)
            order.append(instructions.instructions[line[0]](vals))
        elif line[0] in instructions.smallInts: 
            val = 0

            if len(line) > 1 and line[1] in symbolicAddress:
               val = symbolicAddress[line[1]]
            elif len(line)>1:
                val = line[1]
            order.append(instructions.smallInts[line[0]](val))
        else:
            print(line+"DS")
            exit(1)
        memlock +=1
    for i in order:
        print("hello")
        outputCode.write(str(i.Print())+'\n')
        print(i.Print())


        






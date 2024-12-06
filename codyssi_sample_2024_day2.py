def main(directory):
    print("Part 1:",part1(directory))
    print("Part 2:",part2(directory))
    print("Part 3:",part3(directory))

def part1(directory):
    f=open(directory)
    total=0
    for i,line in enumerate(f):
        if line.strip()=="TRUE":
            total+=i+1
    f.close()
    return total

def alternating(data):
    total=0
    count=1
    for i in range(0,len(data)-1,2):
        #print(data[i],data[i+1])
        #input()
        # if it is odd:
        if count%2!=0 and data[i]=="TRUE" and data[i+1]=="TRUE":
            total+=1
            #input("+1")
        elif count%2==0 and (data[i]=="TRUE" or data[i+1]=="TRUE"):
            total+=1
            #input("+1")
        count+=1
    
    return total


def alternating_recursive(data,total=0):
    count=1
    data2=[]
    for i in range(0,len(data)-1,2):
        #print(data[i],data[i+1])
        #input()
        # if it is odd:
        if (count%2!=0 and data[i]=="TRUE" and data[i+1]=="TRUE") or (count%2==0 and (data[i]=="TRUE" or data[i+1]=="TRUE")):
            data2.append("TRUE")
            total+=1
        else:
            data2.append("FALSE")
        count+=1


    if len(data2)!=1:
        total=alternating_recursive(data2,total)
    # base case
    else:
        match data2[0]:
            case "TRUE":
                return total+1
            case _:
                return total
    return total
        


def part2(directory):
    f=open(directory)
    data=[]
    for statement in f:
        data.append(statement.strip())
    
    f.close()
    return alternating(data)
    
def part3(directory):
    f=open(directory)
    data=[]
    for statement in f:
        data.append(statement.strip())
    result=alternating_recursive(data)
    for item in data:
        if item=="TRUE":
            result+=1
    f.close()
    return result




main("sample_round\datainput_codyssi_sample_2024_day2.txt")
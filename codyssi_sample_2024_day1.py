
def main(input):
    
    print("Part 1: ",part1(input))
    
    print("Part 2: ",part2(input))
    
    print("Part 3: ",part3(input))
    


def part1(input):
    f=open(input,"r")
    sum=0
    for num in f:
        sum+=int(num.strip())
    f.close()
    return sum
    

def part2(input):
    
    f=open(input,"r")
    sum=0
    mostexpensive=[]
    for num in f:
        mostexpensive.append(int(num.strip()))
        mostexpensive.sort()
        if len(mostexpensive)>20:
            sum+=mostexpensive.pop(0)
    f.close()
    return sum

def part3(input):
    
    f=open(input,"r")
    count=1
    sum=0
    for num in f:
        #if odd:
        if count%2!=0:
            sum+=int(num.strip())
        else:
            sum-=int(num.strip())
        count+=1
    f.close()
    return sum

main("datainput_codyssi_sample_2024_day1.txt")
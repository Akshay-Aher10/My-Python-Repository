from ast import In
def FindLargestElment(Arr):
    Max = 0
    iCnt = 0
    
    while iCnt < len(Arr):
        if Arr[iCnt] > Max:
            Max = Arr[iCnt]
        
        iCnt = iCnt+1

    return Max

def main():

    Arr = list()
    size = int(input("Enter no of elements you want\n"))

    print("Enter Elements")

    for i in range(0,size):         
         no = int(input())
         Arr.append(no)

    Ret = FindLargestElment(Arr)

    print("largets element is : ",Ret)


if __name__ == "__main__":
    main()
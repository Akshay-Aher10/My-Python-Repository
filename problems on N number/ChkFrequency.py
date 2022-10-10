# Accept N numbers from user and one number and check frequency of that number  in the list of numbers.

def ChkFrequency(Arr,Num):
    iCnt =0
    for i in Arr:
        if(i == Num):
            iCnt+=1
    return iCnt        

def main():
    Arr = list()

    No = int(input("Enter How many elements you want in list\n"))

    print("Enter Element :")

    for i in range(0,No):
        Value = int(input())
        Arr.append(Value)

    Num = int(input("Enter number to check Frequency of that Number :\n"))
    
    ret = ChkFrequency(Arr,Num)
    print("Frequency of ",Num," : ",ret)


if __name__ =="__main__":
    main()

def ChkLastOccurance(Arr,Num):
    X = -1

    for i in range(len(Arr)-1,0,-1):
        if Arr[i] == Num:
            X=i
            break;
    
    return X


def ChkFirstOccurance(Arr,Num):
    X = -1

    for i in range(0,len(Arr)):
        if Arr[i] == Num:
            X=i
            break;
    
    return X

def main():

    Arr = list()

    No = int(input("Enter How many elements you want in list\n"))
    
    print("Enter Element :")
    for i in range(0,No):
        N = int(input())
        Arr.append(N)

    Num = int(input("Enter number to check Frequency of that Number :\n"))    

    Ret = ChkFirstOccurance(Arr,Num)
    
    if( Ret == -1):
        print("Number is Not present in the List")
    else:
        print("First Occurance on : Index No ",Ret)

    Ret1 = ChkLastOccurance(Arr,Num)
    
    if( Ret1 == -1):
        print("Number is Not present in the List")
    else:
        print("Last Occurance on : Index No ",Ret1)    


if __name__ =="__main__":
    main()
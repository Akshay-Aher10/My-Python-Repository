# Accpet N NUmber from User and Store it into list.
# Return Maximum Element from that list

def Maximum(Arr):

    Max = Arr[0]

    for i in Arr:
        if(i>Max):
            Max = i
    return Max

def Main():

    Data = []

    No = int(input("Enter NO of Element you want in List\n"))
    print("Enter Element :")

    for i in range(0,No):
        no = int(input())
        Data.append(no)

    Ret = Maximum(Data)
    print("Maximum Element is :",Ret)

if __name__ =="__main__":
    Main()
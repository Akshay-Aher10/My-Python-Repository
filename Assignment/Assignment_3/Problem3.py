# Accpet N NUmber from User and Store it into list.
#Return Minimum from List


def Minimum(Arr):

    Min = Arr[0]

    for i in Arr:
        if(i<Min):
            Min = i
    return Min

def Main():

    Data = []

    No = int(input("Enter NO of Element you want in List\n"))
    print("Enter Element :")

    for i in range(0,No):
        no = int(input())
        Data.append(no)

    Ret = Minimum(Data)
    print("Minimum Element is :",Ret)

if __name__ =="__main__":
    Main()
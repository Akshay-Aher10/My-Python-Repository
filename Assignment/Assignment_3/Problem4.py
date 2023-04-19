# Accpet N NUmber from User and Store it into list.
# Accpet 1 Number from user
#Return Frequency of that number



def Frequency(Arr,No):

    Count = 0

    for i in Arr:
        if(i ==No):
            Count +=1
    return Count

def Main():

    Data = []

    No = int(input("Enter NO of Element you want in List\n"))
    Value = int(input("Enter One Number to check Frequency\n"))
    
    print("Enter Element :")
    for i in range(0,No):
        no = int(input())
        Data.append(no)

    Ret = Frequency(Data,Value)
    print("Frequency of",Value,"in the given List is :",Ret)

if __name__ =="__main__":
    Main()
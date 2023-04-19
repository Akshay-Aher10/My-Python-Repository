# Accpet N NUmber from User and Store it into list.
# Return Addtion of All Elements.

def Addition(Arr):

    Ans =0    
    for i in Arr:
        Ans  = Ans+i
    return Ans    

def main():

    Data = []

    No = int(input("Enter NO of Element you want in List\n"))

    print("Enter Element :")
    for i in range(0,No):
        no = int(input())
        Data.append(no)

    Ret = Addition(Data)
    print("Addition of given Element is :",Ret)


if __name__ =="__main__":
    main()

# Accpet N NUmber from User and Store it into list.
#return Addition of All Prime Number.

import MarvellousNum

def Main():

    Data = []

    No = int(input("Enter NO of Element you want in List\n")) 
    print("Enter Element :")
    for i in range(0,No):
        no = int(input())
        Data.append(no)

    Ret = MarvellousNum.PrimeList(Data)
    Ret1 = MarvellousNum.PrimeAddition(Ret)
    print("Addition of Prime Elemnet is ",Ret1)

if __name__ =="__main__":
    Main()
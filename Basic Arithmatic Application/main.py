from ast import Continue
import Arithmetic

def main():
    No1 = int(input("Enter First Number\n"))
    No2 = int(input("Enter Second Number\n"))
    i=0

    print("1:Addition | 2:Substraction | 3:Multiplication | 4:Division | 5:Close the Application")

    while True:
        if i == 1:
            Ret1 = Arithmetic.Addition(No1,No2)
            print("Addition is :",Ret1)
            i=0
            Continue

        elif i == 2:
            Ret1 = Arithmetic.Substraction(No1,No2)
            print("Substraction is :",Ret1)
            i=0
            Continue

        elif i == 3:
            Ret1 = Arithmetic.Multiplication(No1,No2)
            print("Multiplication is :",Ret1)
            i=0
            Continue

        elif i == 4:
            Ret1 = Arithmetic.Division(No1,No2)
            print("Division is :",Ret1)
            i=0
            Continue
        
        elif i == 5:
            print("Thank You")
            exit()

        else:
            i = int(input("Which Operation you want to Perform\n"))
            Continue
           



    

if __name__ =="__main__":
    main()
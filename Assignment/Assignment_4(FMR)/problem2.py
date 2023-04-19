#use Lambda Function which Accept 2 parameter and returns its Multiplication.

Multiplication = lambda No1,No2 :No1*No2

def main():

    Value1 = int(input("Enter First Number\n"))
    Value2 = int(input("Enter Second Number\n"))


    Ret = Multiplication(Value1,Value2)
    print("Multiplication is :",Ret)

if __name__=="__main__":
    main()

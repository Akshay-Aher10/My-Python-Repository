#use Lambda Function which Accept one parameter and return power of 2.

PowerofTwo = lambda no : 2**no

def main():

    Value = int(input("Enter one Number\n"))

    Ret = PowerofTwo(Value)
    print("Answer is :",Ret)

if __name__=="__main__":
    main()
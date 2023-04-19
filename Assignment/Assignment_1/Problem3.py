# Write one Function which Accept 2 numbers and return addition of that 2 number.

def Addition(no1,no2):

    Ans = no1+no2

    return Ans

def main():

    No1 = int(input("Enter First Number\n"))
    No2 = int(input("Enter Second Number\n"))

    ret = Addition(No1,No2)

    print("Addition is :",ret)

if __name__ == "__main__":
    main()



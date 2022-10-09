# accpet number and return sum of digits.

def CountDigit(No):
    Sum = 0
    while No > 0:
        Digit = No%10
        Sum = Sum+Digit
        No = No//10

    return Sum

def main():
    no = int(input("Enter Number\n"))
    ret = CountDigit(no)
    print("Sum of Digits : ",ret)

if __name__ =="__main__":
    main()
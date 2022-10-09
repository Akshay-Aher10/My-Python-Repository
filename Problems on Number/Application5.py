# count Number  of digits in given number

def CountDigit(No):
    i = 0
    while No > 0:
        No%10
        No = No//10
        i += 1

    return i

def main():
    no = int(input("Enter Number\n"))
    ret = CountDigit(no)
    print("Number of Digits : ",ret)

if __name__ =="__main__":
    main()
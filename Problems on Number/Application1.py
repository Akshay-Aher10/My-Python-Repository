#input: 5 / output : 120 

def Factorial(No):
    x=1
    for i in range(1,No+1):
        x = x*i
    return x


def main():
    No = int(input("Enter Number\n"))

    ret = Factorial(No)
    print(ret)


if __name__ =="__main__":
    main()
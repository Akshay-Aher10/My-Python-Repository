#check whether number is divisible by 5 or not and return True/false

def CheckNumber(no):

    if no%5 ==0:
        return True
    else:
        return False    

def main():
    no = int(input("Enter Number\n"))

    ret = CheckNumber(no)

    print(ret)

if __name__ =="__main__":
    main()
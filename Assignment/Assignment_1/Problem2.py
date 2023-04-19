# Write one Function ChkNum() which accept one parameter as Number. if number is even then it should Display Even Number otherwise display "Odd Number" on console.

def ChkNum(no):
    if no%2 == 0 :
        return True
    else:
        return False    


def main():

    no = int(input("Enter Number\n"))

    ret = ChkNum(no)

    if ret == True:
        print("Number is Even Number")
    else:
        print("Number is Odd Number")   
    

if __name__ =="__main__":
    main()
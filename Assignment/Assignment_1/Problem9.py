def DisplayEven(no):
    j=0
    for i in range(0,no):
        j = j+2
        print(j,end=" ")


def main():
    
    no = int(input("Enter Number\n"))

    DisplayEven(no)

if __name__ =="__main__":
    main()
# input : 5
# Output :
#  *  *  *  *  *

#  *  *  *  *  *

#  *  *  *  *  *

#  *  *  *  *  *

#  *  *  *  *  *

def Display(no):

    for i in range(0,no):
        for j in range(0,no):
            print("*",end="  ")

        print("\n")    

def main():
    No1 = int(input("Enter Number\n"))
    Display(No1)

if __name__ == "__main__":
    main()
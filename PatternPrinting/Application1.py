# Display Blow Pattern.(Row = 5, Column = 5)

# *  *  *  *  *

# *  *  *  *  *

# *  *  *  *  *

# *  *  *  *  *

# *  *  *  *  *

def Display(Column,Row):

    print("Pattern :")
    for i in range(0,Row):
        for j in range(0,Column):
            print("*", end="  ")
        print("\n")        

def main():

    Column = int(input("Enter No of Column.\n"))
    Row = int(input("Enter No of Row.\n"))

    Display(Column,Row)

if __name__ =="__main__":
    main()
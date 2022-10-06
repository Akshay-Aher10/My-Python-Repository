# Display Blow Pattern.
# *

# *  *

# *  *  *

# *  *  *  *

# *  *  *  *  *

def Display(Column,Row):

    print("Pattern :")
    
    for i in range(1,Row+1):
        for j in range(1,i+1):
            
            print("*", end="  ")
        print("\n")        

def main():

    Column = int(input("Enter No of Column.\n"))
    Row = int(input("Enter No of Row.\n"))

    Display(Column,Row)



if __name__ =="__main__":
    main()
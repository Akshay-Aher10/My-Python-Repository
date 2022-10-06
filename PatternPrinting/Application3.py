# Display Blow Pattern.(Row = 5, Column = 5)

# 0  1  2  3  4

# 5  6  7  8  9

# 0  1  2  3  4

# 5  6  7  8  9

# 0  1  2  3  4

def Display(Column,Row):

    print("Pattern :")
    no =0

    for i in range(0,Row):

        for j in range(0,Column):
            print(no, end="  ")
            no+=1

        if no >9:
            no =0

        print("\n")        

def main():

    Column = int(input("Enter No of Column.\n"))
    Row = int(input("Enter No of Row.\n"))

    Display(Column,Row)

if __name__ =="__main__":
    main()
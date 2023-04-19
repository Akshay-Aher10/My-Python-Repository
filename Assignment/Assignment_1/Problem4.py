#write a Function which Display "Marvellous" 5 times on Console.

def Display(no):

    for i in range(0,no):
        print("Marvellous")

def main():

    no = int(input("Enter how many times you want to Display\n"))
    Display(no)

if __name__=="__main__":
    main()

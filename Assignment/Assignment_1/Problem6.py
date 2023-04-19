#Check number is positive or negetive

def CheckNumber(no):
    if no< 0:
        return True
    else:
        return False    


def main():
    
    no = int(input("Enter Number\n"))

    ret = CheckNumber(no)

    if ret ==True:
        print("Negetive Number")
    else:
        print("Positive Number")        

if __name__=="__main__":
    main()
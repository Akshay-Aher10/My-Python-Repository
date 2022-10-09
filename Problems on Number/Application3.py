# Check Number is Prime or Not

def ChkPrime(No):

    for i in range(1,No+1):
        if No % 2 == 0:
            break

    if i == No:
        return True
    else:
        return False        

def main():
    No = int(input("Ener Number\n"))
    ret = ChkPrime(No)

    if ret == True:
        print("Number is Prime Number")
    else:
        print("Number is not Prime Number")    

if __name__ =="__main__":
    main()
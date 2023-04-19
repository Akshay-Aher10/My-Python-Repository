# Check Number is Prime or Not

def ChkPrime(No):
    i =2
    while(i<=((No//2))):
        
        if No % i == 0:
            return False 
        i+=1
    return True

               
def main():
    No = int(input("Ener Number\n"))
    ret = ChkPrime(No)

    if ret == True:
        print("Number is Prime Number")
    else:
        print("Number is not Prime Number")    

if __name__ =="__main__":
    main()
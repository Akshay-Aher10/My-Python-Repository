def Recursion(No,Ans=1):    
    if(No==0):
        return Ans

    else:
        Ans = Ans*No   
        return Recursion(No-1,Ans)
                   
def main():
    Value = int(input("Enter your Number\n"))
    Ret = Recursion(Value)    
    print("Summation of Digit",Ret)

if __name__=="__main__":
    main()



def Recursion(No,Ans=0):    
    if(No==0):
        return Ans

    else:
        Ans = Ans+No%10    
        return Recursion(No//10,Ans)
                   
def main():
    Value = int(input("Enter your Number\n"))
    Ret = Recursion(Value)    
    print("Summation of Digit",Ret)

if __name__=="__main__":
    main()
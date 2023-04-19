def Recursion(No):

    if(No>0):
        print("*")
        No-=1
        Recursion(No)
    

def main():
    No = 5
    Recursion(5)

if __name__=="__main__":
    main()
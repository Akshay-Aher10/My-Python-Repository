def Recursion(No):

    if(No>=1):
        No-=1
        Recursion(No)
        print(No+1)

def main():
    No = 5
    Recursion(5)

if __name__=="__main__":
    main()
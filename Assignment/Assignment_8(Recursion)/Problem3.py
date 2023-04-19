def Recursion(No):

    if(No>=1):
        print(No)
        No-=1
        Recursion(No)

def main():
    No = 5
    Recursion(5)

if __name__=="__main__":
    main()
from sys import *

def Addition(No1,No2):
    Ans = No1+No2
    return Ans

def main():

    print("Welcome to : ", argv[0])

    if(len(argv) == 2):
        if(argv[1]=="--U" or argv[1]=="--u"):
            print("Use the Application as :")
            print("python Name_of_Application First_Number Second Number")
            exit()

        elif(argv[1]=="--H" or argv[1]=="--h"):
            print("This Application is used to perform Addition of 2 Numbers")
            exit()

    elif(len(argv) == 3):
        Ret = Addition(int(argv[1]),int(argv[2]))
        print("Addition is :",Ret)

    else:
        print("Invalid numbers of Argument")
        print("Use --U flag to get the Usage")
        exit()    

    print("Thank you For Using This Application")
    print("Akshay Aher")

if __name__ =="__main__":
    main()
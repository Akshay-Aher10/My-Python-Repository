import os

def CheckFile(FileName):

    fd = open(FileName,'r')
    Data = fd.read()

    return Data

def main():
    Name = input("Enter The File Name\n")

    Ret =  CheckFile(Name)

    print(Ret)

if __name__=="__main__":
    main()    
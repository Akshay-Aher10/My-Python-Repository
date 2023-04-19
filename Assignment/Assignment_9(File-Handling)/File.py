import os

def Read_file(FileName):

    if(os.path.exists(FileName)):
        
        fd = open(FileName,'r')
        Data = fd.read()
        print(Data)    

def main():
    Name = input("Enter The File Name\n")

    Read_file(Name)


if __name__=="__main__":
    main()    

import os

def CheckFile(FileName):

    if os.path.exists(FileName):
        return True
    else:
        return False
  
def main():
    Name = input("Enter The File Name\n")

    Ret =  CheckFile(Name)

    if(Ret == True):
        print("File is Exist in Current Path")
    else:
        print("File is not Exist in Current Path")    

if __name__=="__main__":
    main()    
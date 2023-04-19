from sys import argv
import os
import hashlib

def CopyContent(File_Name1,File_Name2):

    if(os.path.exists(File_Name1) and os.path.exists(File_Name2) ):

        fd1 = open(File_Name1,'r')
        data = fd1.read()
        encoded_Data = data.encode('utf-8')
        checksum_of_File1 = (hashlib.md5(encoded_Data)).hexdigest()
        
        fd2 = open(File_Name2,'r')
        data = fd2.read()
        encoded_Data = data.encode('utf-8')
        checksum_of_File2 = (hashlib.md5(encoded_Data)).hexdigest()

        if(checksum_of_File1 == checksum_of_File2):
            return True
        else:
            return False

    else:
        print("File Not Exists")
        
def main():

    if(argv[1]=='-h' or argv[1]=='-H'):
        print("This Application is used to Copy content from existing file and paste that content into newly created file")
        exit()
    elif(argv[1]=='-u' or argv[1]=='-U'):
        print("Usage : Application_Name First_Existing_File_Name Second_Existing_File_Name")
        exit()

    Ret = CopyContent(argv[1], argv[2])

    if(Ret == True):
        print("Success : Files cotain same data")
    else:
         print("Failure : Files cotain different data")   
if __name__ =="__main__":
    main()
from sys import argv
import os

def CopyContent(File_Name):

    if(os.path.exists(File_Name)):

        fd1 = open(File_Name,'r')
        Data = fd1.read()

        fd2 = open("Demo.txt",'w')
        fd2.write(Data)

        fd1.close()
        fd2.close()

    else:
        print("File Not Exists")
        
def main():

    if(len(argv) < 2 or len(argv)>2):
        print("Insufficient Arguments")
        exit()

    if(argv[1]=='-h' or argv[1]=='-H'):
        print("This Application is used to Copy content from existing file and paste that content into newly created file")
        exit()
    elif(argv[1]=='-u' or argv[1]=='-U'):
        print("Usage : Application_Name Existing_File_Name")
        exit()

    CopyContent(argv[1])



if __name__ =="__main__":
    main()
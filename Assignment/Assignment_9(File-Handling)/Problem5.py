from sys import argv
import os


def CopyContent(File_Name1,str):

    if(os.path.exists(File_Name1)):

        fd1 = open(File_Name1,'r')
        data = fd1.read()
        updated_Data = data.rstrip(" \n")
        words = updated_Data.split()
        print(words)
        counter =0
        for word in words:
            #print(word)
            #print(str)
            if word == str:
                print(counter)
                counter+=1

        return counter

    else:
        print("File Not Exists")
        
def main():

    if(argv[1]=='-h' or argv[1]=='-H'):
        print("This Application is used to Copy content from existing file and paste that content into newly created file")
        exit()
    elif(argv[1]=='-u' or argv[1]=='-U'):
        print("Usage : Application_Name Existing_File_Name String")
        exit()

    Ret = CopyContent(argv[1], argv[2])
    print("{string} word repeats {no} no of times in file".format(string =argv[2],no = Ret)) 
if __name__ =="__main__":
    main()
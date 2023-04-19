import os

def Delete_file(FileName):

    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if(size == 0):
            os.remove(FileName)
        else:
            print("Are you sure to delete the file Y/N")
            option = input()
            if(option =='Y' or option =='y'):
                os.remove(FileName)
            else:
                print("File deletion process stoped.")    

def main():
    Name = input("Enter The File Name\n")

    Delete_file(Name)


if __name__=="__main__":
    main()    
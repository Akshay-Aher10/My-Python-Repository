import os
import sys
import shutil

def Directory_Watcher(Dir_Name,Folder_Name,Path,File_Extention):

    FolderName = Folder_Name
    Folder_Path = Path
    NewFolder_Path = os.path.join(Folder_Path,FolderName)
    os.mkdir(NewFolder_Path)

    for Foldername, Subfolder, Filename in os.walk(Dir_Name):
                        
        for fname in Filename:
            if(fname.endswith(File_Extention)):
                File_path = os.path.join(Dir_Name,Foldername,fname)
                  
                shutil.copy(File_path,NewFolder_Path)
                
                

def main(): 
    print()

    if(sys.argv[1] == "-h"):
        print("This script will travel the First directory and Copy all files with given extention from first directory to newly created directory")
        exit()

    if(sys.argv[1] == "-u"):
        print("Usage : <Application_name> <Existing_Dir_Abs_Path> <New_Folder_Name> <Abs_Path_for_New_Folder> <Extention> ")
        exit()

    Directory_Watcher(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

    print("Successfully Coplied all files into {} Folder".format(sys.argv[2]))
    
if(__name__ == "__main__"):
    main()




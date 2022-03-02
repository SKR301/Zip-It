import shutil
import os

dir = "D:\\NewFolder\\"

def writeFolders():
    cmd = "dir "+dir+"/b>dir.txt"
    os.system(cmd)


if __name__=="__main__":
    # dir = input("Enter complete directory to folders:")
    # optimizeDir()
    writeFolders()

    dirFile = open("dir.txt","r")
    folders = dirFile.read()
    folderList = tuple(map(str, folders.split('\n')))

    for folderName in folderList:
        if(folderName == ''):
            continue
        shutil.make_archive(dir+folderName, "zip", dir+folderName)
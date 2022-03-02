import shutil
import os

dir = "D:\\NewFolder"

def writeFolders():
    cmd = "dir "+dir+"/b>dir.txt"
    os.system(cmd)

if __name__=="__main__":
    writeFolders()

    dirFile = open("dir.txt","r")
    folders = dirFile.read()
    folderList = tuple(map(str, folders.split('\n')))

    for folderName in folderList:
        shutil.make_archive(dir+"\\"+folderName, "zip", dir+"\\"+folderName)
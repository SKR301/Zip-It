import shutil
import os

def optimizeDir(dir):
    print(dir)

def writeDirInFile(dir):
    cmd = "dir "+dir+"/b>dir.txt"
    os.system(cmd)

def readToTuple():
    dirFile = open("dir.txt","r")
    folders = dirFile.read()
    return tuple(map(str, folders.split('\n')))

def zipIt(folderList):
    for folderName in folderList:
        if(folderName == ''):
            continue
        shutil.make_archive(dir+"\\"+folderName, "zip", dir+"\\"+folderName)

if __name__=="__main__":
    dir = str(input("Enter complete directory to folders:"))
    writeDirInFile("\""+dir+"\"")
    folderList = readToTuple()
    zipIt(folderList)
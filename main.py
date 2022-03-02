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

def zipItUnique(folderList):
    for folderName in folderList:
        if(folderName == ''):
            continue
        shutil.make_archive(dir+"\\"+folderName, "zip", dir+"\\"+folderName)

def zipItParent(dir):
    shutil.make_archive(dir, "zip", dir)

if __name__=="__main__":
    dir = str(input("Enter complete directory to folders:"))
    type = str(input("'Unique' or 'Parent':"))

    if type in ('Parent','PARENT','parent','p','P'):
        zipItParent(dir)
        print("Creating a Single Zip file for "+dir)

    if type in ('Unique','UNIQUE','unique','UNI','Uni','uni','u','U'):
        writeDirInFile("\""+dir+"\"")
        folderList = readToTuple()
        zipItUnique(folderList)
        print("Creating Unique Zip files for each folder inside "+dir)
import shutil
import os
import sys

def readArgv():
    return sys.argv[1],sys.argv[2]

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
    dir = ""
    type = ""

    try:
        dir,type = readArgv()
    except:
        print("!!!This program require 2 arguments. \n\tpython main.py [directory] [type] \n\n\t[directory]: complete location of the folder (in quotes).\n\t[type]: to zip each folder inside the directory(u,U,unique) or to zip the directory itself(p,P,parent)")
        exit()

    if type in ('Parent','PARENT','parent','p','P'):
        zipItParent(dir)
        print("Creating a Single Zip file for "+dir)

    elif type in ('Unique','UNIQUE','unique','UNI','Uni','uni','u','U'):
        writeDirInFile("\""+dir+"\"")
        folderList = readToTuple()
        zipItUnique(folderList)
        print("Creating Unique Zip files for each folder inside "+dir)

    else:
        print("!!!Invalid type argument. Enter either U or P")
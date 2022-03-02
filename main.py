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
    folder = tuple(map(str, folders.split('\n')))

    

    # shutil.make_archive("simonsZip", "zip", "files")
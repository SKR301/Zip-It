import shutil
import os

dir = "D:\\NewFolder"

def writeFolders():
    cmd = "dir "+dir+"/b>dir.txt"
    os.system(cmd)

if __name__=="__main__":
    writeFolders()
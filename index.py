import os
import sys
from tqdm import tqdm
import subprocess

flag=True

while(flag == True):
    f = input("Any files to upload? (y/n) ")
    f = f.lower()
    if f == "y" or f=="yes":
        filePath = input("Enter file path: ")
        #works
        if os.path.isfile(filePath):
            #works
            fileName = list(filePath.split("/"))[-1]
            subprocess.run("mkdir output" , shell=True)
            subprocess.run("cp {} output".format(filePath))
            
        else:
            print("[INFO] File does not exist\n")

    else:
        flag = False
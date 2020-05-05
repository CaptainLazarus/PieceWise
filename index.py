import os
import sys
from tqdm import tqdm
import subprocess
import argparse

def initArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" , "--input" , help="Input File")
    return vars(parser.parse_args())

def splitFile(fileName , size=90):
    subprocess.run(["split" , "-b" , "{}m".format(size) , fileName])
    subprocess.run(["git" , "add" , "x*"])

args = initArgs()
splitFile(args["input"])
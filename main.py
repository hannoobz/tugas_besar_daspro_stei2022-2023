# File: main.py
from command_runner import *
import argparse

Load = argparse.ArgumentParser()
Load.add_argument("folder_dir",nargs='?',type=str)
LoadFileArgs = Load.parse_args()
folder_dir = LoadFileArgs.folder_dir 

loadgame(folder_dir)

while True:
    masukan = input(">>> ")
    runner(masukan)
 

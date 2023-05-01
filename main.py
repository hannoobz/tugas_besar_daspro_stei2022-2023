# File: main.py

# Import modul command_runner
from command_runner import *

# Import modul argparse 
import argparse

# Menerima argument dari terminal
Load = argparse.ArgumentParser()
Load.add_argument("folder_dir",nargs='?',type=str)
LoadFileArgs = Load.parse_args()
folder_dir = LoadFileArgs.folder_dir 

# Menjalankan prosedur load 
# dengan argument yang diterima
loadgame(folder_dir)

# Loop CLI
while True:
    masukan = input(">>> ")
    runner(masukan)
 

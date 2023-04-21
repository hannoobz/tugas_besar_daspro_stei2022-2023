# File: main.py
from command_runner import *
import argparse
import os
Load = argparse.ArgumentParser()
Load.add_argument("folder_dir",nargs='?',type=str)
LoadFileArgs = Load.parse_args()

if LoadFileArgs.folder_dir == None:
    print("\nTidak ada nama folder yang diberikan!\n")
    print("Usage: python main.py <nama_folder>")
    exit()
elif not os.path.exists("save/"+str(LoadFileArgs.folder_dir)):
    print(f'\nFolder "{LoadFileArgs.folder_dir}" tidak ditemukan.')
    exit()
else:
    LoadArg("save/"+str(LoadFileArgs.folder_dir))
    print("Loading...")
    print("Selamat datang di program “Manajerial Candi”")
    print("Silahkan masukkan username Anda")
    runner("login")

while True:
    masukan = input(">>> ")
    runner(masukan)
 

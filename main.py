# File: main.py
from command_runner import *
#import argparse
#Load = argparse.ArgumentParser()
#Load.add_argument("folder_dir",nargs='?',type=str)
#LoadFileArgs = Load.parse_args()
#print(LoadFileArgs)


#if LoadFileArgs.folder_dir != None:
#    LoadArg(LoadFileArgs.folder_dir)
#    print("Loading...")
#    print("Selamat datang di program “Manajerial Candi”")
#    print("Silahkan masukkan username Anda")
#    runner("login")
#else:
#    print("\nTidak ada nama folder yang diberikan!\n")
#    print("Usage: python main.py <nama_folder>")
#    exit()

while True:
    masukan = input(">>> ")
    runner(masukan)
 

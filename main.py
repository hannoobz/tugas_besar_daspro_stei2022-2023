# File: main.py
from custom_module import *
from command_runner import *
# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat
#
users = loader("user.csv") # Matriks data user
candi = loader("candi.csv") # Matriks data candi
bahan_bangunan = loader("bahan_bangunan.csv") # Data bahan bangunan



while True:
    masukan = input(">>> ")
    runner(masukan)

print(users)
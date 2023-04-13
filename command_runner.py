from list_of_commands import *
users = loader("user.csv") # Matriks data user
candi = loader("candi.csv") # Matriks data candi
bahan_bangunan = loader("bahan_bangunan.csv") # Data bahan bangunan
role = ""
username = ""

def runner(string_command):
    global role
    global username
    if string_command == "login":
        role,username = login(users,role,username)
    if string_command =="logout":
        role = logout(role)

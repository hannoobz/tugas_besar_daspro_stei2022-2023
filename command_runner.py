from list_of_commands import *

users = loader("user.csv") # Matriks data user
candi = loader("candi.csv") # Matriks data candi
bahan_bangunan = loader("bahan_bangunan.csv") # Data bahan bangunan
role = ""
username = ""

#def LoadArg(arg):
#    global users
#    global candi
#    global bahan_bangunan
#    users = loader(arg+"/user.csv")
#    candi = loader(arg+"/candi.csv")
#    bahan_bangunan = loader(arg+"/bahan_bangunan.csv")

def runner(string_command):
    global users
    global role
    global username
    if string_command == "login":
        role,username = login(users,role,username)
    if string_command =="logout":
        role = logout(role)
    if string_command =="summonjin":
        users = summonjin(users,role)

from list_of_commands import *
role = ""
username = ""

# F13 - Load - HaniefFN
def LoadArg(arg):
    global users
    global candi
    global bahan_bangunan
    users = loader(arg+"/user.csv")
    candi = loader(arg+"/candi.csv")
    bahan_bangunan = loader(arg+"/bahan_bangunan.csv")

def runner(string_command):
    global users
    global role
    global username
    if string_command == "login":
        role,username = login(users,role,username)
    if string_command =="logout":
        role,username = logout(role)
    if string_command =="summonjin":
        users = summonjin(users,role)

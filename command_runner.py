from list_of_commands import *
role = ""
username = ""

# F13 - Load - HaniefFN
def loadgame(folder_dir):
    global users
    global candi
    global bahan_bangunan
    if folder_dir == None:
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()
    elif not os.path.exists("save/"+str(folder_dir)):
        print(f'\nFolder "{folder_dir}" tidak ditemukan.')
        exit()
    else:
        users = loader("save/"+str(folder_dir)+"/user.csv")
        candi = loader("save/"+str(folder_dir)+"/candi.csv")
        bahan_bangunan = loader("save/"+str(folder_dir)+"/bahan_bangunan.csv")
        if bahan_bangunan[1]==";EOP":
            bahan_bangunan = manual_append(bahan_bangunan,['pasir',"Jumlah Pasir",0])
            bahan_bangunan = manual_append(bahan_bangunan,['batu',"Jumlah Batu",0])
            bahan_bangunan = manual_append(bahan_bangunan,['air',"Jumlah Air",0])
        print("Loading...")
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda")
        runner("login")

def runner(string_command):
    global users
    global candi
    global bahan_bangunan
    global role
    global username
    if string_command == "login":
        role,username = login(users,role,username)
    if string_command =="logout":
        role,username = logout(role)
    if string_command =="summonjin":
        users = summonjin(users,role)
    if string_command =="laporanjin":
        laporanJin(users,bahan_bangunan,candi,role)
    if string_command =="laporancandi":
        laporanCandi(candi,role)
    if string_command =="hancurkancandi":
        hancurkanCandi(candi,role)
    if string_command =="ayamberkokok":
        ayamBerkokok(candi,role)
    if string_command =="save":
        save(users,candi,bahan_bangunan)
    if string_command =="exit":
        exitgame(users,candi,bahan_bangunan)
    if string_command =="help":
        helpgame(role)
    if string_command =="hapusjin":
        users,candi = hapusjin(users, candi, role)
    if string_command == "ubahjin":
        ubahjin(users,role)
    if string_command == "kumpul":
        bahan_bangunan[1][2],bahan_bangunan[2][2],bahan_bangunan[3][2] = kumpul(role, bahan_bangunan)
    if string_command == "bangun":
        candi, bahan_bangunan = bangun(username, bahan_bangunan, candi, role)
    if string_command == "batchkumpul":
        bahan_bangunan[1][2],bahan_bangunan[2][2],bahan_bangunan[3][2] = batchkumpul(role, users, bahan_bangunan)
    if string_command == "debug":
        print(users)
        print(candi)
        print(bahan_bangunan)

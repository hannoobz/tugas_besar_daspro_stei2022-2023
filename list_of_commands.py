from custom_module import *

#F01 - Login - HaniefFN
def login(users,role,username):
    iteration = 1
    if role != "":
        print("Login gagal!")
        print("Anda telah login dengan username",username+", silahkan lakukan “logout” sebelum melakukan login kembali.")
        return role,username
    username = str(input("Username: "))
    password = str(input("Password: "))
    while True:
        if users[iteration][0] == username:
            if users[iteration][1]==password:
                print("\nSelamat datang,",username+"!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                role = users[iteration][2]
            else:
                print("\nPassword Salah!")
            break
        if users[iteration]==';EOP':
            print("\nUsername tidak terdaftar!")
            break
        iteration += 1
    return role,username

#F02 - Logout - HaniefFN
def logout(role):
    if role !="":
        return ""
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")


#F03 - Summon Jin - Raihan A
def summonjin(users,role):
    if manual_len(users) > 103:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
        return users
    if role != "bandung_bondowoso":
        return users
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        while True:
            TipeJin = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
            if  TipeJin ==1:
                print("Memilih jin “Pengumpul”")
                Tipe = "jin_pengumpul"
                break
            elif TipeJin == 2:
                print("Memilih jin Pembangun")
                Tipe = "jin_pembangun"
                break
            else:
                print(f"Tidak ada jenis jin bernomor {TipeJin}!")
        while True: #Section menerima dan memeriksa Username jin baru
            UnameJin = input("Masukkan username jin: ");ada=False
            for iterate in range (manual_len(users)):
                if users[iterate][0] == UnameJin:
                    print('Username',UnameJin,'sudah diambil!');ada=True
            if ada==False:
                break
        while True: #Section menerima dan memeriksa Pass jin baru
            PassJin = input('Masukkan password jin: ')
            words=0
            for i in PassJin:
                words+=1
            if words < 5 or words > 25:
                print('Password panjangnya harus 5-25 karakter!')
            else:
                break
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"Jin {UnameJin} berhasil dipanggil!")
        return manual_append(users,[UnameJin,PassJin,Tipe])
    

        

            



    
    

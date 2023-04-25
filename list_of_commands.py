from custom_module import *
import os

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
                return role,username
            else:
                print("\nPassword Salah!")
                return "",""
        if users[iteration]==';EOP':
            print("\nUsername tidak terdaftar!")
            return "",""
        iteration += 1

#F02 - Logout - HaniefFN
def logout(role):
    if role !="":
        return "",""
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
 
# F09 - Laporan Jin - Filbert F
def laporanJin(users,bahan,candi, role):
    
    if role != "bandung_bondowoso":
        print ("Tidak bisa akses")
    
    else:
        # Mencari Total Jin, Jin Pengumpul, dan Jin Pembangun
        count_jin = manual_len(users) - 3

        # matriks yang berisi hanya data (judul tidak diproses)
        data_user = removeFirstRow(users)
        data_bahan = removeFirstRow(bahan)
        data_candi = removeFirstRow(candi)

        count_pengumpul = 0
        count_pembangun = 0
        for i in range(manual_len(data_user)):
            if data_user[i][2] == "jin_pengumpul":
                count_pengumpul += 1
            if data_user[i][2] == "jin_pembangun":
                count_pembangun += 1

        # Mencari Jin Termalas dan Terajin
        # Array ini berisi nama jin yang memiliki role "pembangun"
        arr_pembangun = [0 for i in range(count_pembangun + 1)]
        n = 0
        for i in range(manual_len(data_user)):
            if data_user[i][2] == 'jin_pembangun':
                arr_pembangun[n] = data_user[i][0]
                n += 1
        arr_pembangun[n] = ";EOP"

        # Array ini berisi kolom pada matriks data_candi yang mendata pembuat candi
        arr_candi_pembangun = getArrayCol(data_candi,1)

        # Array ini berhubungan dengan arr_pembangun dan menuliskan banyaknya elemen pada
        # arr_pembangun keluar pada arr_candi_pembangun
        arr_banyakcandi = [0 for i in range(manual_len(arr_pembangun) + 1)]
        for i in range(manual_len(arr_pembangun)):
            arr_banyakcandi[i] = howManyX(arr_candi_pembangun, arr_pembangun[i])
        arr_banyakcandi[manual_len(arr_pembangun)] = ";EOP"

        # Jika jumlah jin pembangun = 0
        if count_pembangun == 0:
            jin_malas = "-"
            jin_rajin = "-"

        # Jika jumlah jin pembangun > 0
        else:
            max = arr_banyakcandi[0]
            min = arr_banyakcandi[0]
            id_malas = 0
            id_rajin = 0

            for i in range(manual_len(arr_banyakcandi)):
                if arr_banyakcandi[i] > max: # Kondisi 1
                    id_rajin = i
                    max = arr_banyakcandi[i]
                elif arr_banyakcandi[i] == max: # Kondisi 2
                    if firstLetter(arr_pembangun[i]) < firstLetter(arr_pembangun[id_rajin]):
                        id_rajin = i
                        max = arr_banyakcandi[i]

                if arr_banyakcandi[i] < min: # Kondisi 1
                    id_malas = i
                    min = arr_banyakcandi[i]
                elif arr_banyakcandi[i] == min: # Kondisi 2
                    if firstLetter(arr_pembangun[i]) > firstLetter(arr_pembangun[id_malas]):
                        id_malas = i
                        min = arr_banyakcandi[i]

            jin_malas = arr_pembangun[id_malas]
            jin_rajin = arr_pembangun[id_rajin]

        # Mencari Jumlah Pasir, Batu, dan Air yang digunakan
        sum_pasir = 0
        sum_batu = 0
        sum_air = 0

        if not(data_bahan): # Jika data_bahan kosong
            pass
        else:
            for i in range(manual_len(data_bahan)):
                if data_bahan[i][0] == "Pasir":
                    sum_pasir += int(data_bahan[i][2])
                if data_bahan[i][0] == "Batu":
                    sum_batu += int(data_bahan[i][2])
                if data_bahan[i][0] == "Air":
                    sum_air += int(data_bahan[i][2])

        # Mengeprint Hasil
        print("="*11 + "\nLaporan Jin" + "\n" + "="*11)
        print(f"Total Jin: {count_jin}")
        print(f"Total Jin Pengumpul: {count_pengumpul}")
        print(f"Total Jin Pembangun: {count_pembangun}")
        print(f"Jin Terajin: {jin_rajin}")
        print(f"Jin Termalas: {jin_malas}")
        print(f"Jumlah Pasir: {sum_pasir} unit")
        print(f"Jumlah Batu: {sum_batu} unit")
        print(f"Jumlah Air: {sum_air} unit")
 

# F10 - Laporan Candi - Filbert F
def laporanCandi(candi, role):
    
    if role != "bandung_bondowoso":
        print("Tidak bisa akses")
        
    else:
        # Membaca data
        count = manual_len(candi) - 1

        if count == 0: # array kosong
            print(f"Total Candi: 0")
            print(f"Total Pasir yang digunakan: 0")
            print(f"Total Batu yang digunakan: 0")
            print(f"Total Air yang digunakan: 0")
            print(f"ID Candi Termahal: -")
            print(f"ID Candi Termurah: -")

        else:#candi tidak kosong
            # Menghapus row judul
            data_candi = removeFirstRow(candi)  


            # Mencari Total Pasir, Batu, dan Air Digunakan
            sum_pasir = sumArray(getArrayCol(data_candi,2))
            sum_batu = sumArray(getArrayCol(data_candi,3))
            sum_air = sumArray(getArrayCol(data_candi,4))

            # Mencari Candi Termahal dan Termurah
            arr_bahan = [0 for i in range(manual_len(data_candi) + 1)]
            for i in range(manual_len(data_candi)):
                arr_bahan[i] = getArrayRow(data_candi, i, 2, 5)
            arr_bahan[manual_len(data_candi)] = ";EOP"

            arr_sumBahan = [0 for i in range(manual_len(arr_bahan) + 1)]
            for i in range(manual_len(arr_bahan)):
                arr_sumBahan[i] = sumArray(arr_bahan[i])
            arr_sumBahan[manual_len(arr_bahan)] = ";EOP"

            idmax = maxArrayID(arr_sumBahan)
            idmin = minArrayID(arr_sumBahan)

            price_max = (int(arr_bahan[idmax][0]) * 10000) + (int(arr_bahan[idmax][1]) * 15000) + (int(arr_bahan[idmax][2]) *7500)
            price_min = (int(arr_bahan[idmin][0]) * 10000) + (int(arr_bahan[idmin][1]) * 15000) + (int(arr_bahan[idmin][2]) *7500)

            # Mengeprint Hasil
            print("="*13 + "\nLaporan Candi" + "\n" + "="*13)
            print(f"Total Candi: {count}")
            print(f"Total Pasir yang digunakan: {sum_pasir}")
            print(f"Total Batu yang digunakan: {sum_batu}")
            print(f"Total Air yang digunakan: {sum_air}")
            print(f"ID Candi Termahal: {idmax + 1} (Rp {price_max})")
            print(f"ID Candi Termurah: {idmin + 1} (Rp {price_min})")
    
# F11 - Hancurkan Candi - Filbert F
def hancurkanCandi(candi, role):
    if role != "roro_jonggrang":
        print("Tidak bisa akses")
    else:
        arr_idcandi = getArrayCol(candi, 0)
        count = manual_len(candi) - 1
        if count == 0:
            print("Belum ada candi yang terbangun")
            return candi
        else:
            N = input("Masukan ID Candi: ")
            idx = findIdx(arr_idcandi, N)
            while not(idx):
                print("Tidak ada candi dengan ID tersebut.")
                N = input("Masukan ID Candi: ")
                idx = findIdx(arr_idcandi, N)

            con = input(f"Apakah anda yakin ingin menghancurkan candi ID: {N} (Y/N)?")
            if con == "Y":
                candi = removeElmt(candi,idx)
                print("Candi telah berhasil dihancurkan.")
                return candi
            else:  
                print("Candi gagal dihancurkan")
                return candi
            
# F12 - Ayam Berkokok - Filbert F
def ayamBerkokok(candi, role):
    if role != "roro_jonggrang":
        print("Tidak bisa akses.")
    
    else:
        count_candi = manual_len(candi) - 1
        print("Kukuruyuk.. Kukuruyuk..")
        print(f"Jumlah Candi: {count_candi}")

        if count_candi<100:
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
            exit()
            
        else:
            print("Yah, Bandung Bondowoso memenangkan permainan!")
            exit()
            
# F14 - Save - HaniefFN
def save(users,candi,bahan_bangunan):
    folder_name = str(input("Masukkan nama folder: "))
    print("\n")
    print("Saving...\n")
    if not os.path.exists("save/"+str(folder_name)):
        print("Membuat folder",folder_name,"\n")
    print("Berhasil menyimpan data di folder",folder_name)
    os.makedirs(os.getcwd()+"/"+"save/"+folder_name,exist_ok=True)
    arrtocsv(users,"save/"+str(folder_name)+"/user.csv",3)
    arrtocsv(candi,"save/"+str(folder_name)+"/candi.csv",5)
    arrtocsv(bahan_bangunan,"save/"+str(folder_name)+"/bahan_bangunan.csv",3)
    
# F15 - Help - HaniefFN
def helpgame(role):
    print("=========== HELP ===========")
    if role=="":
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if role=="bandung_bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchbangun")
        print("   Untuk mengerahkan seluruh jin untuk membangun candi")
        print("6. batchkumpul")
        print("   Untuk mengerahkan seluruh jin untuk mengumpulkan resource candi")
        print("7. laporanjin")
        print("   Untuk mengambil laporan kinerja para jin")
        print("8. laporancandi")
        print("   Untuk mengambil laporan pembangunan candi")
        print("9. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if role=="jin_pembangun":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if role=="jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if role=="roro_jonggrang":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk memalsukan pagi hari dan menyelesaikan permainan")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")


# F16 - Exit - HaniefFN
def exitgame(users,candi,bahan_bangunan):
    pilihan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
    if pilihan=="Y" or pilihan=="y":
        save(users,candi,bahan_bangunan)
        exit()
    if pilihan=="N" or pilihan=="n":
        exit()  

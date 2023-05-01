from custom_module import *
import random
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
        return "",""

#F03 - Summon Jin - Raihan A
def summonjin(users,role):
    if manual_len(users) > 102:
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

#F04 - Hapus Jin - M Raihan A
def hapusjin(users, candi, role):
    if role == 'bandung_bondowoso':
        UnameJin = input("Masukkan username jin : ");ada=False
        if UnameJin != 'Bondowoso' and UnameJin != 'Roro':
           for i in range(manual_len(users)):
            if UnameJin == users[i][0]:
                ada = True; indexJin = i
            if ada == True:
                Pilihan=input(f'Apakah anda yakin ingin menghapus jin dengan username {UnameJin} (Y/N)? ')
                if Pilihan == 'N':
                    return users,candi 
                elif Pilihan == 'Y': 
                    for k in range(manual_len(candi)):   #Modifikasi file candi.csv
                        temp_candi = [["id","pembuat","pasir","batu","air",''],"EOP"]
                        if candi[k][1] != UnameJin:
                            manual_append(temp_candi, [candi[k][0], candi[k][1], candi[k][2], candi[k][3], candi[k][4]])
                    candi = temp_candi
                    return removeElmt(users,indexJin),candi
            else:
                pass
        else:
            print('Tidak dapat menghapus user dengan role selain jin_pembangun atau jin_pengumpul')
            return users,candi 
        if ada==False:
            print('Tidak ada jin dengan username tersebut')
            return users,candi
    else:
        print('Role anda bukanlah bandung_bondowoso')
        return users,candi
       
    
#F05 - Ubah tipe Jin - M Raihan A
def ubahjin(users,role):
    if role == 'bandung_bondowoso':
        jinGanti = input('Masukkan username jin : ')
        for i in range(3, manual_len(users)):
            if users[i][0] == jinGanti:
                ada=1
                if users[i][2] == 'jin_pengumpul':
                    ganti = input("Jin ini bertipe "'Pengumpul'". Yakin ingin mengubah ke tipe "'Pembangun'" (Y/N)? ")
                    if ganti == 'Y':
                        users[i][2] = 'jin_pembangun'
                        print('Jin telah berhasil diubah')
                        return users
                    elif ganti == 'N':
                        break
                elif users [i][2] =='jin_pembangun':
                    ganti = input("Jin ini bertipe "'Pembangun'". Yakin ingin mengubah ke tipe "'Pengumpul'" (Y/N)? ")
                    if ganti == 'Y':
                        users[i][2] = 'jin_pengumpul'
                        print('Jin telah berhasil diubah')
                        return users
                    elif ganti == 'N':
                        break
        if ada==0:
            print('Tidak ada jin dengan username tersebut')
            return users
    else:
        print('user anda bukanlah bandung bondowoso')
        
        
#F06 - Bangun Candi - M Raihan A
def bangun(username, bahan_bangunan, candi, role): #Muhammad Raihan Ariffiato
    PasirButuh = random.randint(1, 5)
    BatuButuh = random.randint(1, 5)
    AirButuh = random.randint(1, 5)
    pasir =  int(bahan_bangunan[1][2])
    batu =  int(bahan_bangunan[2][2])
    air =  int(bahan_bangunan[3][2])
    id_candi = 0

    for i in range(1,manual_len(candi)):
        if id_candi<=int(candi[i][0]):
            id_candi = int(candi[i][0])+1

    if role == 'jin_pembangun':
        if pasir >= PasirButuh and batu >= BatuButuh and air >= AirButuh: #Memeriksa bahan bangunan dan menentukan pembangunan candi
            new_candi = [id_candi, username, PasirButuh, BatuButuh, AirButuh]
            candi = manual_append(candi, new_candi)
            bahan_bangunan[1][2] = pasir - PasirButuh
            bahan_bangunan[2][2] = batu - BatuButuh
            bahan_bangunan[3][2] = air - AirButuh
            
            print('Candi berhasil dibangun')

            if (manual_len(candi)-1) < 100:   #Menampilkan jumlah candi yang masih perlu dibangun
                print(f'Sisa candi yang perlu dibangun: {101-(manual_len(candi))}.')
            else:
                print("Sisa candi yang perlu dibangun : 0.")
        else:
            print('Bahan bangunan tidak mencukupi')
            print('Candi tidak bisa dibangun!')
    else:
        print('Role anda bukanlah pembangun, log in dengan akun pembangun!')

    return candi, bahan_bangunan
        
#F07 - Kumpul bahan bangunan - M Raihan A
def kumpul(role, bahan_bangunan):
    pasirKumpul = random.randint(0, 5) 
    batuKumpul = random.randint(0, 5)
    airKumpul = random.randint(0, 5)
    pasir =  int(bahan_bangunan[1][2])
    batu =  int(bahan_bangunan[2][2])
    air =  int(bahan_bangunan[3][2])
    if role == 'jin_pengumpul':
        pasir += pasirKumpul; batu += batuKumpul; air += airKumpul
        print(f'Jin menemukan {pasirKumpul} pasir, {batuKumpul} batu, {airKumpul} air.')
        return pasir,batu,air
    else:
        print('Fungsi ini hanya bisa dilakukan oleh jin pengumpul')
        return pasir,batu,air
    
# FO8 - Batch kumpul/bangun - Filbert F
def batchkumpul(role, users, bahan_bangunan):
    pasir =  int(bahan_bangunan[1][2])
    batu =  int(bahan_bangunan[2][2])
    air =  int(bahan_bangunan[3][2])
    if role != "bandung_bondowoso":
        print(f"Tidak bisa akses dengan role {role}")
        return pasir,batu,air
    else:
        arr_role = getArrayCol(users, 2)
        count_pengumpul = 0
        count_pengumpul = howManyX(arr_role, "jin_pengumpul", count_pengumpul)

        if count_pengumpul == 0 :
            print("Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
            return pasir,batu,air
        else:
            sumpasirKumpul = 0
            sumbatuKumpul = 0
            sumairKumpul = 0
            for i in range(count_pengumpul):
                sumpasirKumpul += random.randint(0, 5) 
                sumbatuKumpul += random.randint(0, 5)
                sumairKumpul += random.randint(0, 5)

            print(f"Mengerahkan {count_pengumpul} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan total {sumpasirKumpul} pasir, {sumbatuKumpul} batu, {sumairKumpul} air.")
            pasir += sumpasirKumpul; batu += sumbatuKumpul; air += sumairKumpul
            return pasir,batu,air

def batchbangun(users, bahan_bangunan, candi, role):
    pasir =  int(bahan_bangunan[1][2])
    batu =  int(bahan_bangunan[2][2])
    air =  int(bahan_bangunan[3][2])
    if role != "bandung_bondowoso":
        print(f"Tidak bisa akses dengan role {role}")
        return candi, bahan_bangunan
    else:
        arr_role = getArrayCol(users, 2)
        count_pembangun = 0
        count_pembangun = howManyX(arr_role, "jin_pembangun", count_pembangun)
        arrusernamepembangun = [0 for i in range(count_pembangun)]
        n = 0
        for i in range(manual_len(users)):
            if users[i][2] == "jin_pembangun":
                arrusernamepembangun[n] = users[i][0]
                n += 1

        if count_pembangun == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
            return candi, bahan_bangunan
        else:
            SumPasirButuh = 0
            SumBatuButuh = 0
            SumAirButuh = 0
            newCandi = [0 for i in range(count_pembangun+1)]
            newCandi[count_pembangun] = ";EOP"
            
            id_candi = 0
            for i in range(1,manual_len(candi)):
                if id_candi<=int(candi[i][0]):
                    id_candi = int(candi[i][0])+1

            for i in range(count_pembangun):
                PasirButuh = random.randint(1, 5)
                BatuButuh = random.randint(1, 5)
                AirButuh = random.randint(1, 5)

                SumPasirButuh += PasirButuh
                SumBatuButuh += BatuButuh
                SumAirButuh += AirButuh

                newCandi[i] = [id_candi+i, arrusernamepembangun[i], PasirButuh, BatuButuh, AirButuh]

            print(f"Mengerahkan {count_pembangun} jin untuk membangun candi dengan total {SumPasirButuh} pasir, {SumBatuButuh} batu, dan {SumAirButuh} air.")
            count_newcandi = manual_len(newCandi)
            if (manual_len(candi) + count_newcandi)  > 100:
                print("Bangun gagal, jumlah candi melebihi 100")
                return candi, bahan_bangunan
            else:
                if pasir < SumPasirButuh:
                    if batu < SumBatuButuh:
                        if air < SumAirButuh:
                            print(f"Bangun gagal. Kurang {SumPasirButuh-pasir} pasir, {SumBatuButuh-batu} batu, dan {SumAirButuh-air} air.")
                            return candi, bahan_bangunan
                        else:
                            print(f"Bangun gagal. Kurang {SumPasirButuh-pasir} pasir dan {SumBatuButuh-batu} batu.")
                            return candi, bahan_bangunan
                    else:
                        if air < SumAirButuh:
                            print(f"Bangun gagal. Kurang {SumPasirButuh-pasir} pasir dan {SumAirButuh-air} air.")
                            return candi, bahan_bangunan
                        else:
                            print(f"Bangun gagal. Kurang {SumPasirButuh-pasir} pasir.")
                            return candi, bahan_bangunan
                elif batu < SumBatuButuh:
                    if air < SumAirButuh:
                        print(f"Bangun gagal. Kurang {SumBatuButuh-batu} batu, dan {SumAirButuh-air} air.")
                        return candi, bahan_bangunan
                    else:
                        print(f"Bangun gagal. Kurang {SumBatuButuh-batu} batu.")
                        return candi, bahan_bangunan
                elif air < SumAirButuh:
                    print(f"Bangun gagal. Kurang {SumAirButuh-air} air.")
                    return candi, bahan_bangunan
                else:
                    print(f"Jin berhasil membangun total {count_newcandi} candi.")
                    for i in range(count_newcandi):
                        candi = manual_append(candi, newCandi[i])
                    bahan_bangunan[1][2] = pasir - SumPasirButuh
                    bahan_bangunan[2][2] = batu - SumBatuButuh
                    bahan_bangunan[3][2] = air - SumAirButuh
                    return candi, bahan_bangunan


# F09 - Laporan Jin - Filbert F
def laporanJin(users,bahan,candi, role):
    
    if role != "bandung_bondowoso":
        print ("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    
    else:
        # Mencari Total Jin, Jin Pengumpul, dan Jin Pembangun
        count_jin = manual_len(users) - 3

        # matriks yang berisi hanya data (judul tidak diproses)
        data_user = removeFirstRow(users)
        data_candi = removeFirstRow(candi)

        count_pengumpul = 0
        count_pembangun = 0
        for i in range(manual_len(data_user)):
            if data_user[i][2] == "jin_pengumpul":
                count_pengumpul += 1
            if data_user[i][2] == "jin_pembangun":
                count_pembangun += 1

        count_candi = manual_len(data_candi)
        username = [";EOP"]
        count = [";EOP"]
        for i in range(count_candi):
            if (howManyX(username, data_candi[i][1], 0) == 0):
                username = manual_append(username, data_candi[i][1])
                count = manual_append(count, 1)
                print("s")
            else:
                count[findIdx(username, data_candi[i][1])] += 1
        
        if count_pembangun <= 1 or count_candi == 0:
            jin_malas = "-"
            jin_rajin = "-"

        else:
            max = count[0]
            min = count[0]
            id_malas = 0
            id_rajin = 0

            for i in range(manual_len(count)):
                if count[i] > max: # Kondisi 1
                    id_rajin = i
                    max = count[i]
                elif count[i] == max: # Kondisi 2
                    if firstLetter(username[i]) < firstLetter(username[id_rajin]):
                        id_rajin = i
                        max = count[i]

                if count[i] < min: # Kondisi 1
                    id_malas = i
                    min = count[i]
                elif count[i] == min: # Kondisi 2
                    if firstLetter(username[i]) > firstLetter(username[id_malas]):
                        id_malas = i
                        min = count[i]

        # Mengeprint Hasil
        print("="*11 + "\nLaporan Jin" + "\n" + "="*11)
        print(f"Total Jin: {count_jin}")
        print(f"Total Jin Pengumpul: {count_pengumpul}")
        print(f"Total Jin Pembangun: {count_pembangun}")
        print(f"Jin Terajin: {username[id_rajin]}")
        print(f"Jin Termalas: {username[id_malas]}")
        print(f"Jumlah Pasir: {bahan[1][2]} unit")
        print(f"Jumlah Batu: {bahan[2][2]} unit")
        print(f"Jumlah Air: {bahan[3][2]} unit")
 

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
            arridcandi =  getArrayCol(data_candi,0)
            
            arr_bahan = [0 for i in range(manual_len(data_candi) + 1)]
            for i in range(manual_len(data_candi)):
                arr_bahan[i] = getArrayRow(data_candi, i, 2, 5)
            arr_bahan[manual_len(data_candi)] = ";EOP"

            arrprice = [0 for i in range(manual_len(arr_bahan) + 1)]
            for i in range(manual_len(arr_bahan)):
                arrprice[i] = (int(arr_bahan[i][0]) * 10000) + (int(arr_bahan[i][1]) * 15000) + (int(arr_bahan[i][2]) *7500)
            arrprice[manual_len(arr_bahan)] = ";EOP"
            
            idmax = find_max_id(arrprice, 0, 1)
            
            idmin = find_min_id(arrprice, 0, 1)

            price_max = arrprice[idmax]
            price_min = arrprice[idmin]

            # Mengeprint Hasil
            print("="*13 + "\nLaporan Candi" + "\n" + "="*13)
            print(f"Total Candi: {count}")
            print(f"Total Pasir yang digunakan: {sum_pasir}")
            print(f"Total Batu yang digunakan: {sum_batu}")
            print(f"Total Air yang digunakan: {sum_air}")
            print(f"ID Candi Termahal: {arridcandi[idmax]} (Rp {price_max})")
            print(f"ID Candi Termurah: {arridcandi[idmin]} (Rp {price_min})")
    
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
            N = int(input("Masukan ID Candi: "))
            idx = findIdx(arr_idcandi, N)
            while not(idx):
                print("Tidak ada candi dengan ID tersebut.")
                N = int(input("Masukan ID Candi: "))
                idx = findIdx(arr_idcandi, N)
            con = input(f"Apakah anda yakin ingin menghancurkan candi ID: {N} (Y/N)?")
            if con == "Y":
                print("Candi telah berhasil dihancurkan.")
                return removeElmt(candi,idx)
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
        print("3. save")
        print("   Untuk menyimpan data permainan")
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
        print("9. save")
        print("   Untuk menyimpan data permainan")
        print("10. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if role=="jin_pembangun":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")
        print("3. save")
        print("   Untuk menyimpan data permainan")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if role=="jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")
        print("3. save")
        print("   Untuk menyimpan data permainan")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if role=="roro_jonggrang":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk memalsukan pagi hari dan menyelesaikan permainan")
        print("4. save")
        print("   Untuk menyimpan data permainan")
        print("5. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")


# F16 - Exit - HaniefFN
def exitgame(users,candi,bahan_bangunan):
    pilihan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
    if pilihan=="Y" or pilihan=="y":
        save(users,candi,bahan_bangunan)
        exit()
    if pilihan=="N" or pilihan=="n":
        exit()  

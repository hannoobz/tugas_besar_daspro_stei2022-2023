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
 

# F09 - Laporan Jin - Filbert F
def laporanJin():
    # Membaca Data
    arr_candi = loader("candi.csv")
    arr_bahan = loader("bahan_bangunan.csv")
    arr_user = loader("user.csv")

    data_candi = getData(arr_candi)
    data_bahan = getData(arr_bahan)
    data_user = getData(arr_user)

    # Mencari Total Jin, Jin Pengumpul, dan Jin Pembangun
    count_jin = manual_len(data_user) - 2

    count_pengumpul = 0
    count_pembangun = 0
    for i in range(manual_len(data_user)):
        if data_user[i][2] == "pengumpul":
            count_pengumpul += 1
        if data_user[i][2] == "pembangun":
            count_pembangun += 1

    # Mencari Jin Termalas dan Terajin
    # Array ini berisi nama jin yang memiliki role "pembangun"
    arr_pembangun = [0 for i in range(count_pembangun + 1)]
    n = 0
    for i in range(manual_len(data_user)):
        if data_user[i][2] == 'pembangun':
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
    print(f"Total Jin: {count_jin}")
    print(f"Total Jin Pengumpul: {count_pengumpul}")
    print(f"Total Jin Pembangun: {count_pembangun}")
    print(f"Jin Terajin: {jin_rajin}")
    print(f"Jin Termalas: {jin_malas}")
    print(f"Jumlah Pasir: {sum_pasir} unit")
    print(f"Jumlah Batu: {sum_batu} unit")
    print(f"Jumlah Air: {sum_air} unit")
 

# F10 - Laporan Candi - Filbert F
def laporanCandi():
    # Membaca data
    arr_candi = loader("candi.csv")
    data_candi = getData(arr_candi) # Bernilai False jika arr_candi kosong

    if not(data_candi): #array kosong
        print(f"Total Candi: 0")
        print(f"Total Pasir yang digunakan: 0")
        print(f"Total Batu yang digunakan: 0")
        print(f"Total Air yang digunakan: 0")
        print(f"ID Candi Termahal: -")
        print(f"ID Candi Termurah: -")
    
    else: #arr_candi tidak kosong
        # Mencari Total Candi
        count = manual_len(data_candi)

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
        print(f"Total Candi: {count}")
        print(f"Total Pasir yang digunakan: {sum_pasir}")
        print(f"Total Batu yang digunakan: {sum_batu}")
        print(f"Total Air yang digunakan: {sum_air}")
        print(f"ID Candi Termahal: {idmax + 1} (Rp {price_max})")
        print(f"ID Candi Termurah: {idmin + 1} (Rp {price_min})")
    

 

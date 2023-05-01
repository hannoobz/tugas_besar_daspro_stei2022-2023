# custom_module.py

# Fungsi manual_split 
# untuk splitting string
# Cara pakai :
# array = manual_split(array,"karakter split")
# tidak bisa langsung :
# manual_split(array,"karakter")
# harus di assign ke variabel array terlebih dahulu
def manual_split(csv_str,char):
    elmt = 0
    for i in range(len(csv_str)):
        if csv_str[i]==char:
            elmt += 1
    dat = ["" for i in range(elmt+1)]
    col = 0
    for i in range(len(csv_str)):
        if csv_str[i] != char:
            dat[col] += csv_str[i]
        else:
            col +=1
    return dat

# Fungsi manual_len 
# mencari length array dengan syarat
# di akhir array terdapat mark "EOP" atau ";EOP"
def manual_len(arr):
    for i in range(1000):
        if arr[i]==";EOP" or arr[i]=="EOP":
            return i

# Fungsi loader
# memuat file menjadi dalam bentuk array
# Contoh format hasil return
# [['username', 'password', 'role'], ['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang'], ';EOP']
# [['id', 'pembuat', 'pasir', 'batu', 'air'], ';EOP']
# [['nama', 'deskripsi', 'jumlah'], ';EOP']
def loader(directory):
    file = open(directory,"r")
    array = file.read()+";EOP"
    array = manual_split(array,"\n")
    for i in range(manual_len(array)):
        array[i] = manual_split(array[i],";")
    file.close()
    return array

# Fungsi manual_append
# pengganti append
# Cara pakai :
# array = manual_append(array,elemenbaru)
def manual_append(array,element):
    length = manual_len(array)
    new_array = ["" for i in range(length+2)]
    for i in range(length):
        new_array[i] = array[i]
    new_array[length] = element
    new_array[length+1] = ";EOP"
    return new_array

# Fungsi removeFirstRow
# untuk menghapus first elemen dari array
# Cara pakai :
# array = removeFirstRow(arr)
# harus di assign ke variabel array terlebih dahulu
def removeFirstRow(arr):
    length = manual_len(arr)
    arr_data = [0 for i in range(manual_len(arr))]
    for i in range(manual_len(arr)):
        arr_data[i] = arr[i+1]
    return arr_data
    
# Fungsi getArrayCol
# untuk membuat array 1 kolom dari matriks
# Cara pakai :
# array = getArrayCol(m,col)
# m = matriks
# col = kolom yang ingin dipilih
# harus di assign ke variabel array terlebih dahulu
def getArrayCol(m, col):
    arrCol = [0 for i in range(manual_len(m)+1)]
    for i in range(manual_len(m)):
        arrCol[i] = m[i][col]
    arrCol[manual_len(m)] = ';EOP'
    return(arrCol)

# Fungsi getArrayRow
# untuk membuat array row dengan batas kolom
# Cara pakai :
# array = getArrayRow(arr,row,col1,col2)
# row = row yang dipilih
# col1,col2 = batasan
# harus di assign ke variabel array terlebih dahulu
def getArrayRow(arr, row, col1, col2):
    arrRow = [0 for i in range(col2-col1+1)]
    for i in range(col1,col2):
            arrRow[i-col1] = arr[row][i]
    arrRow[col2-col1] = ";EOP"
    return(arrRow)

# Fungsi sumArray
# untuk menghitung jumlah integer dalam array integer
# Cara pakai :
# sum = sumArray(arr)
# Fungsi ini bersifat rekursif
def sumArray(arr):
    if manual_len(arr) == 0:
        return 0
    else:
        return int(arr[0]) + sumArray(removeFirstRow(arr))

# Fungsi find_max_id
# untuk mencari id tertinggi dari array of integer
# Cara pakai :
# maxid = find_max_id(arr,0,1)
# max_id = 0 karena id yang pertama di tes adalah id 0
# idx = 1 karena id yg ingin dibandingkan pertama adalah id 1
# Fungsi ini rekursif
def find_max_id(arr, max_id, idx):
    if idx == manual_len(arr):
        return max_id
    else:
        if arr[idx] > arr[max_id]:
            max_id = idx
        return find_max_id(arr, max_id, idx + 1)

# Fungsi find_max_id
# untuk mencari id terendah dari array of integer
# Cara pakai :
# minid = find_min_id(arr,0,1)
# min_id = 0 karena id yang pertama di tes adalah id 0
# idx = 1 karena id yg ingin dibandingkan pertama adalah id 1
# Fungsi ini rekursif
def find_min_id(arr, min_id, idx):
    if idx == manual_len(arr):
        return min_id
    else:
        if arr[idx] < arr[min_id]:
            min_id = idx
        return find_min_id(arr, min_id, idx + 1)

# Fungsi firstLetter
# untuk mengeluarkan huruf pertama
# Cara pakai :
# firstletter = firstletter(char)
def firstLetter(char):
    return char[0]

# Fungsi howManyX
# untuk menghitung jumlah X muncul dalam array
# Cara pakai :
# count = howManyX(arr,x,0)
# parameter count = 0 karena awalnya dihitung dimulai dari 0
# Fungsi ini bersifat rekursif
def howManyX(arr, x, count):
    if manual_len(arr) == 0:
        return count
    elif arr[0] == x:
        count += 1
    return howManyX(removeFirstRow(arr), x, count)

# Fungsi findIdx
# untuk mencari index dimana x ditemukan pada array
# Cara pakai :
# idx = findIdx(arr,x)
# Akan mereturn boolean False jika x tidak ditemukan
def findIdx(arr,x):
    for i in range(manual_len(arr)):
        if arr[i] == x:
            return i
    return False

# Fungsi removeElmt
# untuk menghilangkan Elmt pada id tertentu
# Cara pakai :
# arr = removeElmt(arr,id)
# harus di assign ke variabel
def removeElmt(arr,id):
    new_arr = [0 for i in range(manual_len(arr))]
    c = 0
    for i in range(manual_len(arr)):
        if i != id:
            new_arr[c] = arr[i]
            c += 1
    new_arr[c] = ";EOP"
    return new_arr

# Fungsi arrtocsv
# memasukkan array ke file csv
# Cara pakai :
# arrtocsv(arr,filename,col)
# Tidak perlu di assign ke variabel
def arrtocsv(arr,filename,col):
    csv_file = open(filename,"w")
    for i in range(manual_len(arr)):
        for j in range(col):
            csv_file.write(str(arr[i][j]))
            csv_file.write(";")
        csv_file.write("\n")
    csv_file.close()

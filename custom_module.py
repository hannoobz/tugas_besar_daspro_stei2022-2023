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

# Mengambil sebuah matriks dan hanya mengeluarkan row yang berisi data
# (Menghapus row judul)
def removeFirstRow(arr):
    length = manual_len(arr)
    arr_data = [0 for i in range(manual_len(arr))]
    for i in range(manual_len(arr)):
        arr_data[i] = arr[i+1]
    return arr_data
    
# Mengambil sebuah matriks dan integer kolom dan membuat array berisi
# data pada kolom tersebut 
def getArrayCol(m, col):
    arrCol = [0 for i in range(manual_len(m)+1)]
    for i in range(manual_len(m)):
        arrCol[i] = m[i][col]
    arrCol[manual_len(m)] = ';EOP'
    return(arrCol)

# Mengambil sebuah matriks, integer baris, dan range kolom, lalu 
# membuat array berisi data pada baris tersebut dengan ketentuan pada
# range kolom yang dimasukan
def getArrayRow(arr, row, col1, col2):
    arrRow = [0 for i in range(col2-col1+1)]
    for i in range(col1,col2):
            arrRow[i-col1] = arr[row][i]
    arrRow[col2-col1] = ";EOP"
    return(arrRow)

# Mengeluarkan jumlah dari semua elemen dalam array integer
def sumArray(arr):
    sum = 0
    for i in range(manual_len(arr)):
        sum += int(arr[i])
    return sum

# Mengeluarkan ID integer maksimum dalam sebuah array integer
def maxArrayID(arr):
    max = arr[0]
    id = 0
    for i in range(manual_len(arr)):
        if arr[i] > max:
            max = arr[i]
            id = i
    return id

# Mengeluarkan ID integer minimum dalam sebuah array integer
def minArrayID(arr):
    min = arr[0]
    id = 0
    for i in range(manual_len(arr)):
        if arr[i] < min:
            min = arr[i]
            id = i
    return id

# Mengeluarkan huruf pertama dari sebuah character
def firstLetter(char):
    for i in char:
        return i

# Menguluarkan banyaknya x muncul dalam array
def howManyX(arr,x):
    count = 0
    for i in range(manual_len(arr)):
        if arr[i] == x:
            count+=1
    return count

def findIdx(arr,x):
    for i in range(manual_len(arr)):
        if arr[i] == x:
            return i
    return False

def removeElmt(arr,id):
    new_arr = [0 for i in range(manual_len(arr) - 1)]
    c = 0
    for i in range(manual_len(arr)):
        if i != id:
            new_arr[c] = arr[i]
            c += 1
    return new_arr

# arrtocsv, memasukkan array ke file csv
def arrtocsv(arr,filename,col):
    csv_file = open(filename,"w")
    for i in range(manual_len(arr)):
        for j in range(col):
            csv_file.write(arr[i][j])
            csv_file.write(";")
        csv_file.write("\n")
    csv_file.close()

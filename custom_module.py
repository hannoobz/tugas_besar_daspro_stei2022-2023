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

def manual_pop(array,element):
    length = manual_len(array)
    new_array = ["" for i in range(length)]
    elmt_found = False
    for i in range(length):
        if array[i]==element:
            elmt_found = True
        if elmt_found==False:
            new_array[i]=array[i]
        else:
            new_array[i]=array[i+1]
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

# Mengeluarkan jumlah dari semua elemen dalam array integer (RECURSIVE)
def sumArray(arr):
    if manual_len(arr) == 0:
        return 0
    else:
        for i in range(manual_len(arr)):
            return int(arr[0]) + sumArray(removeFirstRow(arr))

# Mengeluarkan ID integer maksimum dalam sebuah array integer (RECURSIVE)
def maxArrayID(arr, max, id):
    if manual_len(arr) == 0:
        return id
    else:
        if arr[0] > max:
            max = arr[0]
            id = manual_len(arr) - 1
        return maxArrayID(removeFirstRow(arr) , max, id)

# Mengeluarkan ID integer minimum dalam sebuah array integer (RECURSIVE)
def minArrayID(arr, min, id):
    if manual_len(arr) == 0:
        return id
    else:
        if arr[0] < min:
            min = arr[0]
            id = manual_len(arr) - 1
        return minArrayID(removeFirstRow(arr) , min, id)

# Mengeluarkan huruf pertama dari sebuah character
def firstLetter(char):
    return char[0]

# Menguluarkan banyaknya x muncul dalam array (RECURSIVE)
def howManyX(arr, x, count):
    if manual_len(arr) == 0:
        return count
    elif arr[0] == x:
        count += 1
    return howManyX(removeFirstRow(arr), x, count)

def findIdx(arr,x):
    for i in range(manual_len(arr)):
        if arr[i] == x:
            return i
    return False

def removeElmt(array,index):
    length = manual_len(array)
    new_arr = ["" for i in range(length)]
    for i in range(index):
        new_arr[i]=array[i]
    for i in range(index,length):
        new_arr[i]=array[i+1]
    return new_arr

# arrtocsv, memasukkan array ke file csv
def arrtocsv(arr,filename,col):
    csv_file = open(filename,"w")
    for i in range(manual_len(arr)):
        for j in range(col):
            csv_file.write(str(arr[i][j]))
            csv_file.write(";")
        csv_file.write("\n")
    csv_file.close()

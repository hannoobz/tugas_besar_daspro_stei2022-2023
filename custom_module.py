# Fungsi manual_split 
# untuk splitting string
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
def loader(directory):
    file = open(directory,"r")
    array = file.read()+";EOP"
    array = manual_split(array,"\n")
    for i in range(manual_len(array)):
        array[i] = manual_split(array[i],";")
    file.close()
    return array

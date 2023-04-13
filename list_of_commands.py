from custom_module import *
users = loader("user.csv") # Matriks data user


def login():
    username = str(input())
    password = str(input())
    global role 
    role = ""

    iteration = 1
    while True:
        if role != "":
            print("Anda telah login dengan username",username+", silahkan lakukan “logout” sebelum melakukan login kembali.")
            break
        if users[iteration][0] == username:
            if users[iteration][1]==password:
                print("Selamat datang,",username+"!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                role = users[iteration][2]
            else:
                print("Password Salah!")
            break
        if users[iteration]==';EOP':
            print("Username tidak terdaftar!")
            break
        iteration += 1
    

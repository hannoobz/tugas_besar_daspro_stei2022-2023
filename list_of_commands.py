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

#-------------------IMPORT FUNCTION-----------------#
from set import clear_term,header_user,header_regis


#----IMPORT MODUL-----#
import pwinput
import json
import time
import role.user as user_menu

#---------------READ FILE JSON----------------#
path_user = 'database\\user.json'
with open(path_user,"r") as user_data:
    data_user = json.load(user_data)


#----------------TAMBAH DATA USER-----------------#
def tambah_user(data_user):

    with open(path_user, mode='w') as add_user:
        json.dump(data_user, add_user, indent=4)


#------------------------------------LOGIN AND REGISTRATION USER-------------------------------------#
def user():

    clear_term()
    header_user()

    username = input("\nUsername : ")
    password = pwinput.pwinput(mask='X')

    for checkan in range(len(data_user)):
    
        if data_user[checkan]["username"] == username and data_user[checkan]["password"] == password:
            clear_term()
            header_user()

            print("\nlogin berhasil, selamat datang",data_user[checkan]["nama"])
            print("\nMohon Tunggu ...")

            time.sleep(2)
            user_menu.menu(data_user[checkan]["nama"])

        else:
            continue

    clear_term()
    header_user()

    print("\nUsername dan Password tidak sesuai")
    time.sleep(1)

    user()


def user_registration():

    clear_term()
    header_regis()

    name     = input("Name              : ")
    email    = input("Email             : ")
    address  = input("Address           : ")
    phone    = input("Phone             : ")
    gender   = input("Gender (f/m)      : ")
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")

    data_user.append({
        "nama" : name,
        "email" : email,
        "address" : address,
        "phone" : phone,
        "gender" : gender,
        "username" : username,
        "password" : password
    })

    tambah_user(data_user)

    clear_term()
    header_regis()

    print("\nRegistrasi Berhasil")
    print("Silahkan Melakukan Login")
    time.sleep(2)

    user()


#-----------MENU UTAMA YANG DIJALANKAN-----------#
def menu():

    clear_term()
    header_user()

    ask = input("\nSudah Punya Akun (y/n) : ")

    if ask == "y":
        user()

    elif ask == "n":
        user_registration()

    else:
        print("Wrong Input")
        time.sleep(1)

        menu()
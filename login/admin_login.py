from set import clear_term,header_admin,header_regis
import role.admin as admin
from bcrypt import re
import pwinput
import json
import time

#---------------READ FILE JSON----------------#
path_admin = "database\\admin.json"
with open(path_admin,mode="r") as admin_data:
    data_admin = json.load(admin_data)

with open("database\\code.json","r") as akses_kode:
    kode = json.load(akses_kode)


#----------------TAMBAH DATA ADMIN-----------------#
def tambah_admin(data_admin):

    with open(path_admin, mode='w') as add_admin:
        json.dump(data_admin, add_admin, indent=4)


#--------------------------------LOGIN AND REGISTRATION ADMINISTRATOR-----------------------------#
def administator():

    clear_term()
    header_admin()

    username = input("\nUsername : ")
    password = pwinput.pwinput(mask='X')

    for check in range(len(data_admin)):

        if data_admin[check]["username"] == username and data_admin[check]["password"] == password:
            clear_term()
            header_admin()

            print("\nlogin berhasil, selamat datang", data_admin[check]["nama"])
            print("\nMohon Tunggu ...")
            time.sleep(2)

            admin.menu()

            time.sleep(2)
            admin.menu()

        else:
            continue
        
    clear_term()
    header_admin()

    print("\nUsername dan Password tidak sesuai")

    time.sleep(1)
    administator()

def admin_registration(pesan=None):

    clear_term()
    header_regis()

    if pesan : print(pesan)
    name       = input("Name                : ")
    email      = input("Email               : ")
    address    = input("Address             : ")
    phone      = input("Phone               : ")
    gender     = input("Gender (f/m)        : ")
    username   = input("Masukkan Username   : ")
    password   = input("Masukkan Password   : ")

    aturan_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    aturan_gender = "f" or "m"
    if not name or not name.isalnum() : return admin_registration("Nama tidak valid")
    if not re.fullmatch(aturan_email,email) or not email: return admin_registration("Format email tidak valid")
    if not address.isalnum() and not address: return admin_registration("Alamat tidak valid")
    if not phone or not phone.isnumeric() : return admin_registration("No. telepon tidak valid")
    if not gender or not re.fullmatch(aturan_gender,gender): return admin_registration("Gender tidak valid")
    if not username or not username.isalnum() : return admin_registration("Username tidak valid")
    if not password or not username.isalnum() : return admin_registration("Password tidak valid")
    kode_akses = input("Masukkan Kode Akses : ")

    for check in kode:

        if kode_akses == check.get("kode"):
            data_admin.append({
                "name" : name,
                "email" : email,
                "address" : address,
                "phone" : phone,
                "gender" : gender,
                "username" : username,
                "password" : password
            })

            tambah_admin(data_admin)

            clear_term()
            header_regis()

            print("\nRegistrasi Berhasil")
            print("Silahkan Melakukan Login")

            time.sleep(2)
            administator()

        else:
            print("Kode Akses Salah")

            time.sleep(1)
            admin_registration()


#----------MENU UTAMA YANG DIJALANKAN-----------#
def menu():

    clear_term()
    header_admin()

    ask = input("\nSudah Punya Akun (y/n) : ")

    if ask == "y":
        administator()

    elif ask == "n":
        admin_registration()

    else:
        print("\nWrong Input")
        time.sleep(1)
        menu()
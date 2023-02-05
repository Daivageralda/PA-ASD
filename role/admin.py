from set import clear_term,header_admin
import controller.barangController as barangController
import controller.adminController as adminController
import controller.userController as userController
import controller.kasirController as kasirController
import time
import main

def menu():
    clear_term()
    header_admin()

    print("\n1. Barang")
    print("2. Admin")
    print("3. User")
    print("4. Kasir")
    print("5. Log Out")
    ask = input("\nChoose : ")
    if ask == "1":
        barang_control = barangController.barang()
        barang_control.menu_barang()

    elif ask == "2":
        admin_control = adminController.administrator()
        admin_control.menu_admin()

    elif ask == "3":
        user_control = userController.user()
        user_control.menu_user()

    elif ask == "4":
        kasir_control = kasirController.kasir()
        kasir_control.kasir_menu()
        
    elif ask =="5":

        clear_term()
        header_admin()

        print("Berhasil Log Out")

        time.sleep(2)
        main.login_menu()
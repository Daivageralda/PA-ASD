#-------------IMPORT MODUL-------------#
import login.admin_login as admin_login
import login.user_login as user_login
from set import clear_term,header
import time

#----------MENU UTAMA YANG DIJALANKAN-----------#
def login_menu():

    clear_term()

    print("== LOGIN ==")
    print("\n1. Admin")
    print("2. User")
    print("3. Exit")
    login_choose = input("\nChoose : ")
    if login_choose == "1": admin_login.menu()
    elif login_choose == "2": user_login.menu()
    elif login_choose == "3":
        clear_term()
        header()
        print("Terimakasih")
        time.sleep(2)
        raise SystemExit
    else: 
        print("\nWrong Input")
        time.sleep(1)
        login_menu()
     
#---PROGRAM YANG PERTAMA KALI DIJALANKAN----#
def main_menu():

    clear_term()
    header()
    enter = input("\nPress Enter ...")
    if enter == "": login_menu()
    else:
        print("Wrong Input")
        time.sleep(1)
        main_menu()

#--MENJALANKAN PROGRAM---#
if __name__ == "__main__":
    main_menu()
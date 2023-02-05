from set import clear_term,header_user
import transaction.userOnly as userOnly
import main
import time

def menu(nama):

    clear_term()
    header_user()

    print("\n1. Beli")
    print("2. Lihat Seluruh Data Orderan")
    print("3. Cek Profil User")
    print("4. Log Out")

    ask = input("Choose : ")

    if ask == "1":
        order = userOnly.order()
        order.orderan(nama)

    elif ask == "2":
        data_order = userOnly.order()
        data_order.tampilkan_list_order(nama)

    elif ask == "3":
        data_user = userOnly.order()
        data_user.cek_profil(nama)

    elif ask == "4":
        clear_term()
        header_user()

        print("Berhasil Log Out")
        time.sleep(2)

        main.login_menu()

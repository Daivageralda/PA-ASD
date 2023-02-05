from set import clear_term,header_admin,header_update,header_hapus
from prettytable import PrettyTable
import role.admin as admin
import json
import time

class Node:

    def __init__ (self,data):
        self.data = data
        self.next = None

    def getdata(self):
        return self.data

    def getnextnode(self):
        return self.next

    def setdata(self,newdata):
        self.data = newdata

    def setnode(self,newnode):
        self.next = newnode

class administrator:  

    def __init__ (self):
        self.head = None
        self.tail = None


#-----------IMPOR DATA JSON KE DALAM NODE----------#
    def json_node(self):

        path_admin = "database\\admin.json"
        
        with open(path_admin,mode="r") as data_admin:

            global data

            data = json.load(data_admin)
            idx = 0
            val = False

            while not val:

                if idx > (len(data)-1):
                    val = True

                else:
                    newnode = Node(data[idx])

                    if self.tail is not None:
                        self.tail.next = newnode
                        
                    else:
                        self.head = newnode
                    self.tail = newnode
                    idx+=1


#---------------SAVE NODE KE DALAM DATA JSON-------------#
    def node_to_json(self,data):

        path_admin = "database\\admin.json"

        with open(path_admin,mode="w") as data_admin:

            json.dump(data,data_admin,indent=4)
    

    def save_nodes(self):

        list_node = []
        node      = self.head

        while node != None:
            list_node.append(node.data)
            node = node.next

        return self.node_to_json(list_node)


#----------------------------------------PRINT TABEL ADMIN---------------------------------------#
    def printllist(self):

            nodenya       = self.head
            tabel_admin = PrettyTable(["No.","Nama","Gender","E-mail","No. Telepon","Alamat","Username","Password"])

            tabel_admin.clear_rows()

            i = 0

            while nodenya is not None :

                tabel_admin.add_row([
                    (i + 1),
                    nodenya.data["name"],
                    nodenya.data["gender"],
                    nodenya.data["email"],
                    nodenya.data["phone"],
                    nodenya.data["address"],
                    nodenya.data["username"],
                    nodenya.data["password"]
                ])

                i += 1

                nodenya = nodenya.next

            print(tabel_admin)

#--------------------------TAMPILKAN NODE--------------------#
    def tampilkan_admin(self):

        clear_term()
        print("== ADMIN ==\n")

        self.printllist()

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            self.menu_barang()

        else:
            print("Wrong Input")

#-----------------UPDATE DATA SALAH SATU NODE----------------------#
    def code_item(self):
        path_kode = "database\\code.json"
        with open(path_kode,mode="r") as akses_kode:

            global kode
            kode = json.load(akses_kode)


    def update_admin(self):

            clear_term()
            header_update()

            self.printllist()
            self.code_item()

            no_admin   = int(input("Choose Number                : "))
            nama       = input("Masukkan Nama Baru           : ")
            email      = input("Masukkan E-Mail Baru         : ")
            address    = input("Masukkan Alamat Baru         : ")
            phone      = input("Masukkan Nomor Telepon Baru  : ")
            gender     = input("Masukkan Gender Baru (f/m)   : ")
            username   = input("Masukkan Username Baru       : ")
            password   = input("Masukkan Password Baru       : ")
            kode_akses = input("Masukkan Kode Akses          : ")

            for check in kode:

                if kode_akses == check[kode]:
                    mail = data[no_admin-1]["email"]

                    current = self.head

                    while current != None:

                        if current.data["email"] == mail:

                            current.data["name"]        = nama
                            current.data["email"]       = email
                            current.data["address"]     = address
                            current.data["phone"]       = phone
                            current.data["gender"]      = gender
                            current.data["username"]    = username
                            current.data["password"]    = password
                            break

                        current = current.next

                else:
                    print("Kode Akses Salah")
                    time.sleep(1)

                    self.update_admin()

            clear_term()
            header_update()

            self.save_nodes()
            print("\nData Berhasil Diupdate")

            ask = input("\nTekan Enter Untuk Lanjut ...")

            if ask == "":
                self.menu_barang()

            else:
                print("Wrong Input")


#-------------------------MENGHAPUS NODE------------------------#
    def hapus_admin(self):
        clear_term()
        header_hapus()
        
        self.printllist()

        no_admin = int(input("Choose Number : "))
        nama = data[no_admin-1]["name"]

        node_sekarang = self.head
        node_sebelumnya = None
        ditemukan = False

        while not ditemukan:

            if node_sekarang.data["name"] == nama:
                ditemukan=True

            else:
                node_sebelumnya = node_sekarang
                node_sekarang = node_sekarang.getnextnode()

        if node_sebelumnya == None:
            self.head = node_sekarang.getnextnode()

        else:
            node_sebelumnya.setnode(node_sekarang.getnextnode())

        self.save_nodes()
        print("\nData Berhasil Dihapus")

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            self.menu_barang()

        else:
            print("Wrong Input")


#----------MENU YANG DIJALANKAN----------#
    def menu_admin(self):

        clear_term()
        header_admin()

        if self.head is not None:
            pass

        else:
            self.json_node()
        
        print("\n1. Tampilkan Admin")
        print("2. Update Data Admin")
        print("3. Hapus Data Admin")
        print("4. Kembali")

        ask = input("\nChoose : ")

        if ask == "1":
            self.tampilkan_admin()

        elif ask == "2":
            self.update_admin()

        elif ask == "3":
            self.hapus_admin()

        elif ask == "4":
            admin.menu()
from set import clear_term,header_admin,header_update,header_hapus
from prettytable import PrettyTable
import role.admin as admin
import json

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

class user:  

    def __init__ (self):
        self.head = None
        self.tail = None


#-----------IMPOR DATA JSON KE DALAM NODE----------#
    def json_node(self):

        with open("user.json","r") as data_user:

            global data

            data = json.load(data_user)
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

        with open("user.json","w") as data_user:

            json.dump(data,data_user,indent=4)
    

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
            tabel_user = PrettyTable(["No.","Nama","E-Mail","Alamat","No. Telepon","Gender","Username","Password"])

            tabel_user.clear_rows()

            i = 0

            while nodenya is not None :

                tabel_user.add_row([
                    (i + 1),
                    nodenya.data["name"],
                    nodenya.data["email"],
                    nodenya.data["alamat"],
                    nodenya.data["phone"],
                    nodenya.data["gender"],
                    nodenya.data["username"],
                    nodenya.data["password"]
                ])

                i += 1

                nodenya = nodenya.next

            print(tabel_user)

#--------------------------TAMPILKAN NODE--------------------#
    def tampilkan_user(self):

        clear_term()
        print("== USER ==\n")

        self.printllist()

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            self.menu_barang()

        else:
            print("Wrong Input")

#-----------------UPDATE DATA SALAH SATU NODE----------------------#

    def update_user(self):

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

                current = current.next

                

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
    def hapus_user(self):
        clear_term()
        header_hapus()
        
        self.printllist()

        no_user = int(input("Choose Number : "))
        nama = data[no_user-1]["name"]

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
    def menu_user(self):

        clear_term()
        header_admin()

        if self.head is not None:
            pass

        else:
            self.json_node()
        
        print("\n1. Tampilkan User")
        print("2. Update Data User")
        print("3. Hapus Data User")
        print("4. Kembali")

        ask = input("\nChoose : ")

        if ask == "1":
            self.tampilkan_user()

        elif ask == "2":
            self.update_user()

        elif ask == "3":
            self.hapus_user()

        elif ask == "4":
            admin.menu()
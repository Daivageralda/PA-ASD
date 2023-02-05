from set import clear_term, gen_code,header_beli
from prettytable import PrettyTable
import datetime
import role.user as user
import json


class Node:
    def __init__ (self,data):
        self.data =data
        self.next = None

    def getdata(self):
        return self.data

    def getnextnode(self):
        return self.next

    def setdata(self,newdata):
        self.data = newdata

    def setnode(self,newnode):
        self.next = newnode

class order:

    def __init__(self):
        self.head = None
        self.tail = None
    

#-----------IMPOR DATA JSON KE DALAM NODE----------#
    def json_node(self):
        path_order = "database\\order.json"
        with open(path_order,"r") as data_order:

            global order_data

            order_data = json.load(data_order)
            idx = 0
            val = False

            while not val:

                if idx > (len(order_data)-1):
                    val = True

                else:
                    newnode = Node(order_data[idx])

                    if self.tail is not None:
                        self.tail.next = newnode
                        
                    else:
                        self.head = newnode
                    self.tail = newnode
                    idx+=1


#---------------SAVE NODE KE DALAM DATA JSON-------------#
    def node_to_json(self,order_data):

        path_order = "database\\order.json"
        with open(path_order,"w") as data_order:

            json.dump(order_data,data_order,indent=4)


    def save_nodes(self):

        list_node = []
        node      = self.head

        while node != None:
            list_node.append(node.data)
            node = node.next

        return self.node_to_json(list_node)


    def cek_profil(self,nama):
        path_user = "database\\user.json"
        with open(path_user,"r") as data_user:
            user_data = json.load(data_user)

            for check in range(len(user_data)):
                if user_data[check]["nama"] == nama:

                    clear_term()
                    print("== PROFIL USER ==")

                    print("Nama         :",user_data[check]["nama"])
                    print("E-Mail       :",user_data[check]["email"])
                    print("Alamat       :",user_data[check]["address"])
                    print("No. Telepon  :",user_data[check]["phone"])
                    print("Gender       :",user_data[check]["gender"])
                    print("Username     :",user_data[check]["username"])
                    print("Password     :",user_data[check]["password"])

                else:
                    continue

            ask = input("\nTekan Enter Untuk Lanjut ...")

            if ask == "":
                user.menu(nama)

            else:
                print("Wrong Input")


#-------------------------------------------TAMPILKAN LIST DATA PEMBELI------------------------------------#
    def tampilkan_list_order(self,nama):

        self.json_node()

        tabel_order = PrettyTable(["Tanggal Pembelian","Nama Pembeli","Kode Barang","Jumlah","Kode Transaksi"])
        tabel_order.clear_rows()

        node = self.head

        i = 0 

        while node != None:

            tabel_order.add_row([
                node.data["tgl_pembelian"],
                node.data["nama_pembeli"],
                node.data["kode_barang"],
                node.data["jumlah"],
                node.data["kode_transaksi"]
            ])

            i += 1

            node = node.next

        clear_term()
        print("== LIST ORDER ==\n")

        print(tabel_order)

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            user.menu(nama)

        else:
            print("Wrong Input")


#-------------------------------------TAMPILKAN SELURUH BARANG----------------------------------------#
    def tampilkan_barang(self):
        path_barang = "database\\barang.json"
        with open(path_barang,"r") as data_barang:

            global barang
            barang = json.load(data_barang)

            tabel_barang = PrettyTable(["No.", "Kode Barang", "Nama", "Kategori", "Harga", "Stok"])
            tabel_barang.clear_rows()

            for i in range(len(barang)):

                tabel_barang.add_row([
                    i+1,
                    barang[i]["kode_barang"],
                    barang[i]["nama_barang"],
                    barang[i]["kategori"],
                    barang[i]["harga"],
                    barang[i]["stok"]
                ])
        print(tabel_barang)
    

#---------------------------------------------PROSES ORDERAN---------------------------------------------#
    def orderan(self,nama):

        clear_term()
        header_beli()

        self.json_node()
        self.tampilkan_barang()

        no_barang = int(input("No. Barang :"))
        jumlah = int(input("Jumlah : "))

        waktu = datetime.datetime.now()

        data = {
        "tgl_pembelian" : waktu.strftime("%c"),
        "nama_pembeli"  : nama,
        "no_barang"     : no_barang,
        "kode_barang"   : barang[no_barang-1]["kode_barang"],
        "kode_transaksi": gen_code(),
        "jumlah"        : jumlah
        }

        newnode = Node(data)

        if self.tail is not None:
            self.tail.next = newnode
            
        else:
            self.head = newnode
        self.tail = newnode

        self.save_nodes()

        clear_term()
        header_beli()
        
        self.json_node()

        kode = order_data[len(order_data)-1]["kode_transaksi"]
        print("\nBerhasil membuat orderan, kode transaksi anda adalah :", kode)
        print("Silahkan menuji ke loket kasir untuk melakukan pembayaran")

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            user.menu(nama)

        else:
            print("Wrong Input")
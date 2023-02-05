from set import clear_term,header_kasir
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


class kasir:  

    def __init__ (self):
        self.head = None
        self.tail = None


#----------------IMPOR DATA JSON KE DALAM NODE----------------#
    def json_node(self):
        path_order = "database\\order.json"

        with open(path_order,"r") as data_order:

            global data

            data = json.load(data_order)
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


    def impor_data_barang(self):

        path_barang = "database\\barang.json"
        with open(path_barang,"r") as data_barang:

            global barang
            barang = json.load(data_barang)


#---------------SAVE NODE KE DALAM DATA JSON-------------#
    def node_to_json(self,data):
        path_order = "database\\order.json"
        with open(path_order,"w") as data_order:

            json.dump(data,data_order,indent=4)
    

    def save_nodes(self):

        list_node = []
        node      = self.head

        while node != None:
            list_node.append(node.data)
            node = node.next

        return self.node_to_json(list_node)


#----------------UPDATE DATA BARANG-----------------#
    def update_data_barang(self,barang):
        path_barang = "database\\barang.json"
        with open(path_barang,"w") as data_barang:
            json.dump(barang,data_barang,indent=4)


#--------MENGAMBIL NODE PALING DEPAN--------#
    def node_paling_depan(self):

        if self.head == None:
            print("Antrian Kosong")

            return -1

        return self.head.data["kode_transaksi"]


#------------MENGHAPUS NODE TERAKHIR----------#
    def dequeue(self):

        if self.head == None:
            print("Antrian Kosong")
        
        node = self.head
        self.head = self.head.next

        if self.head == None:
            self.tail

        return node.data


#--------------------------------------PROSES BAYAR--------------------------------------#
    def pembayaran(self):
        
        clear_term()
        header_kasir()

        self.impor_data_barang()
        print("\nPembayaran yang harus diproses :",self.node_paling_depan())

        kode_bayar = input("Masukkan Kode Bayar : ")

        for check in range(len(data)):

            if data[check]["kode_transaksi"] == kode_bayar:
                
                for find in range(len(barang)):

                    if data[check]["kode_barang"] == barang[find]["kode_barang"]:

                        total_bayar = barang[find]["harga"] * data[check]["jumlah"]

                        print("Total : Rp.",total_bayar)
                        uang = int(input("Masukkan Jumlah Uang : Rp. "))

                        kembalian = uang - total_bayar
                        print("Kembalian : Rp.",kembalian)

                        self.dequeue()
                        self.save_nodes()

                        barang[find]["stok"] - data[check]["jumlah"]
                        self.update_data_barang(barang)

                        ask = input("\nTekan Enter Untuk Lanjut ...")

                        if ask == "":
                            admin.menu()

                        else:
                            print("Wrong Input")
                    else:
                        continue
            else:
                continue

    def kasir_menu(self):

        clear_term()
        header_kasir()

        if self.head != None:
            pass

        else:
            self.json_node()

        print("Kode Bayar Yang Saat Ini Harus Diproses :",self.node_paling_depan())

        ask = input("\nLanjut Ke Pembayaran ? (y/t) : ")

        if ask == "y":
            self.pembayaran()

        elif ask =="t":
            admin.menu()

        else:
            print("Wrong Input")

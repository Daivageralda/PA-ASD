from set import clear_term,header_admin,header_tambah,gen_code,header_update,header_hapus
from prettytable import PrettyTable
import role.admin as admin
import json
import math

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

class barang:  

    def __init__ (self):
        self.head = None
        self.tail = None


#-----------IMPOR DATA JSON KE DALAM NODE----------#
    def json_node(self):

        path_barang = "database\\barang.json"

        with open(path_barang,"r") as data_barang:

            global data

            data = json.load(data_barang)
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

        path_barang = "database\\barang.json"

        with open(path_barang,"w") as data_barang:

            json.dump(data,data_barang,indent=4)
    

    def save_nodes(self):

        list_node = []
        node      = self.head

        while node != None:
            list_node.append(node.data)
            node = node.next

        return self.node_to_json(list_node)


#------------MENAMBAHKAN DATA KE DALAM NODE--------------#
    def tambah_barang(self):

        clear_term()
        header_tambah()


        name            = input("\nNama Barang     : ")
        kategori        = input("Kategori Barang : ")
        harga           = int(input("Harga           : "))
        stok            = int(input("Stok            : "))

        data = {
            "kode_barang"   : gen_code(),
            "nama_barang"   : name,
            "kategori"      : kategori,
            "harga"         : harga,
            "stok"          : stok
        }

        newnode = Node(data)

        if self.tail is not None:
            self.tail.next = newnode  

        else:
            self.head = newnode
        self.tail = newnode

        clear_term()
        header_tambah()

        self.save_nodes()
        print("\nBerhasil Menambahkan Barang")

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            self.menu_barang()

        else:
            print("Wrong Input")


#----------------------------------------PRINT TABEL BARANG---------------------------------------#
    def printllist(self):

            nodenya       = self.head
            tabel_barang = PrettyTable(["No.", "Kode Barang", "Nama", "Kategori", "Harga", "Stok"])

            tabel_barang.clear_rows()

            i = 0

            while nodenya is not None :

                tabel_barang.add_row([
                    (i + 1),
                    nodenya.data["kode_barang"],
                    nodenya.data["nama_barang"],
                    nodenya.data["kategori"],
                    nodenya.data["harga"],
                    nodenya.data["stok"]
                ])

                i += 1

                nodenya = nodenya.next

            clear_term()
            print("== BARANG ==\n")
            print(tabel_barang)

            ask = input("\nTekan Enter Untuk Lanjut ...")

            if ask == "":
                self.menu_barang()

            else:
                print("Wrong Input")


#-----------------UPDATE DATA SALAH SATU NODE----------------------#
    def update_barang(self):

            clear_term()
            header_update()

            no_barang   = int(input("Choose Number             : "))
            nama        = input("Masukkan Nama Barang Baru : ")
            kategori    = input("Masukkan Kategori Baru    : ")
            harga       = int(input("Masukkan Harga Baru       : "))
            stok        = int(input("Masukkan Jumlah Stok Baru : "))

            kode = data[no_barang-1]["kode_barang"]

            current = self.head

            while current != None:

                if current.data["kode_barang"] == kode:

                    current.data["kode_barang"] = gen_code()
                    current.data["nama_barang"] = nama
                    current.data["kategori"]    = kategori
                    current.data["harga"]       = harga
                    current.data["stok"]        = stok
                    break

                current = current.next

            clear_term()
            header_update()

            self.save_nodes()
            print("\nBarang Berhasil Diupdate")

            ask = input("\nTekan Enter Untuk Lanjut ...")

            if ask == "":
                self.menu_barang()

            else:
                print("Wrong Input")


#-------------------------MENGHAPUS NODE------------------------#
    def hapus_barang(self):
        
        clear_term()
        header_hapus()

        no_barang = int(input("Choose Number : "))
        kode = data[no_barang-1]["kode_barang"]

        node_sekarang = self.head
        node_sebelumnya = None
        ditemukan = False

        while not ditemukan:

            if node_sekarang.data["kode_barang"] == kode:
                ditemukan=True

            else:
                node_sebelumnya = node_sekarang
                node_sekarang = node_sekarang.getnextnode()

        if node_sebelumnya == None:
            self.head = node_sekarang.getnextnode()

        else:
            node_sebelumnya.setnode(node_sekarang.getnextnode())

        self.save_nodes()
        print("\nBarang Berhasil Dihapus")

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            self.menu_barang()

        else:
            print("Wrong Input")


#----------------------------------------SORTING NODE------------------------------------------#
    def sorting_nodes(self):

        list_of_nodes = []
        node = self.head

        while node is not None:

            list_of_nodes.append(node.data)
            node = node.next

        return self.quicksort(list_of_nodes,0,len(list_of_nodes))


    def quicksort(self,node_list, first_idx, last_idx):

        if last_idx <= first_idx:
            return

        part = self.partition(node_list, first_idx, last_idx)
        self.quicksort(node_list, first_idx, part - 1)
        self.quicksort(node_list, part, last_idx)

        return self.insert_list_to_node(node_list) 


    def partition(self,node_list, first_idx, last_idx):

        pivot = node_list[first_idx]["nama_barang"]
        pos_batas = first_idx + 1

        for idx in range(first_idx+1,last_idx):

            if node_list[idx]["nama_barang"] < pivot:
                node_list[pos_batas],node_list[idx]=node_list[idx],node_list[pos_batas]
                pos_batas += 1

        node_list[pos_batas-1],node_list[first_idx] = node_list[first_idx],node_list[pos_batas-1]

        return pos_batas


    def insert_list_to_node(self,main_data):

        self.tail = None    
        idx = 0
        val = False

        while not val:

            if idx > (len(main_data)-1):
                val = True

            else:
                new_node = Node(main_data[idx])

                if self.tail is not None:
                    self.tail.next = new_node

                else:
                    self.head = new_node

                self.tail = new_node
                idx += 1

        print("Sort Successfull")

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            return self.menu_barang()

        else:
            print("Wrong Input")


#------------------------------SEARCHING NODE-----------------------------#
    def jumpSearch(self,arr, x, n):

        prev = 0
        step = math.sqrt(n)

        while arr[int(min(step, n) - 1)] < x:
            step += math.sqrt(n)

            if prev >= n:
                return -1

        while arr[int(prev)] < x:
            prev += 1

            if prev == min(step, n):
                return -1

        if arr[int(prev)] == x:
            return prev

        return -1


    def searching_nodes(self):

        list_of_nodes = []
        cari = input("Cari Barang : ")

        node = self.head

        while node is not None:

            list_of_nodes.append(node.data["nama_barang"])
            node = node.next

        searching =  self.jumpSearch(list_of_nodes,cari,len(list_of_nodes))

        print("Barang ada di urutan :",searching+1)

        ask = input("\nTekan Enter Untuk Lanjut ...")

        if ask == "":
            return self.menu_barang()

        else:
            print("Wrong Input")




#----------MENU YANG DIJALANKAN----------#
    def menu_barang(self):

        clear_term()
        header_admin()

        if self.head is not None:
            pass

        else:
            self.json_node()
        
        print("\n1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Sort Barang")
        print("6. Search Barang")
        print("7. Kembali")

        ask = input("\nChoose : ")

        if ask == "1":
            self.tambah_barang()

        elif ask == "2":
            self.printllist()

        elif ask == "3":
            self.update_barang()

        elif ask == "4":
            self.hapus_barang()

        elif ask =="5":
            self.sorting_nodes()

        elif ask == "6":
            self.searching_nodes()

        elif ask =="7":
            admin.menu()
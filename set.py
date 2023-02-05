import os
import random
import string
def clear_term():
    os.system("cls")
def header():
    print("== Electronic Store ==")
def header_admin():
    print("== ADMIN ==")
def header_user():
    print("== USER ==")
def header_regis():
    print("== REGISTRASI ==")
def header_tambah():
    print("== TAMBAH ==")
def header_update():
    print("== UPDATE ==")
def header_hapus():
    print("== HAPUS ==")
def header_beli():
    print("== BELI ==")
def header_kasir():
    print("== KASIR ==")
def gen_code():
    code_generator = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(4))
    return code_generator
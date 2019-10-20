#!/usr/bin/python3.7
# soal 1 tengtang Sytem login
print("Pendaftaran")
nama=input("Masukan Nama = ")
register_email=input("Masukan Email pendaftaran = ")
register_pasword=input("Masukan Password Pendaftaran = ")
print("\n>>>Yeeeayy. Akun dengan nama {} berhasil didaftarkan<<<\n".format(nama))
print("Note : \n1. Y/y untuk Yes\n2. N/n untuk No")
tanya=input("Apakah anda ingin Login? ")
if (tanya=="Y" or tanya=="y"):
    email_login=input("\nMasukan Email = ")
    pasword_login=input("Masukan Password = ")
    if register_email==email_login and register_pasword==pasword_login:
        print("\n>>>Selamat {}, Anda Berhasil Login<<<\n".format(nama))
    else:
        print("\n>>>Maaf, Email Atau Pasword tidak sesuai<<<\n")
        
else:
    print("\n>>>Terimakasih Sudah Mendaftar<<<\n")
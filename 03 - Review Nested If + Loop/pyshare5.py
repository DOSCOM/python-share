#!/usr/bin/python3.7
kembalian=0
kurang=0
print(">>>Selamat Datang Di Cafein<<<\nSilahkan masukan data untuk memesan kopi")
nama=input("Masukan Nama Anda = ")
email=input("Masukan Email Anda = ")
print("Menu\n1. Vietnam Drip @15k")
print("2. Espresso @25k")
print("3. Caffe Latte @30k")
pilihan=int(input("Masukan pilihan anda = "))
if(pilihan==1):
    produk=("Vietnam Drip")
    harga=15000
    print("Note : \n1. Y/y untuk Yes\n2. N/n untuk No")
    yon=input(">>>Apakah anda yakin ingin memesan {}, dengan harga Rp.{} ???".format(produk,harga))    
    if(yon=='Y' or yon=='y'):
        bayar=int(input("Masukan uang anda = Rp."))
        if(bayar==harga):                   
            print("\n\t>>> Anda Berhasil Memesan {} dengan harga Rp.{}<<<\n".format(produk,harga))
        elif(bayar>harga):
            kembalian=bayar-harga
            # kurang=0
            print("\n\t>>> Anda Berhasil Memesan {} dengan harga Rp.{},kembalian anda Rp.{}<<<".format(produk,harga,kembalian))
        else:
            kurang=harga-bayar
            # kembalian=0
            print("\t\n>>>Maaf :( ,Uang Anda Kurang Rp.{}<<<".format(kurang))
    else:
        print("Selamat Datang Kembali {}".format(nama))
elif(pilihan==2):    
    produk=("Espresso")
    harga=25000
    print("Note : \n1. Y/y untuk Yes\n2. N/n untuk No")
    yon=input(">>>Apakah anda yakin ingin memesan {}, dengan harga Rp.{} ???".format(produk,harga))    
    if(yon=='Y' or yon=='y'):
        bayar=int(input("Masukan uang anda = Rp."))
        if(bayar==harga):                   
            print("\n\t>>> Anda Berhasil Memesan {} dengan harga Rp.{}<<<\n".format(produk,harga))
        elif(bayar>harga):
            kembalian=bayar-harga
            # kurang=0
            print("\n\t>>> Anda Berhasil Memesan {} dengan harga Rp.{},kembalian anda Rp.{}<<<".format(produk,harga,kembalian))
        else:
            kurang=harga-bayar
            # kembalian=0
            print("\t\n>>>Maaf :( ,Uang Anda Kurang Rp.{}<<<".format(kurang))
    else:
        print("Selamat Datang Kembali {}".format(nama))
elif(pilihan==3):    
    produk=("Caffe Latte")
    harga=30000
    print("Note : \n1. Y/y untuk Yes\n2. N/n untuk No")
    yon=input(">>>Apakah anda yakin ingin memesan {}, dengan harga Rp.{} ???".format(produk,harga))    
    if(yon=='Y' or yon=='y'):
        bayar=int(input("Masukan uang anda = Rp."))
        if(bayar==harga):                   
            print("\n\t>>> Anda Berhasil Memesan {} dengan harga Rp.{}<<<\n".format(produk,harga))
        elif(bayar>harga):
            kembalian=bayar-harga
            # kurang=0
            print("\n\t>>> Anda Berhasil Memesan {} dengan harga Rp.{},kembalian anda Rp.{}<<<".format(produk,harga,kembalian))
        else:
            kurang=harga-bayar
            # kembalian=0
            print("\t\n>>>Maaf :( ,Uang Anda Kurang Rp.{}<<<".format(kurang))
    else:
        print("Selamat Datang Kembali {}".format(nama))
else:
    print(">>>Maaf, Menu tidak tersidia")

print("Note : \n1. Y/y untuk Yes\n2. N/n untuk No")
nota=input("\nApakah Anda ingin Mencetak nota belanja : ")
if(nota=='Y' or nota=='y'):
    print("Nama Pembeli\t\t= {} ".format(nama))
    print("Email Pembeli\t\t= {} ".format(email))
    print("Kopi Yang Dibel\t\t = {}".format(produk))
    print("Harga Kopi\t\t= Rp.{}".format(harga))
    print("Uang Pembayaran\t\t= Rp.{}".format(bayar))
    print("Uang Kembalian\t\t= Rp.{}".format(kembalian))
    print("Uang Kurang\t\t= Rp.{}".format(kurang))
elif(nota=='N' or nota=='n'):
    print("\nSelamat Datang Kembali {}".format(nama))
else:
    print("Input Salah")            
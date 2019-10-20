#!/usr/bin/python3.7

saldo=5000000
pasword=20082000
print("Program Mesin ATM")
pin=int(input("Masukan pin anda : "))
if(pin==pasword):
    print("\nMenu")
    print("1. Cek Saldo")
    print("2. Penarikan")
    print("3. Transfer")
    pilih=int(input("Masukan menu pilihan anda = "))
    if(pilih==1):
        print("\n>>>Jumlah saldo anda sekarang : Rp.{} <<<".format(saldo))
    elif(pilih==2):
        tarik=int(input("Jumlah saldo anda sekarang : Rp.{} \nBerapakah uang yang ingin anda ambil : Rp.".format(saldo)))
        if(tarik>=0 and tarik<=saldo):
            saldo=saldo-tarik;
            print("\nNote\nAnda mengambil uang sebesar Rp.{}\nSisa saldo anda adalah Rp.{} ".format(tarik,saldo))
        # elif(saldo<=50000):
        #     print("saldo Endapan")
        else:
            print("\n>>>Maaf, Saldo Anda Tidak Mencukupi<<<\n")
            # print("\nERROR\n")
    elif(pilih==3):
        norek=int(input("Masukan Nomor rekening tujuan : "))
        kirim=int(input("Masukan jumlah uang yang akan anda transfer : Rp. "))
        if(kirim>saldo):
            sisa=kirim-saldo;
            print("\n>>>Maaf, Saldo anda kurang Rp.{} <<<\n".format(sisa))
        elif(kirim>=50000 and kirim<=saldo):
            print("\n>>>Transaksi ke nomor rekening [ {} ] dengan jumlah uang Rp.{} telah berhasil <<".format(norek,kirim))
            saldo=saldo-kirim
            print("Jumlah saldo anda sekarang = Rp.{}".format(saldo))
        else:
            print("\n>>>Jumlah tidak terdefinisi<<<\n")
    else:
        print("Menu Tidak Tersedia")
else:
    print("Maaf, Pin yang anda masukan salah")                
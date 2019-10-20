#!/usr/bin/python3.7

nama=input("Masukan Nama Anda = ")
nim=input("Masukan NIM Anda = ")
alamat=input("Masukan Alamat Anda = ")
ipk=float(input("Masukan IPK Anda = "))
semester=int(input("Masukan Semester Anda = "))
gaji=int(input("Masukan Gaji Orang Tua = Rp."))
if(ipk>3 and ipk<=4 ):
    if(semester>=5 and semester<=8):
        if(gaji>0 and gaji<=3000000):
            print(">>>Selamat {}, Anda mendapatkan Beasiswa<<<".format(nama))
        else:
            print("\n\t>>>Maaf, Pendapatan Tidak sesuai syarat<<<")
    else:
        print("\n\t>>>Maaf, Semester Tidak Sesuai Syarat<<<")
else:
    print("\n\t>>>Maaf, IPK Anda Belum Memenuhi Syarat<<<")
    
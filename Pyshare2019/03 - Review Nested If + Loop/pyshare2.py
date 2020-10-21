#!/usr/bin/python3.7
# Soal 2 Program rekomendasi Pertukaran Barang Berdasarkan poin

Barang_dian=int(input("Masukan Harga Barang Dian = "))
Barang_A=int(input("Masukan Harga Barang A = "))
print(">>>KESIMPULAN<<<")
if(Barang_A>=Barang_dian):
    print("Harga Barang Dian = {} Poin".format(Barang_dian))
    print("Harga Barang A = {} Poin".format(Barang_A))
    untung=Barang_A-Barang_dian
    print("Tukarlah Barang Dian dengan Barang A, Karena Dian akan mengalami keuntung sebesar {} Poin".format(untung))
else:
    print("Harga Barang Dian = {} Poin".format(Barang_dian))
    print("Harga Barang A = {} Poin".format(Barang_A))
    rugi=Barang_dian-Barang_A
    print("carilah Barang Lain saja untuk ditukar, Karena Dian akan mengalami kerugian sebesar {} Poin".format(rugi))

nama=input("masukkan nama : ")
umur=float(input("masukkan umur: "))

if umur>0 and umur<=1:
    print("usia {} sekarang {} tahun . Kategori Bayi".format(nama,umur))
elif umur>1 and umur<=3:
    print("usia {} sekarang {} tahun . Kategori Batita".format(nama,umur))
elif umur>3 and umur<=5:
    print("usia {} sekarang {} tahun . Kategori Batita".format(nama,umur))
elif umur>5 and umur<=12:
    print("usia {} sekarang {} tahun . Kategori Anak-anak".format(nama,umur))
elif umur>12 and umur<=17:
    print("usia {} sekarang {} tahun . Kategori Remaja".format(nama,umur))
elif umur>17 and umur<=30:
    print("usia {} sekarang {} tahun . Kategori Pemuda".format(nama,umur))
elif umur>30 and umur<=60:
    print("usia {} sekarang {} tahun . Kategori Dewasa".format(nama,umur))
elif umur>60 and umur<=100:
    print("usia {} sekarang {} tahun . Kategori Lansia".format(nama,umur))
else:
    print("Unknown")

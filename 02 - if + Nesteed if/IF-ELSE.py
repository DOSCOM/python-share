nama = input("Masukkan nama anda = ")
matkul = input("Mata kuliah anda ? = ")
nilai_akhir = float(input("Nilai akhir = "))

if (nilai_akhir >= 70 and nilai_akhir<= 100):
    print("Selamat {} ! Anda lulus mata kuliah {}".format(nama,matkul))
else :
    print("Maaf {} silahkan mengulangi lagi mata kuliah {}".format(nama,matkul))

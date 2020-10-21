# tipe data dan deklarasi variabel
x=10
y=11.5
nama="doscom"

# output
print(x)
print(y)
print(nama)
print("aku cinta ",nama)
print("aku cinta {}".format(nama))
print("aku cinta "+str(nama))
print("aku cinta ", str(nama))

# # operator penjumlahan
print("{0}+{1}={2}".format(x,y,x+y))

# operator perkalian
print("hasil kali dari x dan y adalah {}".format(x*y))

# hitung luas segita
alas=4
tinggi=5
luas=(alas*tinggi)/2
print("luas segitiga dengan alas {0} dan tinggi {1} adalah {2}".format(alas,tinggi,luas))

# hitung luas lingkaran
phi=3.14
r=7
rumus=phi*r*r
# atau bisa juga
rumus2 = phi * r ** 2
print("luas lingkaran = {}".format(rumus))
print("luas lingkaran2 = {}".format(rumus2))

# input-output
a=input("masukkan nilai a= ")     
b=input("masukkan nilai b= ")     
print("a= {0},b={1},a+b={2}".format(a,b,a+b))
print("a+b= {}".format(a+b))
print("a+b= ",str(a+b))


# sebelum casting tipe data
print("SEBELUM CASTING TIPE DATA")
a=input("masukkan nilai a= ")     
b=input("masukkan nilai b= ")     
print("a= {0},b={1},a+b={2}".format(a,b,a+b))

print("")

# # sesudah casting tipe data
print("SESUDAH CASTING TIPE DATA")
a=int(input("masukkan nilai a= "))
b=int(input("masukkan nilai b= "))
print("a= {0},b={1}, a+b= {2}".format(a,b,a+b))

# multiple input

nama1,nama2=input("masukan nama: ").split()
print("nama ku = {}".format(nama1))
print("nama dia= {}".format(nama2))
print("=====DATA DIRI======")
print("INPUT : ")
nama=input("Masukkan Nama \t: ")
nim=input("Masukkan NIM \t : ")
tmp=input("Masukkan Tempat Lahir : ")
tgl=input("Masukkan Tanggal Lahir : ")
tugas=int(input("Masukkan Nilai Tugas : "))
uts=int(input("Masukkan Nilai UTS : "))
uas=int(input("Masukkan Nilai UAS : "))
akhir=(tugas*0.4)+(uts*0.3)+(uas*0.3)
print(" ")
print(" ")
print(" ")
print("OUTPUT")
print("Nama\t\t : ",nama)
print("NIM\t\t : ",nim)
print("Tempat Lahir\t : ",tmp)
print("Tanggal Lahir\t : ",tgl)
print("Nilai Tugas\t : ",tugas)
print("Nilai UTS\t : ",uts)
print("Nilai UAS\t : ",uas)
print("Nilai Akhir\t : %.2f"%(akhir))

if (akhir>84):
    print("predikat nilai A")
elif (akhir>=75 and akhir<85):
    print("predikat nilai B")
elif (akhir>50 and akhir<=74):
    print("predikat nilai C")
else:
    print("predikat nilai D")




























angka = 0


#membuat fungsi


def nama(namamu):
    global angka
    angka = angka + 9
    print("Namaku adalah :"+namamu+str(angka))

def KelilingLingkaran(r):
    PHI = 3.14
    namaku = "Aldiya"
    return PHI*r*2

def tes(a = 0, b = 0):
    return a+b

def FungsiBaru():
    print("Suhaili Faruq")

def fungsiItung(itung):
    if itung == 0 :
        return 0
    else:
        return fungsiItung(itung-1)+itung

def CetakNama(batas):
    if batas == 0:
        print("Suhaili")
    else:
        print("Suhaili")
        CetakNama(batas-1)

HasilItung = fungsiItung(5)
print(HasilItung)
CetakNama(10)



# LuasLingkaran = lambda jari : 3.14*(jari**2)
#namaKu  = lambda : print("Suhaili faruq")




#print(__name__)

if __name__ == "__main__":
    FungsiBaru()
else:
    nama("Padma")



# nama("aldi")
# jawaban = KelilingLingkaran(30)
# angka = 1
# print("Hasil {}".format(jawaban))
# print(angka)
# # print(namaku)
# nama("Lukman")
# hasil = tes(3)
# print(hasil)

# print("Hellow")
# jari = -5
# print(abs(jari))
# print(str(jari))
# print(type(jari))
# print(float(jari))
# deret = [20,4,12,8,4,9]
# print(max(deret))
# print(min(deret))
# diameter = 5.5
# print(round(diameter))
# hewan = "GAJAH"
# print(len(hewan))
# """
# strip(),lstrip(),rstrip(),isalpha(),len(),upper(),lower()
# """
# print(hewan.lower())







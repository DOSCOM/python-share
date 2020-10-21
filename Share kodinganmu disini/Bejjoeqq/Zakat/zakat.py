import os,sys
from getpass import getpass
#pemanggilan fungsi dan variabel didalam class hanya diawali dengan self. kemudian diikuti dengan fungsi atau class tersebut.
class zakat():
    def __init__(self,nama=[],emas=[],zakat=[],pertahun=[],perbulan=[],nisab=[],keluar=False,forcestop=False):
        #variabel(atribut:class)
        self.nama=nama
        self.emas=emas
        self.zakat=zakat
        self.pertahun=pertahun
        self.perbulan=perbulan
        self.nisab=nisab
        self.keluar=keluar
        self.forcestop=forcestop
    def reset(self):#fungsi(method:class), me-reset variabel jika program dijalankan lebih dari satu kali(tanpa meng-exit program)
        self.zakat=[]
        self.pertahun=[]
        self.perbulan=[]
        self.nisab=[]
        self.keluar=False#variabel untuk kembali ke menu utama(ketik 0 untuk kembali)
        self.forcestop=False#variabel untuk keluar menggunakan sys.exit()
    def cls(self):#clear screen command prompt
        if os.name=="nt":
            os.system("cls")#for windows
        else:
            os.system("clear")#for ios/linux/dll
        self.title()#memanggil tittle untuk di run setiap kali layar di clear
    def formatrupiah(self,uang):#fungsi untuk membuat suatu int ke dalam bentuk rupiah mis 1000000 -> Rp. 1,000,000
        y = str(uang)
        if len(y) <= 3 :
            return 'Rp. ' + y
        else :
            p = y[-3:]#mengabaikan 3 digit pertama : "123456789" -> "456789"
            q = y[:-3]#mengabaikan 3 digit terakhir : "123456789" -> "123456"
            return self.formatrupiah(q) + ',' + p
    def title(self):
        print ("+———————————————————————————————————+")
        print ("|   Penghitung Zakat Penghasilan    |")
        print ("| Menurut Pendapatan Kasar (Brutto) |")
        print ("| Catatan : Ketik 0 untuk mengulang |")
        print ("+———————————————————————————————————+")
    def inputan(self,i,data):
        while True:
            try:
                self.cls()
                print("|{} Data|".format(data))
                self.nama[i] = input("Masukan data nama ke-{} : ".format(i+1))
                if self.nama[i] == "0":#validasi apakah user menginput 0, jika iya akan kembali ke menu utama
                    self.keluar=True
                    break
                self.emas[i] = int(input("Masukan harga emas saat ini: "))
                if self.emas[i] == 0:#validasi apakah user menginput 0, jika iya akan kembali ke menu utama
                    self.keluar=True
                    break
                self.pertahun[i] = int(input("Masukkan total harta : "))
                if self.pertahun[i] == 0:#validasi apakah user menginput 0, jika iya akan kembali ke menu utama
                    self.keluar=True
                    break
                break
            except:
                pass
    def kalkulasi(self,i):
        self.zakat.append(0.025 * self.pertahun[i])
        self.nisab.append(85 * self.emas[i])
        self.perbulan.append(self.zakat[i] / 12)
    def output(self,i):
        print("\n———————————————————————————")
        print(" Zakat Penghasilan (Brutto)")
        print("———————————————————————————")
        print("Nama :",self.nama[i])
        print("Harga 1 gram emas :",self.formatrupiah(self.emas[i]))
        print("Total harta per tahun :",self.formatrupiah(self.pertahun[i]))
        print("Harga nishab (85 gram emas) :",self.formatrupiah(self.nisab[i]))
        print("Zakat penghasilan : 2.5% x",self.formatrupiah(self.pertahun[i]),"=",self.formatrupiah(int(self.zakat[i])))
        if self.pertahun[i] >= self.nisab[i]:
            print("Keterangan : WAJIB Zakat",self.formatrupiah(int(self.zakat[i])),"/tahun")
            print("atau",self.formatrupiah(int(self.perbulan[i])),"/bulan")
        if self.pertahun[i] <= self.nisab[i]:
            print("Keterangan : Anda belum termasuk Wajib Zakat")
    def home(self):
        while True:#program akan terus mengulang jika tidak exit di akhir program (lihat line 111)
            self.cls()
            print("Selamat Datang :)")
            input("Enter...")
            self.reset()
            while True:#jika input salah(terjadi error) program akan mengulang dari baris dibawah ini
                try:
                    self.cls()
                    data=int(input("Masukan banyak data : "))
                    if data == 0:
                        break
                    self.nama=[0]*data#menentukan panjang array sesuai dengan input data
                    self.emas=[0]*data#bertujuan pada saat input nama,emas,gaji jumlahnya sesuai
                    self.pertahun=[0]*data
                    self.cls()
                    for x in range(data):
                        self.inputan(x,data)
                        if self.keluar==True:#if ini untuk kembali ke menu utama, didalam for x untuk keluar dari for x
                            break
                    if self.keluar==True:#if ini untuk kembali ke menu utama, sebelum eksekusi for kalkulasi
                        break
                    for x in range(data):
                        self.kalkulasi(x)
                    self.cls()
                    for x in range(data):
                        self.output(x)

                    n=input("\nApakah anda mau keluar dari aplikasi [Y] : ").upper()
                    if n=="Y":
                        self.forcestop = True#variabel untuk keluar dari program
                        raise#code ini keluar dengan return error, namun jika code ini didalam try, code ini akan membuat program langsung mengeksekusi exceptnya
                    break
                except:
                    if self.forcestop==True:
                        sys.exit()#karena code ini diluar try, maka code ini langsung membuat program keluar dengan return error 0

if __name__ == '__main__':
    #pemanggilan class
    z = zakat()
    z.home()

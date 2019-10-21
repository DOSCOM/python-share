name = input("masukkan nama pembeli = ")
alamat= input("Alamat = ")
NoTelp = input("No Telp = ")
print("\n")
print("=================INFORMASI HARGA MOBIL DEALER JAYA ABADI===============")
print("Pilih Jenis Mobil :")
print("\t 1.Daihatsu ")
print("\t 2.Honda ")
print("\t 3.Toyota ")
print("")
pilihan = int(input("Pilih jenis mobil yang ingin dibeli : "))
print("")

if (pilihan==1):
        print("<<<<<<<< Macam macam mobil pada Daihatsu >>>>>>>>>")
        print("\ta.Grand New Xenia")
        print("\tb.All New Terios")
        print("\tc.New Ayla")
        Pilih1 = input("Mana yang ingin anda pilih ?? = ")

        if(Pilih1 == "a"):
                print("Harga mobil Grand New Xenia adalah 183 juta ")
        elif(Pilih1== "b"):
               print("Harga mobil All New Terios adalah 215 juta")
        elif(Pilih1== "c"):
                print("Harga mobil New Ayla adalah 110 juta")
        else:
    
                print("Tidak terdefinisi")
elif (pilihan==2):
        print("<<<<<<<< Macam macam mobil pada Honda >>>>>>>>>")
        print("\ta.Honda Brio Satya S")
        print("\tb.Honda Jazz ")
        print("\tb.Honda Mobilio ")
        pilih2 = input("Mana yang ingin anda pilih??")

        if(pilih2=="a"):
                print("Harga mobil HOnda Brio Satya S adalah 131 juta")
        elif(pilih2=="b"):
                print("Harga mobil Honda Jazz adalah 232 juta")
        elif(pilih2=="c"):
                print("Harga mobil Honda mobilio adalah 189 juta")
        else:
                print("Tidak terdefinisi")
elif (pilihan==3):
        print("<<<<<<<< Macam macam mobil pada Toyota>>>>>>>>?")
        print("\ta.Alphard")
        print("\tb.Camry")
        print("\tc.Fortuner")

        pilih3 = input("Mana yang ingin anda pilih??")

        if (pilih3=="a"):
                print("Harga mobil Alphard adalah 870 juta")
        elif (pilih3=="b"):
                print("Harga mobil Camry adalah 560 Juta")
        elif (pilih3=="c"):
                print("Harga mobil Fortuner adalah 492 Juta")

nama_HP = input("Masukkan nama HP =")
harga =  int(input("berapa harganya ??? ="))

if (harga > 4000000 ):
    print("HP SPEK HIGH-END")
elif (harga>=2000000 and harga<=4000000):
    print("HP SPEK HIGH-MID")
elif (harga>=100000) and (harga<2000000):
    print("HP SPEK LOW-END")
else:
    print("POTATO PHONE")
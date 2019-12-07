outfit={
    #kay : value
    "kepala":"topi",
    "badan":"baju",
    "kaki":"celana"
}
print(outfit)

outfit2=dict(
    kepala="topi",
    badan="baju",
    kaki=dict(
        atas="celana",
        bawah="sepatu"
    )
)
# #Metode untuk mengakses dictionary
# print(outfit2["kaki"]["bawah"])
# #get
# print(outfit2.get("kepala"))

# for key in outfit2:
#     print(outfit2[key])

# for key,value in outfit2.items():
#     print("%s:%s"%(key,value))

# outfit2["kepala"]="bandana"
# for key,value in outfit2.items():
#     print("%s:%s"%(key,value))

# #menghapus sebuah dictionary
# #pop("key")
# outfit2.pop("kepala")
# print(outfit2)
# #del nama_dic["key"]
# del outfit2["badan"]
# print(outfit2)
##Update semua data
ktp = {
        "Nama":"Mochamad Fatany Rasis",
        "Klmpk":"",
        "Nim":"A11.2018.11123"
    }
user.update(
    {
        "Nama": "Manuel Setyo",
        "Klmpk":"A11.4307",
        "Nim":"A11.2018.11124"
    }
)
#Output biasa
print("Nama saya sekarang adalah",user.get("Nama"))
for key,value in user.items():
    print("%s:%s"%(key,value))

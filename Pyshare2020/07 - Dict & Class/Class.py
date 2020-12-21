#-----------------------------------------------
# kucing = {
# 	"warnaBulu" : ["Putih","Orange"],
# 	"jumlahKaki" : "Empat",
# 	"beratBadan" : 300
# }
# kucing["beratBadan"] = 500 #Mengubah isi dict
# kucing["umur"] = 0.6 #Menambahkan isi dict

# print(kucing) #Mencetak seluruh dict

# print(kucing["warnaBulu"])
# print(kucing["jumlahKaki"])
# print(kucing["beratBadan"])
# print(kucing["umur"])










#-----------------------------------------------
# class kucing:
# 	#Magic method untuk mendeklarasi attribut pada class
# 	def __init__(self): 
# 		self.warnaBulu = ["Putih","Orange"]
# 		self.jumlahKaki = "Empat"
# 		self.beratBadan = 300
# kucingku = kucing() 
# #Mendeklarasi tipe data buatan(tipe data abstract)
# #kucingku adalah variabel yang bertipe data abstract
# kucingku.beratBadan = 500 
# kucingku.umur = 0.6
# #Mengubah isi attribut class
# # setattr(kucingku, 'umur', 0.6) 
# #Menambahkan isi attribut class
# print(kucingku)
# print(kucingku.warnaBulu)
# print(kucingku.jumlahKaki)
# print(kucingku.beratBadan)
# print(kucingku.umur)









#-----------------------------------------------
# class kucing:
# 	def __init__(self): 
# 		self.warnaBulu = ["Putih","Orange"]
# 		self.jumlahKaki = "Empat"
# 		self.beratBadan = 500
# 		self.umur = 0.6
# 	def berlari(self,x):
# 		return "Kucing sedang berlari"+str(x)
# 	def bernafas(self):
# 		print("Kucing sedang bernafas")
# kucingku = kucing()
# print(kucingku)
# print(kucingku.berlari(10))
# kucingku.bernafas()









#-----------------------------------------------
# class hewan:
# 	def makan(self):
# 		print("Sedang makan")
# 	def minum(self):
# 		print("Sedang minum")

# class kucing(hewan):
# 	def __init__(self): 
# 		self.warnaBulu = ["Putih","Orange"]
# 		self.jumlahKaki = "Empat"
# 		self.beratBadan = 500
# 		self.umur = 0.6
# 	def berlari(self):
# 		return "Kucing sedang berlari"
# 	def bernafas(self):
# 		print("Kucing sedang bernafas")

# kucingku = kucing()
# kucingku.makan()
# kucingku.minum()


# class hewan:
# 	def bernafas(self):
# 		print("Sedang bernafas")

# class darat(hewan):
# 	def makan(self):
# 		print("Sedang makan")
# 	def minum(self):
# 		print("Sedang minum")

# class kucing(darat):
# 	def mencakar(self):
# 		print("Sedang nyakar")

# class ayam(darat):
# 	def berenang(self):
# 		print("Sedang berenang")

# ayamku = ayam()
# ayamku.bernafas()
# ayamku.makan()


class inte:
	def __init__(self,x):
		self.x = x
	def __add__(self,x):
		return self.x+x
a = inte(4)
print(a+5)
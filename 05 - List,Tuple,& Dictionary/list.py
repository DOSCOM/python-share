# #metode penghapusan pada list
# list=[1,2,3,4,5,6]
# #metode pop
# list.pop()
# print(list)
# #metode remove
# list.remove(2)
# print(list)
# #metode del
# del list[2]
# print(list)
# #metode clear
# list.clear()
# print(list)
#metode pemotongan pada list
# list=[1,2,3,4,5]
# print(list[1:5])
# print(list[:5])
# print(list[1:])
# print(list[:-1])
# print(list[-3:-1])
# makan =[]
# stop = False
# i = 0

# #Mengisi makanan
# while (not stop):
# 	makan_fav = input("Inputkan Makanan Favoritmu yang ke -{}:".format(i+1))
# 	makan.append(makan_fav)

# 	#increment i
# 	i+= 1

# 	tanya = input("Mau input lagi ?(y/t)")
# 	if(tanya == "t" or tanya=="T"):
# 		stop = True


# print ("Kamu Memiliki {} Makanan Favorit".format(len(makan)))
# for makanan in makan:
# 	print(" - {}".format(makanan))
# angka1=[1,2,3,4]
# angka2=[5,6,7,8]
# # print(angka1+angka2)
# kali=2
# # print(angka1*kali)
# print(angka1*4)

angka=[
    [1,2,3,4],
    [2,3,10,5],
    [3,4,5,6],
    [3,2,4,7]
]
# for i in range(len(angka)):
#     for j in range(len(angka[i])):
#         print(angka[i][j],end=" ")
#     print()
# #baris
# print(angka[1])
# #kolom
# for i in range(len(angka)):
#     print(angka[i][2])


# max = 0
# for i in range(len(angka)):
#     max_baris=0
#     for j in range(len(angka)):
#         print(angka[i][j], end=" ")
#         if angka[i][j]>max_baris:
#             max_baris=angka[i][j]
#     print(" => ", max_baris)
#     if max_baris>max:
#         max=max_baris
# print(max)

print(max(max(larik) for larik in angka))
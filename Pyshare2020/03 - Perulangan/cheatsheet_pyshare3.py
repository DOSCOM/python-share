#CHEATSHEET PYSHARE PERTEMUAN 3 - LOOPING

#ketimbang kamu print 5x mending pake looping
# print("DOSCOM")
# print("DOSCOM")
# print("DOSCOM")
# print("DOSCOM")
# print("DOSCOM")

# for i in range(5):                  #default for | batas awal == 0 | lompatan == 1
#     print("DOSCOM")

# i = 0
# while i<5:                          #membutuhkan parameter bernilai true jika false maka tidak jalan
#     print("DOSCOM")
#     i+=1

# var = "DOSCOM"
#penulisan 1
# for i in range(len(var)):            #kalo ada property len() akan membuat index bernilai integer
#     print(var[i])                    #mencetak setiap string
#     print(i)                         #mencetak index berupa angka
#     print(var)                       #mencetak string

#penulisan 2
# for i in var:                          #index bernilai string variabel
#     print(i, end=" ")                  #default output perulangan selalu vertikal | end= " "  akan membuat output secara horizontal

# i = len(var)
# while i in range(len(var)):            #tidak akan jalan karena while membutuhkan parameter true
#     print("DOSCOM")
#     i-=1

# while 0<i:
#     print(var)
#     i-=1

# for i in range(1,6):                    #batas akhir == n-1 untuk output
#     print("perulangan ke-",i)
#     for j in range(6):
#         print(var[j])
    
# i = 1
# while i<5:
#     print("BAB ke-",i)
#     i+=1
#     j=1
#     while j<4:
#         print("SUB BAB ke-",j)
#         j+=1

# param = True
# while param:
#     inp = int(input("Masukkan batas: "))
#     for i in range(inp):
#         inp1 = input("tekan y untuk keluar : ")
#         if inp1 == "y":
#             break

#SOAL 1 - PRIME
# print("ini adalah program bilangan prima dengan batas 20")
# batas = int(input("Masukkan batas: "))
# for num in range(0,batas+1):
#     if num > 1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#         else:
#             print(num,end=" ")

#SOAL 2 - BINARY TRIANGLE
# print("Ini adalah program segitiga biner dengan bentuk segitiga")
# for i in range(0,10,1):
#     for j in range(0,i):
#         if j % 2 == 0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()
# for x in range(10,0,-1):
#     for y in range(0,x):
#         if y % 2 == 0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

#SOAL 3 - SIMPLY LOGIN SYSTEM WITH PYTHON
# username = input("Username: ")
# if username == 'PeinAkatsuki':
#     cond = True
#     while cond:
#         pwd=input("Masukkan Password: ")
#         if pwd == "1sampai10":
#             print("Anda berhasil Login")
#             cond = False
#         else:
#             print("Password salah")
# else:
#     print("Siapa anda?")
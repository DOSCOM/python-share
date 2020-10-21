nilai = [
    [8, 4, 4, 1],
    [1, 5, 4, 6],
    [0, 9, 8, 2],
    [3, 2, 7, 5]
]

# [8, 4, 4, 1] => 8
# [1, 5, 4, 6] => 6
# [0, 9, 8, 2] => 9
# [3, 2, 7, 5] => 7
#                 9














tampung = [0] * len(nilai)

for i in range(len(nilai)):
    awal = nilai[i][0]
    for j in range(len(nilai[i])):
        if nilai[i][j] > awal:
            awal = nilai[i][j]
    tampung[i] = awal

hasil = tampung[0]
for i in range(len(tampung)):
    if tampung[i] > hasil:
        hasil = tampung[i]
print(hasil)

# print(max(max(larik) for larik in nilai))

# maks = 0
# for i in range(len(nilai)):
#     maksPerBaris = 0
#     for j in range(len(nilai[i])):
#         if nilai[i][j] > maksPerBaris:
#             maksPerBaris = nilai[i][j]
#     if maksPerBaris > maks:
#             maks = maksPerBaris

# print(maks)
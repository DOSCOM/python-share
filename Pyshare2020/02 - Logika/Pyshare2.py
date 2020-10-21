#ini file py-nya materi percabangan if yang inputan,format dan fungsi dimas.
def ujian():
    question = input("apakah kamu lulus ujian? [ya/tidak]: ")
    if question == "tidak":
        print("Ikut remidi")
    else :
        print("Naik kelas")
def grade():
        #file grade_nilai.py
    nilai = int(input("masukan nilai kamu: "))
    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B+"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 60:
        grade = "C+"
    elif nilai >= 50:
        grade = "C"
    elif nilai > 40:
        grade = "D"
    else:
        grade = "E"
    print("Grade: %s" % grade)  # (%) adlah format untuk memanggil nilai.
def filter_kata():
    kata = input("masukan kalimat: ")
    if "anjing" in kata :
        print("dosa kamuuu")
    elif "anjay" in kata:
        print("dosa kamuuu")
    elif "goblok" in kata :
        print("dosa kamuuu")
    elif "diancok" in kata :
        print("dosa kamuuu")
    else:
        print("ga ada")
def umur():
    umur = int(input("masukan umur kalian: "))
    if umur < 18:
        if umur < 8 :
            print("anak-anak")
        elif umur < 13:
            print("semi remaja")
        else:
            print("mulai nakal")
    elif umur >= 18 and umur < 70:
        if umur < 30 :
            print("dewasa")
        elif umur < 40:
            print("mulai menua")
        else:
            print("mulai giat beribadah")
    else:
        print("sudah dialam lain")

if __name__ == "__main__":
    ujian()
    grade()
    filter_kata()
    umur()
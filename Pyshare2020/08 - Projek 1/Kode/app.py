import database

MENU_PROMPT = """ ***Hai.. Welcome***
Silakan pilih menu
[1] Tambah Data Mahasiswa
[2] Liat Daftar Semua Mahasiswa
[3] Cari Mahasiswa berdasarkan nama
[4] Delete Data

Pilihan anda :
"""


def menu():
    connection = database.connect()
    database.buat_table(connection)
    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            nama = input('Masukan Nama Mahasiswa : ')
            usia = input('Berapa Usia Kamu ? : ')
            kampus = input('Kamu Dari Instansi Mana : ')

            database.tambah_data_mhs(connection, nama, usia, kampus)
        elif user_input == "2":
            mhss = database.get_all_mhs(connection)
            for mhs in mhss:
                print(mhs)
        elif user_input == "3":
            nama = input("Mau Cari dari instansi mana ?")
            mhss = database.get_mhs_by_nama(connection, nama)

            for mhs in mhss:
                print(f"{mhs[0]} Namaku {mhs[1]} Usiaku {mhs[2]} Tahun, Asal {mhs[3]}")
        elif user_input == "4":
            iden = input('Id berapa yang mau dihapus ?')
            database.delete_mhs(connection, iden)

            # print(f"The best teknik untuk {nama} adalah {best[2]}")
        else:
            print('Salah input, silakan coba lagi')

if __name__ == "__main__":
    menu()

import sqlite3

CREATE_MHS = "CREATE TABLE IF NOT EXISTS mhs (id INTEGER PRIMARY KEY, nama TEXT, usia TEXT, kampus TEXT);"

INSERT_MHS = "INSERT INTO mhs (nama,usia,kampus) VALUES (?,?,?);"

GET_ALL_MHS = "SELECT * FROM mhs;"

GET_MHS_BY_NAMA = "SELECT * FROM mhs WHERE kampus = ?;"

DELETE_MHS = "DELETE FROM mhs WHERE id = ?;"
# GET_BEST_TEKNIK = """
# SELECT * FROM kopi 
# WHERE nama = ?
# ORDER BY rating DESC
# LIMIT 1;
# """
# CRUD -> Create Read Update Delete


def connect():
    return sqlite3.connect("data.db")


def buat_table(connection):
    with connection:
        connection.execute(CREATE_MHS)


def tambah_data_mhs(connection, nama, usia, kampus):
    with connection:
        connection.execute(INSERT_MHS, (nama, usia, kampus))


def get_all_mhs(connection):
    with connection:
        return connection.execute(GET_ALL_MHS).fetchall()


def get_mhs_by_nama(connection, nama):
    with connection:
        return connection.execute(GET_MHS_BY_NAMA, (nama, )).fetchall()

def delete_mhs(connection, id):
    with connection:
        return connection.execute(DELETE_MHS, (id, ))


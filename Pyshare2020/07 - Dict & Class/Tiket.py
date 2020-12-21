from pysharedoscom import table,menu,cls #pip install pysharedoscom

# table(dic,index=True)
daftarFilm = ["Spongebob","Avengers","Boruto Movie","The Maze Runner"]
hasil = menu(daftarFilm,index=True,title="Film Bioskop",desc="Note : Gunakan arrow up/down",char="%",loc="rl",align=False)
dic = {
	"Judul" : daftarFilm,
	"Harga" : [50000,40000,60000,70000]
}

table(dic,index=True)
help(table)
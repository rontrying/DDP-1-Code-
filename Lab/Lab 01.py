# import library python yang digunakan
import math

#meminta input
nama=input("Nama: ") #input() auto type string
panjang=float(input("Panjang persegi nametag (cm): ")) #float untuk mengantisipasi input int atau float
panjang_trapesium=float(input("Panjang trapesium nametag (cm): ")) #float untuk mengantisipasi input int atau float
jumlah_nametag=int(input("Banyak nametag: ")) #int karena input dijamin valid

#menghitung luas setiap bangun nametag
luas_persegi=panjang**2 #sisi kuadrat
luas_lingkaran=0.5*math.pi*((panjang/2)**2) #1/2 x pi x r kuadrat
luas_segitiga=0.5*panjang*panjang #1/2 x alas x tinggi
luas_trapesium=0.5*(panjang+panjang_trapesium)*panjang #1/2(jumlah sisi sejajar)*tinggi

#menghitung luas nametag
luas_nametag=luas_persegi+luas_lingkaran+luas_segitiga+luas_trapesium
total_luas=luas_nametag*jumlah_nametag

#menghitung harga
harga=total_luas*0.40

#menampilkan output
print(f"Halo, {nama}! Berikut informasi terkait nametag kamu: ")
print() #memberi enter
print(f"Luas 1 nametag: {round(luas_nametag, 2)} cm^2")
print(f"Luas total nametag: {round(total_luas, 2)} cm^2")   
print(f"Uang yang diperlukan: Rp{math.ceil(harga/1000)*1000}")

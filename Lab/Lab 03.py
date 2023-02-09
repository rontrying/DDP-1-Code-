# memberi pesan selamat datang
print("Selamat Datang di Bunker Hacker!\n")

# menentukan variabel awal
basis=8 # basis fungsinya sebagai pembagi dan untuk menentukan sisa dalam konversi
octa="" # octa hasil konversi desimal ke basis 8 dalam bentuk string

# meminta input
jumlah_konversi=int(input("Masukkan berapa kali konversi yang ingin dilakukan: ")) # input dijamin int
print() # memberi enter

# loop sebanyak jumlah konversi (inklusif(dari 0),ekskusif)
for kasus in range(1,jumlah_konversi+1):

    # meminta input angka basis desimal
    angka_desimal=int(input(f"Masukkan angka ke-{kasus} yang ingin dikonversikan (dalam desimal): ")) # pasti lebih besar dari 0

    # iterasi hingga angkanya bernilai 0
    while angka_desimal > 0:
        octa=str(angka_desimal%basis)+octa #algoritma mengisi string dari belakang string sehingga tidak perlu reverse string
        angka_desimal=angka_desimal//basis # angka di floor function setelah diambil sisanya kemudian di assign

    # menampilkan output hasil
    print(f"Hasil konversi desimal ke basis 8 : {octa}\n")

    # octa diassign ke "" agar siap menerima sisa bagi kembali untuk kasus selanjutnya
    octa=""

#menampilkan output pesan terima kasih
print("Terima kasih telah menggunakan Bunker Hacker! ")

# Acknowledgements
# PPT Strings (Part 1) - DDP 1 Gasal 2021/2022
# PPT Repetition - DDP 1 Gasal 2022/2023
# https://www.w3schools.com/python/python_strings_concatenate.asp
# https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html
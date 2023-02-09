# print selamat datang
print("""Selamat datang di program Mengenal Angkatan!
===========================================
Masukkan identitas mahasiswa:""")

database={}
data=""
perintah=""
# mengisi dictionary dengan keys bulan dan value datanya yang mau dicari
while data != "STOP":
    data=input()
    if data != "STOP":
        data=data.split()
        if data[4] not in database:
            database[data[4]]=(data,)
        else:
            database[data[4]]+=(data,)
print()

#iterasi mencari yang sama bulannya
while True:
    # pakai set karena nama dan npm tidak boleh berulang di output
    set_nama=set()
    set_npm=set()
    perintah=input("Cari mahasiswa berdasarkan bulan: ")
    if perintah == "STOP":
        break
    for data in database:
        if data == perintah:
            for identitas in database[data]:
                set_nama.add(identitas[0].lower()) # lower karena case insensitive
                set_npm.add(identitas[1])
    # memberi output
    if len(set_nama) != 0 and len(set_npm) != 0:
        print(f"""================= Hasil ================
Terdapat {len(set_nama)} nama yang lahir di bulan {perintah}:""")
        for nama in set_nama:
            print(f"- {nama.capitalize()}")
        print(f"\nTerdapat {len(set_npm)} NPM yang lahir di bulan {perintah}:")
        for npm in set_npm:
            print(f"- {npm}")
    else:
        print(f"""================= Hasil ================
Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {perintah}.""")
    print()
print()
# print terima kasih
print("Terima kasih telah menggunakan program ini, semangat PMB-nya!")
# menunjukan format selamat datang
print("""Selamat mencoba Program Pemeriksa Nilai Dek Depe!
=================================================

""")
print("Masukkan kunci jawaban: ")

#memberi nilai variabel
jawaban_benar=[]
jawaban_siswa=[]
counter=0
jumlah_soal_benar=0
kunci=""

# meminta input dan mengisi jawaban benar
while kunci != "STOP":
    kunci=input()
    jawaban_benar.append(kunci)
    counter+=1
print("Masukan jawaban kamu: ")

# meminta input dan mengisi jawaban siswa
for i in range(counter-1):
    jawaban=input()
    jawaban_siswa.append(jawaban)

# menghilangkan kata stop dari list jawaban
jawaban_benar.remove("STOP")

# memeriksa kesamaan jawaban
for i in range(len(jawaban_benar)):
    if jawaban_benar[i] == jawaban_siswa[i]:
        jumlah_soal_benar+=1
print()

# menghitung nilai
nilai=int((jumlah_soal_benar/len(jawaban_benar))*100)

# menampilkan output sesuai nilai
if nilai >= 85:
    print("Selamat :D")
elif 55 <= nilai <= 85:
    print("Semangat :)")
else:
    print("nt")

# menampilkan output
print(f"Total jawaban benar adalah {jumlah_soal_benar} dari {len(jawaban_benar)} soal")
print(f"Nilai yang kamu peroleh adalah {nilai}")
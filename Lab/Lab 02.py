# memberi pesan selamat datang
print("Selamat datang ke Dek Depe Holiday Tracker!\n")

#memberi nilai variabel awal
skala_kebahagian=0
total_rating=0
rating_terbesar=0

#meminta input banyak tempat
banyak_tempat=int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
print()

#menghandle nilai 0 dan minus
while banyak_tempat<=0:
    print("Input tidak valid. Silahkan masukkan input kembali!")
    banyak_tempat=int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
    print()

#for loop sesuai banyak tempat
for i in range(1,banyak_tempat+1):
    # meminta nilai tempat dan rating sesuai banyak tempat
    tempat=input(f"Perjalanan {i}: ")
    rating=int(input(f"Rating perjalanan kamu ke {tempat} (indeks 1-10): "))
    print()

    #iterasi agar menemukan nilai terbesar dan tempat paling berkesan
    if rating>=rating_terbesar:
        rating_terbesar=rating
        tempat_terkesan=tempat

    #menghitung total rating dan skala kebahagiaan
    total_rating+=rating
skala_kebahagian=total_rating/banyak_tempat

# mengoutput summary
print("---Summary---")
print(f"Perjalanan paling mengesankan adalah ketika pergi ke {tempat_terkesan}.")
print(f"Skala kebahagiaan Dek Depe adalah {skala_kebahagian:.2f}")

# if elif skala kebahagiaan
if 8 <= skala_kebahagian <= 10:
    print("Dek Depe bahagia karena pengalamannya menyenangkan.")
elif 5 <= skala_kebahagian <=8:
    print("Dek Depe senang karena pengalamannya cukup baik.")
elif skala_kebahagian<5:
    print("Dek Depe sedih karena pengalamannya buruk.")

#mengeluarkan output
print("\nTerimakasih telah menggunakan Dek Depe Holiday Tracker!")
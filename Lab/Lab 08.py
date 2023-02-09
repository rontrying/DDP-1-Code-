# memberi output
print("Masukan data hubungan")

#nilai variabel awal
perintah=""
list_kenalan=[]

# mengisi data
while True:
    perintah=input()
    if perintah == "SELESAI":
        break
    list_kenalan.append(perintah.split())

nama_awal=input("Masukkan nama awal: ")
nama_tujuan=input("Masukkan nama tujuan: ")

#definisi fungsi 
def kenalan (list_kenalan, nama_awal, nama_tujuan):
    for data in list_kenalan:
        if nama_awal == data[0] and nama_tujuan == data[1]:
            return float(data[2])
        elif nama_awal == data[0]:
            try:
                return float(data[2]) + kenalan(list_kenalan, data[1], nama_tujuan)
            except:
                return "a"
        else:
            continue
    return "a"

#if else keterangan hubungan dan keadaan
if type(kenalan(list_kenalan, nama_awal, nama_tujuan)) == str:
    print(f"Tidak ada hubungan antara {nama_awal} dan {nama_tujuan}.")
elif (kenalan(list_kenalan, nama_awal, nama_tujuan)*10) > 1000:
    print(f"Jarak total: {(kenalan(list_kenalan, nama_awal, nama_tujuan)*10):.0f}")
    print(f"{nama_awal} dan {nama_tujuan} tidak saling kenal.")
elif 100 <=(kenalan(list_kenalan, nama_awal, nama_tujuan)*10) <= 1000:
    print(f"Jarak total: {(kenalan(list_kenalan, nama_awal, nama_tujuan)*10):.0f}")
    print(f"{nama_awal} dan {nama_tujuan} mungkin saling kenal.")
else:
    print(f"Jarak total: {(kenalan(list_kenalan, nama_awal, nama_tujuan)*10):.0f}")
    print(f"{nama_awal} dan {nama_tujuan} mungkin saling kenal.")


# pesan selamat datang
print("Selamat datang di Pacil Mart! \n")

# try untuk error file not found
try:
    file_input=open(input("Masukkan nama file input: "),"r")
    #untuk file yang kosong
    baris1=file_input.readline()
    if baris1 == "":
        print("")
    else:
        print("Berikut adalah daftar belanjaanmu: \n\nNama Barang |  Jumlah| Kembalian\n"+"-"*32)
        belanja=baris1.split()
        jumlah=int(belanja[1])//int(belanja[2])
        kembalian=int(belanja[1])-(int(belanja[2])*jumlah)
        # print output
        print(f"{belanja[0]}".ljust(12," ")+"|"+f"{jumlah}".rjust(8," ")+"| "+f"{kembalian}".rjust(9," "))
        for i in file_input.readlines():
            belanja=i.split()
            jumlah=int(belanja[1])//int(belanja[2])
            kembalian=int(belanja[1])-(int(belanja[2])*jumlah)
            # print output
            print(f"{belanja[0]}".ljust(12," ")+"|"+f"{jumlah}".rjust(8," ")+"| "+f"{kembalian}".rjust(9," "))
        # print terima kasih
        print("\nTerima kasih sudah belanja di Pacil Mart!")
# error file tidak ada
except FileNotFoundError:
    print("File tidak tersedia")
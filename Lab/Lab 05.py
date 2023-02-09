# import library python
import math

# fungsi menghitung volume balok
def volume_balok ():
    """fungsi digunakan untuk meminta input panjang, lebar & tinggi balok dan mengembalikan nilainya berupa luasnya"""
    # meminta input
    panjang=float(input("Masukkan panjang balok : "))
    lebar=float(input("Masukkan lebar balok : "))
    tinggi=float(input("Masukkan tinggi balok : "))
    vol_balok=panjang*lebar*tinggi
    return vol_balok

# fungsi menghitung volume kerucut
def volume_kerucut ():
    """fungsi digunakan untuk meminta input jari-jari & tinggi kerucut dan mengembalikan nilainya berupa volumenya"""
    # meminta input
    jari_jari=float(input("Masukkan jari-jari kerucut : "))
    tinggi=float(input("Masukkan tinggi kerucut : "))
    luas=(1/3)*math.pi*(jari_jari**2)*tinggi
    return luas

# output selamat datang
print("Selamat datang di Depot Minuman Dek Depe!\n==========================================")

# nilai variabel awal
stop=False
total_volume=0

# while true minta input sampai stop true
while not stop:
    bentuk=input("Masukkan bentuk galon yang diinginkan (STOP untuk berhenti): ")
    if bentuk == "BALOK":
        total_volume+=volume_balok()
    elif bentuk == "KERUCUT":
        total_volume+=volume_kerucut()
    elif bentuk == "STOP":
        stop=True
    else:
        print("Input tidak benar, masukkan kembali")
    print()

# menghitung total harga
total_harga=total_volume*700

#mengeluarkan output
print("====================================================")

if total_volume != 0: #jika input ada
    print(f"Total volume air yang dikeluarkan adalah : {total_volume:.2f}")
    print(f"Total harga yang harus dibayar adalah : Rp{total_harga:.2f}")
    print("====================================================")
    print("\nTerima kasih telah menggunakan Depot Air Minum Dek Depe")
else: # jika tidak ada input maka total volum pasti 0
    print("Anda tidak memasukkan input satupun :(")
    print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")
    print("====================================================")


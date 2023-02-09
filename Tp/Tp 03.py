# asumsi
# 1. jika nama pelanggan yang buat pesanan sama maka akan dikenali sebagai orang berbeda dengan identitas nomor meja pada dict
# 2. jika poin nomor 1 terjadi pada saat selesai menggunakan meja maka nama receipt akan ditambahkan nomor meja
# 3. jika pelanggan tidak memesan pada buat pesanan maka dianggap tidak membuat meja
# 4. jika pelanggan menghapus semua pesanan maka dianggap selesai menggunakan meja tanpa resi

import os
def validasi_file(nama_file:str) -> bool:
    """cek file dengan iterasi ke dictionary apakah sudah sesuai templete menu atau belum return False jika belum dan return True jika sudah"""
    checker_menu_txt={"sudah aman":(), "belum aman":()}
    with open(nama_file,"r") as file:
        for line in file.readlines():
            line=line.strip()
            if line.startswith("===") and line == line.upper(): #asumsi jenis menu harus huruf kapital dan boleh memiliki spasi
                checker_menu_txt["sudah aman"]+=(line,)
            elif len(line.split(";")) == 3: #cek format menu sudah benar kode;nama;harga
                checker_menu_txt["belum aman"]+=(line.split(";"),)
            else:
                return False
        if not validasi_menu(checker_menu_txt):
            return False
        return True

def validasi_angka (string:str,mode:str="normal") :
    """validasi angka apakah sudah dalam format yang benar atau belum return False jika belum dan return int(angka) jika sudah"""
    try :
        if mode == "normal":
            if int(string) <0:
                return False
        elif mode =="0":
            if int(string) <= 0:
                return False
    except:
        return False
    return int(string)

def validasi_menu (menu:dict) -> bool:
    """fungsi buat validasi bahwa nama menu dan kode menu harus unik return True jika benar dan return False jika salah"""
    list_nama_unik=[]
    set_nama_unik=set()
    for data in menu["belum aman"]:
        list_nama_unik+=data[:-1]
        set_nama_unik.add(data[0])
        set_nama_unik.add(data[1])
        if not validasi_angka(data[2]):
            return False
    if len(list_nama_unik) != len(set_nama_unik):
        return False
    return True

def ribuan (harga:str) -> str:
    """fungsi untuk mengubah bentuk integer menjadi string rupiah agar mudah dibaca pelanggan"""
    counter=0
    harga_rupiah=""
    if len(harga) <= 3:
        return harga
    for angka in harga[::-1]:
        counter+=1
        harga_rupiah=angka+harga_rupiah
        if counter % 3 == 0 and angka != harga[0]:
            harga_rupiah="."+harga_rupiah
    return harga_rupiah

def pencari_menu (list_menu:list, menu:str):
    """menerima list menu dan nama atau kode menu kemudian mereturn [nama_menu,harganya,kode]"""
    for data_menu in list_menu:
        if menu in data_menu:
            return [data_menu[1],int(data_menu[2]),data_menu[0]]
    return False

def validasi_nomor_meja (dict_meja,nomor_meja):
    try:
        if int(nomor_meja) not in dict_meja:
            return False
    except:
        return False
    return True

def validasi_pesanan(dict_pesanan,ubahan,meja,list_menu):
    """mengecek apakah menu tersebut dipesan atau tidak return True jika dipesan dan False jika tidak"""
    for menu in dict_pesanan[meja]["menu, harga, jumlah"]:
        if pencari_menu(list_menu,ubahan)[0] in menu:
            return True
    return False

# memberi nilai variabel struktur data yang digunakan
dict_menu={}
list_menu=[]
dict_pesanan={}
dict_meja={}

#mengecek menu.txt
with open("menu.txt","r") as file:
    for line in file.readlines():
        line=line.strip()
        if line[0] == "=":
            key=line.replace("===","")
            if key not in dict_menu:
                dict_menu[key]=()
                continue
        dict_menu[key]+=(line.split(";"),)
        list_menu.append(line.split(";"))

while True:
    if not validasi_file("menu.txt"):
        print("Daftar menu tidak valid, cek kembali menu.txt!")
        break
    # memberi output
    print("Selamat datang di Kafe Daun Daun Pacilkom")

    perintah=input("Apa yang ingin Anda lakukan? ")
    # menghandle menu buat pesanan
    if perintah == "BUAT PESANAN":
        if len(dict_meja) == 10:
            print("Mohon maaf meja sudah penuh, silakan kembali nanti.")
        else:
            nama=input("Siapa nama Anda? ")
            for i in range(1,11): #mencari meja yang kosong
                if i not in dict_meja:
                    dict_meja[i]=nama
                    break
            dict_pesanan[i]={"menu, harga, jumlah":[], "harga total":0}
            print("\nBerikut ini adalah menu yang kami sediakan:")
            for data in dict_menu:
                print(f"{data}:")
                for menu in dict_menu[data]:
                    print(f"{menu[0]} {menu[1]}, Rp{ribuan(menu[2])}")
        
            print()
            while True:# mengisi dict pesanan dan meja
                menu=input("Masukkan menu yang ingin Anda pesan: ")
                if menu == "SELESAI":
                    print()
                    break
                elif not pencari_menu(list_menu,menu):
                    print(f"Menu {menu} tidak ditemukan. ",end="")
                else:
                    if [pencari_menu(list_menu, menu)[0],pencari_menu(list_menu, menu)[1],1] not in dict_pesanan[i]["menu, harga, jumlah"]:
                        dict_pesanan[i]["menu, harga, jumlah"]+=[[pencari_menu(list_menu, menu)[0],pencari_menu(list_menu, menu)[1],1]]
                    else:
                        for data_menu in dict_pesanan[i]["menu, harga, jumlah"]:
                            if data_menu == [pencari_menu(list_menu, menu)[0],pencari_menu(list_menu, menu)[1],1]:
                                data_menu[2]+=1
                                data_menu[1]+=pencari_menu(list_menu,menu)[1]
                    dict_pesanan[i]["harga total"]+=pencari_menu(list_menu, menu)[1]
                    print(f"Berhasil memesan {pencari_menu(list_menu, menu)[0]}. ",end="")

            if dict_pesanan[i]["harga total"] == 0:
                del dict_pesanan[i]
                del dict_meja[i]
                print("\n---")
                continue
            # memberi output
            print(f"Berikut adalah pesanan terbaru Anda:")
            for data_menu in dict_pesanan[i]["menu, harga, jumlah"]:
                print(f"{data_menu[0]} {data_menu[2]} buah, total Rp{ribuan(str(data_menu[1]))}")

            total_harga=dict_pesanan[i]["harga total"]
            print(f"\nTotal pesanan: Rp{ribuan(str(total_harga))}")
            print(f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {i}. Terima kasih.")

    # handle menu ubah pesanan
    elif perintah == "UBAH PESANAN":
        nomor_meja=input("Nomor meja berapa? ")
        if not validasi_nomor_meja(dict_meja,nomor_meja):
            print("Nomor meja kosong atau tidak sesuai!")
            print("\n---")
            continue
        print("\nBerikut ini adalah menu yang kami sediakan:")
        for data in dict_menu:
            print(f"{data}:")
            for menu in dict_menu[data]:
                print(f"{menu[0]} {menu[1]}, Rp{ribuan(menu[2])}")
        
        print(f"\nBerikut adalah pesanan Anda:")
        for data_menu in dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"]:
            print(f"{data_menu[0]} {data_menu[2]} buah, total {ribuan(str(data_menu[1]))}")
        
        print()
        while True: # mengubah data sesuai input user
            ubah=input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            if ubah == "SELESAI":
                print()
                break

            elif ubah == "GANTI JUMLAH":
                menu_ganti=input("Menu apa yang ingin Anda ganti jumlahnya: ")
                if not pencari_menu(list_menu,menu_ganti):
                    print(f"Menu {menu_ganti} tidak ditemukan!",end=" ")
                    continue
                elif not validasi_pesanan(dict_pesanan,menu_ganti,int(nomor_meja),list_menu):
                    print(f"Menu {menu_ganti} tidak Anda pesan sebelumnya.",end=" ")
                    continue
                else:
                    jumlah_ganti=input("Masukkan jumlah pesanan yang baru: ")
                    if not validasi_angka(jumlah_ganti,"0"):
                        print("Jumlah harus bilangan positif!")
                        continue
                    jumlah_ganti=validasi_angka(jumlah_ganti,"0")
                    for data_menu in dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"]:
                            if pencari_menu(list_menu,menu_ganti)[0] in data_menu:
                                dict_pesanan[int(nomor_meja)]["harga total"]-=(pencari_menu(list_menu, menu_ganti)[1]*data_menu[2])
                                data_menu[2]=jumlah_ganti
                                data_menu[1]=(pencari_menu(list_menu,menu_ganti)[1]*jumlah_ganti)
                                dict_pesanan[int(nomor_meja)]["harga total"]+=(pencari_menu(list_menu, menu_ganti)[1]*data_menu[2])
                                break
                    print(f"Berhasil mengubah pesanan {pencari_menu(list_menu,menu_ganti)[0]} {jumlah_ganti} buah.",end=" ")
            # menghandle menu hapus
            elif ubah == "HAPUS":
                menu_hapus=input("Menu apa yang ingin Anda hapus dari pesanan: ")
                jumlah_hapus=0
                if not pencari_menu(list_menu,menu_hapus):
                    print(f"Menu {menu_hapus} tidak ditemukan!",end=" ")
                    continue
                elif not validasi_pesanan(dict_pesanan,menu_hapus,int(nomor_meja),list_menu):
                    print(f"Menu {menu_hapus} tidak Anda pesan sebelumnya.",end=" ")
                    continue
                else:
                    for data_menu in dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"]:
                            if pencari_menu(list_menu,menu_hapus)[0] in data_menu:
                                jumlah_hapus=data_menu[2]
                                dict_pesanan[int(nomor_meja)]["harga total"]-=(pencari_menu(list_menu, menu_hapus)[1]*data_menu[2])
                                dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"].remove(data_menu)
                    print(f"{jumlah_hapus} buah {pencari_menu(list_menu,menu_hapus)[0]} dihapus dari pesanan. ",end=" ")
                    if dict_pesanan[int(nomor_meja)]["harga total"] == 0:
                        del dict_pesanan[int(nomor_meja)]
                        del dict_meja[i]
                        print("menu terakhir dihapus, silakan buat pesanan kembali...") # asumsi menu terakhir dihapus dianggap tidak menggunakan meja
                        continue
            # menghandle menu tambah pesanan
            elif ubah == "TAMBAH PESANAN":
                menu_tambah=input("Menu apa yang ingin Anda pesan: ")
                if not pencari_menu(list_menu,menu_tambah):
                    print(f"Menu {menu_tambah} tidak ditemukan!",end=" ")
                    continue
                else:
                    if [pencari_menu(list_menu, menu_tambah)[0],pencari_menu(list_menu, menu_tambah)[1],1] not in dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"]:
                        dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"]+=[[pencari_menu(list_menu, menu_tambah)[0],pencari_menu(list_menu, menu_tambah)[1],1]]
                    else:
                        for data_menu in dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"]:
                            if data_menu == [pencari_menu(list_menu, menu_tambah)[0],pencari_menu(list_menu, menu_tambah)[1],1]:
                                data_menu[2]+=1
                                data_menu[1]+=pencari_menu(list_menu,menu_tambah)[1]
                    dict_pesanan[int(nomor_meja)]["harga total"]+=pencari_menu(list_menu, menu_tambah)[1]
                    print(f"Berhasil memesan {pencari_menu(list_menu, menu_tambah)[0]}. ",end="")
            
            else: # menghandle input user yang salah
                print("perintah tidak dikenali silakan masukan kembali...")
                continue
        # memberi output menu
        print(f"Berikut adalah pesanan Anda:")
        for data_menu in dict_pesanan[int(nomor_meja)]["menu, harga, jumlah"]:
            print(f"{data_menu[0]} {data_menu[2]} buah, total Rp{ribuan(str(data_menu[1]))}")

        total_harga=dict_pesanan[int(nomor_meja)]["harga total"]
        print(f"\nTotal pesanan: Rp{ribuan(str(total_harga))}")

    #menu selesai menggunakan meja
    elif perintah == "SELESAI MENGGUNAKAN MEJA":
        meja_selesai=input("Nomor meja berapa? ")
        if not validasi_nomor_meja(dict_meja,meja_selesai):
            print("Nomor meja kosong atau tidak sesuai!")
            print("\n---")
            continue
        else:
            nama=dict_meja[int(meja_selesai)]
            total_harga=dict_pesanan[int(meja_selesai)]["harga total"]
            nama_file=f"receipt_{nama}.txt"
            for (_,_,files) in os.walk(f"./", topdown=True):
                if len(files) != 0:
                    for file in files:
                        if file.find(".txt") != -1 and file == f"receipt_{nama}.txt": # mencari apakah sudah ada receipt sama atau belum
                            nama_file=f"receipt_{nama}_{meja_selesai}.txt"
            # membuka file resi
            with open(nama_file,"w") as resi:
                for menu in dict_pesanan[int(meja_selesai)]["menu, harga, jumlah"]:
                    print(f"{pencari_menu(list_menu,menu[0])[2]};{menu[0]};{menu[2]};{pencari_menu(list_menu,menu[0])[1]};{menu[1]}", file=resi)
                print(f"\nTotal {total_harga}", file=resi, end="")
            print(f"Pelanggan atas nama {nama} selesai menggunakan meja {meja_selesai}.")
            del dict_pesanan[int(meja_selesai)]
            del dict_meja[int(meja_selesai)]
    else:# menghandle input user
        print("perintah tidak dikenali silakan masukan kembali...")
    print("\n---")


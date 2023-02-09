# import modul
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as tkmsg

#asumsi
# 1. jika pelanggan memencet kembali pada saat memilih menu maka dianggap tidak jadi memesan dan meja kosong
# 2. jika pelanggan memencet ubah meja maka meja akan langsung terubah sehingga tombol kembali digunakan untuk memilih menu kembali

# definisikan class Menu, Meals dan drinks
class Menu:
    def __init__(self, kode_menu, nama_menu, harga):
        self.kode_menu = kode_menu
        self.nama_menu = nama_menu
        self.harga = int(harga)

class Meals(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan
        self.tingkat_kegurihan=tingkat_kegurihan


class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan
        self.tingkat_kemanisan=tingkat_kemanisan

class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan
        self.tingkat_keviralan=tingkat_keviralan

# landing page
class Main(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        button1 = tk.Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white")
        button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        button1.grid(row=0, column=0, padx=10, pady=40)
        button2.grid(row=1, column=0)
        self.master.protocol("WM_DELETE_WINDOW",self.kembali)
    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        SelesaiGunakanMeja(self.master)
    
    def kembali(self):
        for widget in self.master.winfo_children():
            if isinstance(widget,tk.Toplevel):
                widget.destroy()
        self.master.destroy()

# menu buat pesanan jika pelanggan mengklik lanjut maka akan masuk dalam menu pesanan
class BuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.lbl_nama.grid(column=0, row=0, pady=(80,0), padx=(40,20))
        self.string_nama=tk.StringVar()
        self.input_nama=tk.Entry(self,textvariable=self.string_nama)
        self.input_nama.grid(column=1,row=0, pady=(80,0), padx=(0,40))
        self.button_kembali=tk.Button(self,text="Kembali", bg="#4472C4", fg="white", command=self.kembali)
        self.button_kembali.grid(column=0,row=1, pady=(60,10), padx=(40,10), ipadx=50)
        self.button_lanjut=tk.Button(self,text="Lanjut", bg="#4472C4", fg="white",command=self.lanjut)
        self.button_lanjut.grid(column=1,row=1, pady=(60,10), padx=(0,40), ipadx=50)
        self.protocol("WM_DELETE_WINDOW",self.kembali)
        self.mainloop()
    def kembali(self):
        self.destroy()
    def lanjut(self):
        if len(list_meja) == 0:
            tkmsg.showinfo("Meja Penuh", "Mohon maaf, meja sedang penuh. Silakan datang kembali di lain kesempatan.")
            self.destroy()
        else:
            nomor_meja=sorted(list_meja)[0]
            # dijamin nama pembeli tidak mungkin sama
            dict_nama[self.string_nama.get()]=[]
            dict_nama[self.string_nama.get()].append(nomor_meja)
            list_meja.remove(nomor_meja)
            self.destroy()
            Menu(self.master,self.string_nama.get())

# Tampilan menu dengan tabel combobox yang terhubung dengan harga
class Menu(tk.Toplevel):
    def __init__(self, master = None,nama=""):
        super().__init__(master)
        self.geometry("800x400")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        for i in range(1):
            self.columnconfigure(i, minsize=200)
        self.rowconfigure(0, minsize=50)
        self.nama=nama
        self.label_nama=tk.Label(self,text=f"Nama pemesan: {self.nama}")
        self.label_nama.grid(row=0, column=0, sticky="NW", padx=60)
        self.label_meja=tk.Label(self,text=f"No Meja: {dict_nama[self.nama][0]}")
        self.label_meja.grid(row=0, column=0, sticky="NE", padx=(0,160))
        self.button_ubah=tk.Button(self, text="Ubah", bg="#4472C4", fg="white", command=self.ubah_meja)
        self.button_ubah.grid(row=0, column=0,sticky="NE", padx=120)
        # definisikan static variabel class Table
        Table.baris=3
        Table.list=[]
        Table.nama=nama
        self.label_meals=tk.Label(self, text="MEALS")
        self.label_meals.grid(row=2, column=0, sticky="NW", padx=60)
        self.table_meals=Table("MEALS", self)
        self.label_drinks=tk.Label(self, text="DRINKS")
        self.label_drinks.grid(row=4, column=0, sticky="NW", padx=60)
        self.table_drinks=Table("DRINKS", self)
        self.label_sides=tk.Label(self, text="SIDES")
        self.label_sides.grid(row=6, column=0, sticky="NW", padx=60)
        self.table_sides=Table("SIDES", self)
        self.label_total_harga=tk.Label(self, text=f"Total Harga: 0", font="Arial 15 bold")
        self.label_total_harga.grid(row=8, column=0, sticky="NE",padx=(0,80))
        self.button_kembali=tk.Button(self,text="Kembali", bg="#4472C4", fg="white", command=self.kembali)
        self.button_kembali.grid(column=0,row=9, sticky="NSW" ,ipadx=50, padx=(230,0), pady=(35,0))
        self.button_lanjut=tk.Button(self,text="Lanjut", bg="#4472C4", fg="white",command=self.lanjut)
        self.button_lanjut.grid(column=0,row=9, pady=(35,0), padx=(0,270), ipadx=50, sticky="NSE")
        self.protocol("WM_DELETE_WINDOW",self.kembali)
        self.mainloop()
    # fungsi perintah setiap tombol untuk modifikasi data
    def lanjut(self):
        for data in Table.list:
            dict_nama[self.nama].append([data[0].get(),dict_menu[data[1]]])
        dict_nama[self.nama].append(total_harga)
        self.destroy()
    def ubah_meja(self):
        self.destroy()
        UbahMeja(self.master,dict_nama[self.nama][0], self.nama)
    def kembali(self):
        list_meja.append(dict_nama[self.nama][0])
        del dict_nama[self.nama]
        self.destroy()

# class membuat table dengan inherit tk.frame
class Table(tk.Frame):
    baris=3
    list=[]
    nama=""
    def __init__(self, jenis, master = None):
        super().__init__(master)
        self.baris=Table.baris
        Table.baris+=2
        self.grid(row=self.baris, column=0, columnspan=1, padx=40)
        self.jenis = jenis
        self.data = self.generate_data()
        self.total_rows = len(self.data)
        self.total_columns = len(self.data[0])
        self.deafult_table()
        self.generate_table()
    def generate_table(self):
        for i in range(1,self.total_rows):
            for j in range(self.total_columns-1):
                entry = tk.Entry(self, width = 23, fg = 'black')
                entry.grid(row = i, column = j)
                entry.insert(tk.END, self.data[i][j])
                entry['state'] = 'readonly'
            # kolom paling kanan -> combobox    
            values = tuple([k for k in range(10)])
            opsi_jumlah = ttk.Combobox(self, values = values, width=23)
            opsi_jumlah.set(0)
            opsi_jumlah.bind("<<ComboboxSelected>>", self.get_value) # jika pelanggan memilih jumlah
            Table.list.append([opsi_jumlah,self.data[i][0]])
            opsi_jumlah.grid(row = i, column = self.total_columns - 1)
    def get_value (self, i):
        """fungsi mengatur jumlah harga"""
        global dict_menu
        global dict_nama
        global total_harga
        temp_harga=0
        for data in self.list:
            temp_harga+=(int(data[0].get())*(dict_menu[data[1]].harga))
        self.master.label_total_harga["text"]=f"total harga: {temp_harga}"
        total_harga=temp_harga
    def generate_data(self):
        """fungsi mengolah data untuk ditampilkan"""
        data=[("Kode", "Nama", "harga", "kegurihan", "Jumlah")]
        if self.jenis == "MEALS":
            for kelas in dict_menu.values():
                if isinstance(kelas, Meals):
                    data.append((kelas.kode_menu, kelas.nama_menu, kelas.harga, kelas.tingkat_kegurihan))
        elif self.jenis == "DRINKS":
            for kelas in dict_menu.values():
                if isinstance(kelas, Drinks):
                    data.append((kelas.kode_menu, kelas.nama_menu, kelas.harga, kelas.tingkat_kemanisan))
        elif self.jenis == "SIDES":
            for kelas in dict_menu.values():
                if isinstance(kelas, Sides):
                    data.append((kelas.kode_menu, kelas.nama_menu, kelas.harga, kelas.tingkat_keviralan))
        return data
    def deafult_table(self):
        """fungsi untuk membuat table pertama"""
        for i in range(1):
            for j in range(5):
                entry = tk.Entry(self, width = 23, fg = 'black')
                entry.grid(row = i, column = j)
                entry.insert(tk.END, self.data[i][j])
                entry['state'] = 'readonly'

# fungsi untuk membuat menu ganti meja 
class UbahMeja(tk.Toplevel):
    def __init__(self, master = None, nomor=0, nama="", self_config=""):
        """definisikan widget dan variabel awal"""
        super().__init__(master)
        self.geometry("400x400")
        self.nomor=int(nomor)
        self.nama=nama
        self.config=self_config
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_command = tk.Label(self, text="Silakan klik meja kosong yang diinginkan:")
        self.lbl_command.grid(column=0, row=0, sticky="NEW", columnspan=2, padx=(90,0))
        self.btn_table=[]
        self.generate_table()
        self.press(nomor)
        self.lbl_info=tk.Label(self, text="Info", font="Arial 10 bold")
        self.lbl_info.grid(row=7, column=0, sticky="NW", padx=(20,0))
        self.lbl_info_isi=tk.Label(self, text="Merah: Terisi", font="Arial 9")
        self.lbl_info_isi.grid(row=8, column=0, sticky="NW", padx=(20,0))
        self.lbl_info_kosong=tk.Label(self, text="Abu-abu: Kosong", font="Arial 9")
        self.lbl_info_kosong.grid(row=9, column=0, sticky="NW", padx=(20,0))
        self.lbl_info_anda=tk.Label(self, text="Biru: Meja Anda", font="Arial 9")
        self.lbl_info_anda.grid(row=10, column=0, sticky="NW", padx=(20,0))
        self.button_lanjut=tk.Button(self,text="Kembali", bg="#4472C4", fg="white",command=self.kembali)
        self.button_lanjut.grid(column=0,row=11, sticky="NSW", ipadx=60, pady=20, padx=(110,0), columnspan=2)
        self.protocol("WM_DELETE_WINDOW",self.kembali)
        self.mainloop()
    # membuat tombol dalam bentuk table
    def generate_table(self):
        for i in range(1,6):
            button_meja = tk.Button(self, width = 10, fg = 'white', text=f"{i-1}", height=1, bg="grey", command= lambda i=i: self.press(i-1))
            button_meja.grid(row = i, column = 0, pady=10, sticky="E",ipadx=10, padx=(83,20))
            self.btn_table.append([button_meja,i-1])
        for i in range(1,6):
            button_meja = tk.Button(self, width = 10, fg = 'white', text=f"{i+4}", height=1, bg="grey", command=lambda i=i: self.press(i+4))
            button_meja.grid(row = i, column = 1,sticky="W", pady=10, ipadx=10)
            self.btn_table.append([button_meja,i+4])
    # perintah ganti meja
    def press (self,nomor):
        if self.nomor != nomor:
            if nomor in list_meja:
                list_meja.remove(nomor)
                list_meja.append(self.nomor)
                self.nomor=nomor
            else:
                tkmsg.showerror("ERROR", "Meja sedang diisi pelanggan lain")
        for table in self.btn_table:
            if int(table[1]) == self.nomor:
                table[0]["bg"]="#4472C4"
            elif table[1] not in list_meja:
                table[0]["bg"]="red"
            else:
                table[0]["bg"]="grey"
    # catat nomor meja fix
    def kembali(self):
        global dict_nama
        dict_nama[self.nama][0]=self.nomor
        self.destroy()
        Menu(self.master,self.nama)

# perintah selesai menggunakan meja
class SelesaiGunakanMeja(tk.Toplevel):
    # buat tombol meja dan warnai merah yang sedang terisi
    def __init__(self, master = None):
        super().__init__(master)
        self.geometry("400x400")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_command = tk.Label(self, text="Silakan klik meja yang selesai digunakan:")
        self.lbl_command.grid(column=0, row=0, sticky="NEW", columnspan=2, padx=(90,0))
        self.btn_table=[]
        self.generate_table()
        self.configure_table()
        self.lbl_info=tk.Label(self, text="Info", font="Arial 10 bold")
        self.lbl_info.grid(row=7, column=0, sticky="NW", padx=(20,0))
        self.lbl_info_isi=tk.Label(self, text="Merah: Terisi", font="Arial 9")
        self.lbl_info_isi.grid(row=8, column=0, sticky="NW", padx=(20,0))
        self.lbl_info_kosong=tk.Label(self, text="Abu-abu: Kosong", font="Arial 9")
        self.lbl_info_kosong.grid(row=9, column=0, sticky="NW", padx=(20,0))
        self.button_kembali=tk.Button(self,text="Kembali", bg="#4472C4", fg="white", command=self.kembali)
        self.button_kembali.grid(column=0,row=10, sticky="NSEW", padx=(80,0), ipadx=10, pady=20, columnspan=2)
        self.protocol("WM_DELETE_WINDOW",self.kembali)
        self.mainloop()
    def generate_table(self):
        for i in range(1,6):
            button_meja = tk.Button(self, width = 10, fg = 'white', text=f"{i-1}", height=1, bg="grey", command= lambda i=i: self.press(i-1))
            button_meja.grid(row = i, column = 0, pady=10, sticky="E",ipadx=10, padx=(83,20))
            self.btn_table.append([button_meja,i-1])
        for i in range(1,6):
            button_meja = tk.Button(self, width = 10, fg = 'white', text=f"{i+4}", height=1, bg="grey", command=lambda i=i: self.press(i+4))
            button_meja.grid(row = i, column = 1,sticky="W", pady=10, ipadx=10)
            self.btn_table.append([button_meja,i+4])
    def configure_table(self):
        for table in self.btn_table:
            if table[1] not in list_meja:
                table[0]["bg"]="red"
    def press(self , nomor):
        if nomor in list_meja:
            tkmsg.showerror("Error",message=f"Meja {nomor} sedang kosong tidak bisa selesai menggunakan meja!")
        else:
            for nama,data in dict_nama.items():
                if data[0] == nomor:
                    self.destroy()
                    break
            MenuDone(self.master, nama)

    def kembali(self):
        self.destroy()

# tampilkan kembali menu berdasarkan data yang telah diterima
class MenuDone(tk.Toplevel):
    def __init__(self, master = None,nama=""):
        super().__init__(master)
        self.geometry("800x400")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        for i in range(1):
            self.columnconfigure(i, minsize=200)
        self.rowconfigure(0, minsize=50)
        self.nama=nama
        self.label_nama=tk.Label(self,text=f"Nama pemesan: {self.nama}")
        self.label_nama.grid(row=0, column=0, sticky="NW", padx=60)
        self.label_meja=tk.Label(self,text=f"No Meja: {dict_nama[self.nama][0]}")
        self.label_meja.grid(row=0, column=0, sticky="NE", padx=(0,160))
        TableDoneEat.baris=3
        TableDoneEat.list=[]
        TableDoneEat.nama=nama
        TableDoneEat.database=dict_nama[self.nama][1:-1]
        self.label_meals=tk.Label(self, text="MEALS")
        self.label_meals.grid(row=2, column=0, sticky="NW", padx=60)
        self.table_meals=TableDoneEat("MEALS", self)
        self.label_drinks=tk.Label(self, text="DRINKS")
        self.label_drinks.grid(row=4, column=0, sticky="NW", padx=60)
        self.table_drinks=TableDoneEat("DRINKS", self)
        self.label_sides=tk.Label(self, text="SIDES")
        self.label_sides.grid(row=6, column=0, sticky="NW", padx=60)
        self.table_sides=TableDoneEat("SIDES", self)
        self.label_total_harga=tk.Label(self, text=f"Total Harga: {dict_nama[self.nama][-1]}", font="Arial 15 bold")
        self.label_total_harga.grid(row=8, column=0, sticky="NE",padx=(0,80))
        self.button_kembali=tk.Button(self,text="Kembali", bg="#4472C4", fg="white", command=self.kembali)
        self.button_kembali.grid(column=0,row=9, sticky="NSW" ,ipadx=50, padx=(240,0), pady=(35,0))
        self.button_lanjut=tk.Button(self,text="Selesai Menggunakan Meja", bg="#4472C4", fg="white",command=self.lanjut)
        self.button_lanjut.grid(column=0,row=9, pady=(35,0), padx=(0,190), ipadx=20, sticky="NSE")
        self.protocol("WM_DELETE_WINDOW",self.kembali)
        self.mainloop()
    def lanjut(self):
        global dict_nama
        global list_meja
        list_meja.append(dict_nama[self.nama][0])
        del dict_nama[self.nama]
        self.destroy()
        try:
            SelesaiGunakanMeja(self.master).configure_table()
        except:
            pass
    # jika kembali maka tidak jadi selesai menggunakan meja
    def kembali(self):
        self.destroy()

#class untuk membuat tabel data yang sudah fix
class TableDoneEat(tk.Frame):
    baris=3
    nama=""
    def __init__(self, jenis, master = None):
        super().__init__(master)
        self.baris=TableDoneEat.baris
        TableDoneEat.baris+=2
        self.grid(row=self.baris, column=0, columnspan=1, padx=40)
        self.jenis = jenis
        self.data = self.generate_data()
        self.total_rows = len(self.data)
        self.total_columns = len(self.data[0])
        self.deafult_table()
        self.generate_table()
    def generate_table(self):
        for i in range(1,self.total_rows):
            for j in range(self.total_columns):
                entry = tk.Entry(self, width = 23, fg = 'black')
                entry.grid(row = i, column = j)
                entry.insert(tk.END, self.data[i][j])
                entry['state'] = 'readonly'
    def generate_data(self):
        data=[("Kode", "Nama", "harga", "kegurihan", "Jumlah")]
        if self.jenis == "MEALS":
            for list_data in TableDoneEat.database:
                if isinstance(list_data[1], Meals):
                    data.append((list_data[1].kode_menu, list_data[1].nama_menu, list_data[1].harga, list_data[1].tingkat_kegurihan, list_data[0]))
        elif self.jenis == "DRINKS":
            for list_data in TableDoneEat.database:
                if isinstance(list_data[1], Drinks):
                    data.append((list_data[1].kode_menu, list_data[1].nama_menu, list_data[1].harga, list_data[1].tingkat_kemanisan, list_data[0]))
        elif self.jenis == "SIDES":
            for list_data in TableDoneEat.database:
                if isinstance(list_data[1], Sides):
                    data.append((list_data[1].kode_menu, list_data[1].nama_menu, list_data[1].harga, list_data[1].tingkat_keviralan, list_data[0]))
        return data
    def deafult_table(self):
        for i in range(1):
            for j in range(5):
                entry = tk.Entry(self, width = 23, fg = 'black')
                entry.grid(row = i, column = j)
                entry.insert(tk.END, self.data[i][j])
                entry['state'] = 'readonly'

#variabel awal untuk menyimpan data
dict_nama={}
dict_menu={}
list_meja=[i for i in range(10)]
total_harga=0

def main():
    with open('menu.txt', 'r') as file:
    #mengolah data menu
        for line in file.readlines():
            line=line.strip()
            if line[0] == "=":
                key=line.replace("===","")
                continue
            if key == "MEALS":
                menu=Meals(line.split(";")[0],line.split(";")[1],line.split(";")[2],line.split(";")[3])
            if key == "DRINKS":
                menu=Drinks(line.split(";")[0],line.split(";")[1],line.split(";")[2],line.split(";")[3])
            if key == "SIDES":
                menu=Sides(line.split(";")[0],line.split(";")[1],line.split(";")[2],line.split(";")[3])
            dict_menu[menu.kode_menu]=menu
    window = tk.Tk()
    cafe = Main(window)
    window.mainloop()


if __name__ == '__main__':
    main()
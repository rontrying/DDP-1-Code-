# import module tkinter
import tkinter as tk
import tkinter.messagebox as tkmsg

#class menampilkam menu awal
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Karung Ajaib")
        self.pack()
        self.create_widgets()

    #Binding Event Handler dengan buttons yang ada
    def create_widgets(self):
        self.label = tk.Label(self, \
                              text = 'Selamat datang Dek Depe di Karung Ajaib. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_karung = tk.Button(self, \
                                                text = "LIHAT DAFTAR KARUNG", \
                                                command = self.popup_lihat_karung)
        self.btn_masukkan_item = tk.Button(self, \
                                            text = "MASUKKAN ITEM", \
                                            command = self.popup_add_item)
        self.btn_keluarkan_item = tk.Button(self, \
                                        text = "KELUARKAN ITEM", \
                                        command = self.popup_keluarkan_item)
        self.btn_exit = tk.Button(self, \
                                  text = "EXIT", \
                                  command = self.master.destroy)

        self.label.pack()
        self.btn_lihat_daftar_karung.pack()
        self.btn_masukkan_item.pack()
        self.btn_keluarkan_item.pack()
        self.btn_exit.pack()

    # semua item dalam karung
    def popup_lihat_karung(self):
        PopupLihatKarung(self.master)

    # menu masukkan item
    def popup_add_item(self):
        PopupAddItem(self.master)

    # menu keluarkan item
    def popup_keluarkan_item(self):
        PopupKeluarkanItem(self.master)

#class untuk menampilkan toplevel yang berisi menu lihat karung dan memunculkan barang barangnya
class PopupLihatKarung(object):
  def __init__(self,master):
    self.main_window = tk.Toplevel()
    self.main_window.wm_title("Lihat Karung")

    self.title = tk.Label(self.main_window, text='Daftar Karung Ajaib')
    self.nama = tk.Label(self.main_window, text='Nama Item')
    self.title.pack()
    self.nama.pack()

    #Tampilkan halaman Lihat Karung Ajaib
    for index,barang in enumerate(sorted(item_set)):
        temp=tk.Label(self.main_window,text=f"{index+1}. {barang}")
        temp.pack()
    self.exit_button = tk.Button(self.main_window, text="EXIT", command = self.main_window.destroy)
    self.exit_button.pack()
    
# Class Masukkan Item 
class PopupAddItem(object):
    
  def __init__(self,master):
    self.main_window = tk.Toplevel()
    self.main_window.wm_title("Masukkan item")
    self.main_window.geometry("280x100")

    for i in range(3):
        self.main_window.columnconfigure(i)
    #Widget untuk tampilan Masukkan Item
    self.label=tk.Label(self.main_window,text="Input Masukan item")
    self.barang=tk.StringVar()
    self.input=tk.Entry(self.main_window,textvariable=self.barang)
    self.info=tk.Label(self.main_window,text="Nama item")
    self.label.grid(row=0,column=1)
    self.info.grid(row=1,column=0)
    self.input.grid(row=1,column=1)
    self.submit_button = tk.Button(self.main_window, text = 'Masukkan', command = self.masukkan_item)
    self.submit_button.grid(row=2,column=1)
  def masukkan_item(self):
    #Method untuk Masukkan Item
    item=self.barang.get()
    if item not in item_set:
        item_set.add(item)
        tkmsg.showinfo(title="berhasil!",message=f"Berhasil Masukan item {item}")
    else:
        tkmsg.showwarning(message=f"Item dengan nama {item} sudah ada di dalam KarungAjaib. Item {item} tidak bisa dimasukkan lagi.")
    self.main_window.destroy()



# Class Keluarkan Item
class PopupKeluarkanItem(object):
    
  def __init__(self, master):
    self.main_window = tk.Toplevel()
    self.main_window.wm_title("Keluarkan item")
    self.main_window.geometry("280x100")

    for i in range(3):
        self.main_window.columnconfigure(i)
    #Widget untuk tampilan Keluarkan Item
    self.label=tk.Label(self.main_window,text="Input Keluarkan item")
    self.barang=tk.StringVar()
    self.input=tk.Entry(self.main_window,textvariable=self.barang)
    self.info=tk.Label(self.main_window,text="Nama item")
    self.label.grid(row=0,column=1)
    self.info.grid(row=1,column=0)
    self.input.grid(row=1,column=1)
    self.submit_button = tk.Button(self.main_window, text = 'Ambil', command = self.keluarkan_item)
    self.submit_button.grid(row=2,column=1)
  def keluarkan_item(self):
    #Method untuk Keluarkan Item
    item=self.barang.get()
    if item not in item_set:
        tkmsg.showwarning(title="ItemNotFound",message=f"Item dengan nama {item} tidak ditemukan di dalam karung")
    else:
        item_set.remove(item)
        tkmsg.showinfo(title="berhasil!",message=f"Berhasil mengeluarkan item {item}")
    self.main_window.destroy()

#menampung barang barang
item_set = set()
if __name__ == "__main__":
    root = tk.Tk()
    m=MainWindow(root)
    root.mainloop() #run agar program terus berjalan
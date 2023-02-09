# import library python yang digunakan
import turtle as mandor
import random as acak
from tkinter import messagebox

# memanggil objek turtle screen
mandor.getscreen()

# meminta input lapisan bawah
lapisan_bawah=mandor.numinput("Input lapisan bawah","Jumlah batu bata lapisan bawah")

# memvalidasi input lapisan bawah dan meminta input kembali jika user input invalid
while lapisan_bawah <= 0 or lapisan_bawah > 25 or lapisan_bawah % 1 != 0 :
    if lapisan_bawah > 25:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai maksimal untuk jumlah batu lapisan bawah adalah 25 ")
    elif lapisan_bawah ==0:
        messagebox.showwarning("Kesalahan User Input", "Input jumlah lapisan bawah 0 tidak akan \
membentuk candi apapun, dan akan menyebabkan error pada saat menginput lapisan atas, \
karena lapisan atas harus lebih kecil dari lapisan bawah sekaligus tidak boleh negatif ")
    elif lapisan_bawah <0:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai minimal untuk jumlah batu lapisan bawah adalah 0 ")
    elif lapisan_bawah % 1 != 0:
        messagebox.showwarning("Kesalahan User Input", "Input jumlah lapisan bawah bernilai koma akan \
membuat perhitungan tidak sama antar lapisan dan batu candi sehingga akan menyebabkan \
error karena bentuk candi tidak akan simetris nantinya")
    lapisan_bawah=mandor.numinput("Input lapisan bawah","Jumlah batu bata lapisan bawah")

# meminta input lapisan atas
lapisan_atas=mandor.numinput("Input lapisan atas","Jumlah batu bata lapisan atas")

# memvalidasi input lapisan atas dan meminta input kembali jika user input invalid
while lapisan_atas < 1 or lapisan_atas > 24 or lapisan_bawah < lapisan_atas or lapisan_atas % 1 != 0:
    if lapisan_atas > 24:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai maksimal untuk jumlah batu lapisan atas adalah 24 ")
    elif lapisan_atas < 1:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai minimal untuk jumlah batu lapisan atas adalah 1 ")
    elif lapisan_atas % 1 != 0:
        messagebox.showwarning("Kesalahan User Input", "Input jumlah lapisan atas bernilai koma akan \
membuat perhitungan tidak sama antar lapisan dan batu candi sehingga akan menyebabkan \
error karena bentuk candi tidak akan simetris nantinya")
    elif lapisan_bawah < lapisan_atas:
        messagebox.showerror("Error", "Input error \
karena lapisan atas tidak mungkin lebih besar dari lapisan atas")
    lapisan_atas=mandor.numinput("Input lapisan atas","Jumlah batu bata lapisan atas")

# meminta input panjang
panjang=mandor.numinput("Input Panjang", "Panjang satu buah lapisan batu bata (piksel):")

# memvalidasi input panjang dan meminta input kembali jika user input invalid
while panjang < 1 or panjang > 35 or panjang % 1 != 0:
    if panjang > 35:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai maksimal untuk panjang satu buah lapisan batu bata (piksel) adalah 35 ")
    elif panjang < 1:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai minimal untuk panjang satu buah lapisan batu bata (piksel) adalah 1 ")
    elif panjang % 1 != 0:
        messagebox.showwarning("Kesalahan User Input", "Input panjang bernilai koma akan \
membuat perhitungan tidak sama antar lapisan dan batu candi sehingga akan menyebabkan \
error karena bentuk candi tidak akan simetris nantinya")
    panjang=mandor.numinput("Input Panjang","Panjang satu buah lapisan batu bata (piksel):")

# meminta input lebar
lebar=mandor.numinput("Input Lebar", "Lebar satu buah lapisan batu bata (piksel):")

# memvalidasi input lebar dan meminta input kembali jika user input invalid
while lebar < 1 or lebar > 25 or lebar % 1 != 0:
    if lebar > 25:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai maksimal untuk lebar satu buah lapisan batu bata (piksel) adalah 25 ")
    elif lebar < 1:
        messagebox.showwarning("Kesalahan User Input","Input tidak \
valid dikarenakan nilai minimal untuk lebar satu buah lapisan batu bata (piksel) adalah 1 ")
    elif lebar % 1 != 0:
        messagebox.showwarning("Kesalahan User Input", "Input lebar bernilai koma akan \
membuat perhitungan tidak sama antar lapisan dan batu candi sehingga akan menyebabkan \
error karena bentuk candi tidak akan simetris nantinya")
    lebar=mandor.numinput("Input Lebar","Lebar satu buah lapisan batu bata (piksel):")

# memberi nilai variabel awal yang selanjutnya akan digunakan
jumlah_batu_bata=0
koordinat_x=-((panjang*lapisan_bawah)/2)
koordinat_y=(lebar*(lapisan_atas-lapisan_bawah+1))/2
tingkat=lapisan_bawah
panjang_total=panjang*lapisan_bawah

mandor.speed(0) # mengatur kecepatan
mandor.hideturtle() # menghilangkan turtle
mandor.penup() # berhenti menulis
mandor.setpos(koordinat_x,koordinat_y) # mengatur koordinat awal agar candi tergambar di tengah

#mulai menggambar batu bata
while tingkat != (lapisan_atas-1):
    # untuk menghindari turtle berputar putar pada iterasi pertama
    if lapisan_bawah != tingkat: #karena lapisan bawah = tingkat pada iterasi pertama
        mandor.penup()
        mandor.left(180)
        # untuk mengkhususkan penambahan panjang total pada iterasi ke 2
        if lapisan_bawah == (tingkat+1): #lapisan bawah = tingkat + 1 pada iterasi ke 2
            panjang_total+=(panjang/2)

    mandor.fd(panjang_total)

    mandor.left(90)
    mandor.fd(lebar)
    mandor.left(90)

    # dijalankan menggambar batu bata setiap baris
    for i in range(int(tingkat)):
        mandor.pendown()
        if tingkat == lapisan_bawah or tingkat == lapisan_atas:
            mandor.fillcolor("#BC4A3C")
        elif i == 0 or i == (tingkat-1):
            mandor.fillcolor("#BC4A3C")
        else:
            mandor.colormode(255)
            merah=acak.randint(0,255)
            hijau=acak.randint(0,255)
            biru=acak.randint(0,255)
            while merah == 188 and hijau == 74 and biru == 60:
                merah=acak.randint(0,255)
                hijau=acak.randint(0,255)
                biru=acak.randint(0,255)
            mandor.fillcolor(merah,hijau,biru)
        mandor.begin_fill()
        mandor.fd(panjang)
        mandor.left(90)
        mandor.fd(lebar)
        mandor.left(90)
        mandor.fd(panjang)
        mandor.left(90)
        mandor.fd(lebar)
        mandor.end_fill()
        mandor.left(90)
        mandor.fd(panjang)
        jumlah_batu_bata+=1
    panjang_total-=panjang # mengurangi pergeseran turtle setiap tingkatnya
    tingkat-=1 # pengurangan 1 batu bata setiap tingkat

mandor.penup()

#mengatur koordinat tulisan
mandor.setpos(0,koordinat_y-50)

#output text jumlah batu bata
mandor.write(f"Candi warna-warni dengan {jumlah_batu_bata} batu bata", False, "center", ("times new roman", 20, "normal"))

# exit dengan mengklik layar
mandor.exitonclick()
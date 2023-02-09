# import module
import os
import sys
import re

#enter pada terminal
print()

# fungsi mengscan file per baris
def scan_line (tempat,tandai,khusus=""):
    # menghindari file selain .txt
    if tempat.find(".txt") != -1:
        # pake regex dengan asumsi kalo -w wildcard tidak memuat spasi
        if "*" in tandai :
            awal=tandai[:tandai.find("*")]
            akhir=tandai[tandai.find("*")+1:]
            if khusus == "w": # untuk w
                tandai=rf"{awal}\S*{akhir}"
            else:
                tandai=rf"{awal}.*{akhir}"
        with open(tempat,"r") as file1:
            lines=file1.readlines()
            for index,line in enumerate(lines):
                # tambah spasi agar match dengan -w dan assign ke variabel sebagai baris yg dicari
                baris_find=" "+line.replace("\n","")+" "
                if khusus == "i":
                    baris_find=baris_find.lower()
                if "*" in tandai:
                    result=re.search(tandai,baris_find)
                else:
                    result=baris_find.find(tandai)
                lokasi=tempat.replace("./","").replace("\\","/")
                if result != None and result != -1: # tetap print line agar sama dengan file aslinya
                    print(f"{lokasi:<40} line {index+1:<3} {line[:40].rstrip():<40}")
    else:
        print("Argumen program tidak benar.")

# scan direktori
def scan_file(direktori, tandai, khusus=""):
    for (root,_,files) in os.walk(f"./{direktori}", topdown=True):
        if len(files) != 0:
            for file in files:
                if file.find(".txt") != -1: # klo txt scan filenya
                    scan_line(f"{root}/{file}",tandai, khusus)

def file_not_exist(file_atau_direktori): #perintah path not exist
    print(f"Path {file_atau_direktori} tidak ditemukan")

# cek ketentuan perintah
if len(sys.argv) == 3 and sys.argv[1].count("*") <2:
    # hilangkan x* dan *x menjadi x
    if sys.argv[1].find("*") == 0 or sys.argv[1].find("*") == (len(sys.argv[1])-1):
                    sys.argv[1]=sys.argv[1].replace("*","")
    if os.path.isfile(sys.argv[2]) == True: #check apakah file ada
        scan_line(f"{sys.argv[2]}",sys.argv[1])
    elif os.path.exists(sys.argv[2]) == True: #check apakah direktori ada
        scan_file(sys.argv[2], f"{sys.argv[1]}")
    else:
        file_not_exist(sys.argv[2])

# cek ketentuan perintah
elif len(sys.argv) == 4 and str(sys.argv[1]) == "-w" and sys.argv[2].count("*") <2 :
    # hilangkan x* dan *x menjadi x
    if sys.argv[2].find("*") == 0 or sys.argv[2].find("*") == (len(sys.argv[2])-1):
                    sys.argv[2]=sys.argv[2].replace("*","")
    if os.path.isfile(sys.argv[3]) == True: #check apakah file ada
        scan_line(f"{sys.argv[3]}",f" {sys.argv[2]} ","w")
    elif os.path.exists(sys.argv[3]) == True: #check apakah direktori ada
        scan_file(sys.argv[3], f" {sys.argv[2]} ","w")
    else:
        file_not_exist(sys.argv[3])

# cek ketentuan perintah
elif len(sys.argv) == 4 and str(sys.argv[1]) == "-i" and sys.argv[2].count("*") <2:
    # hilangkan x* dan *x menjadi x
    if sys.argv[2].find("*") == 0 or sys.argv[2].find("*") == (len(sys.argv[2])-1):
                    sys.argv[2]=sys.argv[2].replace("*","")
    if os.path.isfile(sys.argv[3]) == True: #check apakah file ada
        scan_line(f"{sys.argv[3]}",f"{sys.argv[2].lower()}","i")
    elif os.path.exists(sys.argv[3]) == True: #check apakah direktori ada
        scan_file(sys.argv[3], f"{sys.argv[2].lower()}","i")
    else:
        file_not_exist(sys.argv[3])
else:
    print("Argumen program tidak benar.")
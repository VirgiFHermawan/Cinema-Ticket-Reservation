def menu():
    import os
    os.system("CLS")
    print("------------------------------")
    print("|     THEATER OF DREAM     |  ")
    print("------------------------------")
    print("\tDaftar Menu")
    print("1. Daftar Film dan Harga")
    print("2. Pesan Tiket")
    print("3. Keluar")
    pil = int(input("\nMASUKAN MENU YANG AKAN DIPILIH\t : "))
    if pil in range(1, 4):
        pilihmenu(pil)
    else:
        menu()


def pilihmenu(pil):
    import os
    os.system("CLS")
    if pil == 1:
        tabel()
    elif pil == 2:
        pesantiket()
    else:
        keluar()


def tabel():
    import os
    os.system("CLS")
    print("------------------------------")
    print("    NAMA FILM SEDANG TAYANG   ")
    print("------------------------------")
    print("\t |    NAMA FILM   | JAM TAYANG | STUDIO |  KATEGORI  |    HARGA   | ")
    print("----------------------------------------------------------------------")
    print("\t |                  | 11.30 | STUDIO 01 | SEMUA UMUR | Rp. 50.000 |")
    print("\t |     THE BOX      | 13.20 | STUDIO 01 | SEMUA UMUR | Rp. 50.000 |")
    print("\t |                  | 16.20 | STUDIO 01 | SEMUA UMUR | Rp. 50.000 |")
    print("----------------------------------------------------------------------")
    print("\t |                  | 11.30 | STUDIO 02 | SEMUA UMUR | Rp. 50.000 |")
    print("\t | GODZILLA VS KONG | 13.20 | STUDIO 02 | SEMUA UMUR | Rp. 50.000 |")
    print("\t |                  | 16.20 | STUDIO 02 | SEMUA UMUR | Rp. 50.000 |")
    print("----------------------------------------------------------------------")
    print("\t |                  | 11.30 | STUDIO 03 |   DEWASA   | Rp. 50.000 |")
    print("\t |     ANABELLE     | 13.20 | STUDIO 03 |   DEWASA   | Rp. 50.000 |")
    print("\t |                  | 16.20 | STUDIO 03 |   DEWASA   | Rp. 50.000 |")
    print("----------------------------------------------------------------------")
    print("\t |                  | 11.30 | STUDIO 04 | SEMUA UMUR | Rp. 50.000 |")
    print("\t |  STAND BY ME 2   | 13.20 | STUDIO 04 | SEMUA UMUR | Rp. 50.000 |")
    print("\t |                  | 16.20 | STUDIO 04 | SEMUA UMUR | Rp. 50.000 |")
    print("----------------------------------------------------------------------")
    print("TEKAN ENTER UNTUK KEMBALI KE MENU AWAL ")
    input()
    menu()


def pesantiket():
    import os
    os.system("CLS")
    print("-------------------------")
    print("Masukan Data Anda")
    print("Mohon untuk mengisi data anda menggunakan huruf kapital")
    input("Nama\t:")
    j = input("Film yang di pilih\t:")
    if j == "THE BOX":
        htm = 50000
        print("ANDA MEMILIH FILM THE BOX")
        print("---------------------------")
        print("SILAHKAN PILIH JADWAL FILM")
        input("JADWAL FILM \t:")
        print("TIKET YANG DI PESAN")
        jumlah = int(input("Tiket\t:"))
        print("PILIH KURSI\t:")
        input("Kursi\t:")
        totalbiaya = htm * jumlah
        print("Jumlah yang harus dibayar :", totalbiaya)
        bayar = int(input("Uang yang dibayarkan\t:"))
        if bayar < totalbiaya:
            print("Maaf uang anda kurang!")
            maaf = totalbiaya - bayar
            print("Maaf uang anda kurang Rp.", maaf)
            kurang = int(input("masukan kekurangan anda : Rp."))
            kembali = (kurang + bayar) - totalbiaya
            print("Kembalian Anda Sebesar : Rp.", kembali)
        else:
            kembalian = bayar - totalbiaya
            print("-------------------------------")
            print("Kembalian Anda Sebesar : Rp.", kembalian)
            print("-------------------------------")
    elif j == "GODZILLA VS KONG":
        htm = 50000
        print("ANDA MEMILIH FILM GODZILLA VS KONG")
        print("---------------------------")
        print("SILAHKAN PILIH JADWAL FILM")
        input("JADWAL FILM \t:")
        print("TIKET YANG DI PESAN")
        jumlah = int(input("Tiket\t:"))
        print("PILIH KURSI\t:")
        input("Kursi\t:")
        totalbiaya = htm * jumlah
        print("Jumlah yang harus dibayar :", totalbiaya)
        bayar = int(input("Uang yang dibayarkan\t:"))
        if bayar < totalbiaya:
            print("Maaf uang anda kurang!")
            maaf = totalbiaya - bayar
            print("Maaf uang anda kurang Rp.", maaf)
            kurang = int(input("masukan kekurangan anda : Rp."))
            kembali = (kurang + bayar) - totalbiaya
            print("Kembalian Anda Sebesar : Rp.", kembali)
        else:
            kembalian = bayar - totalbiaya
            print("-------------------------------")
            print("Kembalian Anda Sebesar : Rp.", kembalian)
            print("-------------------------------")
    elif j == "ANABELLE":
        htm = 50000
        print("ANDA MEMILIH FILM ANABELLE")
        print("---------------------------")
        print("SILAHKAN PILIH JADWAL FILM")
        input("JADWAL FILM \t:")
        print("TIKET YANG DI PESAN")
        jumlah = int(input("Tiket\t:"))
        print("PILIH KURSI\t:")
        input("Kursi\t:")
        totalbiaya = htm * jumlah
        print("Jumlah yang harus dibayar :", totalbiaya)
        bayar = int(input("Uang yang dibayarkan\t:"))
        if bayar < totalbiaya:
            print("Maaf uang anda kurang!")
            maaf = totalbiaya - bayar
            print("Maaf uang anda kurang Rp.", maaf)
            kurang = int(input("masukan kekurangan anda : Rp."))
            kembali = (kurang + bayar) - totalbiaya
            print("Kembalian Anda Sebesar : Rp.", kembali)
        else:
            kembalian = bayar - totalbiaya
            print("-------------------------------")
            print("Kembalian Anda Sebesar : Rp.", kembalian)
            print("-------------------------------")
    else:
        htm = 50000
        print("ANDA MEMILIH FILM STAND BY ME DORAEMON 2")
        print("---------------------------")
        print("SILAHKAN PILIH JADWAL FILM")
        input("JADWAL FILM \t:")
        print("TIKET YANG DI PESAN")
        jumlah = int(input("Tiket\t:"))
        print("PILIH KURSI\t:")
        input("Kursi\t:")
        totalbiaya = htm * jumlah
        print("Jumlah yang harus dibayar :", totalbiaya)
        bayar = int(input("Uang yang dibayarkan\t:"))
        if bayar < totalbiaya:
            print("Maaf uang anda kurang!")
            maaf = totalbiaya - bayar
            print("Maaf uang anda kurang Rp.", maaf)
            kurang = int(input("masukan kekurangan anda : Rp."))
            kembali = (kurang + bayar) - totalbiaya
            print("Kembalian Anda Sebesar : Rp.", kembali)
        else:
            kembalian = bayar - totalbiaya
            print("-------------------------------")
            print("Kembalian Anda Sebesar : Rp.", kembalian)
            print("-------------------------------")

def keluar():
    print("Anda keluar Program")

print("Selamat Datang di dalam Project 2 ISA Semester 2")
print("     Project Backend Programming (BEP)     ")
print("            CEP - CCIT FTUI           ")
print("-------------------------------------------------")
print("Anggota : ")
print("1. Siti Rayhanah - 2020010094")
print("2. Yudhistira Nuzuli Ardana - 2020010086 ")
print("3. Virgi Febrian Hermawan - 2020010102")
print("-------------------------------------------------")
print("KLIK ENTER UNTUK MENUJU TABEL FILM")
input()
tabel()






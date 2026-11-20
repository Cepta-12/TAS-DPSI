from apotek.transaksi import transaksi_penjualan, tampilkan_riwayat
from apotek.obat import (
    cek_kedaluwarsa,
    tambah_obat,
    tampilkan_obat,
    kelompokkan_obat,
    ubah_obat,
    hapus_obat,
    tambah_stok,
    kurangi_stok,
    cek_stok_menipis,
) 
#Mengimpor fungsi dari file obat di dalam folder apotek
from apotek.laporan import laporan_pendapatan
def menu_obat(): #fungsi menu obat

    while True:

        print("\n================================")
        print("       MANAJEMEN DATA OBAT")
        print("================================")
        print("1. Tambah Obat")
        print("2. Tampilkan Obat")
        print("3. Ubah Data Obat")
        print("4. Hapus Data Obat")
        print("5. Cek Kedaluwarsa")
        print("6. Kelompokkan Obat")
        print("0. Kembali")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":

            
            tampilkan_obat()
            tambah_obat()

        elif pilihan == "2":

            tampilkan_obat()

        elif pilihan == "3":

            ubah_obat()

        elif pilihan == "4":

            hapus_obat()

        elif pilihan == "5":
            cek_kedaluwarsa()
            
        elif pilihan == "6":
            kelompokkan_obat()

        elif pilihan == "0":

            break

        else:

            print("Pilihan tidak tersedia!")


def menu_stok(): #fungsi menu stok obat
    while True:
        print("\n=== MANAJEMEN STOK OBAT ===")
        print("1. Tambah Stok")
        print("2. Kurangi Stok")
        print("3. Cek Stok Menipis")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_stok()
        elif pilihan == "2":
            kurangi_stok()
        elif pilihan == "3":
            cek_stok_menipis()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid!")


def menu_utama(): #Fungsi untuk menampilkan menu utama apotek


    while True:

        print("\n===================================")
        print("      SISTEM MANAJEMEN APOTEK")
        print("===================================")

        print("1. Manajemen Data Obat")
        print("2. Manajemen Stok Obat")
        print("3. Transaksi Penjualan")
        print("4. Riwayat Penjualan")
        print("5. Laporan Pendapatan")
        print("0. Keluar")

        print("===================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("Kamu memilih Manajemen Data Obat")
            menu_obat()

        elif pilihan == "2":
            print("Kamu memilih Manajemen Stok Obat")
            menu_stok()
        elif pilihan == "3":
            print("Kamu memilih Transaksi Penjualan")
            transaksi_penjualan()
        elif pilihan == "4":
            print("Kamu memilih Riwayat Penjualan")
            tampilkan_riwayat()
        elif pilihan == "5":
            print("Kamu memilih Laporan Pendapatan")
            laporan_pendapatan()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak tersedia!")


menu_utama()

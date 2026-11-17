
from apotek.obat import daftar_obat
from apotek.data import muat_data, simpan_data
from datetime import datetime

riwayat_penjualan = muat_data("data/riwayat.json", [])


# LIST UNTUK MENYIMPAN RIWAYAT TRANSAKSI



# FUNGSI TRANSAKSI PENJUALAN
def transaksi_penjualan():
    print("\n=== TRANSAKSI PENJUALAN OBAT ===")

    if len(daftar_obat) == 0:
        print("Belum ada obat yang tersedia!")
        return

    total = 0
    daftar_beli = []

    while True:
        print("\nDaftar Obat:")

        for obat in daftar_obat:
            print(
                obat["kode"],
                "-",
                obat["nama"],
                "- Rp",
                format(obat["harga"], ","),
                "- Stok:",
                obat["stok"]
            )

        kode = input("\nMasukkan kode obat (0 untuk selesai): ")

        if kode == "0":
            break

        obat_ditemukan = None

        for obat in daftar_obat:
            if obat["kode"] == kode:
                obat_ditemukan = obat
                break

        if obat_ditemukan == None:
            print("Kode obat tidak ditemukan!")
            continue
        
        tanggal_input = obat_ditemukan.get("kedaluwarsa")

        if tanggal_input:
            try:
                tanggal_expired = datetime.strptime(
                    tanggal_input, "%d-%m-%Y"
                ).date()

                if tanggal_expired < datetime.now().date():
                    print("Obat sudah kedaluwarsa dan tidak bisa dijual!")
                    continue

            except ValueError:
                print("Tanggal kedaluwarsa obat tidak valid!")
                continue

        else:
            print("Obat belum memiliki tanggal kedaluwarsa!")
            continue


       
        # Memasukkan jumlah obat
        try:
            jumlah = int(input("Jumlah yang dibeli: "))
        except ValueError:
            print("Jumlah harus berupa angka!")
            continue

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            continue

        # Menghitung jumlah obat yang sudah masuk keranjang
        jumlah_di_keranjang = 0

        for item in daftar_beli:
            if item["kode"] == obat_ditemukan["kode"]:
                jumlah_di_keranjang += item["jumlah"]

        # Menghitung sisa stok
        stok_tersedia = obat_ditemukan["stok"] - jumlah_di_keranjang

        if jumlah > stok_tersedia:
            print("Stok obat tidak mencukupi!")
            print("Sisa stok yang bisa dibeli:", stok_tersedia)
            continue

        # Menghitung subtotal
        subtotal = obat_ditemukan["harga"] * jumlah

             
        daftar_beli.append({
            "kode": obat_ditemukan["kode"],
            "nama": obat_ditemukan["nama"],
            "harga": obat_ditemukan["harga"],
            "jumlah": jumlah,
            "subtotal": subtotal
        })

        total += subtotal

        print("Obat berhasil dimasukkan ke keranjang!")
        print("Subtotal: Rp", format(subtotal, ","))

    if len(daftar_beli) == 0:
        print("Tidak ada transaksi yang dilakukan.")
        return

    print("\n=== RINCIAN PEMBELIAN ===")

    for item in daftar_beli:
        print(
            item["nama"],
            "x",
            item["jumlah"],
            "= Rp",
            format(item["subtotal"], ",")
        )

    print("\nTotal pembayaran: Rp", format(total, ","))

    while True:
        try:
            bayar = int(input("Masukkan uang pembayaran: "))

            if bayar < total:
                print("Uang pembayaran masih kurang!")
            else:
                break

        except ValueError:
            print("Pembayaran harus berupa angka!")

    kembalian = bayar - total

    # MENGURANGI STOK SETELAH PEMBAYARAN BERHASIL
    for item in daftar_beli:
        for obat in daftar_obat:
            if obat["kode"] == item["kode"]:
                obat["stok"] -= item["jumlah"]
                break

    # MENYIMPAN DATA TRANSAKSI
    transaksi = {
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "daftar_beli": daftar_beli,
        "total": total,
        "bayar": bayar,
        "kembalian": kembalian
    }

    riwayat_penjualan.append(transaksi)



    simpan_data("data/riwayat.json", riwayat_penjualan)
    simpan_data("data/obat.json", daftar_obat)




    
    # MENAMPILKAN STRUK PEMBELIAN
    print("\n" + "=" * 45)
    print("          APOTEK KELOMPOK B")
    print("             STRUK PEMBELIAN")
    print("=" * 45)

    print("Tanggal:", transaksi["tanggal"])
    print("-" * 45)

    print("RINCIAN PEMBELIAN:")

    for nomor, item in enumerate(daftar_beli, start=1):
        print(f"\n{nomor}. {item['nama']}")
        print(f"   Harga satuan : Rp{item['harga']:,}")
        print(f"   Jumlah       : {item['jumlah']}")
        print(f"   Subtotal     : Rp{item['subtotal']:,}")

    print("-" * 45)
    print(f"Total      : Rp{total:,}")
    print(f"Bayar      : Rp{bayar:,}")
    print(f"Kembalian  : Rp{kembalian:,}")
    print("=" * 45)
    print("      TERIMA KASIH TELAH BERBELANJA")
    print("=" * 45)
    print("Transaksi berhasil!")


# FUNGSI MENAMPILKAN RIWAYAT PENJUALAN

# FUNGSI MENAMPILKAN RIWAYAT PENJUALAN
def tampilkan_riwayat():
    print("\n===== RIWAYAT PENJUALAN =====")

    if not riwayat_penjualan:
        print("Belum ada riwayat penjualan.")
        return

    for nomor, transaksi in enumerate(riwayat_penjualan, start=1):
        print("\nTransaksi ke-", nomor)

        print("Tanggal:", transaksi.get("tanggal", "Tanggal lama"))
        print("Total: Rp", format(transaksi["total"], ","))

        print("Daftar Obat:")

        for item in transaksi.get("daftar_beli", []):
            print(
                item["nama"],
                "| Jumlah:", item["jumlah"],
                "| Subtotal: Rp", format(item["subtotal"], ",")
            )

        print("--------------------------------")

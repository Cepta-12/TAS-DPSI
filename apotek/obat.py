from datetime import datetime
from apotek.data import muat_data, simpan_data
# Memuat data obat dari file JSON saat aplikasi dimulai
daftar_obat = muat_data("data/obat.json", [])

# KATEGORI OBAT MENGGUNAKAN TUPLE
KATEGORI_OBAT = (
    "Tablet",
    "Kapsul",
    "Sirup",
    "Salep",
    "Lainnya"
)

# 1. FUNGSI MENAMBAHKAN OBAT

# 1. FUNGSI MENAMBAHKAN OBAT
def tambah_obat():
    print("\n===== TAMBAH OBAT =====")

    # Input kode obat
    kode_obat = input("Masukkan kode obat: ").strip().upper()

    # SET untuk mengecek kode duplikat
    kode_terdaftar = {
        obat["kode"].strip().upper()
        for obat in daftar_obat
    }

    if kode_obat in kode_terdaftar:
        print("Kode obat sudah digunakan!")
        return

    nama = input("Masukkan nama obat: ")

    # Memilih kategori menggunakan TUPLE
    print("\nPilih Kategori Obat:")

    for nomor, kategori_obat in enumerate(KATEGORI_OBAT, start=1):
        print(f"{nomor}. {kategori_obat}")

    while True:
        pilihan_kategori = input("Pilih kategori (1-5): ")

        if pilihan_kategori.isdigit():
            nomor = int(pilihan_kategori)

            if 1 <= nomor <= len(KATEGORI_OBAT):
                kategori = KATEGORI_OBAT[nomor - 1]
                break

        print("Pilihan kategori tidak valid!")

    # Input harga dan stok
    try:
        harga = int(input("Masukkan harga obat: "))
        stok = int(input("Masukkan jumlah stok: "))

        if harga <= 0:
            print("Harga harus lebih dari 0!")
            return

        if stok < 0:
            print("Stok tidak boleh negatif!")
            return

    except ValueError:
        print("Harga dan stok harus berupa angka!")
        return

    # Input tanggal kedaluwarsa
    while True:
        tanggal_input = input(
            "Masukkan tanggal kedaluwarsa (DD-MM-YYYY): "
        )

        try:
            tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y")

            if tanggal.date() < datetime.now().date():
                print("Tanggal kedaluwarsa tidak boleh di masa lalu!")
            else:
                break

        except ValueError:
            print("Format tanggal salah! Contoh: 25-12-2027")

    # Membuat data obat
    obat_baru = {
        "kode": kode_obat,
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok,
        "kedaluwarsa": tanggal_input
    }

    daftar_obat.append(obat_baru)
    simpan_data("data/obat.json", daftar_obat)

    print("\nObat berhasil ditambahkan!")

# 2. FUNGSI MENAMPILKAN OBAT
def tampilkan_obat():

    print("\n" + "=" * 75)
    print("Data Obat")
    print("=" * 75)

    if len(daftar_obat) == 0:

        print("Belum ada data obat!")

    else:

        print(
            f"{'KODE':<10}"
            f"{'NAMA OBAT':<20}"
            f"{'KATEGORI':<15}"
            f"{'HARGA':<15}"
            f"{'STOK':<8}"
            f"{'KEDALUWARSA':<12}"
        )

        print("-" * 75)

        for obat in daftar_obat:

            print(
                f"{obat['kode']:<10}"
                f"{obat['nama']:<20}"
                f"{obat['kategori']:<15}"
                f"Rp{obat['harga']:<13,}"
                f"{obat['stok']:<8}"
               f"{obat.get('kedaluwarsa', '-'):<12}"
            )

        print("-" * 75)

        print("Total jenis obat:", len(daftar_obat))

# 2.1 FUNGSI MENGELOMPOKKAN OBAT BERDASARKAN KATEGORI
def kelompokkan_obat():
    print("\n===== PENGELOMPOKAN OBAT BERDASARKAN KATEGORI =====")

    if len(daftar_obat) == 0:
        print("Belum ada data obat!")
        return

    # Membuat dictionary untuk mengelompokkan obat
    kelompok_obat = {}

    for obat in daftar_obat:
        kategori = obat.get("kategori", "Tidak berkategori").strip()

        if kategori == "":
            kategori = "Tidak berkategori"

        if kategori not in kelompok_obat:
            kelompok_obat[kategori] = []

        kelompok_obat[kategori].append(obat)

    # Menampilkan obat berdasarkan kategori
    for kategori, daftar in sorted(kelompok_obat.items()):

        print("\nKategori:", kategori)
        print("-" * 60)

        for nomor, obat in enumerate(daftar, start=1):
            print(
                f"{nomor}. {obat['nama']} "
                f"| Kode: {obat['kode']} "
                f"| Harga: Rp{obat['harga']:,} "
                f"| Stok: {obat['stok']}"
            )

        print("Jumlah obat dalam kategori:", len(daftar))

# 3. FUNGSI MENGUBAH DATA OBAT

def ubah_obat():
    print("\n=== UBAH DATA OBAT ===")

    if len(daftar_obat) == 0:
        print("Belum ada data obat!")
        return

    kode = input("Masukkan kode obat yang ingin diubah: ")

    for obat in daftar_obat:
        if obat["kode"] == kode:
            print("\nData obat ditemukan!")
            print("Nama saat ini:", obat["nama"])
            print("Kategori saat ini:", obat["kategori"])
            print("Harga saat ini:", obat["harga"])
            print("Stok saat ini:", obat["stok"])
            print("Kedaluwarsa saat ini:", obat.get("kedaluwarsa", "-"))

            print("\nMasukkan data baru:")

            nama = input("Nama obat baru: ")

            print("\nPilih Kategori Obat:")
            for nomor, kategori_obat in enumerate(KATEGORI_OBAT, start=1):
                print(f"{nomor}. {kategori_obat}")

            while True:
                pilihan_kategori = input("Pilih kategori (1-5): ")

                if pilihan_kategori.isdigit():
                    nomor = int(pilihan_kategori)

                    if 1 <= nomor <= len(KATEGORI_OBAT):
                        kategori = KATEGORI_OBAT[nomor - 1]
                        break

                print("Pilihan kategori tidak valid!")

            kedaluwarsa = input(
                "Tanggal kedaluwarsa baru (DD-MM-YYYY): "
            )

            try:
                harga = int(input("Harga baru: "))
                stok = int(input("Stok baru: "))

                if harga <= 0 or stok < 0:
                    print("Harga harus positif dan stok tidak boleh negatif!")
                    return

                tanggal = datetime.strptime(
                    kedaluwarsa, "%d-%m-%Y"
                )

                if tanggal.date() < datetime.now().date():
                    print("Tanggal kedaluwarsa tidak boleh di masa lalu!")
                    return

            except ValueError:
                print("Input harga, stok, atau tanggal tidak valid!")
                return

            obat["nama"] = nama
            obat["kategori"] = kategori
            obat["harga"] = harga
            obat["stok"] = stok
            obat["kedaluwarsa"] = kedaluwarsa

            simpan_data("data/obat.json", daftar_obat)

            print("\nData obat berhasil diubah!")
            return

    print("Kode obat tidak ditemukan!")

# 4. FUNGSI MENGHAPUS DATA OBAT
def hapus_obat():
    print("\n=== HAPUS DATA OBAT ===")

    if len(daftar_obat) == 0:
        print("Belum ada data obat!")
        return

    kode = input("Masukkan kode obat yang ingin dihapus: ")

    for obat in daftar_obat:
        if obat["kode"] == kode:
            print("\nData obat ditemukan!")
            print("Nama obat:", obat["nama"])

            konfirmasi = input("Yakin ingin menghapus obat ini? (y/n): ")

            if konfirmasi.lower() == "y":
                daftar_obat.remove(obat)
                simpan_data("data/obat.json", daftar_obat)
                print("Data obat berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan!")

            return

    print("Kode obat tidak ditemukan!")


# 5. FUNGSI MENAMBAH STOK OBAT
def tambah_stok():
    print("\n=== TAMBAH STOK OBAT ===")

    kode = input("Masukkan kode obat: ")

    for obat in daftar_obat:
        if obat["kode"] == kode:
            print("Nama obat:", obat["nama"])
            print("Stok saat ini:", obat["stok"])

            try:
                jumlah = int(input("Jumlah stok yang ditambahkan: "))

                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                    return

                obat["stok"] += jumlah
                simpan_data("data/obat.json", daftar_obat)
                print("Stok berhasil ditambahkan!")
                print("Stok sekarang:", obat["stok"])
                return

            except ValueError:
                print("Masukkan jumlah dalam bentuk angka!")
                return

    print("Kode obat tidak ditemukan!")


# 6. FUNGSI MENGURANGI STOK OBAT
def kurangi_stok():
    print("\n=== KURANGI STOK OBAT ===")

    kode = input("Masukkan kode obat: ")

    for obat in daftar_obat:
        if obat["kode"] == kode:
            print("Nama obat:", obat["nama"])
            print("Stok saat ini:", obat["stok"])

            try:
                jumlah = int(input("Jumlah stok yang dikurangi: "))

                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                    return

                if jumlah > obat["stok"]:
                    print("Stok tidak mencukupi!")
                    return

                obat["stok"] -= jumlah
                simpan_data("data/obat.json", daftar_obat)
                print("Stok berhasil dikurangi!")
                print("Stok sekarang:", obat["stok"])
                return

            except ValueError:
                print("Masukkan jumlah dalam bentuk angka!")
                return

    print("Kode obat tidak ditemukan!")


# 7. FUNGSI CEK STOK MENIPIS
def cek_stok_menipis():
    print("\n=== DAFTAR OBAT DENGAN STOK MENIPIS ===")

    ditemukan = False

    for obat in daftar_obat:
        if obat["stok"] <= 5:
            print(
                obat["kode"],
                "-",
                obat["nama"],
                "- Sisa stok:",
                obat["stok"]
            )
            ditemukan = True

    if ditemukan == False:
        print("Tidak ada obat dengan stok menipis.")
        #Fungsi Cek kedaluwarsa
def cek_kedaluwarsa():
    from datetime import datetime

    print("\n===== CEK KEDALUWARSA OBAT =====")

    hari_ini = datetime.now().date()
    ditemukan = False

    for obat in daftar_obat:
        tanggal_input = obat.get("kedaluwarsa")

        if not tanggal_input:
            continue

        try:
            tanggal_expired = datetime.strptime(
                tanggal_input, "%d-%m-%Y"
            ).date()

            selisih = (tanggal_expired - hari_ini).days

            if selisih < 0:
                print(
                    "SUDAH KEDALUWARSA:",
                    obat["nama"],
                    "| Tanggal:", tanggal_input
                )
                ditemukan = True

            elif selisih <= 30:
                print(
                    "HAMPIR KEDALUWARSA:",
                    obat["nama"],
                    "| Sisa hari:", selisih
                )
                ditemukan = True

        except ValueError:
            print("Tanggal tidak valid:", obat["nama"])

    if not ditemukan:
        print("Tidak ada obat yang kedaluwarsa atau hampir kedaluwarsa.")
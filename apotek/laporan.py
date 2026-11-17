
from apotek.transaksi import riwayat_penjualan


# FUNGSI LAPORAN PENDAPATAN
def laporan_pendapatan():
    print("\n" + "=" * 45)
    print("       LAPORAN PENDAPATAN APOTEK")
    print("=" * 45)

    if not riwayat_penjualan:
        print("Belum ada transaksi penjualan!")
        return

    total_pendapatan = 0
    total_obat_terjual = 0

    # Menghitung seluruh transaksi
    for transaksi in riwayat_penjualan:
        total_pendapatan += transaksi.get("total", 0)

        for item in transaksi.get("daftar_beli", []):
            total_obat_terjual += item.get("jumlah", 0)

    print("Jumlah transaksi    :", len(riwayat_penjualan))
    print("Total obat terjual  :", total_obat_terjual)
    print("Total pendapatan    : Rp", format(total_pendapatan, ","))

    print("\n=== RINCIAN TRANSAKSI ===")

    for nomor, transaksi in enumerate(riwayat_penjualan, start=1):
        print("\nTransaksi ke-", nomor)
        print("Tanggal :", transaksi.get("tanggal", "-"))
        print("Total   : Rp", format(transaksi.get("total", 0), ","))

        print("Obat yang terjual:")

        for item in transaksi.get("daftar_beli", []):
            print(
                "-",
                item.get("nama", "Obat"),
                "| Jumlah:", item.get("jumlah", 0),
                "| Subtotal: Rp",
                format(item.get("subtotal", 0), ",")
            )

    print("\n" + "=" * 45)
    print("Laporan berhasil ditampilkan!")

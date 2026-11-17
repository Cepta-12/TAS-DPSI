import json
import os


# FUNGSI MEMUAT DATA DARI FILE JSON
def muat_data(nama_file, data_default):
    os.makedirs("data", exist_ok=True)

    if os.path.exists(nama_file):
        with open(nama_file, "r", encoding="utf-8") as file:
            return json.load(file)

    return data_default


# FUNGSI MENYIMPAN DATA KE FILE JSON
def simpan_data(nama_file, data):
    os.makedirs("data", exist_ok=True)

    with open(nama_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

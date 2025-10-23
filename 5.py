import os
import csv
import json
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def buat_folder(nama_folder):
    try:
        if not os.path.exists(nama_folder):
            os.makedirs(nama_folder)
            logging.info(f"Folder '{nama_folder}' berhasil dibuat.")
        else:
            logging.info(f"Folder '{nama_folder}' sudah ada.")
    except Exception as e:
        logging.error(f"Gagal membuat folder: {e}")

def tulis_csv(nama_file):
    try:
        with open(nama_file, mode='w', newline='') as file:  
            writer = csv.writer(file)
            writer.writerow(['nim', 'nama', 'hadir_uts'])
            writer.writerow(['230103202', 'Nabil Dzaka', 1])
            writer.writerow(['230103258', 'Alfian Muhammad', 0])
            writer.writerow(['230103270', 'Iqbal Abdul Aziz', 1])
        logging.info("File CSV berhasil dibuat dan diisi data.")
    except Exception as e:
        logging.error(f"Gagal menulis CSV: {e}")

def baca_csv_dan_simpan_json(nama_file_csv, nama_file_json):
    try:
        with open(nama_file_csv, mode='r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            total = len(data)
            hadir = sum(int(row['hadir_uts']) for row in data)
            persentase = (hadir / total) * 100 if total > 0 else 0

            ringkasan = {
                "total_mahasiswa": total,
                "hadir": hadir,
                "persentase_hadir": f"hadir_uts" "{persentase:.2f}%"
            }

        with open(nama_file_json, mode='w') as file_json:
            json.dump(ringkasan, file_json, indent=4)
        logging.info("File JSON ringkasan berhasil dibuat.")
    except Exception as e:
        logging.error(f"Gagal membaca CSV atau menulis JSON: {e}")

# Ini untuk menjalankan program
logging.info("Program dimulai...")

folder = "data"
csv_file = os.path.join(folder, "presensi.csv")
json_file = os.path.join(folder, "ringkasan.json")

buat_folder(folder)
tulis_csv(csv_file)
baca_csv_dan_simpan_json(csv_file, json_file)

logging.info("Program selesai tanpa error.")

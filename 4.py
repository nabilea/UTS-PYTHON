# LIST DAFTAR JADWAL
jadwal = {
    "Senin": ["Basis Data", "Pemrograman Web"],
    "Selasa": ["Sistem Operasi", "Jaringan Komputer"],
    "Rabu": ["Kecerdasan Buatan", "Algoritma"],
    "Kamis": ["Pemrograman Mobile", "Keamanan Informasi"],
    "Jumat": ["Analisis Sistem", "Etika Profesi"]
}

def jadwal_hari(hari):
    # Cek apakah hari ada di data
    if hari in jadwal:
        print("Jadwal kuliah hari", hari, ":")
        for matkul in jadwal[hari]:
            print("-", matkul)
    else:
        print("Tidak ada jadwal untuk hari tersebut.")

# Input dari pengguna
hari_input = input("Masukkan nama hari untuk melihat jadwal: ")
jadwal_hari(hari_input.capitalize())

# Penjelasan singkat
print("\nPenjelasan: Pencarian hari dilakukan dengan cara mengecek satu per satu isi list atau dictionary.")

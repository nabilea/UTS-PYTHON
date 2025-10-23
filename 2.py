# SISTEM KOPERASI PENCATATAN SETORAN
setor1 = int(input("Masukkan setoran pertama: "))
setor2 = int(input("Masukkan setoran kedua: "))
setor3 = int(input("Masukkan setoran ketiga: "))

# Validasi input
if setor1 <= 0 or setor2 <= 0 or setor3 <= 0:
    print("Input tidak valid bos.")
else:
    total = setor1 + setor2 + setor3
    print("Total setoran:", total)

    # Menentukan kategori berdasarkan total
    if total < 300000:
        print("Kategori: Rendah")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")
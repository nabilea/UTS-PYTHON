def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung total ongkos kirim berdasarkan kota, berat, dan asuransi."""
    tarif_dasar = {
        "Solo": 10000,
        "Jogja": 12000,
        "Semarang": 15000
    }

    if kota not in tarif_dasar:
        return "Kota tidak tersedia."

    total = tarif_dasar[kota] + 2000 * berat_kg

    if asuransi:
        total += 3000

    return total


# ==== Contoh Pemanggilan ====
print("Ongkir ke Solo (2 kg, tanpa asuransi): Rp", hitung_ongkir(2, "Solo"))
print("Ongkir ke Jogja (3 kg, dengan asuransi): Rp", hitung_ongkir(3, "Jogja", True))

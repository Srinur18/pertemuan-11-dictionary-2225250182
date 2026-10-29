
# ==========================================
# LATIHAN 03 - METHOD DICTIONARY
# Algoritma dan Pemrograman | Pertemuan 11
# ==========================================

mahasiswa = {
    "nama": "Sri Nur Rahmawati",
    "nim": "2225250182",
    "kelas": "3F"
}

print("Daftar key:")
print(list(mahasiswa.keys()))

print("\nDaftar value:")
print(list(mahasiswa.values()))

print("\nPasangan key-value:")
print(list(mahasiswa.items()))

print("\nNilai semester:")
print(mahasiswa.get("semester", "Belum tersedia"))

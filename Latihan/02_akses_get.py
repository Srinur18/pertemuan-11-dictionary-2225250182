
# ==========================================
# LATIHAN 02 - AKSES DAN UPDATE
# Algoritma dan Pemrograman | Pertemuan 11
# ==========================================

mahasiswa = {
    "nama": "Sri Nur Rahmawati",
    "nim": "2225250182",
    "kelas": "3F"
}

print("Nama awal :", mahasiswa["nama"])
print("Kelas awal:", mahasiswa["kelas"])

mahasiswa["kelas"] = "3F"
mahasiswa["semester"] = 3

print("\nData setelah diperbarui:")

for key, value in mahasiswa.items():
    print(f"{key.title():10}: {value}")

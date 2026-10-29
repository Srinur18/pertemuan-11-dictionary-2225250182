
# ==========================================
# LATIHAN 04 - PERULANGAN DICTIONARY
# Algoritma dan Pemrograman | Pertemuan 11
# ==========================================

nilai = {
    "Algoritma": 90,
    "Kalkulus": 85,
    "Geometri": 88,
    "Teori Bilangan": 92
}

print("=" * 42)
print("          DAFTAR NILAI")
print("=" * 42)

for mata_kuliah, skor in nilai.items():
    print(f"{mata_kuliah:20}: {skor}")

rata_rata = sum(nilai.values()) / len(nilai)

print("-" * 42)
print(f"Rata-rata nilai      : {rata_rata:.2f}")
print("=" * 42)

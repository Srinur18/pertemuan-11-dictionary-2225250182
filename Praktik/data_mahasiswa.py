
# ==================================================
# PRAKTIK - PENGOLAHAN DATA MAHASISWA
# Algoritma dan Pemrograman | Pertemuan 11
# Nama : Sri Nur Rahmawati
# NIM  : 2225250182
# Kelas: 3F
# ==================================================


def buat_data_mahasiswa(nama, nim, kelas, nilai):
    """Membentuk data mahasiswa dalam dictionary."""

    return {
        "nama": nama.strip().title(),
        "nim": nim.strip(),
        "kelas": kelas.strip().upper(),
        "nilai": float(nilai)
    }


def tentukan_predikat(nilai):
    """Menentukan predikat berdasarkan nilai."""

    if nilai >= 85:
        return "Sangat Baik"
    elif nilai >= 75:
        return "Baik"
    elif nilai >= 60:
        return "Cukup"
    return "Perlu Peningkatan"


def tampilkan_data(data):
    """Menampilkan data mahasiswa."""

    print("=" * 44)
    print("       HASIL PENGOLAHAN DATA")
    print("=" * 44)
    print(f"Nama     : {data['nama']}")
    print(f"NIM      : {data['nim']}")
    print(f"Kelas    : {data['kelas']}")
    print(f"Nilai    : {data['nilai']:.2f}")
    print(f"Predikat : {tentukan_predikat(data['nilai'])}")
    print("=" * 44)


def main():
    data_mahasiswa = buat_data_mahasiswa(
        "  Sri Nur Rahmawati  ",
        " 2225250182 ",
        " 3f ",
        90
    )

    tampilkan_data(data_mahasiswa)


if __name__ == "__main__":
    main()

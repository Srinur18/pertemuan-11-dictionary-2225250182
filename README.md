# Pertemuan 11 — Dictionary/Map dalam Python

## 1. Nama, NIM, dan Kelas

- **Nama:** Sri Nur Rahmawati
- **NIM:** 2225250182
- **Kelas:** 3F

## 2. Tujuan

- Memahami struktur data dictionary dalam Python.
- Menggunakan pasangan key-value untuk menyimpan data.
- Mengakses, menambahkan, dan memperbarui data berdasarkan key.
- Mengolah data menggunakan perulangan dan fungsi.
- Menguji program serta mengelola kode menggunakan VS Code dan GitHub.

## 3. Struktur Program

```text
pertemuan-11-dictionary-2225250013/
├── README.md
├── .gitignore
├── latihan/
└── praktik/
    └── data_mahasiswa.py
```

Program utama berada pada `praktik/data_mahasiswa.py`. Folder `latihan/` digunakan untuk menyimpan latihan dictionary sesuai pengerjaan.

## 4. Cara Menjalankan

Pastikan Python sudah terpasang dan terminal berada di direktori proyek.

```bash
python3 praktik/data_mahasiswa.py
```

## 5. Algoritma

1. Membuat dictionary untuk menyimpan data mahasiswa dengan NIM sebagai key.
2. Menyimpan informasi mahasiswa sebagai value.
3. Mengakses data berdasarkan NIM.
4. Memeriksa keberadaan key sebelum menampilkan data.
5. Memperbarui nilai mahasiswa berdasarkan NIM.
6. Menambahkan data mahasiswa baru ke dictionary.
7. Menggunakan `items()` untuk menampilkan seluruh pasangan key-value.
8. Menghitung rata-rata nilai berdasarkan data yang tersimpan.
9. Menampilkan hasil pengolahan data.

## 6. Test Case

| No. | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Mencari NIM `A999` yang tidak tersedia | Program menampilkan pesan bahwa data tidak ditemukan. |
| 2 | Mengubah nilai mahasiswa dengan NIM `A002` menjadi `82` | Nilai mahasiswa berubah menjadi `82`. |
| 3 | Menambahkan mahasiswa dengan NIM `A006` | Data `A006` tersimpan dan dapat diakses. |
| 4 | Menampilkan seluruh data menggunakan `items()` | Seluruh pasangan NIM dan data mahasiswa ditampilkan. |
| 5 | Menghitung rata-rata nilai | Rata-rata sesuai dengan nilai yang tersimpan dalam dictionary. |

## 7. Refleksi

Melalui kegiatan ini, saya memahami bahwa dictionary dapat menyimpan data dalam pasangan key-value sehingga data dapat diakses menggunakan key tertentu. Saya juga mempelajari cara menambahkan dan memperbarui data, menampilkan seluruh isi dictionary, serta menghitung rata-rata nilai. Kesalahan saat mengakses key perlu diperhatikan dengan memastikan key tersedia sebelum digunakan.
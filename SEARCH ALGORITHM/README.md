penjelasan tentang search algorithm
# Search Algorithm

## 1. Pengertian
Search Algorithm adalah algoritma yang digunakan untuk mencari data tertentu di dalam sekumpulan data berdasarkan nilai atau kriteria yang ditentukan. Algoritma ini membantu menemukan data yang dibutuhkan secara lebih efektif dan efisien.

## 2. Jenis-Jenis Search Algorithm

### A. Linear Search
Linear Search adalah metode pencarian yang memeriksa setiap elemen data secara berurutan, mulai dari elemen pertama hingga data yang dicari ditemukan atau seluruh data telah diperiksa.

- **Kelebihan:** Sederhana dan dapat digunakan pada data yang belum terurut.
- **Kekurangan:** Membutuhkan waktu lebih lama jika jumlah data besar.
- **Kompleksitas waktu:** \(O(n)\).

### B. Binary Search
Binary Search adalah metode pencarian yang membagi ruang pencarian menjadi dua bagian secara berulang. Algoritma ini membandingkan nilai yang dicari dengan elemen tengah, kemudian melanjutkan pencarian pada bagian yang sesuai.

- **Kelebihan:** Lebih cepat untuk mencari data dalam jumlah besar.
- **Kekurangan:** Data harus dalam keadaan terurut.
- **Kompleksitas waktu:** \(O(\log n)\).

## 3. Perbedaan Linear Search dan Binary Search

| Aspek | Linear Search | Binary Search |
|---|---|---|
| Metode | Memeriksa satu per satu | Membagi pencarian menjadi dua |
| Data terurut | Tidak wajib | Wajib |
| Kompleksitas waktu | \(O(n)\) | \(O(\log n)\) |
| Penggunaan | Data sederhana atau belum terurut | Data terurut |

## 4. Kesimpulan
Search Algorithm merupakan bagian penting dalam pemrograman untuk menemukan data yang dibutuhkan. Linear Search cocok digunakan untuk data sederhana atau belum terurut, sedangkan Binary Search lebih efisien untuk data yang sudah terurut dan berjumlah besar.

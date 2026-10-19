# Expert System (Sistem Pakar)


## 1. Pengertian Expert System

Expert System atau sistem pakar adalah sistem komputer yang dirancang untuk meniru kemampuan seorang ahli dalam menganalisis masalah dan mengambil keputusan berdasarkan pengetahuan serta aturan tertentu. Sistem ini merupakan salah satu penerapan kecerdasan buatan (*Artificial Intelligence* atau AI) yang dapat membantu pengguna menyelesaikan masalah dalam bidang kesehatan, pendidikan, pertanian, dan teknologi komputer.

## 2. Tujuan Expert System

Tujuan Expert System adalah membantu pengguna memperoleh solusi atau rekomendasi berdasarkan pengetahuan yang telah dimasukkan ke dalam sistem. Sistem ini juga bertujuan mempermudah proses pengambilan keputusan, meningkatkan konsistensi hasil analisis, dan menyediakan akses terhadap pengetahuan seorang ahli.

## 3. Komponen Expert System

Expert System memiliki beberapa komponen utama, yaitu:

- **Knowledge Base:** Menyimpan pengetahuan, fakta, dan aturan yang digunakan untuk menyelesaikan masalah.
- **Inference Engine:** Memproses informasi dan menerapkan aturan untuk menghasilkan kesimpulan.
- **User Interface:** Menjadi penghubung antara pengguna dan sistem.
- **Explanation Facility:** Memberikan penjelasan mengenai alasan sistem menghasilkan suatu kesimpulan.

## 4. Cara Kerja Expert System

Cara kerja Expert System dimulai ketika pengguna memasukkan informasi atau gejala yang dialami. Informasi tersebut kemudian diproses oleh Inference Engine dengan mencocokkannya terhadap pengetahuan dan aturan yang tersimpan dalam Knowledge Base. Setelah proses pencocokan selesai, sistem menghasilkan kesimpulan atau rekomendasi yang ditampilkan kepada pengguna.

## 5. Metode Penalaran Expert System

Expert System umumnya menggunakan dua metode penalaran, yaitu:

- **Forward Chaining:** Proses penalaran dimulai dari fakta yang tersedia, kemudian aturan diterapkan untuk memperoleh kesimpulan.
- **Backward Chaining:** Proses penalaran dimulai dari kesimpulan atau hipotesis yang ingin dibuktikan, kemudian sistem mencari fakta yang mendukung kesimpulan tersebut.

## 6. Kelebihan Expert System

- Memberikan rekomendasi secara cepat.
- Menghasilkan keputusan yang konsisten berdasarkan aturan yang sama.
- Menyimpan pengetahuan yang dapat digunakan berulang kali.
- Membantu pengguna menganalisis masalah.
- Dapat digunakan kapan saja selama sistem tersedia.

## 7. Kekurangan Expert System

- Hasil bergantung pada kualitas pengetahuan dan aturan yang dimasukkan.
- Sulit menangani masalah baru yang belum tercakup dalam aturan.
- Membutuhkan waktu dan keahlian untuk mengembangkan sistem.
- Knowledge Base perlu diperbarui agar tetap akurat dan relevan.

## 8. Contoh Penerapan Expert System

Expert System dapat diterapkan dalam berbagai bidang. Dalam bidang kesehatan, sistem dapat membantu melakukan penilaian awal berdasarkan gejala pengguna. Dalam bidang pertanian, sistem dapat membantu mengidentifikasi kemungkinan masalah tanaman. Dalam bidang teknologi komputer, sistem dapat menganalisis gangguan berdasarkan gejala seperti komputer tidak menyala, kinerja lambat, atau masalah koneksi internet.

## 9. Implementasi Expert System Menggunakan Python

Contoh berikut merupakan sistem pakar sederhana untuk mengidentifikasi kemungkinan masalah komputer berdasarkan gejala yang dimasukkan pengguna.

### Kode Program

```python
# Expert System: Deteksi Masalah Komputer

def sistem_pakar():
    print("=== SISTEM PAKAR DETEKSI MASALAH KOMPUTER ===")
    print("Jawab pertanyaan dengan ya atau tidak.\n")

    tidak_nyala = input(
        "Apakah komputer tidak bisa menyala? "
    ).lower()

    lambat = input(
        "Apakah komputer berjalan lambat? "
    ).lower()

    panas = input(
        "Apakah komputer terasa panas? "
    ).lower()

    internet = input(
        "Apakah komputer tidak bisa terhubung ke internet? "
    ).lower()

    print("\n=== HASIL DIAGNOSIS ===")

    if tidak_nyala == "ya":
        print("Kemungkinan masalah: Catu daya atau baterai.")
        print("Saran: Periksa kabel daya dan sambungan listrik.")

    elif panas == "ya":
        print("Kemungkinan masalah: Panas berlebih.")
        print("Saran: Periksa ventilasi dan kebersihan kipas.")

    elif lambat == "ya":
        print("Kemungkinan masalah: Beban aplikasi atau memori.")
        print("Saran: Tutup aplikasi yang tidak diperlukan.")

    elif internet == "ya":
        print("Kemungkinan masalah: Koneksi jaringan.")
        print("Saran: Periksa Wi-Fi atau kabel jaringan.")

    else:
        print("Masalah belum dapat diidentifikasi.")
        print("Saran: Periksa komputer lebih lanjut.")


sistem_pakar()
```

### Contoh Output

```text
=== SISTEM PAKAR DETEKSI MASALAH KOMPUTER ===
Jawab pertanyaan dengan ya atau tidak.

Apakah komputer tidak bisa menyala? tidak
Apakah komputer berjalan lambat? ya
Apakah komputer terasa panas? tidak
Apakah komputer tidak bisa terhubung ke internet? tidak

=== HASIL DIAGNOSIS ===
Kemungkinan masalah: Beban aplikasi atau memori.
Saran: Tutup aplikasi yang tidak diperlukan.
```

### Penjelasan Program

Program menerima jawaban pengguna sebagai fakta, kemudian menggunakan struktur `if-elif-else` untuk mencocokkan fakta dengan aturan yang telah ditentukan. Setiap aturan menghubungkan gejala dengan kemungkinan masalah dan saran penanganan. Hasil yang ditampilkan merupakan perkiraan berdasarkan aturan sederhana, bukan diagnosis teknis yang pasti.

## 10. Perbedaan Expert System dan Multi-Agent System

Expert System berfokus pada penggunaan pengetahuan dan aturan untuk menghasilkan kesimpulan atau rekomendasi. Sementara itu, Multi-Agent System terdiri dari beberapa agen yang menjalankan tugas berbeda dan berinteraksi untuk mencapai tujuan tertentu. Expert System menitikberatkan pada penalaran berbasis pengetahuan, sedangkan Multi-Agent System menitikberatkan pada interaksi dan koordinasi antaragen.

## 11. Kesimpulan

Expert System merupakan salah satu penerapan kecerdasan buatan yang dirancang untuk meniru kemampuan penalaran seorang ahli dalam menyelesaikan masalah tertentu. Sistem ini memanfaatkan Knowledge Base dan Inference Engine untuk memproses fakta, menerapkan aturan, dan menghasilkan rekomendasi. Meskipun memiliki keterbatasan dalam menghadapi masalah yang belum tercakup dalam aturan, Expert System tetap bermanfaat untuk membantu analisis dan pengambilan keputusan.

## 12. Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Simpan kode program ke dalam file bernama `expert_system.py`.
3. Buka terminal atau Command Prompt pada folder tempat file disimpan.
4. Jalankan perintah berikut:

   ```bash
   python expert_system.py
   ```

5. Jawab pertanyaan yang muncul dengan mengetik `ya` atau `tidak`.
6. Sistem akan menampilkan kemungkinan masalah dan saran penanganannya.



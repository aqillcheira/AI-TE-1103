# Multi-Agent System (MAS)

## 1. Pengertian

Multi-Agent System (MAS) adalah sistem yang terdiri dari beberapa agen yang bekerja secara mandiri dan berinteraksi satu sama lain untuk mencapai tujuan tertentu. Setiap agen memiliki tugas dan tanggung jawab yang berbeda, tetapi dapat bekerja sama untuk menyelesaikan suatu masalah. MAS banyak digunakan dalam bidang kecerdasan buatan (*Artificial Intelligence*), robotika, dan otomatisasi.

## 2. Komponen Multi-Agent System

Komponen utama Multi-Agent System terdiri dari agen, komunikasi, lingkungan, dan koordinasi. Agen merupakan entitas yang menjalankan tugas tertentu secara mandiri. Komunikasi digunakan untuk bertukar informasi antaragen, sedangkan lingkungan merupakan tempat agen bekerja dan memperoleh informasi. Koordinasi berfungsi mengatur pembagian tugas agar setiap agen dapat bekerja secara efektif untuk mencapai tujuan bersama.

## 3. Cara Kerja

Multi-Agent System bekerja dengan membagi suatu permasalahan menjadi beberapa tugas yang ditangani oleh agen berbeda. Setiap agen menerima informasi, memproses data sesuai tugasnya, dan bertukar informasi dengan agen lain jika diperlukan. Hasil dari setiap agen kemudian digunakan untuk menghasilkan keputusan atau menyelesaikan masalah secara keseluruhan.

## 4. Jenis-Jenis Multi-Agent System

- **Cooperative MAS:** Agen bekerja sama untuk mencapai tujuan bersama.
- **Competitive MAS:** Agen memiliki tujuan yang berbeda atau saling bersaing.
- **Hybrid MAS:** Menggabungkan kerja sama dan persaingan antaragen.
- **Hierarchical MAS:** Agen diatur berdasarkan tingkatan atau pembagian wewenang.

## 5. Kelebihan

- Pembagian tugas menjadi lebih terstruktur.
- Mampu menangani masalah yang kompleks.
- Memungkinkan beberapa tugas dilakukan secara bersamaan.
- Fleksibel dan mudah dikembangkan sesuai kebutuhan.

## 6. Kekurangan

- Komunikasi dan koordinasi antaragen dapat menjadi rumit.
- Membutuhkan sumber daya komputasi tambahan.
- Kesalahan informasi dapat memengaruhi hasil sistem.
- Konflik keputusan dapat terjadi antaragen.

## 7. Contoh Penerapan

Multi-Agent System dapat diterapkan dalam berbagai bidang, seperti robotika, transportasi, pertanian pintar, dan kecerdasan buatan. Contohnya, beberapa robot gudang dapat bekerja sama untuk memindahkan barang, agen lalu lintas dapat mengatur lampu berdasarkan kepadatan kendaraan, dan agen pertanian dapat memantau kelembapan tanah serta membantu mengatur penyiraman tanaman.

## 8. Implementasi Menggunakan Python

Contoh implementasi berikut menggunakan tiga agen untuk menentukan kelulusan mahasiswa.

### Kode Program

```python
class DataAgent:
    def bekerja(self):
        return [80, 75, 90, 85, 70]


class AnalysisAgent:
    def bekerja(self, nilai):
        return sum(nilai) / len(nilai)


class DecisionAgent:
    def bekerja(self, rata_rata):
        if rata_rata >= 75:
            return "LULUS"
        return "TIDAK LULUS"


# Membuat agen
data = DataAgent()
analisis = AnalysisAgent()
keputusan = DecisionAgent()

# Menjalankan agen
nilai = data.bekerja()
rata_rata = analisis.bekerja(nilai)
hasil = keputusan.bekerja(rata_rata)

# Menampilkan hasil
print("Nilai:", nilai)
print("Rata-rata:", rata_rata)
print("Status:", hasil)
```

### Contoh Output

```text
Nilai: [80, 75, 90, 85, 70]
Rata-rata: 80.0
Status: LULUS
```

### Penjelasan Program

1. **DataAgent** bertugas menyediakan data nilai mahasiswa.
2. **AnalysisAgent** menghitung rata-rata dari data nilai.
3. **DecisionAgent** menentukan status kelulusan berdasarkan rata-rata nilai.
4. Hasil dari setiap agen digunakan oleh agen berikutnya hingga menghasilkan keputusan akhir.

Program ini merupakan simulasi dasar Multi-Agent System menggunakan beberapa objek Python dengan tugas berbeda. Program belum menggunakan agen AI otonom atau mekanisme komunikasi antaragen yang kompleks.

## 9. Kesimpulan

Multi-Agent System merupakan pendekatan komputasi yang memanfaatkan beberapa agen untuk bekerja secara mandiri maupun bersama-sama dalam menyelesaikan suatu masalah. Setiap agen memiliki peran tertentu yang saling mendukung melalui pembagian tugas, komunikasi, dan koordinasi. Sistem ini menjadi salah satu pendekatan penting dalam pengembangan kecerdasan buatan dan otomatisasi modern.

## 10. Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Simpan kode program dalam file `multi_agent_system.py`.
3. Buka terminal pada folder tempat file disimpan.
4. Jalankan perintah berikut:

   ```bash
   python multi_agent_system.py
   ```

5. Hasil program akan ditampilkan di terminal.

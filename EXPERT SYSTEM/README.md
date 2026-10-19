## 🧠 Expert System (Sistem Pakar) & Knowledge Base Visualization

Dalam proyek ini, program Python berfungsi sebagai sebuah **Sistem Pakar (Expert System)** sederhana yang meniru cara berpikir seorang ahli pertanian (pakar irigasi). Sistem ini mengambil keputusan kapan dan berapa lama pompa harus menyala secara otomatis berdasarkan tingkat kelembapan tanah, dengan menerapkan **Logika Fuzzy Metode Sugeno Orde Nol**.

---

### 1. Pengertian Visualisasi Sistem Pakar
Visualisasi Sistem Pakar menggambarkan bagaimana pengetahuan dari seorang pakar (*Knowledge Base*) diterjemahkan kedalam fungsi matematika dan aturan logika formal (*Inference Engine*). 

Komponen utama sistem pakar dalam skrip ini meliputi:
* **Basis Pengetahuan (*Knowledge Base*):** Berisi fungsi keanggotaan linier (`fuzzy_dry`, `fuzzy_moist`, `fuzzy_wet`) yang mendefinisikan batasan kondisi tanah (kering, lembap, basah).
* **Mesin Inferensi (*Inference Engine*):** Fungsi `fuzzy_control()` yang mengevaluasi nilai kelembapan masukan menggunakan metode Sugeno untuk menghasilkan keputusan kuantitatif.
* **Basis Aksi/Antarmuka (*User Interface / Actuator*):** Mengambil hasil keputusan pakar untuk mengontrol durasi penyiraman secara real-time.

---

### 2. Cara Kerja & Alur Keputusan Pakar

Ilustrasi visualisasi alur penalaran sistem pakar dari input sensor hingga eksekusi keputusan:

```text
       [ Nilai Input Sensor (ADC: 650) ]
                      │
                      ▼
       [ Konversi ke Persentase Kelembapan (37.5%) ]
                      │
                      ├─► Apakah Kering?  (fuzzy_dry)   ──► Bobot: 0.625
                      ├─► Apakah Lembap? (fuzzy_moist)  ──► Bobot: 0.300
                      └─► Apakah Basah?   (fuzzy_wet)   ──► Bobot: 0.000
                      │
                      ▼
       [ Mesin Inferensi: Sugeno Orde Nol ]
       Output = (0.625 * 100% + 0.300 * 45% + 0.0 * 0%) / Total Bobot
                      │
                      ▼
       [ Keputusan Pakar: Output Fuzzy = 75.8% ]
                      │
           ┌──────────┴──────────┐
           ▼                     ▼
     (Jika < 15%)          (Jika >= 15%)
     Status: OFF         Durasi Pompa: 3790 ms

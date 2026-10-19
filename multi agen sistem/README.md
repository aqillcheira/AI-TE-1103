## 🤖 Multi-Agent System (MAS) Architecture & Visualization

Dalam implementasi berbasis skrip berorientasi objek ini, sistem irigasi dipecah ke dalam arsitektur **Multi-Agent System (MAS)**. Alih-alih menjalankan seluruh proses dalam satu fungsi tunggal, tugas sistem dibagi ke dalam entitas otonom (*agen*) yang memiliki peran spesifik dan dikoordinasikan secara terpusat oleh agen pengawas (*supervisor*).

---

### 1. Pengertian Visualisasi Multi-Agent System
Visualisasi Multi-Agent System menggambarkan bagaimana sekumpulan modul independen yang memiliki kecerdasan dan tugas masing-masing saling berkomunikasi dan bertukar data untuk menyelesaikan masalah yang kompleks. 

Berdasarkan struktur kode di atas, sistem ini dibagi menjadi 4 kelas agen utama:
1. **Sensor Agent (`SensorAgent`):** Berperan sebagai agen pemantau lingkungan yang bertugas membaca data input mentah dari sensor kelembapan tanah (ADC) dan mengubahnya menjadi nilai persentase bermakna.
2. **Fuzzy Logic Agent (`FuzzyLogicAgent`):** Berperan sebagai agen pakar (*expert/reasoning agent*) yang memproses tingkat kelembapan menggunakan fungsi keanggotaan Sugeno orde nol untuk menghasilkan keputusan kendali.
3. **Actuator Agent (`ActuatorAgent`):** Berperan sebagai agen eksekutor fisik yang menerjemahkan hasil keputusan pakar menjadi tindakan nyata pada perangkat keras (menyalakan/mematikan pompa dan mengatur waktu peresapan air).
4. **Supervisor Agent (`IrrigationSupervisorAgent`):** Berperan sebagai agen koordinator pusat yang mengatur ritme komunikasi, urutan eksekusi siklus (*run cycle*), dan jeda waktu sampling antar-agen.

---

### 2. Cara Kerja & Alur Komunikasi Antar-Agent

Ilustrasi visualisasi alur pertukaran pesan dan data dalam satu siklus eksekusi sistem multi-agen:

```text
 ┌─────────────────────────────────────────────────────────────┐
 │                IrrigationSupervisorAgent                    │
 │               (Pengatur Siklus & Koordinasi)                │
 └──────┬──────────────────────┬───────────────────────┬───────┘
        │                      │                       │
        │ 1. Minta Data        │ 2. Evaluasi Nilai     │ 3. Eksekusi Aksi
        ▼                      ▼                       ▼
 ┌──────────────┐       ┌──────────────┐        ┌──────────────┐
 │ SensorAgent  │       │ FuzzyAgent   │        │ ActuatorAgent│
 │ (Baca ADC &  │──────►│ (Hitung      │───────►│ (Kontrol     │
 │  Konversi)   │ Data  │  Sugeno)     │ Output │  Pompa/Relay)│
 └──────────────┘       └──────────────┘        └──────────────┘

## 🤖 Multi-Agent System (MAS) Architecture & Visualization

Meskipun implementasi kode di atas berjalan dalam struktur *loop* prosedural tunggal, pendekatan konseptualnya dapat dipetakan dan diskalakan ke dalam arsitektur **Multi-Agent System (MAS)**. Dalam paradigma MAS, sistem dibagi menjadi beberapa entitas otonom (*agen*) yang memiliki tugas spesifik dan saling berkoordinasi untuk mencapai tujuan bersama: menjaga tingkat kelembapan tanah secara optimal.

---

### 1. Pengertian Visualisasi Multi-Agent System
Visualisasi MAS menggambarkan bagaimana proses kontrol irigasi didelegasikan ke dalam klaster agen mandiri yang berinteraksi dalam satu lingkungan terdistribusi. Setiap agen dalam sistem ini bertindak sebagai modul yang independen namun saling mengirimkan data:
* **Sensor Agent:** Bertanggung jawab membaca kondisi lingkungan (kelembapan tanah).
* **Fuzzy Logic Agent (Pakar):** Berperan sebagai agen pemikir yang memproses data dan mengambil keputusan (*decision-making*).
* **Actuator Agent:** Bertindak sebagai eksekutor fisik (mengontrol pompa air/relay).
* **Supervisor/Coordinator Agent:** Mengatur sinkronisasi alur kerja dan penjadwalan siklus antar-agen.

---

### 2. Cara Kerja & Alur Komunikasi Antar-Agent

Ilustrasi visualisasi komunikasi dan pertukaran pesan antar-agen dalam siklus eksekusi program:

```text
 ┌──────────────────────┐
 │    Sensor Agent      │ ──(Mengirim Data Mentah / ADC: 650)──┐
 └──────────────────────┘                                       │
                                                                ▼
 ┌──────────────────────┐                             ┌───────────────────┐
 │     Actuator Agent   │ ◄──(Menerima Keputusan Aksi)─ │ Coordinator Agent │
 └──────────────────────┘                             └───────────────────┘
            ▲                                                   │
            │ (Memerintahkan Pompa ON/OFF & Soaking)            │
            │                                                   ▼
                                                      ┌───────────────────┐
                                                      │ Fuzzy Logic Agent │
                                                      │  (Pakar Evaluasi) │
                                                      └───────────────────┘

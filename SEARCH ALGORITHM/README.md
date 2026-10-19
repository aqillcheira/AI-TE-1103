## 🔍 Search & Optimization Algorithm (Fuzzy Logic Evaluation)

Meskipun sistem ini beroperasi menggunakan logika fuzzy (bukan algoritma pencarian jalur graf seperti *A\** atau *Dijkstra*), dalam konteks kecerdasan buatan (*Artificial Intelligence*), fungsi kendali fuzzy dalam skrip ini bertindak sebagai **State Evaluation & Space Search Algorithm** (Algoritma Pencarian dan Evaluasi Ruang Keadaan) untuk mencari titik keputusan optimal dari rentang nilai input sensor.

---

### 1. Pengertian Visualisasi Algoritma Pencarian
Visualisasi algoritma pencarian dalam sistem ini menggambarkan bagaimana program **"menelusuri" ruang kemungkinan (*search space*)** dari tingkat kelembapan tanah ($0\%$ hingga $100\%$) untuk menentukan aksi kontrol pompa yang paling presisi. 

Alih-alih mencari rute fisik, algoritma ini melakukan pencarian nilai dalam fungsi keanggotaan (*Membership Functions*) untuk mengevaluasi tiga kondisi utama:
1. **Kering** (`fuzzy_dry`)
2. **Lembap** (`fuzzy_moist`)
3. **Basah** (`fuzzy_wet`)

---

### 2. Cara Kerja Algoritma (Alur Pencarian Nilai)

Ilustrasi alur pencarian dan evaluasi keputusan dalam skrip:

```text
 [ Input Sensor (ADC: 650) ] 
            │
            ▼
   Konversi ke Persentase (Moisture: 37.5%)
            │
            ├──────► Evaluasi fuzzy_dry(37.5%)   ──► Bobot Kering  = 0.625
            ├──────► Evaluasi fuzzy_moist(37.5%)  ──► Bobot Lembap = 0.300
            └──────► Evaluasi fuzzy_wet(37.5%)    ──► Bobot Basah  = 0.000
            │
            ▼
   [ Proses Inferensi Sugeno Orde Nol ]
   Output = (Dry*100 + Moist*45 + Wet*0) / Total Bobot
            │
            ▼
   [ Keputusan Akhir: Output Fuzzy = 75.8% ] ──► Durasi Pompa ON# AI-TE-1103
Tugas Matkul Kecerdasan Buatan

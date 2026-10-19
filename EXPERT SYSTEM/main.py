


def sistem_pakar():
    print("=== SISTEM PAKAR DETEKSI MASALAH KOMPUTER ===")
    print("Jawab pertanyaan dengan ya atau tidak.\n")

    tidak_nyala = input("Apakah komputer tidak bisa menyala? ").lower()
    lambat = input("Apakah komputer berjalan lambat? ").lower()
    panas = input("Apakah komputer terasa panas? ").lower()
    internet = input("Apakah komputer tidak bisa terhubung ke internet? ").lower()

    print("\n=== HASIL DIAGNOSIS ===")

    if tidak_nyala == "ya":
        print("Kemungkinan masalah: Catu daya atau baterai.")
        print("Saran: Periksa kabel daya dan sambungan listrik.")

    elif panas == "ya":
        print("Kemungkinan masalah: Komputer mengalami panas berlebih.")
        print("Saran: Periksa ventilasi dan kebersihan kipas.")

    elif lambat == "ya":
        print("Kemungkinan masalah: Beban aplikasi atau penggunaan memori tinggi.")
        print("Saran: Tutup aplikasi yang tidak diperlukan.")

    elif internet == "ya":
        print("Kemungkinan masalah: Koneksi jaringan.")
        print("Saran: Periksa Wi-Fi atau kabel jaringan.")

    else:
        print("Masalah belum dapat diidentifikasi.")
        print("Saran: Periksa komputer lebih lanjut.")

sistem_pakar()

import time

try:
    import serial
except ImportError:
    serial = None


# Fungsi keanggotaan: KERING
def fuzzy_dry(x: float) -> float:
    if x <= 30.0:
        return 1.0
    if x >= 50.0:
        return 0.0
    return (50.0 - x) / 20.0


# Fungsi keanggotaan: LEMBAP
def fuzzy_moist(x: float) -> float:
    if x <= 30.0 or x >= 80.0:
        return 0.0
    if x < 55.0:
        return (x - 30.0) / 25.0
    return (80.0 - x) / 25.0


# Fungsi keanggotaan: BASAH
def fuzzy_wet(x: float) -> float:
    if x <= 60.0:
        return 0.0
    if x >= 80.0:
        return 1.0
    return (x - 60.0) / 20.0


# Fuzzy Sugeno orde nol:
# Kering = 100%, Lembap = 45%, Basah = 0%
def fuzzy_control(moisture: float) -> float:
    dry = fuzzy_dry(moisture)
    moist = fuzzy_moist(moisture)
    wet = fuzzy_wet(moisture)

    total = dry + moist + wet

    if total <= 0.0:
        return 0.0

    output = (dry * 100.0 + moist * 45.0 + wet * 0.0) / total

    return output


def main():
    # Konstanta kalibrasi sensor dan sistem
    SENSOR_DRY = 800  # Nilai saat tanah kering
    SENSOR_WET = 350  # Nilai saat tanah basah

    MAX_PUMP_MS = 5000.0
    SAMPLE_INTERVAL = 5.0  # dalam detik
    SOAK_TIME = 30.0  # dalam detik

    print("Sistem Irigasi Fuzzy Logic (Python)")

    # Contoh simulasi loop utama
    # Jika menggunakan pembacaan serial dari Arduino, aktifkan kode PySerial di bawah:
    # ser = serial.Serial('COM3', 9600)

    try:
        while True:
            start_time = time.time()

            # --- Bagian ini bisa diganti dengan pembacaan sensor fisik / Serial ---
            # Contoh dummy nilai raw ADC dari sensor:
            raw = 650
            # ---------------------------------------------------------------------

            # Konversi nilai sensor ke persentase kelembapan
            moisture = (
                100.0
                * (SENSOR_DRY - raw)
                / float(SENSOR_DRY - SENSOR_WET)
            )
            moisture = max(0.0, min(100.0, moisture))  # Batasi 0 - 100

            # Hitung keputusan fuzzy
            output = fuzzy_control(moisture)

            print(f"ADC: {raw} | Kelembapan: {moisture:.1f}% | Output fuzzy: {output:.1f}%")

            # Tanah cukup basah: pompa tetap mati
            if moisture >= 70.0 or output < 15.0:
                print("Pompa: OFF\n")
            else:
                # Durasi pompa disesuaikan output fuzzy
                pump_time = (output / 100.0) * (MAX_PUMP_MS / 1000.0)  # dalam detik

                if pump_time > 0:
                    print(f"Pompa ON selama {pump_time * 1000:.0f} ms")
                    # Simulasi Relay ON (misal menggunakan GPIO Raspberry Pi / aktuator lain)
                    time.sleep(pump_time)
                    print("Pompa OFF - menunggu air meresap\n")
                    time.sleep(SOAK_TIME)

            # Jeda sesuai interval sampling
            elapsed = time.time() - start_time
            if elapsed < SAMPLE_INTERVAL:
                time.sleep(SAMPLE_INTERVAL - elapsed)

    except KeyboardInterrupt:
        print("\nSistem dihentikan oleh pengguna.")


if __name__ == "__main__":
    main()

import time
import random
from typing import Dict, Any

# ==========================================
# 1. SENSOR AGENT
# ==========================================
class SensorAgent:
    def __init__(self, sensor_dry: int = 800, sensor_wet: int = 350):
        self.sensor_dry = sensor_dry
        self.sensor_wet = sensor_wet

    def read_soil_moisture(self) -> Dict[str, Any]:
        """Membaca nilai sensor ADC (disimulasikan acak untuk demo) dan mengkonversinya ke %"""
        raw_adc = random.randint(400, 750) # Simulasi fluktuasi kelembapan tanah
        
        # Konversi ke persentase kelembapan (0% = kering, 100% = basah)
        moisture = 100.0 * (self.sensor_dry - raw_adc) / float(self.sensor_dry - self.sensor_wet)
        moisture = max(0.0, min(100.0, moisture))
        
        return {
            "raw_adc": raw_adc,
            "moisture_percent": round(moisture, 1)
        }


# ==========================================
# 2. FUZZY LOGIC AGENT (Pakar)
# ==========================================
class FuzzyLogicAgent:
    def _fuzzy_dry(self, x: float) -> float:
        if x <= 30.0: return 1.0
        if x >= 50.0: return 0.0
        return (50.0 - x) / 20.0

    def _fuzzy_moist(self, x: float) -> float:
        if x <= 30.0 or x >= 80.0: return 0.0
        if x < 55.0: return (x - 30.0) / 25.0
        return (80.0 - x) / 25.0

    def _fuzzy_wet(self, x: float) -> float:
        if x <= 60.0: return 0.0
        if x >= 80.0: return 1.0
        return (x - 60.0) / 20.0

    def evaluate(self, moisture: float) -> float:
        """Fuzzy Sugeno Orde Nol: Menghitung persentase output daya/durasi pompa"""
        dry = self._fuzzy_dry(moisture)
        moist = self._fuzzy_moist(moisture)
        wet = self._fuzzy_wet(moisture)

        total = dry + moist + wet
        if total <= 0.0:
            return 0.0

        # Aturan Sugeno: Kering = 100%, Lembap = 45%, Basah = 0%
        output = (dry * 100.0 + moist * 45.0 + wet * 0.0) / total
        return round(output, 1)


# ==========================================
# 3. ACTUATOR AGENT (Pompa / Relay)
# ==========================================
class ActuatorAgent:
    def __init__(self, max_pump_ms: float = 5000.0):
        self.max_pump_ms = max_pump_ms

    def execute_action(self, moisture: float, fuzzy_output: float) -> None:
        """Mengontrol status pompa berdasarkan keputusan agen fuzzy"""
        if moisture >= 70.0 or fuzzy_output < 15.0:
            print("[Actuator Agent] Status Pompa: OFF (Tanah sudah cukup basah)")
        else:
            pump_time_sec = (fuzzy_output / 100.0) * (self.max_pump_ms / 1000.0)
            if pump_time_sec > 0:
                print(f"[Actuator Agent] Status Pompa: ON selama {pump_time_sec * 1000:.0f} ms")
                time.sleep(pump_time_sec)
                print("[Actuator Agent] Status Pompa: OFF - Memasuki waktu soaking (meresap)\n")


# ==========================================
# 4. COORDINATOR / SUPERVISOR AGENT
# ==========================================
class IrrigationSupervisorAgent:
    def __init__(self):
        self.sensor_agent = SensorAgent()
        self.fuzzy_agent = FuzzyLogicAgent()
        self.actuator_agent = ActuatorAgent()

    def run_cycle(self):
        print("--- [Supervisor] Memulai Siklus Pemantauan Multi-Agent ---")
        
        # 1. Perintah ke Sensor Agent
        sensor_data = self.sensor_agent.read_soil_moisture()
        print(f"[Sensor Agent] Data diterima -> ADC: {sensor_data['raw_adc']} | Kelembapan: {sensor_data['moisture_percent']}%")

        # 2. Perintah ke Fuzzy Logic Agent
        fuzzy_output = self.fuzzy_agent.evaluate(sensor_data['moisture_percent'])
        print(f"[Fuzzy Agent] Keputusan pakar -> Output kontrol: {fuzzy_output}%")

        # 3. Perintah ke Actuator Agent
        self.actuator_agent.execute_action(sensor_data['moisture_percent'], fuzzy_output)


def main():
    supervisor = IrrigationSupervisorAgent()
    print("=== SISTEM IRIGASI OTOMATIS MULTI-AGENT BERBASIS FUZZY LOGIC ===")
    
    try:
        while True:
            supervisor.run_cycle()
            print("[Supervisor] Menunggu siklus sampling berikutnya (5 detik)...\n")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nSistem Multi-Agent dihentikan oleh pengguna.")

if __name__ == "__main__":
    main()

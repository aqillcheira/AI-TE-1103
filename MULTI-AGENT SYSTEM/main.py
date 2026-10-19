
# Multi-Agent System sederhana

class DataAgent:
    def get_data(self):
        print("[Data Agent] Mengambil data nilai...")
        return [80, 75, 90, 85, 70]


class AnalysisAgent:
    def analyze(self, nilai):
        print("[Analysis Agent] Menghitung rata-rata...")
        return sum(nilai) / len(nilai)


class DecisionAgent:
    def decide(self, rata_rata):
        print("[Decision Agent] Menentukan hasil...")
        if rata_rata >= 75:
            return "LULUS"
        else:
            return "TIDAK LULUS"


# Menjalankan setiap agen
data_agent = DataAgent()
analysis_agent = AnalysisAgent()
decision_agent = DecisionAgent()

nilai = data_agent.get_data()
rata_rata = analysis_agent.analyze(nilai)
hasil = decision_agent.decide(rata_rata)

print("\n=== HASIL SISTEM ===")
print("Nilai:", nilai)
print("Rata-rata:", rata_rata)
print("Status:", hasil)

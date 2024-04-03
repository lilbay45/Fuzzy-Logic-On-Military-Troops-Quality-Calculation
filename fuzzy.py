import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd

# Baca data dari file CSV dengan delimiter koma
flpath=r"C:\Users\bainu\Downloads\fuzzz\data_pasukan.xlsx"
data = pd.read_excel(flpath)
print(data.shape)


# Definisikan Input variabel
intensitas_latihan = ctrl.Antecedent(np.arange(0, 101, 1), "intensitas_latihan")
kursus_kemampuan = ctrl.Antecedent(np.arange(0, 101, 1), "kursus_kemampuan")
kebugaran_fisik = ctrl.Antecedent(np.arange(0, 101, 1), "kebugaran_fisik")

# Definisikan Output Variable
kualitas_pasukan = ctrl.Consequent(np.arange(0, 101, 1), "kualitas_pasukan")

# Definisikan fungsi keanggotaan untuk variabel input dan output
intensitas_latihan.automf(3)
kursus_kemampuan.automf(3)
kebugaran_fisik.automf(3)

# Fungsi keanggotaan untuk variabel kualitas pasukan
kualitas_pasukan["rendah"] = fuzz.trimf(kualitas_pasukan.universe, [0, 25, 50])
kualitas_pasukan["sedang"] = fuzz.trimf(kualitas_pasukan.universe, [40, 60, 80])
kualitas_pasukan["tinggi"] = fuzz.trimf(kualitas_pasukan.universe, [75, 90, 100])

# Rules
rule1 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["poor"] & kebugaran_fisik["poor"], kualitas_pasukan["rendah"])
rule2 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["poor"] & kebugaran_fisik["average"], kualitas_pasukan["rendah"])
rule3 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["poor"] & kebugaran_fisik["good"], kualitas_pasukan["sedang"])
rule4 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["average"] & kebugaran_fisik["poor"], kualitas_pasukan["rendah"])
rule5 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["average"] & kebugaran_fisik["average"], kualitas_pasukan["sedang"])
rule6 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["average"] & kebugaran_fisik["good"], kualitas_pasukan["sedang"])
rule7 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["good"] & kebugaran_fisik["poor"], kualitas_pasukan["sedang"])
rule8 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["good"] & kebugaran_fisik["average"], kualitas_pasukan["tinggi"])
rule9 = ctrl.Rule(intensitas_latihan["poor"] & kursus_kemampuan["good"] & kebugaran_fisik["good"], kualitas_pasukan["tinggi"])


# Control System
kualitas_pasukan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
kualitas_pasukan = ctrl.ControlSystemSimulation(kualitas_pasukan_ctrl)

# Inisialisasi list untuk menyimpan hasil
hasil_kualitas_pasukan = []


# Iterasi melalui setiap record dalam data
for index, row in data.iterrows():
    # Masukkan nilai variabel input dari data yang dibaca
    kualitas_pasukan.input['intensitas_latihan'] = row['intensitaslatihan']
    kualitas_pasukan.input['kursus_kemampuan'] = row['kursuskemampuan']
    kualitas_pasukan.input['kebugaran_fisik'] = row['kebugaranfisik']

    # Hitung nilai variabel output
    kualitas_pasukan.compute()

    # Simpan hasil
    hasil_kualitas_pasukan.append(kualitas_pasukan.output['kualitas_pasukan'])

# Tambahkan hasil ke data frame
data['hasil_tingkat_kehebatan'] = hasil_kualitas_pasukan

# Simpan ke file Excel
data.to_excel('hasil_kualitaspasukan.xlsx', index=False)

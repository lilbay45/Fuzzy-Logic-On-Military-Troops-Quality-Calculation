# Fuzzy-Logic-On-Military-Troops-Quality-Calculation


1. **Impor Library**: Kode dimulai dengan mengimpor library yang diperlukan, yaitu NumPy untuk manipulasi array, dan scikit-fuzzy (skfuzzy) untuk pemrosesan logika fuzzy.

2. **Inisialisasi Variabel**: Variabel input dan output dideklarasikan menggunakan objek `Antecedent` untuk variabel input (intensitas latihan, kursus kemampuan, kebugaran fisik) dan `Consequent` untuk variabel output (kualitas pasukan). Rentang nilai untuk masing-masing variabel ditentukan menggunakan `np.arange()`.

3. **Fungsi Keanggotaan**: Untuk setiap variabel, fungsi keanggotaan fuzzy ditentukan. Fungsi `trimf()` digunakan untuk membuat fungsi keanggotaan segitiga dengan parameter yang telah ditentukan.

4. **Aturan Fuzzy**: Aturan-aturan fuzzy didefinisikan berdasarkan kombinasi nilai input yang mungkin. Setiap aturan terdiri dari kondisi (premises) dan konsekuensi (conclusion). Aturan-aturan ini menghubungkan variabel input dengan variabel output dan menentukan bagaimana input mempengaruhi output.

5. **Sistem Kontrol**: Selanjutnya, sistem kontrol fuzzy dibuat dengan menggunakan objek `ControlSystem` yang menerima daftar aturan fuzzy sebagai argumennya. Sistem kontrol ini menyatukan semua aturan fuzzy yang telah didefinisikan sebelumnya.

6. **Simulasi**: Objek `ControlSystemSimulation` dibuat dengan menggunakan sistem kontrol yang telah dibuat sebelumnya. Ini memungkinkan kita untuk mensimulasikan perilaku sistem kontrol fuzzy dengan memberikan nilai input tertentu.

7. **Input dan Evaluasi**: Nilai-nilai input (intensitas latihan, kursus kemampuan, kebugaran fisik) dimasukkan ke dalam simulasi menggunakan atribut `input`. Kemudian, metode `compute()` dipanggil untuk mengevaluasi sistem kontrol fuzzy berdasarkan nilai input yang telah diberikan.

8. **Output**: Setelah evaluasi, output dari sistem kontrol fuzzy dapat diakses melalui atribut `output`. Dalam kasus ini, outputnya adalah tingkat kualitas pasukan. 

9. **Output**: Nilai output ditampilkan untuk memberikan hasil dari evaluasi sistem kontrol fuzzy.

Dengan demikian, kode tersebut mengimplementasikan logika fuzzy untuk menentukan tingkat kualitas pasukan berdasarkan intensitas latihan, kursus kemampuan, dan kebugaran fisik yang diberikan.

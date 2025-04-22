# Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan mempunyai lebih dari 1000 karyawan yang tersebar di seluruh penjuru Indonesia. Meskipun telah berkembang menjadi perusahaan yang besar dan mapan, perusahaan masih menghadapi tantangan dalam pengelolaan sumber daya manusia. Khususnya dalam mempertahankan karyawan

### Permasalahan Bisnis
Meskipun Jaya Jaya Maju telah berkembang menjadi perusahaan multinasional dengan lebih dari 1000 karyawan, perusahaan menghadapi tantangan serius berupa tingginya attrition rate (rasio karyawan yang keluar), yang telah mencapai lebih dari 10%. Tingginya tingkat attrition ini mengindikasikan adanya permasalahan internal yang berdampak langsung pada stabilitas operasional dan efisiensi bisnis.
### Cakupan Proyek

Proyek ini berfokus pada analisis data untuk mengetahui faktor apa saja yang berpengaruh pada tingkat attrition. Dalam proyek ini juga membuat dashboard untuk memonitor dan mengelola faktor yang berpengaruh dan model machine learning untuk memprediksi potensi karyawan yang resign

### Persiapan
Sumber Data : [Data Karyawan](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:
* Install Library yang digunakan
  ```
  pip install -r requirements. txt
  ```
* Load model
  ```
  best_model = joblib.load('model_xgb.joblib')
  ```
* Load dataset
  ```
  data_predict = pd.read_csv('Data Prediction Employee.csv')
  ```
## Business Dashboard
![Jaya Jaya Maju Dashboard](https://github.com/user-attachments/assets/e5c8a487-d060-4339-89f5-667b49123067)

Dashboard ini dibuat untuk memonitor dan menganalisis attrition di perusahaan Jaya Jaya Maju. Dashboard dapat dilihat melalui [link ini](https://lookerstudio.google.com/reporting/e9c46dc9-aa51-4bbb-80a6-98d9f67190e1) Dengan total karyawan 1058, terdapat 179 orang yang mengalami attrition dan menyisakan 879 karyawan aktif dengan rata-rata usia 33,47 tahun dan rata-rata gaji 6.625,95. Angka attrition rate berada di 16,92%. 

Dari segi gender, attrition lebih banyak terjadi pada laki-laki sebanyak 108 (60.3%) dibandingkan dengan perempuan sebanyak 71 (39.7%). Total karyawan laki-laki dan perempuan sebanyak 620 dan 438

Jika dilihat dari status pernikahan, mayoritas attrition terjadi pada karyawan yang single atau belum menikah sebanyak 94 orang (52.5%). Ini menunjukkan bahwa karyawan yang single lebih terbuka pada peluang baru atau berada dalam fase eksplorasi karier. Sementara attrition terendah terjadi pada karyawan dengan status bercerai. 

Berdasarkan Job Role, Laboratory Technician memiliki jumlah attrition tertinggi sebanyak 49 orang, diikuti oleh Sales Executive dan Research Scientist. 

Catatan: untuk mengakses dashboardnya perlu login ke akun Gmail
## Conclusion


### Rekomendasi Action Items (Optional)
* Fokus pada strategi retensi untuk usia muda, khususnya di usia 25–35 tahun.
* Evaluasi kondisi kerja dan kepuasan di departemen R&D dan Sales
* Kaji ulang dukungan perusahaan terhadap karyawan yang sudah menikah agar lebih seimbang antara pekerjaan dan kehidupan pribadi

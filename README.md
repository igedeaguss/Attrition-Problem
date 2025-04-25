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
* Unduh tiga file utama yaitu model_xgb.joblib, requirements.txt , prediction.py
* Set Environment
  ```
  python -m venv env
  venv\Scripts\activate
  ```
* Install Library
  ```
  pip install -r requirements. txt
  ```
* Atur Path File Model dan Dataset
    * Load Model
      ```
      best_model = joblib.load('model_xgb.joblib')
      ```
    * Load dataset
      ```
      data_predict = pd.read_csv('Data Prediction Employee.csv')
      ```
* Run prediction.py
  ```
  python prediction.py
  ```
## Business Dashboard
![gedeaguss-Dashboard](https://github.com/user-attachments/assets/efa7fa0f-f2f1-4d8c-b55e-c68c5bcf3f9a)

Dashboard ini dirancang untuk mengidentifikasi faktor-faktor utama yang mempengaruhi keputusan karyawan melakukan attrition. Dari total 1.058 karyawan, sebanyak 179 orang keluar sehingga menghasilkan tingkat attrition sebesar 16,92%. Rata-rata usia karyawan adalah 33 tahun dengan gaji rata-rata sekitar 6.625 unit mata uang lokal. Saat ini terdapat 879 karyawan aktif di perusahaan.

Departemen R&D memiliki jumlah karyawan yang melakukan atrisi tertinggi, yaitu sebanyak 107 orang. Angka ini lebih tinggi dibandingkan departemen Sales (66 orang) dan HR (6 orang). Salah satu faktor yang mendasari tingginya angka atrisi di R&D adalah total karyawannya yang juga paling banyak dibandingkan departemen lain. Namun, jika dilihat lebih dalam, faktor lain yang mendorong atrisi adalah tingkat ketidakpuasan terhadap lingkungan kerja. Sebanyak 34.58% karyawan R&D yang resign merasa tidak puas (Low) terhadap lingkungan kerjanya dan menjadikannya tertinggi dibandingkan departemen lain. Selain itu, meskipun sebagian besar merasa memiliki work-life balance yang baik (52.34% merasa ‘Excellent’), masih terdapat 12.15% yang merasa buruk (Low) dalam aspek tersebut. Hal ini mengindikasikan bahwa beban kerja dan kualitas lingkungan kerja di R&D mungkin masih menjadi tantangan yang memengaruhi keputusan karyawan untuk resign.

Berdasarkan grafik Job Level, karyawan pada level 1 memiliki jumlah atrisi terbanyak, yaitu sebanyak 108 orang. Salah satu faktor penyebabnya adalah tingkat kepuasan kerja (Job Satisfaction), di mana 26.85% karyawan Job Level 1 yang resign merasa 'Low'. Hal ini juga didukung oleh tingkat kepuasan terhadap lingkungan kerja (Environment Satisfaction) yang berada pada angka 29.63%. Meskipun sedikit lebih baik dibandingkan Job Level 2 yang mencapai 35.14%. Dalam aspek Work Life Balance, 50.93% karyawan level 1 merasa 'Excellent', namun tetap terdapat 11.11% yang merasa 'Low'. Kondisi ini menandakan bahwa perusahaan perlu memberikan perhatian lebih kepada karyawan di level terbawah dengan meningkatkan kualitas pengalaman kerja mereka, seperti melalui pelatihan, sistem penghargaan, mentoring, atau peningkatan komunikasi manajerial.

Karyawan yang melakukan atrisi terbanyak berada pada rentang gaji 1.000–6.000, dengan jumlah mencapai 136 orang, sementara yang paling sedikit berada di rentang gaji 16.000–21.000 dengan hanya 5 orang. Dari sisi kenaikan gaji, atrisi paling banyak terjadi pada rentang kenaikan 11–16%, sebanyak 112 karyawan. Selain itu, sebanyak 98 karyawan yang resign tercatat mengalami lembur (overtime), yang setara dengan 54.7% dari total karyawan yang mengalami atrisi. Hal ini mengindikasikan bahwa karyawan dengan gaji rendah dan beban kerja tambahan berpotensi lebih tinggi mengalami atrisi. 

Berdasarkan latar belakang pendidikan dan gender, terlihat bahwa sebagian besar karyawan yang mengalami attrition berasal dari **bidang pendidikan Life Sciences dan Medical**, yang juga merupakan dua bidang dengan jumlah karyawan tertinggi. Dari segi jenjang pendidikan, karyawan dengan gelar **Bachelor (S1)** mendominasi angka attrition, diikuti oleh Master dan College, yang mencerminkan distribusi umum tingkat pendidikan dalam perusahaan. Sementara itu, dari sisi gender, **laki-laki menunjukkan jumlah attrition yang lebih tinggi dibanding perempuan**, namun hal ini juga sejalan dengan jumlah total karyawan pria yang lebih besar secara keseluruhan. Temuan ini menunjukkan bahwa faktor pendidikan dan gender tidak menunjukkan kecenderungan signifikan terhadap tingkat pengunduran diri jika tidak dilihat secara proporsional, namun tetap penting untuk dipertimbangkan dalam strategi retensi tenaga kerja.

Berdasarkan status pernikahan, tingkat attrition tertinggi terjadi pada karyawan dengan status lajang sebesar 52,5% (94 karyawan). Tingginya jumlah attrition pada kelompok ini terutama dipengaruhi oleh tingkat kepuasan kerja (*Job Satisfaction*) yang rendah, di mana sebanyak 26,60% dari mereka berada pada kategori “Low”. Sementara itu, sebagian besar karyawan lajang justru merasa puas terhadap lingkungan kerjanya (*Environment Satisfaction*) dengan persentase “High” sebesar 31,91%. Selain itu, faktor *Work Life Balance* tampaknya bukan menjadi penyebab utama tingginya attrition karena hanya 7,45% saja yang merasa work-life balance mereka buruk (“Low”), sehingga mayoritas tetap merasakan keseimbangan antara pekerjaan dan kehidupan pribadi. Dengan demikian dapat disimpulkan bahwa upaya menekan angka attrition di kalangan karyawan lajang sebaiknya difokuskan pada peningkatan kepuasan kerja melalui program pengembangan karir atau motivasi internal lainnya.

Berdasarkan usia, karyawan berusia 31 tahun merupakan kelompok dengan jumlah attrition tertinggi. Selain itu, terdapat peningkatan signifikan dalam jumlah karyawan yang melakukan attrition pada rentang usia 25 hingga 31 tahun. Setelah melewati usia tersebut, angka attrition cenderung menurun secara signifikan. Hal ini mengindikasikan bahwa periode muda hingga awal tiga puluhan merupakan masa kritis di mana risiko keluar dari perusahaan lebih tinggi, kemungkinan disebabkan oleh faktor-faktor seperti pencarian peluang karir baru atau perubahan prioritas hidup.

Berdasarkan grafik Work Life Balance, Job Satisfaction, dan Environment Satisfaction dapat disimpulkan bahwa tingkat kepuasan karyawan terhadap work-life balance, job satisfaction, dan environment satisfaction memiliki pengaruh signifikan terhadap angka attrition. Karyawan yang memiliki tingkat kepuasan tinggi pada ketiga aspek tersebut cenderung lebih sedikit meninggalkan perusahaan. Sebaliknya, semakin rendah kepuasan mereka—terutama dalam hal job satisfaction dan environment satisfaction—semakin besar kemungkinan mereka untuk keluar. Meskipun jumlah karyawan dengan work-life balance rendah relatif kecil, risiko attrition tetap ada jika keseimbangan antara pekerjaan dan kehidupan pribadi terganggu. Oleh karena itu, perusahaan perlu fokus meningkatkan kualitas lingkungan kerja serta kepuasan kerja secara menyeluruh sambil memastikan program keseimbangan hidup-pekerjaan berjalan efektif guna menekan angka perpindahan karyawan.


Dashboard dapat dilihat melalui [link ini](https://lookerstudio.google.com/reporting/e9c46dc9-aa51-4bbb-80a6-98d9f67190e1)

Catatan: untuk mengakses dashboardnya perlu login ke akun Gmail
## Conclusion
Berdasarkan hasil analisis data karyawan, ditemukan bahwa attrition dipengaruhi oleh kombinasi faktor demografis, kondisi pekerjaan, dan tingkat kepuasan karyawan. Karyawan dengan status lajang menunjukkan tingkat attrition tertinggi, yang terutama terkait dengan rendahnya kepuasan kerja meskipun mereka relatif puas terhadap lingkungan kerja dan work-life balance. Departemen R&D memiliki jumlah attrition terbesar karena populasi karyawannya paling banyak sekaligus tingginya ketidakpuasan terhadap lingkungan kerja di departemen tersebut. Selain itu, karyawan pada level jabatan terendah (Job Level 1) juga mengalami angka keluar yang tinggi akibat rendahnya kepuasan kerja dan lingkungan kerja.

Faktor finansial seperti rentang gaji rendah serta beban lembur turut memperbesar risiko attrition. Dari sisi demografi pendidikan dan gender tidak ditemukan kecenderungan signifikan secara proporsional meski laki-laki mendominasi jumlah total resign.

Secara keseluruhan, tingkat kepuasan dalam aspek job satisfaction dan environment satisfaction menjadi indikator utama dalam memprediksi kemungkinan seorang karyawan untuk keluar dari perusahaan. Work-life balance berperan penting namun bukan faktor dominan penyebab attrition.

### Rekomendasi Action Items (Optional)
* Perusahaan perlu meningkatkan kepuasan kerja karyawan, khususnya bagi mereka di level pekerjaan terbawah dan yang berstatus lajang, dengan menyediakan program pelatihan yang relevan serta sistem penghargaan untuk memotivasi.
* Meningkatkan kualitas lingkungan kerja terutama di departemen R&D dengan memperbaiki fasilitas, komunikasi antar tim, dan manajemen beban kerja agar karyawan merasa lebih nyaman dan dihargai.
* Mengoptimalkan program work-life balance melalui fleksibilitas jam kerja, cuti tambahan, atau dukungan kesejahteraan mental sehingga karyawan dapat menyeimbangkan kehidupan pribadi dan pekerjaan secara efektif.
* Melakukan evaluasi struktur gaji dan kebijakan lembur agar beban kerja tidak memberatkan karyawan bergaji rendah serta memastikan kompensasi sesuai dengan kontribusi mereka.
* Memperkuat sistem mentoring dan komunikasi manajerial untuk membantu karyawan level awal memahami jalur karir serta mendapatkan dukungan dalam pengembangan profesionalnya.
* Melakukan survei kepuasan secara berkala untuk mengidentifikasi masalah lebih dini terkait job satisfaction maupun environment satisfaction sehingga tindakan korektif dapat segera dilakukan.

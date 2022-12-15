# Laporan Proyek Machine Learning - Nabilah Sofieyanti

## Domain Proyek
Dalam keberlangsungan hidup manusia tidaklah terlepas dari kebutuhan, terlebih kebutuhan primer yakni sandang, pangan, dan papan. Papan sebagai nama lain dari rumah atau tempat tinggal termasuk pada kebutuhan primer tersebut yang mana untuk mempertahankan hidup yang layak, kebutuhan ini harus terpenuhi. 
Untuk memenuhi kebutuhan papan ini, tidaklah mudah. Untuk menjadi kepemilikan pribadi apalagi di daerah besar seperti ibukota Jakarta, tidaklah membutuhkan biaya yang sedikit. Namun dalam memenuhi kebutuhan ini hendaknya untuk menyesuaikan dengan kebutuhan serta standar kehidupan masing-masing. Sehingga untuk memprediksi berapa harga yang sesuai dengan penyesuaian kebutuhan dapat dilakukan berdasarkan pada data historis penjualan.


## Business Understanding
Dalam urusan bisnis, terkait jual beli rumah merupakan hal yang tidak mudah. Untuk mendapatkan harga yang tepat dan sesuai perlu dilakukan prediksi agar tidak terjadi kerugian. Harga rumah ini dipengaruhi oleh beberapa fitur yang ada pada rumah tersebut antara lain luas tanah, luas bangunan, jumlah kamar tidur, jumlah kamar mandi, dan garasi. Namun, apakah yang menjadi hal terpenting dalam penentuan harga suatu rumah? dan bagaimana penentuan harga berdasarkan fitur tertentu dengan mudah? Maka, diperlukan sistem untuk memprediksi harga rumah tersebut. 

### Problem Statements
Berdasarkan kondisi yang telah dijelaskan, maka akan dikembangkan sebuah sistem prediksi harga rumah sebagai berikut :
- Fitur apakah yang paling berpengaruh terhadap harga rumah?
- Berapa harga rumah dengan karakteristik tertentu?

### Goals
Untuk menjawab pertanyaan di atas, tujuan dari masalah tersebut antara lain:
- Mengetahui fitur apakah yang paling berpengaruh terhadap harga rumah
- Membuat model machine learning yang dapat memprediksi harga rumah berdasarkan fitur yang ada

    ### Solution statements
    - Untuk mengetahui fitur apa yang sangat berkorelasi dengan harga rumah bisa dilakukan dengan melihat plot antar variabel dengan fitur target yaitu harga dan dengan skor korelasinya.
    - Model machine learning yang dapat digunakan adalah K- Nearest Neighbor, Random Forest, Boosting Algorithm dengan menggunakan metrik MSE yang kemudian dipilih model terbaik berdasarkan MSE terkecil.

## Data Understanding
Dataset yang digunakan dalam proyek ini adalah daftar harga rumah di daerah Jakarta yang bersumber dari  [Kaggle](https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah?select=DATA+RUMAH.xlsx). Dataset ini memiliki 1010 records dengan 8 kolom.
Variabel-variabel pada dataset ini sebagai berikut :
- NO: Nomor data
- NAMA RUMAH: Title rumah
- HARGA: Harga rumah dalam milyar (menjadi fitur target)
- LB: Luas Bangunan dalam m^2
- LT: Luas Tanah dalam m^2
- KT: Jumlah kamar tidur
- KM: Jumlah kamar mandi
- GRS: Jumlah kapasitas mobil dalam garasi

Fitur-fitur tersebut akan digunakan dalam menemukan pola pada data. Serta untuk membuat model prediktif dengan machine learning ini menggunakan Google Colaboratory.
Dilakukan beberapa teknik exploratory data analysis, tidak missing value pada dataset tersebut, dilakukan check menggunakan boxplot dengan metode IQR, univariate dan multivariate analysis pada fitur numerik.

## Data Preparation
Tahap persiapan data termasuk hal yang penting dalam machine learning. Tahap ini melakukan proses transformasi pada data sehingga menjadi bentuk yang cocok dan mempermudah untuk proses pemodelan. Pada bagian ini akan dilakukan tahap persiapan data, yaitu :
- Data cleaning dengan menghapus variabel yang tidak akan digunakan serta penanganan outliers
- Data transform dengan merubah variabel harga menjadi satuan milyar rupiah
- Pembagian dataset dengan fungsi train_test_split dari library sklearn dengan pembagian untuk data test 20% dari jumlah dataset
- Standarisasi (dilakukan untuk membuat fitur data menjadi bentuk yang mudah diolah oleh model).

## Modeling
Tahap pemodelan yaitu tahapan menggunakan algoritma machine learning dalam menjawab permasalahan yang ada. Pada proyek ini menggunakan tiga algoritma, yang kemudian akan dievaluasi mana yang memiliki performa lebih baik dari masing-masing algoritma untuk dijadikan model yang memberikan hasil prediksi terbaik. Algoritma-algoritma tersebut yaitu :
1. K-Nearest Neighbor
Algoritma KNN menggunakan kesamaan fitur untuk memprediksi nilai dari data baru. Kelebihan dari algoritma ini adalah sederhana mudah dipahami serta mudah digunakan. Namun kekurangan ketika dihadapkan pada jumlah fitur yang besar (curve of dimensionality). 
Dengan menggunakan library sklearn.neighbors (KNeighborstRegressor) dan sklearn.metrics (mean_squared_error), parameter yang digunakan sebagai berikut :
- n_neighbors:tetannga (diisi dengan 10)
2. Random Forest
Termasuk supervised learning yang dapat digunakan untuk masalah klasifikasi dan regresi. Dalam proyek ini merupakan permasalahan regresi sehingga cocok untuk menggunakan algoritma ini dengan teknik bagging dimana setiap model dilatih secara paralel. Adapun kelebihannya sering digunakan karena sederhana tetapi memiliki stabilitas yang mumpuni.
Dengan menggunakan library sklearn.ensemble (RandomForestRegressor), parameter yang digunakan sebagai berikut :
- n_estimator: jumlah trees (diisi dengan 50)
- max_depth: ukuran banyak pohon dapat splitting setiap node dalam jumlah pengamatan yang diinginkan (diisi dengan 16)
- random_state: sebagai kontrol random number generator yang digunakan (diisi dengan 55)
- njobs: jumlah job yang digunakan secara paralel (diisi dengan -1)
3. Boosting Algorithm
Teknik boosting bekerja membangun model dari data latih secara berurutan dan iteratif. Kelebihannya dapat meningkatkan akurasi prediksi, namun bergantung pula pada ruang lingkup masalah dari dataset yang digunakan yang juga menjadi kekurangannya. 
Dengan menggunakan library sklearn.ensemble (AdaBoostRegressor), parameter yang digunakan sebagai berikut :
- learning_rate: bobot terapan pada setiap regressor masing-masing iterasi boosting (Diisi dengan 0.05)
- random_state: sebagai kontrol random number generator yang digunakan (diisi dengan 55)

Model yang terbaik ialah Random Forest karena model inilah yang nilai diprediksinya paling mendekati dengan nilai aslinya.

## Evaluation
Metrik evaluasi yang digunakan disini adalah MSE (Mean Squared Error). MSE ini bekerja dengan menghitung jumlah selisih kuadrat rata-rata sebenarnya dengan nilai prediksi. Sebelumnya dilakukan proses scaling pada data test terlebih dahulu. Kemudian baru dilakukan evaluasi dengan metrik MSE. Dari hasil proyek ini nilai error untuk data test dari ketiga algoritma hampir sama namun untuk data train error Random forest lebih kecil.
|index|train|test|
|---|---|---|
|KNN|0\.002429889012342572|0\.003013691413955065|
|RF|0\.0004706460141604776|0\.0025643552270918158|
|Boosting|0\.002212213191047915|0\.0030434564468961533|
![Teks alternatif](data:image/png;base64,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)

Serta dilakukan prediksi, hasil prediksi Random Forest adalah yang paling mendekati nilai aslinya sehingga inilah model yang terbaik untuk kasus ini.  
|index|y\_true|prediksi\_KNN|prediksi\_RF|prediksi\_Boosting|
|---|---|---|---|---|
|184|7\.15|5\.4|6\.6|5\.2|

## Conclusion
Berdasarkan problem statement serta yang ditentukan sebelumnya, maka dapat diketahui bahwa fitur yang paling berpengaruh dalam prediksi harga rumah ialah luas tanah dan luas bangunan. Kedua fitur tersebut berkorelasi paling tinggi terhadap harga rumah. Serta model sistem prediksi terbaik adalah model Random Forest karena memiliki nilai error terkecil dan hasil prediksi mendekati nilai aslinya. 

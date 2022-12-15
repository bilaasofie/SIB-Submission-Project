# Laporan Proyek Machine Learning - Nabilah Sofieyanti

## Project Overview
Domain proyek _machine learning_ ini adalah terkait hiburan film yaitu "Sistem Rekomendasi Film"

## Latar Belakang
Sebuah film dapat menjadi sebuah alternatif untuk mendapatkan hiburan. Pada zaman sekarang, platform penyedia layanan video/film sangatlah sudah tidak asing lagi. Seperti Netflix, Disney+ Hotstar, Youtube, dan masih banyak lagi. Untuk menarik _experience_ pengguna dalam menggunakan suatu platform dengan lebih lama lagi serta menarik kepuasaan pengguna, sistem rekomendasi akan menjadi jawabannya. Sistem rekomendasi merupakan suatu model yang akan memberikan rekomendasi yang sesuai berdasarkan data-data pengguna. Dengan sistem rekomendasi inilah pengguna akan lebih mudah mendapatkan film/video yang sesuai dengan ketertarikannya.

## Business Understanding
### Problem Statements
Berdasarkan kondisi yang telah dijelaskan, maka akan dikembangkan sebuah sistem rekomendasi dengan _problem statement_ sebagai berikut :
- Bagaimana model _machine learning_ mengenai sistem rekomendasi film berdasarkan dengan genre film yang disukai atau ditonton sebelumnya agar pengguna lebih mudah untuk mendapatkan tontonan yang sesuai dengan ketertarikannya?
- Apakah hasil sistem rekomendasi film yang dibuat akurat?

### Goals
Untuk menjawab pertanyaan di atas, tujuan dari masalah tersebut antara lain:
- Menghasilkan model _machine learning_ mengenai sistem rekomendasi film berdasarkan dengan genre yang sesuai data personalisasi pengguna.
- Mengetahui keakuratan model sistem rekomendasi film yang dibuat.

### Solution Approach
Untuk menyelesaikan masalah ini, solusi yang dapat diajukan yaitu teknik _content based filtering_.
- _Content Based Filtering_ adalah suatu teknik yang dapat merekomendasikan item yang mirip dengan yang disukai pengguna di masa lalu. Algoritma ini bekerja dengan menyarankan item serupa dengan profil minat pengguna. Berdasarkan masalah ini, sistem dapat merekomendasikan film berdasarkan dengan genre. 
    Kelebihan : Sangat cocok digunakan untuk membuat sistem rekomendasi berdarsakan kemiripan atribut suatu item. 
    Kelemahan : Kurang _reliable_ karena tidak ada masukan pendapat dari pengguna sebelumnya. Sehingga sangat membutuhkan preferensi pengguna dan riwayat interaksi pengguna.

## Data Understanding
Dataset yang digunakan dalam proyek ini adalah daftar film pada platform Disney+ Hotstar yang bersumber dari  [Kaggle](https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows). Dataset ini memiliki 1450 records dengan 12 variabel.
Variabel-variabel pada dataset ini sebagai berikut :
- show_id: kode film yang unik 
- type: tipe Movie/TV Show
- title: judul film
- director: nama director
- cast: nama cast film
- country: asal negara produksi film
- data_added: tanggal ditambahkan di Disney+
- release_year: tahun rilis film
- rating: rating film
- duration: total durasi film
- listed_in: genre film
- description: sinopsis film

5 data teratas dataset sebagai berikut :
|index|show\_id|type|title|director|cast|country|date\_added|release\_year|rating|duration|listed\_in|description|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|s1|Movie|Duck the Halls: A Mickey Mouse Christmas Special|Alonso Ramirez Ramos, Dave Wasson|Chris Diamantopoulos, Tony Anselmo, Tress MacNeille, Bill Farmer, Russi Taylor, Corey Burton|NaN|November 26, 2021|2016|TV-G|23 min|Animation, Family|Join Mickey and the gang as they duck the halls\!|
|1|s2|Movie|Ernest Saves Christmas|John Cherry|Jim Varney, Noelle Parker, Douglas Seale|NaN|November 26, 2021|1988|PG|91 min|Comedy|Santa Claus passes his magic bag to a new St\. Nic\.|
|2|s3|Movie|Ice Age: A Mammoth Christmas|Karen Disher|Raymond Albert Romano, John Leguizamo, Denis Leary, Queen Latifah|United States|November 26, 2021|2011|TV-G|23 min|Animation, Comedy, Family|Sid the Sloth is on Santa's naughty list\.|
|3|s4|Movie|The Queen Family Singalong|Hamish Hamilton|Darren Criss, Adam Lambert, Derek Hough, Alexander Jean, Fall Out Boy, Jimmie Allen|NaN|November 26, 2021|2021|TV-PG|41 min|Musical|This is real life, not just fantasy\!|
|4|s5|TV Show|The Beatles: Get Back|NaN|John Lennon, Paul McCartney, George Harrison, Ringo Starr|NaN|November 25, 2021|2021|NaN|1 Season|Docuseries, Historical, Music|A three-part documentary from Peter Jackson capturing a moment in music history with The Beatles\.|

Dilakukan _Exploratory Data Analysis_ (EDA) pada dataset sebagai berikut:
- Seluruh tipe variabel adalah object atau string kecuali variabel release_year yang merupakan integer. 
- Dilakukan pengecekan _missing value_ dan ternyata terdapat _missing value_ pada dataset pada variabel director(473), cast(190), dan country(219). Namun karena variabel yang akan digunakan hanyalah variabel title dan listed_in maka ini tidak akan berpengaruh.
- Melihat data unik variabel listed_in (genre), disetiap film terdapat beberapa genre.
- Informasi dari eksplorasi data pada variabel type 
![Type Film](data:image/png;base64,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)
![barchart](data:image/png;base64,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)
Dilakukan visualisasi data untuk type film. Menggunakan barchart dan piechart. Dikarenakan hanya ada dua tipe film maka akan cocok jika menggunakan piechart.
**Insight** :Hasilnya jumlah type movie lebih banyak yaitu daripada TV Show dengan persentase masing-masing 73% dan 27%.

## Data Preparation
Sebelum membuat model, tahap persiapan data termasuk hal yang penting dalam machine learning agar model yang dihasilkan dapat berjalan dengan baik. Adapun tahap persiapan yang dilakukan yaitu:
- Duplikasi data 
Hal ini dilakukan agar dataset asli tidak terkontaminasi dan bisa digunakan kembali jika dibutuhkan untuk keperluan pengembangan model. Isi dari variabel `data` diduplikasi dan ditampung ke variabel baru bernama `df`.
- Data cleaning 
Menghapus variabel yang tidak diperlukan. Dilakukan agar lebih praktis. Variabel utama yang digunakan untuk membuat model sistem rekomendasi disini hanyalah `title` dan `listed_in` sehingga untuk variabel lainnya yaitu `show_id`, `type`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, dan `description` dapat dihapus.  Kemudian pengecekan missing value kembali dan untuk dataframe baru tidak ada missing value.
- Data transform dengan mengonversi data `title` menjadi dalam bentuk list untuk kebutuhan model

## Modeling and Result
Selanjutnya, tahap pemodelan dengan teknik _content based filtering_. Karena dengan teknik tersebut kita dapat membuat suatu sistem rekomendasi berdasarkan atributnya yaitu genre untuk menyelesaikan masalah dalam proyek ini. 
**Tahapan Content Based Learning serta Cosine Similarity yang dilakukan :** 
- Dilakukan pemodelan dengan menggunakan TF-IDF Vektorizer untuk menemukan fitur penting dari genre film. 
- Melakukan fit lalu ditransformasikan ke bentuk matrik. Matrik yang kita miliki berukuran (818, 39). Nilai 818 merupakan ukuran data dan 39 merupakan matrik genre
- Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
- Selanjutnya, membuat matriks TF-IDF untuk beberapa title dan genre dengan output sebagai berikut :

|title|anthology|western|musical|superhero|mystery|adventure|thriller|historical|concert|survival|science|sports|espionage|drama|music|of|animation|crime|nature|documentary|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|The Princess and the Frog|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.6450688892698928|0\.0|0\.0|0\.0|
|Finding Nemo|0\.0|0\.0|0\.0|0\.0|0\.0|0\.5055015327312692|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.5249581559756893|0\.0|0\.0|0\.0|
|Flora & Ulysses|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.508465577872396|0\.0|0\.46243725587712303|0\.0|0\.0|0\.0|0\.0|
|Rogue One: A Star Wars Story|0\.0|0\.0|0\.0|0\.0|0\.0|0\.3597595292244921|0\.0|0\.0|0\.0|0\.0|0\.6087471405535897|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Mickey's Christmas Carol|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.6450688892698928|0\.0|0\.0|0\.0|
|X-Men: First Class|0\.0|0\.0|0\.0|0\.6686629068076828|0\.0|0\.26750483815830356|0\.0|0\.0|0\.0|0\.0|0\.45264348011613936|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|The Legend of Mor'du|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.5430501061720114|0\.0|0\.0|0\.0|
|Baby's Day Out|0\.0|0\.0|0\.0|0\.0|0\.0|0\.3349342936460984|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.8258165297186604|0\.0|0\.0|
|The Parent Trap|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Up, Up and Away|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.4698101173466414|0\.0|0\.0|0\.0|0\.0|
- Menghitung _similarity degree_ antar title dengan teknik cosine similarity
- Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa title dengan output sebagai berikut:

|title|X-Men: The Last Stand|Magic Camp|Nature&\#39;s Half Acre|Disney Adventures in Babysitting|Prom|
|---|---|---|---|---|---|
|The Poof Point|0\.5720562674462165|0\.19657084614935902|0\.0|0\.6267962320976612|0\.6207507601960423|
|Loop|0\.1765320655057864|0\.4160300100335083|0\.1778202911913546|0\.0|0\.0|
|Meet the Deedles|0\.0|0\.2789761998285643|0\.0|0\.11987518493620222|0\.11871898452349734|
|Marvel Rising: Playing With Fire|0\.23747223837467094|0\.0|0\.0|0\.8850738892000256|0\.6383783621137964|
|Forky Asks a Question: What is Reading?|0\.1453411045819531|0\.7641244192512806|0\.1464017172448984|0\.18116086428504044|0\.17941356132017902|
|Forky Asks a Question: What is a Friend?|0\.1453411045819531|0\.7641244192512806|0\.1464017172448984|0\.18116086428504044|0\.17941356132017902|
|Swiss Family Robinson|0\.26239485332214496|0\.15661627418099655|0\.06694120810642182|0\.19841897445356094|0\.0|
|Mr\. Holland's Opus|0\.0|0\.0|0\.0|0\.0|0\.2846320410354253|
|Lilo & Stitch 2: Stitch Has a Glitch|0\.0|0\.20504114560475492|0\.0|0\.0881055275109676|0\.08725574657153484|
|Alvin and the Chipmunks: Chipwrecked|0\.09361413718555618|0\.49217217948338765|0\.09429727730352408|0\.11668562758356467|0\.11556019056471338|

Hasil diatas menunjukan kesamaan antar title. Dapat dilihat misalnya untuk 'BURN-E' dan 'Dr. Seuss' Horton Hears a Who!' menghasilkan nilai 1 maka kedua title ini _similar_. 

- Kemudian membuat fungsi rekomendasi untuk menghasilkan keluaran 10-top recommendations berdasarkan kesamaan genre

- Uji coba langsung dilakukan dengan memanggil fungsi rekomendasi yang sudah dibuat sebelumnya dengan memasukan title yang pengguna tonton atau pengguna sukai. Misalnya film berjudul 'Aquamarine' dijadikan sebagai inputan model dengan informasi film tersebut 

|index|show\_id|type|title|director|cast|country|date\_added|release\_year|rating|duration|listed\_in|description|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1443|s1444|Movie|Aquamarine|Elizabeth Allen Rosenbaum|Jake McDorman, Arielle Kebbel, Claudia Karvan, Bruce Spence, Tammin Sursok, Roy Billing|United States|August 13, 2021|2006|PG|104 min|Comedy, Coming of Age, Fantasy|Two 13-year-old best friends embark on an adventure when they discover a mermaid in a swimming pool\.|

Film tersebut bergenre Comedy, Coming of Age, Fantasy. Dengan memanggil fungsi rekomendasi yang telah dibuat, output 10 top recommendations sebagai berikut:

|index|title|listed\_in|
|---|---|---|
|0|Up, Up and Away|Comedy, Coming of Age, Fantasy|
|1|Life-Size 2|Comedy, Coming of Age, Fantasy|
|2|The Ultimate Christmas Present|Comedy, Coming of Age, Fantasy|
|3|The Swap|Comedy, Coming of Age, Fantasy|
|4|Luck of the Irish|Comedy, Coming of Age, Fantasy|
|5|The Wizards Return: Alex vs\. Alex|Comedy, Coming of Age, Fantasy|
|6|Don't Look Under the Bed|Coming of Age, Fantasy|
|7|Disney Avalon High|Coming of Age, Fantasy|
|8|The Thirteenth Year|Coming of Age, Fantasy|
|9|Miss Peregrine's Home for Peculiar Children|Coming of Age, Fantasy|

Dari tabel diatas genre item hasil rekomendasi terlihat sesuai dengan title inputannya yaitu bergenre : Comedy, Coming of Age, Fantasy.

## Evaluation
Untuk evaluasi model yang telah dibuat, menguji keakuratan digunakan metrik **precision** dengan mengukur jumlah prediksi benar yang dibuat. Precision menggambarkan tingkat keakuratan antara data yang diminta dengan hasil prediksi yang diberikan oleh model [[1]](https://ksnugroho.medium.com/confusion-matrix-untuk-evaluasi-model-pada-unsupervised-machine-learning-bc4b1ae9ae3f)
Dengan formula: True positives/(True Positives+False Positives)
Kelebihan dari metrik ini sangat baik untuk klasifikasi serta bagus digunakan jika kelasnya seimbang. Sehingga kekurangannya ialah tidak baik untuk data yang imbalance.
Hasil output dari precision dengan data uji coba sebelumnya sebagai berikut:
```python
Comedy: 100.0
Coming of Age: 100.0
Fantasy: 100.0
```
**Kesimpuan** : Dari hasil 10 rekomendasi film diatas dan hasil pengukuran kinerja model menunjukan bahwa 100% akurat.

## REFERENCES
[1] Kuncahyo Setyo Nugroho. "Confusion Matrix untuk Evaluasi Model pada Supervised Learning". Tersedia:[Tautan](https://ksnugroho.medium.com/confusion-matrix-untuk-evaluasi-model-pada-unsupervised-machine-learning-bc4b1ae9ae3f)
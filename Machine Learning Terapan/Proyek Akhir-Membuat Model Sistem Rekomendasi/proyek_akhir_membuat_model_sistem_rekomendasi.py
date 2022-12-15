# -*- coding: utf-8 -*-
"""Proyek Akhir : Membuat Model Sistem Rekomendasi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h7zBjoy3BbKszfV79mlxaPpZe1DeNVbY

Nama : Nabilah Sofieyanti

Proyek Akhir : Membuat Model Sistem Rekomendasi

Machine Learning Terapan

## Import Library

Langkah pertama yang dilakukan adalah import library yang dibutuhkan.
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""## Load Dataset

Data yang digunakan adalah dataset yang bersumber dari Kaggle berjudul "Disney+ Movies and TV Shows". Dataset ini memiliki 1450 record dan 12 variabel.
"""

data = pd.read_csv('/content/disney_plus_titles.csv')
data.head()

"""## Data Understanding

Dilakukan beberapa exploratory data sebagai berikut :

### Deskripsi Variabel

Deskripsi variabel-variabel dalam dataset yang digunakan adalah sebagai berikut:
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

### Tipe Data
"""

data.info()

"""Hasil fungsi info() menunjukan seluruh tipe variabel adalah object atau string kecuali variabel release_year yang merupakan integer

### Pengecekan Missing Value
"""

data.isnull().sum()

"""Dilakukan cek missing value, ternyata pada variabel director, cast, dan country terdapat missing value.

### Melihat listed_in(genre) unik dari film
"""

print(data['listed_in'].unique())

"""### Visualisasi Data Variabel Type"""

type_film = data['type'].value_counts()

ax=plt.axes()
ax.pie(x=type_film.values,
        labels=data['type'].unique(),
        autopct='%1.0f%%')

ax.set_title('Film Types')

type_film_count = data['type'].value_counts()

sns.barplot(x=type_film_count.values,
            y=type_film_count.index,
            palette='Set1').set_title('Film Types')

plt.tight_layout()
plt.show()

"""Dilakukan visualisasi data untuk type film. Menggunakan barchart dan pie chart. Dikarenakan hanya ada dua tipe film maka akan cocok jika menggunakan pie chart. Insight : Hasilnya jumlah type movie lebih banyak yaitu daripada TV Show dengan persentase masing-masing 73% dan 27%.

## Data Preparation

### Duplikasi Data

Dilakukan duplikasi data agar dataset asli tidak terkontaminasi dan agar mudah dan bisa digunakan kembali jika dibutuhkan untuk pengembangan model. Dataframe yang baru bernama df yang merupakan hasil duplikasi.
"""

df = data.copy()
df.head()

"""### Data Cleaning

Karena untuk membuat model sistem rekomendasi dalam masalah ini hanya membutuhkan variabel title dan listed_in (genre) maka variabel lainnya dapat dihapus. Variabel yang dihapus yaitu variabel show_id, type, director, cast, country, date_added, release_year, rating, duration, dan description.
"""

df = df.drop(columns=['show_id', 'type', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'description'])
df

"""Kembali pengecekan missing value pada data yang baru, tidak ada missing value sehingga proses data cleaning selesai"""

df.isna().sum()

"""### Data Transform

Mengonversi data 'title' menjadi dalam bentuk list
"""

title = df['title'].tolist()
print(len(title))

"""## Modeling and Result

### TF-IDF Vectorizer

Sistem rekomendasi akan dibangun berdasarkan genre dengan TF-IDF Vectorizer
"""

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data listed_in
tf.fit(df['listed_in']) 
 
# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names()

"""Melakukan fit lalu ditransformasikan ke bentuk matrik. Matrik yang kita miliki berukuran (818, 39). Nilai 818 merupakan ukuran data dan 39 merupakan matrik genre"""

tfidf_matrix = tf.fit_transform(df['listed_in']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()"""

tfidf_matrix.todense()

"""Selanjutnya, membuat matriks TF-IDF untuk beberapa title dan genre"""

pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names(),
    index=df.title
).sample(22, axis=1).sample(10, axis=0)

"""### Cosine Similarity

Menghitung similarity degree antar title dengan teknik cosine similarity
"""

cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

"""Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa title"""

cosine_sim_df = pd.DataFrame(cosine_sim, index=df['title'], columns=df['title'])
print('Shape:', cosine_sim_df.shape)
 
# Melihat similarity matrix pada setiap title
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Hasil diatas menunjukan kesamaan antar title. Dapat dilihat misalnya untuk 'BURN-E' dan 'Dr. Seuss' Horton Hears a Who!' menghasilkan nilai 1 maka kedua title ini similar. 

Kemudian membuat fungsi rekomendasi untuk menghasilkan keluaran 10-top recommendations berdasarkan kesamaan genre
"""

def film_recommendations(title, similarity_data=cosine_sim_df, items=df[['title', 'listed_in']], k=10):
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,title].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop title agar title yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(title, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

"""Uji coba langsung dilakukan dengan memanggil fungsi rekomendasi yang sudah dibuat sebelumnya dengan memasukan title yang pengguna tonton atau pengguna sukai"""

#menemukan informasi film dengan title inputan
df[df.title.eq('Aquamarine')]

"""Misalkan title input dengan title 'Aquamarine'. Title judul tersebut bergenre Comedy, Coming of Age, Fantasy."""

# Mendapatkan rekomendasi film yang mirip dengan title inputan
film_recommendations('Aquamarine')

"""Hasil rekomendasi sesuai dengan genre pada title input yaitu Comedy, Coming of Age, Fantasy.

## Evaluation

Untuk evaluasi model yang telah dibuat, menguji keakuratan digunakan metrik **precision** dengan mengukur jumlah prediksi benar yang dibuat.
"""

feature_recomendation = film_recommendations('Aquamarine')

feature = df[df['title'] == 'Aquamarine']
feature

get_feature_listed_in=[]
for i in range(len(feature.listed_in)):
    for x in feature.listed_in.str.split(','):
        if x not in get_feature_listed_in:
            get_feature_listed_in.append(x)

get_feature_listed_in

feature_recomendation

for i in get_feature_listed_in[0]:
  print(i + ": " + str((
      (feature_recomendation['listed_in'].str.contains(i).count()/feature_recomendation['listed_in'].count())*100)
  ))

"""Kesimpulan : Dari hasil 10 rekomendasi film diatas dan hasil pengukuran kinerja model menunjukan bahwa 100% akurat."""
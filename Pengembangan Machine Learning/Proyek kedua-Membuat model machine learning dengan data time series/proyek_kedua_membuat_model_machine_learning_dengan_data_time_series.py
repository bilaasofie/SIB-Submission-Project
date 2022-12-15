# -*- coding: utf-8 -*-
"""Proyek Kedua : Membuat Model Machine Learning dengan Data Time Series.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zFceV4vmaDocJjoQEmsRFe6Sp8DRjUJu

Nama : Nabilah Sofieyanti

Proyek Kedua : Membuat Model Machine Learning dengan Data Time Series

Belajar Pengembangan Machine Learning

# Import library
"""

#import library
import numpy as np
import pandas as pd
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split

"""# Load dataset"""

df = pd.read_csv('household_power_consumption.txt', sep=';')
df.head()

"""# Data Preprocessing

## Mengubah tipe data
"""

df['Date'] = pd.to_datetime(df['Date'])
df.info()

df['Time'] = pd.to_timedelta(df['Time'])
df.info()

df['DateTime'] = df['Date'] + df['Time']

"""## Dataframe yang akan dipakai"""

df = df[['DateTime', 'Global_intensity']]
df

df.info()

df['Global_intensity'] = pd.to_numeric(df['Global_intensity'], errors='coerce')
df.info()

#mengecek apakah ada nilai yang hilang dari dataset
df.isnull().sum()

df = df.dropna()
df.info()

"""# Plot data"""

#membuat plot dari data kita dapat menggunakan fungsi plot dari library matplotlib
datetime = df['DateTime'].values
global_intensity  = df['Global_intensity'].values
 
 
plt.figure(figsize=(25,10))
plt.plot(datetime, global_intensity)
plt.title('Global_intensity',
          fontsize=20);

"""# Mae < 10% skala data"""

minMae = (df['Global_intensity'].max() - df['Global_intensity'].min()) * 10/100
minMae

"""# Split data"""

#bagi data untuk data training dan data test
datetime_train, datetime_test, GI_train, GI_test = train_test_split(datetime, global_intensity, test_size=0.2)

def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    series = tf.expand_dims(series, axis=-1)
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-1], w[-1:]))
    return ds.batch(batch_size).prefetch(1)

"""# Pengunaan callbacks"""

#callbacks
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('mae')<minMae) and (logs.get('val_mae')<minMae):
      print("\nMAE dari model < 10% skala data, stop training!")
      self.model.stop_training = True
callbacks = myCallback()

"""# Arsitektur model sequential"""

train_set = windowed_dataset(GI_train, window_size=60, batch_size=100, shuffle_buffer=1000)
val_set = windowed_dataset(GI_test, window_size=60, batch_size=100, shuffle_buffer=1000)

model = tf.keras.models.Sequential([
  tf.keras.layers.LSTM(60, return_sequences=True),
  tf.keras.layers.LSTM(60),
  tf.keras.layers.Dense(30, activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1),
])

"""# Model compile serta melatih model"""

#optimizer (dgn parameter learning rate) dan loss
optimizer = tf.keras.optimizers.SGD(lr=1.0000e-04, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(), 
              optimizer=optimizer,
              metrics=["mae"]) 
history = model.fit(train_set, validation_data=val_set, epochs=100, callbacks=[callbacks])

"""# Plot akurasi dan loss"""

#plot akurasi
plt.plot(history.history['mae'])
plt.plot(history.history['val_mae'])
plt.title('mae')
plt.ylabel('mae')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#plot loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import concurrent.futures
from multiprocessing import Pool 
import tensorflow as tf
import csv
from google.colab import files
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder


# read csv
f = pd.read_csv('pitches_with_umpiress.csv', nrows=99999)

# filter rows with incorrect call == 1
f = f[f['incorrect_call'] == 1]

# select relevant columns
x = f[['Type', 'MPH']]
y = f['umpire']

# drop rows with missing values
x = x.replace('--', np.nan)
x = x.dropna()
y = y[x.index]

# encode umpire names as integers
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# one-hot-encode the Type column
x = pd.get_dummies(x, columns=['Type'])

# split into train and validation sets
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

# replace missing values with mean of column
train_mean = x_train.mean()
x_train = x_train.fillna(train_mean)
x_val = x_val.fillna(train_mean)

# convert data to tensors
train_ds = tf.data.Dataset.from_tensor_slices((x_train.values.astype(np.float32), y_train))
train_ds = train_ds.shuffle(buffer_size=len(x_train)).batch(32)

val_ds = tf.data.Dataset.from_tensor_slices((x_val.values.astype(np.float32), y_val))
val_ds = val_ds.batch(32)

# build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(len(encoder.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train the model
history = model.fit(train_ds, validation_data=val_ds, epochs=50, verbose=1)

# make predictions for each umpire
umpire_names = encoder.inverse_transform(np.unique(y))
for umpire_name in umpire_names:
    umpire_data = f[f['umpire'] == umpire_name][['Type', 'MPH']]
    umpire_data = pd.get_dummies(umpire_data, columns=['Type'])
    umpire_data = umpire_data.replace('--', np.nan)
    umpire_data = umpire_data.fillna(x.mean())
    umpire_pred = encoder.inverse_transform(np.argmax(model.predict(umpire_data.values.astype(np.float32)), axis=1))[0]
    print(f"{umpire_name} - Classification: {umpire_pred}")

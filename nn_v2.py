import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = pd.read_csv('pitches_updated_inning.csv')
data = data.dropna(subset=['umpire', 'inning_num', 'zone', 'MPH', 'incorrect_call', 'Type'])

umpires = data['umpire'].unique()

for umpire in umpires:
    umpire_data = data[data['umpire'] == umpire]
    
    X = umpire_data[['Type', 'MPH', 'inning_num', 'zone']]
    y = umpire_data['incorrect_call']
    
    # Encode categorical variable 'Type'
    label_encoder = LabelEncoder()
    X['Type'] = label_encoder.fit_transform(X['Type'])
    onehot_encoder = OneHotEncoder(sparse=False)
    X = onehot_encoder.fit_transform(X)
    
    # Split data into train, validation, and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1)

    # Build neural network
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(32, input_dim=X_train.shape[1], activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # Train model
    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val))
    
    # Print weights
    print(umpire)
    print('Type:', model.layers[0].get_weights()[0][:, :4])
    print('MPH:', model.layers[0].get_weights()[0][:, 4:5])
    print('Inning Num:', model.layers[0].get_weights()[0][:, 5:6])
    print('Zone:', model.layers[0].get_weights()[0][:, 6:])

    # Evaluate model
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print('Accuracy:', accuracy)

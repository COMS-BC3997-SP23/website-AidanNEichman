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


# define a function to get umpire name from a game id
def get_umpire_name(game_id):
    url = f'https://www.espn.com/mlb/recap/_/gameId/{game_id}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    umpire_info = soup.find(text=lambda text: text and "Home Plate Umpire" in text)
    ind = 0
    for char in str(soup):
        if char == "H":
            if str(soup)[ind:ind+17] == "Home Plate Umpire":
                break
        ind+=1
    temp = str(soup)[ind+36:ind+70]
    umpire_name = ""
    for char in temp:
        if char == '<':
            break
        else:
            umpire_name+=char
    return umpire_name

# read csv
f = pd.read_csv('pitches_updated_empty_gone.csv')

# replace empty strings with NaN values
f = f.replace('', np.nan)

found_game_ids = set()
umpire_dict = {}

# create a pool of processes
pool = Pool()

# iterate over rows and get umpire name using multiprocessing
for index, row in f.iterrows():
    game_id = row['Game']
    if game_id in found_game_ids:
        f.at[index, 'umpire'] = umpire_dict[game_id]
    else:
        # apply the function to the game_id using the pool of processes
        umpire_name = pool.apply(get_umpire_name, args=(game_id,))
        found_game_ids.add(game_id)
        umpire_dict[game_id] = umpire_name
        f.at[index, 'umpire'] = umpire_name

# close the pool of processes
pool.close()

f.to_csv('pitches_with_umpires.csv', index=False)

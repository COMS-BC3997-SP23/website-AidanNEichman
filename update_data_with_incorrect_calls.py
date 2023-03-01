import csv
from google.colab import files

#open our existing file
with open('/content/pitches.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = []
    #iterate through each row
    for row in reader:
        #obtain the coordinates of the ball over the plate
        play_hitzone = row['play-hitzone']
        #obtain the result of the pitch (ball, strike looking, hit, foul ball, etc.)
        pitch_type = row['Pitch']
        play_hitzone_parts = play_hitzone.split('; ')
        #check that there is a sufficient coordinate pair, otherwise print a skip and move on
        if len(play_hitzone_parts) != 2:
            print(f"Skipping row with invalid play-hitzone format: {play_hitzone}")
            continue
        #split the coordinates
        top, right = play_hitzone_parts
        #take the numerical values of the coords out from the "px" and other symbols
        top_value_parts = top.split(': ')
        right_value_parts = right.split(': ')
        #again, check for a valid pairing
        if len(top_value_parts) != 2 or len(right_value_parts) != 2:
            print(f"Skipping row with invalid top/right format: {play_hitzone}")
            continue
        #get the float values and adjust will found ratio
        top_value = float(top_value_parts[1].rstrip('px'))*1.06
        right_value = float(right_value_parts[1].rstrip('px;'))*1.03
        #if there was an incorrect call (either ball or strike looking when it should not have been)
        #I should probably adjust this to 0,1, or 2 as to account for whether or not an ump is strike-happy or ball-happy
        if (0 <= top_value <= 23 and 11 <= right_value <= 33 and pitch_type == 'Ball') or \
           ((top_value < 0 or top_value > 23 or right_value < 11 or right_value > 33) and pitch_type == 'Strike Looking'):
            incorrect_call = 1
        else:
            incorrect_call = 0
        row['incorrect_call'] = incorrect_call
        rows.append(row)

#filter out rows without an entry in the "incorrect_call" column
rows = [row for row in rows if 'incorrect_call' in row and row['incorrect_call'] != '']

#create an updated file
with open('pitches_updated_empty_gone.csv', 'w', newline='') as csvfile:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()
    writer.writerows(rows)
files.download('pitches_updated_empty_gone.csv')
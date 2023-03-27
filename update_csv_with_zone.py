import csv
from google.colab import files

#open our existing file
with open('/content/umpires_grouped.csv', 'r') as csvfile:
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
        #if the coordinates fall within certain ranges, set zone to 1, otherwise set it to 0
        if (top_value > 23):
          if (right_value > 33):
            zone = 10
          elif (33 >= right_value > 25.6):
            zone = 11
          elif (25.6 >= right_value > 18.3):
            zone = 12
          elif (18.3 >= right_value > 11):
            zone = 13
          else:
            zone = 14
        elif (23 >= top_value > 15.3):
          if (right_value > 33):
            zone = 15
          elif (33 >= right_value > 25.6):
            zone = 1
          elif (25.6 >= right_value > 18.3):
            zone = 2
          elif (18.3 >= right_value > 11):
            zone = 3
          else:
            zone = 16
        elif (15.3 >= top_value > 7.6):
          if (right_value > 33):
            zone = 17
          elif (33 >= right_value > 25.6):
            zone = 4
          elif (25.6 >= right_value > 18.3):
            zone = 5
          elif (18.3 >= right_value > 11):
            zone = 6
          else:
            zone = 18
        elif (7.6 >= top_value >= 0):
          if (right_value > 33):
            zone = 19
          elif (33 >= right_value > 25.6):
            zone = 7
          elif (25.6 >= right_value > 18.3):
            zone = 8
          elif (18.3 >= right_value > 11):
            zone = 9
          else:
            zone = 20
        elif (top_value < 0):
          if (right_value > 33):
            zone = 21
          elif (33 >= right_value > 25.6):
            zone = 22
          elif (25.6 >= right_value > 18.3):
            zone = 23
          elif (18.3 >= right_value > 11):
            zone = 24
          else:
            zone = 25
        row['zone'] = zone
        rows.append(row)

#filter out rows without an entry in the "zone" column
rows = [row for row in rows if 'zone' in row and row['zone'] != '']

#create an updated file
with open('pitches_updated_zone.csv', 'w', newline='') as csvfile:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()
    writer.writerows(rows)
files.download('pitches_updated_zone.csv')

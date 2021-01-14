import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_json(
    r'C:\Users\Mr_BadBoy\Desktop\my_spotify_data\MyData\StreamingHistory0.json')

print(df['trackName'].value_counts())


artist_group = df.groupby('artistName')


art_vals = artist_group['trackName'].value_counts()

print(art_vals)

art_vals.to_csv('data2.csv')

list_times = df.groupby(['artistName']).sum(
).sort_values('msPlayed', ascending=False)
list_times['hPlayed'] = list_times['msPlayed'] / (1000*60*60)
print(list_times.head(20))

song_times = df.groupby(['trackName']).sum(
).sort_values('msPlayed', ascending=False)
song_times['hPlayed'] = song_times['msPlayed'] / (1000*60*60)
print(song_times.head(20))

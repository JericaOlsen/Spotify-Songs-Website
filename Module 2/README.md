# Module 2

Create a module and import it into your project to calculate the mean,median,mode,range, and other descriptive statistics.

## Execution

```python
import pandas as pd
import mystatistics

'''
Module1: Introduces user to the system
'''

def read_csv(filename):
    """
    Param:
        filename (string): Name of the file

    Returns:
        DataFrame: The dataframe of the csv file
    """
    df=pd.read_csv(filename) 
    return df

def creat_dict(file):
    """
    Args:
        file (DataFrame):The dataframe of the csv file 

    Returns:
        Dict: Dictionary of the csv file
    """

    dict_top_songs = file.to_dict('records')
    return dict_top_songs

def get_statistics(song_dict):
    """_summary_

    Args:
        dict (dictionary): Dictionary of all the songs

    Returns:
        Mean, Median, Mode: The mean, median, and mode of the chosen variable of the songs
    """
    danceability_list = []
    for item in song_dict:
        danceability_list.append(item["danceability"])

    dance_mean = mystatistics.mean(danceability_list)
    dance_median = mystatistics.median(danceability_list)
    dance_mode = mystatistics.mode(danceability_list)
    return dance_mean, dance_median, dance_mode

if __name__=='__main__':
    """
    CSV file that has a dataset of songs fron 125 different genres
    """
    filename='dataset.csv'
    df = read_csv(filename)
    dict_top_songs = creat_dict(df)
    dance_mean, dance_median, dance_mode = get_statistics(dict_top_songs)
    print("Mean danceability of the top songs is: " + str(dance_mean))
    print("Median danceability of the top songs is: "+ str(dance_median))
    print("Mode danceability of the top songs is: "+ str(dance_mode))
```

## Description

This program uses the module I created titled mystatistics and uses it to calculate the mean, median and mode of the danceability of all the tracks.

## Example Output

```python
Mean danceability of the top songs is: 0.5668000657894737
Median danceability of the top songs is: 0.58
Mode danceability of the top songs is: 0.647
```
## Dataset

The dataset was switched to one that contains over 100k songs from Spotify that contain 125 different genres. Every track contains the following traits.

- track_id: ID of the track
- artists: Name of thee artist
- album_name: Name of the album
- track_name: Name of the track
- popularity: Popularity of the track rate from 0 to 100. 100 means it is the most popular
- duration_ms: Track length in ms
- explicit: Yes or no on if the track is explicit
- danceability: Rating from 0.0 to 1.0 on how danceable a song is
- energy: Rating from 0.0 to 1.0 that shows how intense or energetic a track is. 
- key: The key the track is in
- loudness: Loudness of the track in decibels
- mode: If the track is major(1) of minor(0)
- speechiness: Scale of how many spoken words are in the track based from 0.0 to 1.0
- acousticness: Rating of 0.0 to 1.0 of how acoustic the track is
- instrumentalness: Rating if there are vocals in the track. If there are it will be closer to 1.0
- liveness: Rating on how much a live audience is detected in the track. 1.0 means the track has a live audience.
- valence: A rating of 0.0 to 1.0 of how positive a track is. 1.0 os more positive
- tempo: Overall tempo of a track in BPM
- time_signature: Time signature of the songs
- track_genre: Genre of the track 
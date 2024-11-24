# Module 3

Refactor the application to use advanced OOP principles.

## Execution

```python
class Genre:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def __str__(self):
        return(self.name)
    
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            song.genre = self

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            song.genre = None
    
    def list_songs(self):
        for song in self.songs:
            print(str(song))

        
    
class Song:
    def __init__(self, name, ID, artist, album, popularity, duration, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness,valence, tempo, genre= None):
        self.name = name
        self.ID = ID
        self.artist = artist
        self.album = album
        self.popularity = popularity
        self.duration = duration
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumental = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.genre = genre
    
    def __str__(self):
        return (
            "Name: " + self.name + 
            ", Artist: "+ self.artist +
            ", Album: "+ self.album 
        )
```

This program then used the organize_genres function to be able to organize the dictionary of all the songs

```python
def organize_genres(song_dict):
    """
    Args:
        song_dict (dict): Dictionary of the song csv file

    """
    genre_list = []
    count = 1
    for song in song_dict:
        genre_here = False
        for genre in genre_list:
            if song['track_genre'] == str(genre):
                #Genre has already been made
                genre_here = True

        if genre_here == False:
            genre_name = Genre(song['track_genre'])
            genre_list.append(genre_name)
        
        song_id = 'song' + str(count)
        song_id = Song(
                song['track_name'], 
                song['track_id'], 
                song['artists'], 
                song['album_name'],
                song['popularity'],
                song['duration_ms'],
                song['danceability'],
                song['energy'],
                song['key'],
                song['loudness'],
                song['mode'],
                song['speechiness'],
                song['acousticness'],
                song['instrumentalness'],
                song['liveness'],
                song['valence'],
                song['tempo'],
                song['track_genre']
            )
        genre_name.add_song(song_id)
        count+=1

    return genre_list
```

## Description

This program used the Genre and Song class to be able to organize the dataset of all the songs so they grouped together by genres. I decided to create two classes so each song could be contained in an object but that each song could be contained in a genre object. This will make it easier to manipulate and compare the data. See the example below for a possible use.

## Example Output

This example shows the mean, median, and mode danceability of different genres.The closer number is to 1.0 the more danceable a song is.

```python
acoustic
Danceability
Mean: 0.549593
Median: 0.5585
Mode: 0.568

afrobeat
Danceability
Mean: 0.66958
Median: 0.691
Mode: 0.778

alt-rock
Danceability
Mean: 0.534493
Median: 0.5425
Mode: 0.731
```
## Dataset

The dataset contains over 100k top songs from Spotify that contain 125 different genres. Every track has the following traits.

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
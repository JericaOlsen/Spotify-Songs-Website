import pandas as pd
import mystatistics

'''
Module3: Introduces OOP principles to the project
'''

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


def get_danceability(genre_list):
    """
    Args:
        genre_list (dictionary): list of each song genres

    Returns:
        Nothing
    """
    
    for item in genre_list:
        danceability_list = []
        for song in item.songs:
            danceability_list.append(song.danceability)

        print(item)

        dance_mean = mystatistics.mean(danceability_list)
        dance_median = mystatistics.median(danceability_list)
        dance_mode = mystatistics.mode(danceability_list)
        print("Danceability\nMean: " + str(dance_mean) + "\nMedian: " + str(dance_median) + "\nMode: " + str(dance_mode) + '\n')
    


if __name__=='__main__':
    """
    CSV file that has a dataset of songs fron 125 different genres
    """
    filename="dataset.csv"
    df = read_csv(filename)
    dict_top_songs = creat_dict(df)
    genre_list = organize_genres(dict_top_songs)
    
    get_danceability(genre_list)

    
        





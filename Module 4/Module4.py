import pandas as pd
import mystatistics
import logging

'''
Module4: Used generator and iterators in your code. Also add robust error/file handling and the logger application
ChatGPT was used to add some of the error handling
'''

class FileManager:
    def __init__(self, filename):
        self.name = filename
        logging.info("FileManager was created")

    def read_csv(self):
        try:
            df=pd.read_csv(self.name) 
            logging.info("CSV file was read from the path" )
            return df
        except FileNotFoundError:
            logging.error("The file could not be read as it does not exists")
            print("The file " + self.name +" does not exist and could not be read")
        except pd.errors.EmptyDataError:
            logging.error("The file is empty")
            print("The file is empty")
        except Exception as e:
            logging.error("An unexpected error occured: {e}")
            print("An unexpected error occurred: {e}")

class AllGenres:
    def __init__(self, genre_list):
        if not isinstance(genre_list,list):
            logging.error("genre_list is not a list")
            raise TypeError("genre_list must be a list of Genre ojects")
        self.genres = [genre_list]
        logging.info("AllGenres class was created")

    def genre_gen(self):
        for genre in self.genres:
            yield genre

class Genre:
    def __init__(self, name):
        self.name = name
        self.songs = []
        logging.info("Genre class was created")

    def __str__(self):
        return(self.name)
    
    def __iter__(self):
        for song in self.songs:
            yield song
    
    def add_song(self, song):
        """
        Args:
            song (Song object):A song object
        """
        if song not in self.songs:
            self.songs.append(song)
            song.genre = self
        else:
            logging.error("Song could not be added to the song list as it is already in the genre")
            print(song.name + " is already in the this genre")

    def remove_song(self,song):
        """

        Args:
            song (Song object): A song object
        """
        if song in self.songs:
            self.songs.remove(song)
            song.genre = None
            logging.info("A song was removed from the songs")
        else:
            logging.error("A song could not be added to the list")
            print("The song " + song.name + "does not exists in the current songlist")

    def list_songs(self):
        if self.songs == []:
            logging.error("There are no songs in the list")
            print("There are no songs in the lists to list out")
        for song in self.songs:
            print(str(song))
        logging.info("The songs in the genre were listed")

        
    
class Song:
    def __init__(self, name, ID, artist, album, popularity, duration, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness,valence, tempo, genre):
        variables = [name,ID,artist,album,genre,acousticness,instrumentalness,danceability,energy,liveness,loudness,speechiness,tempo,valence,key,mode,popularity,duration]
        for variable in variables:
            if not isinstance(variable,float) and not isinstance(variable,str) and not isinstance(variable,int):
                print("The variable " + variable + " is not a float, string, or integer please format it as a one of these variables")
                logging.error("One of the variables entered is not a float, string, or integer")      
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
        logging.info("The class Song was created")
    
    def __str__(self):
        return (
            "Name: " + self.name + 
            ", Artist: "+ self.artist +
            ", Album: "+ self.album 
        )
    

def creat_dict(file):
    """
    Args:
        file (DataFrame):The dataframe of the csv file 

    Returns:
        Dict: Dictionary of the csv file
    """

    dict_top_songs = file.to_dict('records')
    logging.info("The file containg the top songs was changed into a dictionary")
    return dict_top_songs

def organize_genres(song_dict):
    """
    Args:
        song_dict (dict): Dictionary of the song csv file

    """
    try:
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

        logging.info("The list of song classes were organized into genre classes")
        return genre_list
    except KeyError as e:
        logging.error("Missing an expected value for song dictionary: {e}")

    except Exception as e:
        logging.error("There was an error while trying to organize the genres")

def get_danceability(all_genres):
    """
    Args:
        all_genres (Class): A class containing a list of all genres

    Returns:
        Nothing
    """
    if not isinstance(all_genres,AllGenres):
        logging.error("all_genres is not an instance of AllGenres")
        raise TypeError("all_genres must be an instance of AllGenres")
    try:
        for genre in genre_list:
            danceability_list = []
            for song in genre:
                danceability_list.append(song.danceability)

            if danceability_list:
                dance_mean = mystatistics.mean(danceability_list)
                dance_median = mystatistics.median(danceability_list)
                dance_mode = mystatistics.mode(danceability_list)
                print(genre)
                print("Danceability\nMean: " + str(dance_mean) + "\nMedian: " + str(dance_median) + "\nMode: " + str(dance_mode) + '\n')
                logging.info("The danceability of all the songs in one of the genres had the mean, median, and mode was calculated." )
            else:
                logging.warning("There are no songs in the genre")
                print("No songs were found in this genre")
        
    except Exception as e:
        logging.error("There was an error while calculating danceability")
    


if __name__=='__main__':
    """
    CSV file that has a dataset of songs fron 125 different genres
    """
    logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="Module4Log.log"
    )

    filename="dataset.csv"
    csv_manager = FileManager(filename)
    df = csv_manager.read_csv()
    dict_top_songs = creat_dict(df)
    genre_list = organize_genres(dict_top_songs)
    all_genres = AllGenres(genre_list)
    get_danceability(all_genres)

    
        





# Module 4

Refactor the application to use generator and iterators. Also include robust error handling and file handling in your code with a logger.

## Execution

### Generator and iterator

I chose to a iterator in my code with the Genres class and a generator with the new class AllGenres. AllGenres contains a list of all the Genres that we can now access the genres in this list with the generator. For the Genre class we can now easily iterate through the list of songs in each genre.

```python
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
```

### Error Handling and Logging

I implemented error handling in the creation of my song class to make sure it accepts the right values. I also added it to the functions add_song(), remove_song(), organize_genres(), and get_danceability() to make sure they work correctly. For logging I used it in all of my code mainly to keep track of when certain classes and functions are used, but I also used it for logging certain errors to make it easier to track when an error happens.

```python
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
        logging.info("The class song was created")
    
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
    logging.info("The file of type songs was changed into a dictionary")
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
```

Here is the logging setup.

```python
    logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="Module4Log.log"
    )
```

### File Handler

For the file handler I chose to make a class to read the csv file. This way all of the functions dealing with file handling can be contained in one class and can be used for any csv file.

```python
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
```

## Summary

This program uses the new class AllGenres so that we can use a generators to iterate through the list of genres and an iterator to iterate through the list of songs for each genre. This program also includes a file handling, error handling, and logging to keep track of the flow of code.

## Example Output

This example shows that the program still shows the mean, median, and mode danceability of different genres.The closer number is to 1.0 the more danceable a song is.

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
This is the example output of the file the logger writes to

```python
2024-09-16 20:05:37 - root - INFO - FileManager was created
2024-09-16 20:05:37 - root - INFO - CSV file was read from the path
2024-09-16 20:05:38 - root - INFO - The file containg the top songs was changed into a dictionary
2024-09-16 20:05:38 - root - INFO - Genre class was created
2024-09-16 20:05:38 - root - INFO - The class Song was created
2024-09-16 20:05:38 - root - INFO - The class Song was created
2024-09-16 20:05:38 - root - INFO - The class Song was created
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
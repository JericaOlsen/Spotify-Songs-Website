import pandas as pd
import mystatistics
import logging
import matplotlib
import matplotlib.pyplot as plt
import time
import multiprocessing
matplotlib.use('TkAgg', force=True)

'''
Module7: Implement asynchronous data fetching and multiprocessing to speed up data processing.
ChatGPT was used to create multiprocessing code and pool usage.
'''

class FileManager:
    def __init__(self, filename):
        if not isinstance(filename,str):
            logging.error("Filename is not a string")
            raise ValueError("Filename is not a string")
        self.name = filename
        logging.info("FileManager was created")

    def read_csv_chunks(self, chunk_sz =1000):
        try:
            df=pd.read_csv(self.name, chunksize=chunk_sz) 
            logging.info("CSV chunk file was read from the path" )
            return df
        except FileNotFoundError:
            logging.error("The file could not be read as it does not exists")
            print("The file " + self.name +" does not exist and could not be read")
            raise FileNotFoundError("File is not found")
        except pd.errors.EmptyDataError:
            logging.error("The file is empty")
            print("The file is empty")
            raise pd.errors.EmptyDataError("The file is empty")

    def read_csv(self):
        try:
            df=pd.read_csv(self.name) 
            logging.info("CSV chunk file was read from the path" )
            return df
        except FileNotFoundError:
            logging.error("The file could not be read as it does not exists")
            print("The file " + self.name +" does not exist and could not be read")
            raise FileNotFoundError("File is not found")
        except pd.errors.EmptyDataError:
            logging.error("The file is empty")
            print("The file is empty")
            raise pd.errors.EmptyDataError("The file is empty")


class AllGenres:
    def __init__(self, genre_list):
        if not isinstance(genre_list,list):
            logging.error("genre_list is not a list")
            raise TypeError("genre_list must be a list of Genre ojects")
        self.genres = genre_list
        logging.info("AllGenres class was created")

    def __iter__(self):
        for genre in self.genres:
            yield genre

class Genre:
    def __init__(self, name):
        if not isinstance(name,str):
            logging.error("The genre name is not a string")
            raise ValueError("The genre name is not a string")
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
        if not isinstance(song,Song):
            logging.error("Song is not a song object")
            raise ValueError("Song is not a song object")
        if song not in self.songs:
            self.songs.append(song)
            song.genre = self
        else:
            logging.error("Song could not be added to the song list as it is already in the genre")
            print(song.name + " is already in the this genre")
            raise ValueError("Song already is in the song list")

    def remove_song(self,song):
        """

        Args:
            song (Song object): A song object
        """
        if not isinstance(song,Song):
            logging.error("Song is not a song object")
            raise ValueError("Song is not a song object")
        if song in self.songs:
            self.songs.remove(song)
            song.genre = None
            logging.info("A song was removed from the songs")
        else:
            logging.error("A song could not be added to the list")
            print("The song " + song.name + "does not exists in the current songlist")
            raise ValueError("Song is not in the song list")

    def list_songs(self):
        if self.songs == []:
            logging.error("There are no songs in the list")
            print("There are no songs in the lists to list out")
            raise ValueError("There are no songs in the song list")
        for song in self.songs:
            print(str(song))
        logging.info("The songs in the genre were listed")

  
class Song:
    def __init__(self, name, ID, artist, album, popularity, duration, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness,valence, tempo, genre,explicit):
        variables = [name,ID,artist,album,genre,acousticness,instrumentalness,danceability,energy,liveness,loudness,speechiness,tempo,valence,key,mode,popularity,duration,explicit]
        for variable in variables:
            if not isinstance(variable,(float,str,int)) and not isinstance(variable,bool):
                print("The variable  is not a float, string, or integer please format it as a one of these variables")
                logging.error("One of the variables entered is not a float, string, or integer")  
                raise ValueError("One of the variables entered is not a float, string, or integer")    
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
        self.explicit = explicit
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
    if not isinstance(file,pd.DataFrame):
        logging.error("File is not a dataframe")
        raise ValueError("File is not a dataframe")
    dict_top_songs = file.to_dict('records')
    logging.info("The file containg the top songs was changed into a dictionary")
    return dict_top_songs

def process_chunk(chunk):
    dict_top_songs = creat_dict(chunk)
    return organize_genres(dict_top_songs)

def organize_genres(song_dict_list):
    """
    Args:
        song_dict _list(list): Dictionary of the song csv file

    """
    if not isinstance(song_dict_list, list):
        logging.error("song_dict_list is not a list")
        raise ValueError("song_dict is not a list")
    try:
        genre_list = []
        count = 1
        for song in song_dict_list:
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
                song['track_genre'],
                song['explicit']
            )
            genre_name.add_song(song_id)
            count+=1

        logging.info("The list of song classes were organized into genre classes")
        return genre_list
    except KeyError:
        logging.error("This dictionary is missing an expected value")
        raise ValueError("Missing an expected value for song dictionary")

def get_mean_median_mode(all_genres,value):
    """
    Args:
        all_genres (Class): A class containing a list of all genres
        value (String): A string of which value we want to get the data on

    Returns:
        dance_data (Dataframe): A datafram containing the mean median and mode values for the specified value of each genre
    """

    data = []
    if not isinstance(all_genres,AllGenres):
        logging.error("all_genres is not an instance of AllGenres")
        raise ValueError("all_genres must be an instance of AllGenres")
    if not isinstance(value,str):
        logging.error("value is not a string")
        raise ValueError("value must be a string")
    try:
        for genre in all_genres:
            value_list = []
            for songs in genre:
                for song in songs:
                    if value == 'popularity':
                        value_list.append(song.popularity)
                    elif value == 'duration':
                        value_list.append(song.duration)
                    elif value == 'danceability':
                        value_list.append(song.danceability)
                    elif value == 'energy':
                        value_list.append(song.energy)
                    elif value == 'loudness':
                        value_list.append(song.loudness)
                    elif value == 'mode':
                        value_list.append(song.mode)
                    elif value == 'speechiness':
                        value_list.append(song.speechiness)
                    elif value == 'acousticness':
                        value_list.append(song.acousticness)
                    elif value == 'instrumental':
                        value_list.append(song.instrumental)
                    elif value == 'liveness':
                        value_list.append(song.liveness)
                    elif value == 'valence':
                        value_list.append(song.valence)
                    elif value == 'tempo':
                        value_list.append(song.tempo)
                    else:
                        raise ValueError("This value is not an value associated with Songs")
            if value_list:
                dance_mean =  mystatistics.mean(value_list)
                dance_median =  mystatistics.median(value_list)
                dance_mode =  mystatistics.mode(value_list)
                data.append({ 
                    "Genre": songs.name,
                    "Mean": dance_mean,
                    "Median": dance_median,
                    "Mode": dance_mode})
                
                logging.info("The specified value of all the songs in one of the genres had the mean, median, and mode was calculated." )
            else:
                logging.warning("There are no songs in the genre")
                print("No songs were found in this genre")
        df_dance = pd.DataFrame(data)
        return df_dance
    except ValueError:
        logging.error("This value is not an value associated with Songs")
        raise ValueError("This value is not an value associated with Songs")
    except Exception:
        logging.error("There was an error while calculating the mean, median, and mode of the specified value")
    
def create_bar_graph(df,name):
    if not isinstance(df, pd.DataFrame):
        logging.error("Df is not a dataframe")
        raise ValueError("Df is not a dataframe")
    if not isinstance(name, str):
        logging.error("Name is not a string")
        raise ValueError("Name is not a string")
    colors = ['#3aab59','#3aab8d','#3a5eab']
    df.plot(color= colors,kind='bar', x='Genre', y=['Mean','Median','Mode'], title=name)
    figure = plt.gcf()
    figure.set_size_inches(32,18)
    save_path = r"C:\Users\whati\Downloads\Python_Dev_Project\Module9\flaskFolder\static\Graphs"    
    plt.savefig(save_path + '\\'+ name +'.png', bbox_inches='tight')
    plt.close()
    logging.info("Overall bar graph was saved")

    sorted_df = df.sort_values(by='Median', ascending=False)
    top_10 = sorted_df.head(10)
    top_name = 'Top_' + name
    top_10.plot(color=colors,kind='bar', x='Genre', y=['Mean','Median'], title=top_name)
    figure = plt.gcf()
    figure.set_size_inches(32,18)
    save_path = r"C:\Users\whati\Downloads\Python_Dev_Project\Module9\flaskFolder\static\Graphs"    
    plt.savefig(save_path +'\\'+ top_name +'.png', bbox_inches='tight')
    plt.close()
    logging.info("Top 10 bar graph was saved")


def filter_explicit(all_genres):

    data = []
    if not isinstance(all_genres,AllGenres):
        logging.error("all_genres is not an instance of AllGenres")
        raise ValueError("all_genres must be an instance of AllGenres")
    try:
        for genres in all_genres:
            for genre in genres:
                explicit = 0
                non_explicit = 0
                for song in genre:
                    if song.explicit == True:
                        explicit+=1
                    else:
                        non_explicit+=1
            data.append({
                'Genre':genre.name,
                'Explicit': explicit,
                'Non-explicit': non_explicit
            })
        df_data = pd.DataFrame(data)
        logging.info("Ratio of explicit to non-explicit songs was calculated")
        return df_data
    except Exception:
        logging.error("There was an error while calculating ratio of explicit songs")

def create_pie(df,variable, name):
    if not isinstance(df, pd.DataFrame):
        logging.error("Df is not a dataframe")
        raise ValueError("Df is not a dataframe")
    if not isinstance(name, str) and not isinstance(variable,str):
        logging.error("Name or variable is not a string")
        raise ValueError("Name or variable is not a string")
    
    if(variable == 'explicit'):
        slice1 = df[df[variable]==True].shape[0]
        slice2 = df[df[variable]==False].shape[0]
        labels = ['Explicit','Non-explicit']
    elif(variable == 'mode'):
        slice1 = (df[variable]==1).sum() #Major 
        slice2 = (df[variable]==0).sum() #Minor
        labels = ['Major','Minor']
    elif(variable == 'time_signature'):
        slice1 = (df[variable]==4).sum() 
        slice2 = (df[variable]==3).sum() 
        labels = ['Time signature 4','Time signature 3']
    else:
        logging.error("We cannot create a pie chart of this variable")
        return
    
    colors = ['#42c966','#1f6131']
    plt.pie([slice1,slice2],labels=labels,autopct='%1.1f%%',colors=colors, textprops={'fontsize': 34})
    plt.axis()
    plt.title(name, fontsize=40)
    figure = plt.gcf()
    figure.set_size_inches(32,18)
    save_path = r"C:\Users\whati\Downloads\Python_Dev_Project\Module9\flaskFolder\static\Graphs"    
    plt.savefig(save_path + '\\' + name +'.png')
    plt.close()
    logging.info("Pie chart was created")
    
def main():
    """
    CSV file that has a dataset of songs fron 125 different genres
    """
    logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="Module6Log.log"
    )

    start_time = time.time()

    filename="dataset.csv"
    csv_manager = FileManager(filename)
    chunks = csv_manager.read_csv_chunks()
    with multiprocessing.Pool() as pool:
        genre_list = pool.map(process_chunk,chunks)


    df = csv_manager.read_csv()   

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("File organization time: " + str(elapsed_time))

    all_genres = AllGenres(genre_list)
    

    data_list_values = ['popularity','duration','danceability','energy','speechiness','acousticness','liveness','valence','tempo']
    df_data_lists = [get_mean_median_mode(all_genres,value) for value in data_list_values]
    data_list_names = ['Popularity_of_Genres','Duration_of_Genres', 'Danceability_of_Genres','Energy_of_Genres','Speechiness_of_Genres','Acousticness_of_Genres','Liveness_of_Genres','Valence_of_Genres','Tempo_of_Genres']

    list(map(create_bar_graph,df_data_lists, data_list_names))

    pie_list_names = ['Ratio of Explicit Songs','Ratio of Major to Minor Songs', 'Ratio of the Time Signature of Songs']
    pie_list_values = ['explicit', 'mode', 'time_signature']

    for i in range(len(pie_list_names)):
        create_pie(df,pie_list_values[i], pie_list_names[i])


    
        

if __name__ == "__main__":
    main()



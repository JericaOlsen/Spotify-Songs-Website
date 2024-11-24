import Module8
import Module6
import pytest
import pandas as pd
import multiprocessing
import time
import pyspark
from pyspark.sql.utils import AnalysisException


def test_FileManager_incorrectcreation():
    """_summary_
    Test that file name is a string
    """
    with pytest.raises(ValueError) as excinfo:
        Module8.FileManager(1)
    assert str(excinfo.value) == "Filename is not a string"


def test_FileManager_filenotfound():
    """_summary_
    Test that if the file cannot be found it won't run
    """
    with pytest.raises(FileNotFoundError) as excinfo:
        file = Module8.FileManager("fake.csv")
        file.read_csv_spark()
    assert str(excinfo.value) == "File is not found"

def test_FileManager_emptydataerror():
    """_summary_
    Test that if file is empty it will raies an error
    """
    with pytest.raises(ValueError) as excinfo:
        file = Module8.FileManager("empty.csv")
        file.read_csv_spark()
    assert str(excinfo.value) == "The DataFrame is empty"


def test_AllGenres_incorrectcreation():
    """_summary_
    Tests that if the value passed into the class creation is not a list it won't run
    """
    with pytest.raises(TypeError) as excinfo:
        Module8.AllGenres("not a list")
    assert str(excinfo.value) == "genre_list must be a list of Genre ojects"

def test_Genre_incorrectcreation():
    """_summary_
    Tests that the name put into genre class creation is a string
    """
    with pytest.raises(ValueError) as excinfo:
        Module8.Genre(123)
    assert str(excinfo.value) == "The genre name is not a string"

def test_Genre_add_song_incorrectsongtype():
    """_summary_
    Tests that the song used to add a song is a song object
    """
    with pytest.raises(ValueError) as excinfo:
        acoustic = Module8.Genre("Acoustic")
        acoustic.add_song("Incorrect song type")
    assert str(excinfo.value) == "Song is not a song object"

def test_Genre_add_song_songalreadyexists():
    """_summary_
    Tests that if the song already exists in the genre it will not be added again
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module8.FileManager(filename)
        df = csv_manager.read_csv_spark()
        dict_top_songs = Module8.creat_dict(df)
        genre = Module8.Genre(dict_top_songs[0]['track_genre'])
        song = Module8.Song(
                dict_top_songs[0]['track_name'], 
                dict_top_songs[0]['track_id'], 
                dict_top_songs[0]['artists'], 
                dict_top_songs[0]['album_name'],
                dict_top_songs[0]['popularity'],
                dict_top_songs[0]['duration_ms'],
                dict_top_songs[0]['danceability'],
                dict_top_songs[0]['energy'],
                dict_top_songs[0]['key'],
                dict_top_songs[0]['loudness'],
                dict_top_songs[0]['mode'],
                dict_top_songs[0]['speechiness'],
                dict_top_songs[0]['acousticness'],
                dict_top_songs[0]['instrumentalness'],
                dict_top_songs[0]['liveness'],
                dict_top_songs[0]['valence'],
                dict_top_songs[0]['tempo'],
                dict_top_songs[0]['track_genre'],
                dict_top_songs[0]['explicit']
            )
        genre.add_song(song)
        genre.add_song(song)
    assert str(excinfo.value) == "Song already is in the song list"

def test_Genre_remove_song_incorrectsongtype():
    """_summary_
    Tests that the song used to remove a song is a song object
    """
    with pytest.raises(ValueError) as excinfo:
        acoustic = Module8.Genre("Acoustic")
        acoustic.remove_song("Incorrect song type")
    assert str(excinfo.value) == "Song is not a song object"

def test_Genre_remove_song_songdoesntexists():
    """_summary_
    Test that if the song is not in the song list it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module8.FileManager(filename)
        df = csv_manager.read_csv_spark()
        dict_top_songs = Module8.creat_dict(df)
        genre = Module8.Genre(dict_top_songs[0]['track_genre'])
        song = Module8.Song(
                dict_top_songs[0]['track_name'], 
                dict_top_songs[0]['track_id'], 
                dict_top_songs[0]['artists'], 
                dict_top_songs[0]['album_name'],
                dict_top_songs[0]['popularity'],
                dict_top_songs[0]['duration_ms'],
                dict_top_songs[0]['danceability'],
                dict_top_songs[0]['energy'],
                dict_top_songs[0]['key'],
                dict_top_songs[0]['loudness'],
                dict_top_songs[0]['mode'],
                dict_top_songs[0]['speechiness'],
                dict_top_songs[0]['acousticness'],
                dict_top_songs[0]['instrumentalness'],
                dict_top_songs[0]['liveness'],
                dict_top_songs[0]['valence'],
                dict_top_songs[0]['tempo'],
                dict_top_songs[0]['track_genre'],
                dict_top_songs[0]['explicit']
            )
        genre.add_song(song)
        song2 = Module8.Song(
                dict_top_songs[0]['track_name'], 
                dict_top_songs[0]['track_id'], 
                dict_top_songs[0]['artists'], 
                dict_top_songs[0]['album_name'],
                dict_top_songs[0]['popularity'],
                dict_top_songs[0]['duration_ms'],
                dict_top_songs[0]['danceability'],
                dict_top_songs[0]['energy'],
                dict_top_songs[0]['key'],
                dict_top_songs[0]['loudness'],
                dict_top_songs[0]['mode'],
                dict_top_songs[0]['speechiness'],
                dict_top_songs[0]['acousticness'],
                dict_top_songs[0]['instrumentalness'],
                dict_top_songs[0]['liveness'],
                dict_top_songs[0]['valence'],
                dict_top_songs[0]['tempo'],
                dict_top_songs[0]['track_genre'],
                dict_top_songs[0]['explicit']
            )
        genre.remove_song(song2)
    assert str(excinfo.value) == "Song is not in the song list"

def test_Genre_list_songs_emptylist():
    """_summary_
    Tests that if the song list is empty the function will not run
    """
    with pytest.raises(ValueError) as excinfo:
        acoustic = Module8.Genre("Acoustic")
        acoustic.list_songs()
    assert str(excinfo.value) == "There are no songs in the song list"

def test_Song_incorrectcreation():
    """_summary_
    Tests that if the value passed into the class creation is not a formatted correctly it won't run
    """
    with pytest.raises(ValueError) as excinfo:

        song = Module8.Song(
                'Mock track', 
                '123433', 
                'ab', 
                'c',
                0.7,
                0.4,
                0.6,
                0.8,
                [],
                0.7,
                0.5,
                0.3,
                0.2,
                0.4,
                0.7,
                0.5,
                0.8,
                'rock',
                False
            )
    assert str(excinfo.value) == "One of the variables entered is not a float, string, or integer"

def test_create_dict():
    """_summary_
    Tests that if variable put into create_dict is not a file it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module8.creat_dict([1,2,3])
    assert str(excinfo.value) == "File is not a dataframe"

def test_organize_genres_keyerror():
    """_summary_
    Tests that if the variable is not correctly formatted it won't run 
    """
    with pytest.raises(ValueError) as excinfo:
        incorrect_dict = [{"track_name":"Song1","track_genre":"Rock","track_id":12321231}]
        Module8.organize_genres(incorrect_dict)
    assert str(excinfo.value) == "Missing an expected value for song dictionary"

def test_organize_genre_notdict():
    """_summary_
    Tests that if the value is not a dictionary organize_genres will not run
    """
    with pytest.raises(ValueError) as excinfo:
        Module8.organize_genres("Incorrect list")
    assert str(excinfo.value) == "song_dict is not a list"

def test_get_mean_median_mode_AllGenres():
    """_summary_
    Tests that if variable is not an AllGenres object the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module8.get_mean_median_mode([], 'popularity')
    assert str(excinfo.value) == "all_genres must be an instance of AllGenres"

def test_get_mean_median_mode_wrong_values():
    """_summary_
    Tests that if variable of value is not a string the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module8.FileManager(filename)
    df = csv_manager.read_csv_spark()

    song_dict = Module8.creat_dict(df)
    genre_list = Module8.organize_genres(song_dict)
    all_genres = Module8.AllGenres(genre_list)
    with pytest.raises(ValueError) as excinfo:
        Module8.get_mean_median_mode(all_genres, 123)
    assert str(excinfo.value) == "value must be a string"

def test_get_mean_median_mode_unknown_value():
    """_summary_
    Tests that if variable of value is not a string associated with song variable the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module8.FileManager(filename)
    df = csv_manager.read_csv_spark()

    song_dict = Module8.creat_dict(df)
    genre_list = Module8.organize_genres(song_dict)
    all_genres = Module8.AllGenres(genre_list)
    with pytest.raises(ValueError) as excinfo:
        Module8.get_mean_median_mode(all_genres, 'swaginess')
    assert str(excinfo.value) == "This value is not an value associated with Songs"

def test_create_bar_graph_incorrect_df():
    """_summary_
    Tests that if variable of df is not a DataFrame the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module8.create_bar_graph([],"Incorrect Graph")
    assert str(excinfo.value) == "Df is not a dataframe"

def test_create_bar_graph_incorrect_name():
    """_summary_
    Tests that if variable of name is not a string the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module8.FileManager(filename)
    df = csv_manager.read_csv_spark()

    song_dict = Module8.creat_dict(df)
    genre_list = Module8.organize_genres(song_dict)
    all_genres = Module8.AllGenres(genre_list)

    df_data_lists = Module8.get_mean_median_mode(all_genres,'popularity')

    with pytest.raises(ValueError) as excinfo:
        Module8.create_bar_graph(df_data_lists,123)
    assert str(excinfo.value) == "Name is not a string"

# def filter_explicit_incorrect_allGenres():
#     """_summary_
#     Tests that if variable of allGenres is not a AllGenres object the program won't run
#     """
#     with pytest.raises(ValueError) as excinfo:
#         Module8.filter_explicit(12)
#     assert str(excinfo.value) == "all_genres must be an instance of AllGenres"

def test_create_pie_incorrect_df():
    """_summary_
    Tests that if variable of df is not a DataFrame the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module8.create_pie([], "mode", "Incorrect Pie Chart")
    assert str(excinfo.value) == "Df is not a dataframe"

def test_create_pie_incorrect_name():
    """_summary_
    Tests that if variable of name is not a string the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module8.FileManager(filename)
    df = csv_manager.read_csv_spark()

    with pytest.raises(ValueError) as excinfo:
        Module8.create_pie(df,"mode", 123)
    assert str(excinfo.value) == "The variable name or graph name is not a string"


# def test_file_processing_time():
#     """_summary_
#     Tests multiprocessing of files is faster than previous code
#     """
#     start_time = time.time()

#     filename="dataset.csv"
#     csv_manager = Module8.FileManager(filename)
#     chunks = csv_manager.read_csv_spark_chunks()
#     with multiprocessing.Pool() as pool:
#         genre_list = pool.map(Module8.process_chunk,chunks)

#     end_time = time.time()
#     elapsed_time = end_time - start_time
    

#     assert elapsed_time < 14, "Elapsed time is not less than the previous elapsed time"

# test_FileManager_emptydataerror()
import Module6
import pytest
import pandas as pd

def test_FileManager_incorrectcreation():
    """_summary_
    Test that file name is a string
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.FileManager(1)
    assert str(excinfo.value) == "Filename is not a string"


def test_FileManager_filenotfound():
    """_summary_
    Test that if the file cannot be found it won't run
    """
    with pytest.raises(FileNotFoundError) as excinfo:
        file = Module6.FileManager("fake.csv")
        file.read_csv()
    assert str(excinfo.value) == "File is not found"

def test_FileManager_emptydataerror():
    """_summary_
    Test that if file is empty it will raies an error
    """
    with pytest.raises(pd.errors.EmptyDataError) as excinfo:
        file = Module6.FileManager("empty.csv")
        file.read_csv()
    assert str(excinfo.value) == "The file is empty"


def test_AllGenres_incorrectcreation():
    """_summary_
    Tests that if the value passed into the class creation is not a list it won't run
    """
    with pytest.raises(TypeError) as excinfo:
        Module6.AllGenres("not a list")
    assert str(excinfo.value) == "genre_list must be a list of Genre ojects"

def test_Genre_incorrectcreation():
    """_summary_
    Tests that the name put into genre class creation is a string
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.Genre(123)
    assert str(excinfo.value) == "The genre name is not a string"

def test_Genre_add_song_incorrectsongtype():
    """_summary_
    Tests that the song used to add a song is a song object
    """
    with pytest.raises(ValueError) as excinfo:
        acoustic = Module6.Genre("Acoustic")
        acoustic.add_song("Incorrect song type")
    assert str(excinfo.value) == "Song is not a song object"

def test_Genre_add_song_songalreadyexists():
    """_summary_
    Tests that if the song already exists in the genre it will not be added again
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module6.FileManager(filename)
        df = csv_manager.read_csv()
        dict_top_songs = Module6.creat_dict(df)
        genre = Module6.Genre(dict_top_songs[0]['track_genre'])
        song = Module6.Song(
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
        acoustic = Module6.Genre("Acoustic")
        acoustic.remove_song("Incorrect song type")
    assert str(excinfo.value) == "Song is not a song object"

def test_Genre_remove_song_songdoesntexists():
    """_summary_
    Test that if the song is not in the song list it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module6.FileManager(filename)
        df = csv_manager.read_csv()
        dict_top_songs = Module6.creat_dict(df)
        genre = Module6.Genre(dict_top_songs[0]['track_genre'])
        song = Module6.Song(
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
        song2 = Module6.Song(
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
        acoustic = Module6.Genre("Acoustic")
        acoustic.list_songs()
    assert str(excinfo.value) == "There are no songs in the song list"

def test_Song_incorrectcreation():
    """_summary_
    Tests that if the value passed into the class creation is not a formatted correctly it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module6.FileManager(filename)
        df = csv_manager.read_csv()
        dict_top_songs = Module6.creat_dict(df)
        song = Module6.Song(
                dict_top_songs[0]['track_name'], 
                dict_top_songs[0]['track_id'], 
                dict_top_songs[0]['artists'], 
                dict_top_songs[0]['album_name'],
                dict_top_songs[0]['popularity'],
                dict_top_songs[0]['duration_ms'],
                dict_top_songs[0]['danceability'],
                dict_top_songs[0]['energy'],
                [],
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
    assert str(excinfo.value) == "One of the variables entered is not a float, string, or integer"

def test_create_dict():
    """_summary_
    Tests that if variable put into create_dict is not a file it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.creat_dict([1,2,3])
    assert str(excinfo.value) == "File is not a dataframe"

def test_organize_genres_keyerror():
    """_summary_
    Tests that if the variable is not correctly formatted it won't run 
    """
    with pytest.raises(ValueError) as excinfo:
        incorrect_dict = [{"track_name":"Song1","track_genre":"Rock","track_id":12321231}]
        Module6.organize_genres(incorrect_dict)
    assert str(excinfo.value) == "Missing an expected value for song dictionary"

def test_organize_genre_notdict():
    """_summary_
    Tests that if the value is not a dictionary organize_genres will not run
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.organize_genres("Incorrect list")
    assert str(excinfo.value) == "song_dict is not a list"

def test_get_mean_median_mode_AllGenres():
    """_summary_
    Tests that if variable is not an AllGenres object the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.get_mean_median_mode([], 'popularity')
    assert str(excinfo.value) == "all_genres must be an instance of AllGenres"

def test_get_mean_median_mode_wrong_values():
    """_summary_
    Tests that if variable of value is not a string the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module6.FileManager(filename)
    df = csv_manager.read_csv()
    dict_top_songs = Module6.creat_dict(df)
    genre_list = Module6.organize_genres(dict_top_songs)
    all_genres = Module6.AllGenres(genre_list)
    with pytest.raises(ValueError) as excinfo:
        Module6.get_mean_median_mode(all_genres, 123)
    assert str(excinfo.value) == "value must be a string"

def test_get_mean_median_mode_unknown_value():
    """_summary_
    Tests that if variable of value is not a string associated with song variable the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module6.FileManager(filename)
    df = csv_manager.read_csv()
    dict_top_songs = Module6.creat_dict(df)
    genre_list = Module6.organize_genres(dict_top_songs)
    all_genres = Module6.AllGenres(genre_list)
    with pytest.raises(ValueError) as excinfo:
        Module6.get_mean_median_mode(all_genres, 'swaginess')
    assert str(excinfo.value) == "This value is not an value associated with Songs"

def test_create_bar_graph_incorrect_df():
    """_summary_
    Tests that if variable of df is not a DataFrame the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.create_bar_graph([],"Incorrect Graph")
    assert str(excinfo.value) == "Df is not a dataframe"


def test_create_bar_graph_incorrect_name():
    """_summary_
    Tests that if variable of name is not a string the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module6.FileManager(filename)
    df = csv_manager.read_csv()
    dict_top_songs = Module6.creat_dict(df)
    genre_list = Module6.organize_genres(dict_top_songs)
    all_genres = Module6.AllGenres(genre_list)
    df = Module6.get_mean_median_mode(all_genres, 'popularity')
    with pytest.raises(ValueError) as excinfo:
        Module6.create_bar_graph(df,123)
    assert str(excinfo.value) == "Name is not a string"

def filter_explicit_incorrect_allGenres():
    """_summary_
    Tests that if variable of allGenres is not a AllGenres object the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.filter_explicit(12)
    assert str(excinfo.value) == "all_genres must be an instance of AllGenres"

def test_create_pie_incorrect_df():
    """_summary_
    Tests that if variable of df is not a DataFrame the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module6.create_pie([], "Incorrect Pie Chart")
    assert str(excinfo.value) == "Df is not a dataframe"

def test_create_pie_incorrect_name():
    """_summary_
    Tests that if variable of name is not a string the program won't run
    """
    filename="dataset.csv"
    csv_manager = Module6.FileManager(filename)
    df = csv_manager.read_csv()
    dict_top_songs = Module6.creat_dict(df)
    genre_list = Module6.organize_genres(dict_top_songs)
    all_genres = Module6.AllGenres(genre_list)
    df = Module6.filter_explicit(all_genres)
    with pytest.raises(ValueError) as excinfo:
        Module6.create_bar_graph(df,123)
    assert str(excinfo.value) == "Name is not a string"
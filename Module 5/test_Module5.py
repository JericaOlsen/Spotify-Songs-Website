import Module5
import pytest
import pandas as pd

def test_FileManager_incorrectcreation():
    """_summary_
    Test that file name is a string
    """
    with pytest.raises(ValueError) as excinfo:
        Module5.FileManager(1)
    assert str(excinfo.value) == "Filename is not a string"


def test_FileManager_filenotfound():
    """_summary_
    Test that if the file cannot be found it won't run
    """
    with pytest.raises(FileNotFoundError) as excinfo:
        file = Module5.FileManager("fake.csv")
        file.read_csv()
    assert str(excinfo.value) == "File is not found"

def test_FileManager_emptydataerror():
    """_summary_
    Test that if file is empty it will raies an error
    """
    with pytest.raises(pd.errors.EmptyDataError) as excinfo:
        file = Module5.FileManager("empty.csv")
        file.read_csv()
    assert str(excinfo.value) == "The file is empty"


def test_AllGenres_incorrectcreation():
    """_summary_
    Tests that if the value passed into the class creation is not a list it won't run
    """
    with pytest.raises(TypeError) as excinfo:
        Module5.AllGenres("not a list")
    assert str(excinfo.value) == "genre_list must be a list of Genre ojects"

def test_Genre_incorrectcreation():
    """_summary_
    Tests that the name put into genre class creation is a string
    """
    with pytest.raises(ValueError) as excinfo:
        Module5.Genre(123)
    assert str(excinfo.value) == "The genre name is not a string"

def test_Genre_add_song_incorrectsongtype():
    """_summary_
    Tests that the song used to add a song is a song object
    """
    with pytest.raises(ValueError) as excinfo:
        acoustic = Module5.Genre("Acoustic")
        acoustic.add_song("Incorrect song type")
    assert str(excinfo.value) == "Song is not a song object"

def test_Genre_add_song_songalreadyexists():
    """_summary_
    Tests that if the song already exists in the genre it will not be added again
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module5.FileManager(filename)
        df = csv_manager.read_csv()
        dict_top_songs = Module5.creat_dict(df)
        genre = Module5.Genre(dict_top_songs[0]['track_genre'])
        song = Module5.Song(
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
                dict_top_songs[0]['track_genre']
            )
        genre.add_song(song)
        genre.add_song(song)
    assert str(excinfo.value) == "Song already is in the song list"

def test_Genre_remove_song_incorrectsongtype():
    """_summary_
    Tests that the song used to remove a song is a song object
    """
    with pytest.raises(ValueError) as excinfo:
        acoustic = Module5.Genre("Acoustic")
        acoustic.remove_song("Incorrect song type")
    assert str(excinfo.value) == "Song is not a song object"

def test_Genre_remove_song_songdoesntexists():
    """_summary_
    Test that if the song is not in the song list it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module5.FileManager(filename)
        df = csv_manager.read_csv()
        dict_top_songs = Module5.creat_dict(df)
        genre = Module5.Genre(dict_top_songs[0]['track_genre'])
        song = Module5.Song(
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
                dict_top_songs[0]['track_genre']
            )
        genre.add_song(song)
        song2 = Module5.Song(
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
                dict_top_songs[0]['track_genre']
            )
        genre.remove_song(song2)
    assert str(excinfo.value) == "Song is not in the song list"

def test_Genre_list_songs_emptylist():
    """_summary_
    Tests that if the song list is empty the function will not run
    """
    with pytest.raises(ValueError) as excinfo:
        acoustic = Module5.Genre("Acoustic")
        acoustic.list_songs()
    assert str(excinfo.value) == "There are no songs in the song list"

def test_Song_incorrectcreation():
    """_summary_
    Tests that if the value passed into the class creation is not a formatted correctly it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        filename="dataset.csv"
        csv_manager = Module5.FileManager(filename)
        df = csv_manager.read_csv()
        dict_top_songs = Module5.creat_dict(df)
        song = Module5.Song(
                dict_top_songs[0]['track_name'], 
                dict_top_songs[0]['track_id'], 
                dict_top_songs[0]['artists'], 
                dict_top_songs[0]['album_name'],
                dict_top_songs[0]['popularity'],
                dict_top_songs[0]['duration_ms'],
                dict_top_songs[0]['danceability'],
                dict_top_songs[0]['energy'],
                False,
                dict_top_songs[0]['loudness'],
                dict_top_songs[0]['mode'],
                dict_top_songs[0]['speechiness'],
                dict_top_songs[0]['acousticness'],
                dict_top_songs[0]['instrumentalness'],
                dict_top_songs[0]['liveness'],
                dict_top_songs[0]['valence'],
                dict_top_songs[0]['tempo'],
                dict_top_songs[0]['track_genre']
            )
    assert str(excinfo.value) == "One of the variables entered is not a float, string, or integer"

def test_create_dict():
    """_summary_
    Tests that if variable put into create_dict is not a file it won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module5.creat_dict([1,2,3])
    assert str(excinfo.value) == "File is not a dataframe"

def test_organize_genres_keyerror():
    """_summary_
    Tests that if the variable is not correctly formatted it won't run 
    """
    with pytest.raises(ValueError) as excinfo:
        incorrect_dict = [{"track_name":"Song1","track_genre":"Rock","track_id":12321231}]
        Module5.organize_genres(incorrect_dict)
    assert str(excinfo.value) == "Missing an expected value for song dictionary"

def test_organize_genre_notdict():
    """_summary_
    Tests that if the value is not a dictionary organize_genres will not run
    """
    with pytest.raises(ValueError) as excinfo:
        Module5.organize_genres("Incorrect list")
    assert str(excinfo.value) == "song_dict is not a list"

def test_get_danceability():
    """_summary_
    Tests that if variable is not an AllGenres object the program won't run
    """
    with pytest.raises(ValueError) as excinfo:
        Module5.get_danceability([])
    assert str(excinfo.value) == "all_genres must be an instance of AllGenres"
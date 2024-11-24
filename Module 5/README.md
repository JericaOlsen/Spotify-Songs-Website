# Module 5

Add error testing into the code to make sure it runs as expected

## Execution

#### test_Module5.py file

```python
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
```

## Summary

For this program I created a new file titled test_Module5.py. I decided to use pytest method of error testing so I could contain all of the testing in a separate file. I created 15 different tests that are able to make sure the creation of the different classes and functions work as expected.

## Example Output

This example output shows that all the tests passed after running the file.

```python
platform win32 -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0                                                                       
rootdir: C:\Users\whati\Downloads\Python_Dev_Project\Module 5
collected 15 items

test_Module5.py ...............                                                                                            [100%]

====================================================== 15 passed in 3.31s ======================================================= 
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
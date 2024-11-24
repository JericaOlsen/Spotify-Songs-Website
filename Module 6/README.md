# Module 6

Module6: Visualize your data with graphs and add error testing for this

## Execution

### Modified/Added Functions

For this program I edited the the function get_mean_median_mode() and added the functions create_bar_graph(), filter_explicit(), and create_pie().

```python
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
            for song in genre:
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
                dance_mean = mystatistics.mean(value_list)
                dance_median = mystatistics.median(value_list)
                dance_mode = mystatistics.mode(value_list)
                data.append({ 
                    "Genre": genre.name,
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
    plt.savefig(name,bbox_inches='tight')
    plt.close()
    logging.info("Overall bar graph was saved")

    sorted_df = df.sort_values(by='Median', ascending=False)
    top_10 = sorted_df.head(10)
    top_name = 'Top ' + name
    top_10.plot(color=colors,kind='bar', x='Genre', y=['Mean','Median'], title=top_name)
    figure = plt.gcf()
    figure.set_size_inches(32,18)
    plt.savefig(top_name,bbox_inches='tight')
    plt.close()
    logging.info("Top 10 bar graph was saved")


def filter_explicit(all_genres):

    data = []
    if not isinstance(all_genres,AllGenres):
        logging.error("all_genres is not an instance of AllGenres")
        raise ValueError("all_genres must be an instance of AllGenres")
    try:
        for genre in all_genres:
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

def create_pie(df,name):
    if not isinstance(df, pd.DataFrame):
        logging.error("Df is not a dataframe")
        raise ValueError("Df is not a dataframe")
    if not isinstance(name, str):
        logging.error("Name is not a string")
        raise ValueError("Name is not a string")
    
    total_explicit = df['Explicit'].sum()
    total_nonexplicit = df['Non-explicit'].sum()

    colors = ['#42c966','#1f6131']
    plt.pie([total_explicit,total_nonexplicit],labels=['Explicit','Non-explicit'],autopct='%1.1f%%',colors=colors)
    plt.axis()
    plt.title(name)
    figure = plt.gcf()
    figure.set_size_inches(32,18)
    plt.savefig(name)
    plt.close()
    logging.info("Pie chart was created")
    
if __name__=='__main__':
    """
    CSV file that has a dataset of songs fron 125 different genres
    """
    logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="Module5Log.log"
    )

    filename="dataset.csv"
    csv_manager = FileManager(filename)
    df = csv_manager.read_csv()
    dict_top_songs = creat_dict(df)
    genre_list = organize_genres(dict_top_songs)
    all_genres = AllGenres(genre_list)

    data_list_values = ['popularity','duration','danceability','energy','speechiness','acousticness','liveness','valence','tempo']
    df_data_lists = [get_mean_median_mode(all_genres,value) for value in data_list_values]
    data_list_names = ['Popularity of Genres','Duration of Genres', 'Danceability of Genres','Energy of Genres','Speechiness of Genres','Acousticness of Genres','Liveness of Genres','Valence of Genres','Tempo of Genres']
    result = list(map(create_bar_graph,df_data_lists, data_list_names))

    explicit_data = filter_explicit(all_genres)
    create_pie(explicit_data,'Ratio of Explicit Songs')
    logging.info("Program has been completed")
```

### test_Module6.py File Additions

For error testing I made sure to modify my tests 

```python
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
```

## Summary

For this program I created the new functions create_bar_graph() and edited the previous function get_danceability() to get_mean_median_mode(). This way I can now calculate the mean, median, and mode of any of the attributes of songs that are integers and then turn them into a bar graph that has all the genres mean median and modes displayed and the top ten genres based on median. 

I also made the new functions filter_explicit() and create_pie() that found the ratio of explicit to non-explicit songs for each genre and then created a pie char showing the overall ratio in percentages.

For testing I made sure to modify my tests to make sure get_mean_median_mode() works correctly and made new tests for the other functions.

## Example Output

### Bar Graphs 

This shows some of the bar graph examples that had trends

![Bar Graph of Speechiness of Genres](<Speechiness of Genres-1.png>)

![Bar Graph of Top 10 Speechiness of Genres](<Top Speechiness of Genres-1.png>)

![Bar Graph of Popularity of Genres](<Popularity of Genres-1.png>)

![Bar Graph of Top 10 Popularity of Genres](<Top Popularity of Genres-1.png>)

### Pie Chart

This is the output of the ratio of explicit to non-explicit songs

![Ratio of Explicit to Non-Explicit Songs](<Ratio of Explicit Songs-1.png>)

### Test Cases

This example output shows that all the tests passed after running the file.

```python
==================================================== test session starts =====================================================
platform win32 -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\whati\Downloads\Python_Dev_Project\Module 6
collected 21 items

test_Module6.py .....................                                                                                   [100%]

==================================================== 21 passed in 13.34s ===================================================== 
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
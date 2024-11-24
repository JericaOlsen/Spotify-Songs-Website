# Module 8

Module8: Modify your program to use pyspark

ChatGPT was used to create pyspark csv reading and filtering functions

## Execution

### Modified/Added Functions

For this program I added a read_csv_spark function to my file manager to be able to read the csv file as to a Spark Dataframe as well as modified the create_dict function so it could change the Spark DataFrame into a dictionary

```python
    def read_csv_spark(self):
        
        if not os.path.isfile(self.name):
            logging.error("The file could not be read as it does not exist")
            raise FileNotFoundError("File is not found")
        
        schema = StructType([
                StructField("", IntegerType(), True),
                StructField("track_id", StringType(), True),
                StructField("artists", StringType(), True),
                StructField("album_name", StringType(), True),
                StructField("track_name", StringType(), True),
                StructField("popularity", IntegerType(), True),
                StructField("duration_ms",IntegerType(), True),
                StructField("explicit",BooleanType(), True), 
                StructField("danceability",FloatType(), True),
                StructField("energy",FloatType(), True),
                StructField("key",IntegerType(), True),
                StructField("loudness",FloatType(), True),
                StructField("mode",IntegerType(), True),
                StructField("speechiness",FloatType(), True),
                StructField("acousticness",FloatType(), True),
                StructField("instrumentalness",FloatType(), True),
                StructField("liveness",FloatType(), True),
                StructField("valence",FloatType(), True),
                StructField("tempo",FloatType(), True),
                StructField("time_signature",IntegerType(), True),
                StructField("track_genre",StringType(), True),
            ])
        try:

            spark = SparkSession.builder.appName("CSV Reader").getOrCreate()
            df = spark.read.csv(self.name,header=True,quote='"',escape='\\',multiLine=True, encoding='UTF-8', schema=schema)
            df = df.select("track_id", "artists", "album_name", "track_name", "popularity", "duration_ms",
               "explicit", "danceability", "energy", "key", "loudness", "mode",
               "speechiness", "acousticness", "instrumentalness", "liveness", "valence",
               "tempo", "time_signature", "track_genre")

            if df.isEmpty():
                logging.error("The file is empty")
                raise ValueError("The DataFrame is empty")
        
            logging.info("CSV chunk file was read from the path" )
            return df
        except AnalysisException as e:
            logging.error("The file could not be read as it does not exists")
            raise FileNotFoundError("File is not found")
        except Exception as e:
            logging.error("An unexpected error occured")
            raise e


def creat_dict(file):
    """
    Args:
        file (DataFrame):The dataframe of the csv file 

    Returns:
        Dict: Dictionary of the csv file
    """
    if not isinstance(file, DataFrame):
        logging.error("File is not a dataframe")
        raise ValueError("File is not a dataframe")
    dict_top_songs = file.collect()  # Collect the data to the driver
    dict_top_songs = [row.asDict() for row in dict_top_songs]  # Convert Row objects to dictionaries

    logging.info("The file containg the top songs was changed into a dictionary")
    return dict_top_songs
```
I also was able to get rid of my filter_explicit function and use my create_pie function to be able to create pie graphs more efficiently and for the three variables of all the songs, explicit, mode, and time signature.

```python
def create_pie(df,var_name,graph_name):
    """_summary_

    Args:
        df (Spark DataFrame): A Spark DataFrame of all the songs
        var_name (Str): A string containg the variable name for the songs
        graph_name (Str): The name of the pie chart

    Raises:
        ValueError: checks if df is a Spark DataFrame
        ValueError: checks if the graph name or variable name is a string
    """
    if not isinstance(df, DataFrame):
        logging.error("Df is not a dataframe")
        raise ValueError("Df is not a dataframe")
    if not isinstance(graph_name, str) or not isinstance(var_name, str):
        logging.error("The variable name or graph name is not a string")
        raise ValueError("The variable name or graph name is not a string")
    
    if(var_name == 'explicit'):
        slice1 = df.filter(df.explicit == 'True').count()
        slice2 = df.filter(df.explicit == 'False').count()
        labels = ['Explicit','Non-explicit']
    elif(var_name == 'mode'):
        slice1 = df.filter(df.mode == '1').count() #Major 
        slice2 = df.filter(df.mode == '0').count() #Minor
        labels = ['Major','Minor']
    elif(var_name == 'time_signature'):
        slice1 = df.filter(df.time_signature == '4').count()
        slice2 = df.filter(df.time_signature == '3').count()
        labels = ['Time signature 4','Time signature 3']

    colors = ['#42c966','#1f6131']
    plt.pie([slice1,slice2],labels=labels,autopct='%1.1f%%',colors=colors, textprops={'fontsize': 34})
    plt.axis()
    plt.title(graph_name, fontsize=40)
    figure = plt.gcf()
    figure.set_size_inches(32,18)
    plt.savefig(graph_name)
    plt.close()
    logging.info("Pie chart was created")
  ```

### test_Module8.py Modifications

For error testing I modified my tests to work with Spark files with the most modification happening for my tests for the file manager. 

```python
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
```

## Summary

For this program I was able to modify it to work with pyspark by changing how I read in the csv and turn it into a dictionary. I also modified my creation of the pie charts to be able to more efficiently create pie charts for the mode of songs, the ratio of explicit songs, and the time signatures of songs.

## Example Output

```python
24/10/31 20:09:33 WARN Shell: Did not find winutils.exe: java.io.FileNotFoundException: java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset. -see https://wiki.apache.org/hadoop/WindowsProblems
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/10/31 20:09:33 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
File organization time with Spark: 7.400861501693726
SUCCESS: The process with PID 9172 (child process of PID 29520) has been terminated.
SUCCESS: The process with PID 29520 (child process of PID 2620) has been terminated.
SUCCESS: The process with PID 2620 (child process of PID 12452) has been terminated.
```

### Pie Chart Output

![Ratio of Explicit to Non-Explicit Songs](<Ratio of Explicit Songs.png>)
![Ratio of the Time Signature of Songs](<Ratio of the Time Signature of Songs.png>)
![Ratio of Major to Minor Songs](<Ratio of Major to Minor Songs.png>)

### Test Cases

This example output shows that all the tests passed after running the file.

```python
test_Module8.py .....................                                                                                      [100%]

====================================================== 21 passed in 22.87s ====================================================== 
SUCCESS: The process with PID 7088 (child process of PID 3912) has been terminated.
SUCCESS: The process with PID 3912 (child process of PID 26944) has been terminated.
SUCCESS: The process with PID 26944 (child process of PID 20516) has been terminated.
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
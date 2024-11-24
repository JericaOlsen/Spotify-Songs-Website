# Module 7

Module6: Module7: Implement asynchronous data fetching and multiprocessing to speed up data processing.

ChatGPT was used to create multiprocessing code and pool usage.



## Execution

### Modified/Added Functions

For this program I used multiprocessing to read in my csv file and organize it faster. I did this by using chunks of the data and processing them in threads. To accomplish this the read_csv_chunks() function was created and the multiprocessing module was used.

```python
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

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("File organization time: " + str(elapsed_time))
```

### test_Module7.py Additions

For error testing I added this test to ensure that the multiprocessing did run faster than the previous implementation. I got the number 14 seconds by running the time module on the previous module and rounding down.

```python
def test_file_processing_time():
    """_summary_
    Tests multiprocessing of files is faster than previous code
    """
    start_time = time.time()

    filename="dataset.csv"
    csv_manager = Module7.FileManager(filename)
    chunks = csv_manager.read_csv_chunks()
    with multiprocessing.Pool() as pool:
        genre_list = pool.map(Module7.process_chunk,chunks)

    end_time = time.time()
    elapsed_time = end_time - start_time
    

    assert elapsed_time < 14, "Elapsed time is not less than the previous elapsed time"
```

## Summary

For this program I was able to make my code run faster by using multiprocessing for my file handling. I made sure to separate my code into chunks and then process it using threads. I also created a test case to make sure the multiprocessing handled the file faster than the previous implementation.

## Example Output

### Current vs Previous Output

Current output
```python
File organization time: 5.2888946533203125
```

Previous output
```python
File organization time: 15.533825397491455
```

### Test Cases

This example output shows that all the tests passed after running the file.

```python
collected 22 items

test_Module7.py ......................                                                                                     [100%]

====================================================== 22 passed in 20.02s ====================================================== 
PS C:\Users\whati\Downloads\Python_Dev_Project\Module 7> 
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
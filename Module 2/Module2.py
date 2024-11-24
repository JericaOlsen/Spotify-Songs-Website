import pandas as pd
import mystatistics

'''
Module2: Creates a python module to get median, mean, and mode of the dataset.
'''

def read_csv(filename):
    """
    Param:
        filename (string): Name of the file

    Returns:
        DataFrame: The dataframe of the csv file
    """
    df=pd.read_csv(filename) 
    return df

def creat_dict(file):
    """
    Args:
        file (DataFrame):The dataframe of the csv file 

    Returns:
        Dict: Dictionary of the csv file
    """

    dict_top_songs = file.to_dict('records')
    return dict_top_songs

def get_statistics(song_dict):
    """_summary_

    Args:
        dict (dictionary): Dictionary of all the songs

    Returns:
        Mean, Median, Mode: The mean, median, and mode of the chosen variable of the songs
    """
    danceability_list = []
    for item in song_dict:
        danceability_list.append(item["danceability"])

    dance_mean = mystatistics.mean(danceability_list)
    dance_median = mystatistics.median(danceability_list)
    dance_mode = mystatistics.mode(danceability_list)
    return dance_mean, dance_median, dance_mode

if __name__=='__main__':
    """
    CSV file that has a dataset of songs fron 125 different genres
    """
    filename='dataset.csv'
    df = read_csv(filename)
    dict_top_songs = creat_dict(df)
    dance_mean, dance_median, dance_mode = get_statistics(dict_top_songs)
    print("Mean danceability of the top songs is: " + str(dance_mean))
    print("Median danceability of the top songs is: "+ str(dance_median))
    print("Mode danceability of the top songs is: "+ str(dance_mode))


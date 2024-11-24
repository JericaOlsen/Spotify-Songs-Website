import pandas as pd


'''
Module1: Introduces user to the system
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


if __name__=='__main__':
    """
    CSV file that has a dataset of songs fron 125 different genres
    """
    filename='dataset.csv'
    df = read_csv(filename)
    dict_top_songs = creat_dict(df)
    print(df.head(15))
    print(dict_top_songs)


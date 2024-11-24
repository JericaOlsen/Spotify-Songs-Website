# Module 1

Create a profession-style development enviroment and then fetch data from a CSV file and store it in a Python data structure.

## Execution

```python
import pandas as pd

'''
Module1: Introduces user into the system
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
    dict_top_songs = df.to_dict('records')
    return dict_top_songs


if __name__=='__main__':
    """
    CSV file that has the top 200 spotify songs from 2000-2019
    """
    filename='songs_normalize.csv'
    df = read_csv(filename)
    dict_top_songs = creat_dict(df)
    print(df.head(15))

```

## Description

This program takes the csv file 'song_normalize.csv' and reads it into a panda dataframe. It then coverts this dataframe into a dictionary and prints 15 of those entries.

## Example Output

```python
             artist                                              song  duration_ms  ...  valence tempo                  genre
0    Britney Spears                            Oops!...I Did It Again       211160  ...    0.894   95.053                    pop  
1         blink-182                              All The Small Things       167066  ...    0.684  148.726              rock, pop  
2        Faith Hill                                           Breathe       250546  ...    0.278  136.859           pop, country  
3          Bon Jovi                                      It's My Life       224493  ...    0.544  119.992            rock, metal  
4            *NSYNC                                       Bye Bye Bye       200560  ...    0.879  172.656                    pop  
5             Sisqo                                        Thong Song       253733  ...    0.714  121.549      hip hop, pop, R&B  
6            Eminem                               The Real Slim Shady       284200  ...    0.760  104.504                hip hop  
7   Robbie Williams                                           Rock DJ       258560  ...    0.861  103.035              pop, rock  
8   Destiny's Child                                       Say My Name       271333  ...    0.734  138.009               pop, R&B  
9             Modjo                            Lady - Hear Me Tonight       307153  ...    0.869  126.041       Dance/Electronic  
10  Gigi D'Agostino                                  L'Amour Toujours       238759  ...    0.808  139.066                    pop  
11        Eiffel 65  Move Your Body - Gabry Ponte Original Radio Edit       268863  ...    0.960  129.962                    pop  
12     Bomfunk MC's                                        Freestyler       306333  ...    0.568  163.826                    pop  
13            Sting                                       Desert Rose       285960  ...    0.147  111.989              rock, pop  
14        Melanie C                           Never Be The Same Again       294200  ...    0.398  160.067  pop, Dance/Electronic
```
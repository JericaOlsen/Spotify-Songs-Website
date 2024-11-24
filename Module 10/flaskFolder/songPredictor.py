from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


def get_songs_genre(song, df):
    """_summary_

    Args:
        song (song name): string of the song name
        df (dataframe): Dataframe of all the songs

    Returns:
        dataframe: Dataframe containing only the genre of the selected song
    """
    selected_song = df[df['track_name']==song]

    if selected_song.empty:
        return "No song in dataset"
    
    selected_genre = selected_song['track_genre'].iloc[0]

    filtered_df = df[df['track_genre'] == selected_genre]

    return filtered_df

def get_similar_songs(name, genre_df, top_n=3):
    """_summary_

    Args:
        name (string): Name of the song
        genre_df (dataframe): Dataframe of only the same genre of the song
        top_n (int, optional): Number of similar songs returned. Defaults to 3.

    Returns:
        list: list of songs that are similar to the selected song.
    """
    columns = ['popularity','danceability','energy','key','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
    x = genre_df[columns]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(x)

    cosine_sim = cosine_similarity(X_scaled)

    if name not in genre_df['track_name'].values:
        return f"Song '{name}' not found in the dataset."

    genre_df = genre_df.reset_index()
    idx = genre_df[genre_df['track_name'] == name].index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]

    song_indices = [i[0]for i in sim_scores]

    return genre_df['track_name'].iloc[song_indices]


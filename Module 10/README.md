# Module 10

Module10: Integrate machine learning into your application

ChatGPT was used to create syntax for flask functions and AJAX request as well as the outline for the machine learning function

## Setup

For the setup of this application i used pythonanywhere to set up a cloud server to run my website. It can be accessed through the url
https://jericao.pythonanywhere.com/

## Execution

### Added HTML

For this I had to add in an extra form to display similar songs once a random song is selected by the user.I also added in another AJAX request for this form to access my flask function.

```python

<form id="genre-form">
    <label for="genre">Choose a genre:</label>
    <select name="genre" id="genre">
        {% for genre in genres %}
            <option value="{{ genre[0] }}">{{ genre[0] }}</option>
        {% endfor %}
    </select>
    <button type="submit">Get Random Songs</button>
</form>

<div id="songs-list"></div>


    <h3>Similar Songs Based on Features:</h3>
    <div id="selected-song-info"></div>
    <div id="similar-songs-list"></div>

<script>
// Handle the genre form submission (AJAX for random songs)
    document.getElementById('genre-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const genre = document.getElementById('genre').value;

    // Send AJAX request to get random songs based on selected genre
    fetch('/get_random_songs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'genre=' + encodeURIComponent(genre)
    })
    .then(response => response.json())  // Convert the response into JSON
    .then(songs => {
        const songsList = document.getElementById('songs-list');
        songsList.innerHTML = ''; // Clear previous song list

        if (songs.length === 0) {
            songsList.innerHTML = '<p>No songs found for this genre.</p>';
        } else {
            songs.forEach(song => {
                const songElement = document.createElement('div');
                songElement.classList.add('song');
                src = "https://open.spotify.com/embed/track/" + song.track_id
                songElement.innerHTML = `
                    <div>
                        <strong>Track Name:</strong> ${song.track_name} <br>
                        <strong>Artist:</strong> ${song.artists} <br>
                        <strong>Album:</strong> ${song.album_name} <br>
                        <strong>Popularity:</strong> ${song.popularity} <br>
                        <strong>Duration:</strong> ${song.duration_ms} ms <br>
                        <iframe src=${src} width="300" height="80" frameBorder="0" allow="encrypted-media"></iframe>
                        <button onclick="selectSong('${song.track_name}', '${song.artists}', '${song.album_name}')">Select</button>
                    </div>
                `;
                songsList.appendChild(songElement);
            });
        }
    })
    .catch(error => console.error('Error fetching data:', error));
    });

// Function to handle when a user selects a song
function selectSong(track_name,artists,album_name) {
    // Display the selected song information
    const selectedSongInfo = document.getElementById('selected-song-info');
    selectedSongInfo.innerHTML = `
        <h4>Selected Song:</h4>
        <p><strong>Track Name:</strong> ${track_name}</p>
        <p><strong>Artist:</strong> ${artists}</p>
        <p><strong>Album:</strong> ${album_name}</p>
    `;

    // Send AJAX request to get similar songs based on the selected song
    fetch('/get_similar_songs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'song_name=' + encodeURIComponent(track_name)
    })
    .then(response => response.json())  // Convert the response into JSON
    .then(data => {
        const similarSongsList = document.getElementById('similar-songs-list');
        similarSongsList.innerHTML = ''; // Clear previous similar songs list

        if (data.similar_songs.length === 0) {
            similarSongsList.innerHTML = '<p>No similar songs found.</p>';
        } else {
            data.similar_songs.forEach(song => {
                const songElement = document.createElement('div');
                songElement.classList.add('song');
                src = "https://open.spotify.com/embed/track/" + song.track_id;
                songElement.innerHTML = `
                    <div>
                        <strong>Track Name:</strong> ${song.track_name} <br>
                        <iframe src=${src} width="300" height="80" frameBorder="0" allow="encrypted-media"></iframe>
                    </div>
                `;
                similarSongsList.appendChild(songElement);
            });
        }
    })
    .catch(error => console.error('Error fetching similar songs:', error));
}


    </script>
</body>

</html>
```

### Added Flask App Function

I also added in a function to my flask application to use my songPredictor functions.

```python
filename="dataset.csv"
csv_manager = Module9.FileManager(filename)
df = csv_manager.read_csv()

# Flask route to handle song selection
@app.route('/get_similar_songs', methods=['POST'])
def get_song_recommendations():

    selected_song = request.form['song_name']
    
    # Modify to only songs of the same genre
    genre_songs_df = songPredictor.get_songs_genre(selected_song, df)

    # Get similarity-based recommendations
    similar_songs = songPredictor.get_similar_songs(selected_song, genre_songs_df, top_n=3)
    similar_song_names = similar_songs.tolist()

    # Connect to the SQLite database
    conn = sqlite3.connect('music_genres.db')
    cursor = conn.cursor()

    # Create a list to hold the song details along with track_id
    song_details = []

    # Query the database to get track_id for each similar song
    for song_name in similar_song_names:
        cursor.execute("SELECT track_id FROM tracks WHERE track_name = ?", (song_name,))
        result = cursor.fetchone()

        if result:
            track_id = result[0]
            song_details.append({
                'track_name': song_name,
                'track_id': track_id
            })

    # Close the database connection
    conn.close()

    # Return the recommendations with track_id
    return jsonify({
        'similar_songs': song_details
    })
```
### Song Prediction Program

I also created some new functions that will filter out the dataframe I have by genres and then use maching learning techniques to return with the most similar songs depending on what song the suer picks.

```python
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

```
## Summary

For this module I created a songPrediction.py program so that I could reccomend songs to a user based on how similar the attributes of the song are. I then created a new form that will displays these songs and the option for the customer to select the songs they want to get reccomendations from from my random song form generator.I also added in the ability for the user to play a preview of each song displayed.

## Example Output

![Website 1](<MachineLearning1.png>)
![Website 1](<MachineLearning2.png>)

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

# Module 9

Module9: Create a 3-tier web application that allows users to interact with the data

ChatGPT was used to create syntax for flask functions and AJAX/JavaScript scripts


## Setup

For the setup of this application that flask app.py requires that the files are set up like this.

```plaintext
Website/
├── app.py
├── music_genres.db
├── templates/
│   ├── index.html
├── static/
│   ├── style.css
    ├── Graphs/
│       ├── Acousticness of Genres.png
│       ├── Top Accousticness of Genres.png
│       ├── Danceability of Genres.png
│       ├── Top Danceablitiy of Genres.png
│       ├── Duration of Genres.png
│       ├── Top Duration of Genres.png
│       ├── Energy of Genres.png
│       ├── Top Energy of Genres.png
│       ├── Liveness of Genres.png
│       ├── Top Liveness of Genres.png
│       ├── Popularity of Genres.png
│       ├── Top Popularity of Genres.png
│       ├── Speechiness of Genres.png
│       ├── Top Speechiness of Genres.png
│       ├── Tempo of Genres.png
│       ├── Top Tempo of Genres.png
│       ├── Valence of Genres.png
│       ├── Top Valence of Genres.png
│       ├── Ratio of Explicit Songs.png
│       ├── Ratio of Major to Minor Songs.png
│       ├── Ratio of the Time Signature of Songs.png

```

After the files are setup run the app with the python app.py command

Then access the website on the http://localhost:8000/ url

## Execution

### HTML

For this I had my HTML setup like this

```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top Spotify Songs</title>
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>
    <h1>Top Spotify Songs</h1>
    <h2>Welcome! Here you can find data on a range of over 100K songs in over 125 different genres.</h2>

    <form id='pie-chart-form' method="POST">
        <label for="dropdown">Select a Pie Chart:</label>
        <select name="dropdown" id="dropdown">
            <option value="Ratio of Explicit Songs" {% if selected_image=='Ratio of Explicit Songs.png' %}selected{%
                endif %}>Ratio of Explicit Songs</option>
            <option value="Ratio of Major/Minor Songs" {% if selected_image=='Ratio of Major to Minor Songs.png'
                %}selected{% endif %}>Ratio of Major/Minor Songs</option>
            <option value="Ratio of The Time Signatures of Songs" {% if
                selected_image=='Ratio of the Time Signature of Songs.png' %}selected{% endif %}>Ratio of The Time Signatures of Songs</option>
        </select>
        <button type="submit" id="SubmitButton">Submit</button>
    </form>

    {% if selected_image %}
    <img src="{{ url_for('static', filename=selected_image) }}" alt="{{ selected_image }}" id="PieImage">
    {% endif %}




    <h2>What attribute do you want to look at?</h2>
    <div id="bar-graphs-container">

    <div id="image-container">
        <img id="image-display" src="static/Graphs/Popularity of Genres.png" alt="Default Image" width="800">
    </div>


<div id="button-containers">
    <button onclick="changeImage('/static/Graphs/Popularity of Genres.png')">Popularity of Genres</button>
    <button onclick="changeImage('/static/Graphs/Duration of Genres.png')">Duration of Genres</button>
    <button onclick="changeImage('/static/Graphs/Tempo of Genres.png')">Tempo of Genres</button>
    <button onclick="changeImage('/static/Graphs/Valence of Genres.png')">Valence of Genres</button>
    <button onclick="changeImage('/static/Graphs/Liveness of Genres.png')">Liveness of Genres</button>
    <button onclick="changeImage('/static/Graphs/Acousticness of Genres.png')">Acousticness of Genres</button>
    <button onclick="changeImage('/static/Graphs/Speechiness of Genres.png')">Speechiness of Genres</button>
    <button onclick="changeImage('/static/Graphs/Energy of Genres.png')">Energy of Genres</button>
    <button onclick="changeImage('/static/Graphs/Danceability of Genres.png')">Danceability of Genres</button>
</div>
<button onclick="toggleGraph()" id="toggle-container-button">Switch to Top 10</button>

</div>

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
    <script>
        
        let isTop10 = false;  // Track whether we are in "Top 10" mode


        // Change the image source when a button is clicked
        function changeImage(imagePath) {
            const imageDisplay = document.getElementById('image-display');
            imageDisplay.src = imagePath;  // Change the image source
            currentGraph = imagePath;  // Update the current graph to the new one
        }

        function toggleGraph(){
            isTop10 = !isTop10;

            const button = document.getElementById('toggle-container-button');
            if(isTop10){
                button.textContent = "Switch to Regular Graph";
                if(currentGraph === "/static/Graphs/Popularity of Genres.png"){
                    document.getElementById('image-display').src = "/static/Graphs/Top Popularity of Genres.png";
                }
                else if(currentGraph === '/static/Graphs/Duration of Genres.png' ){
                    document.getElementById('image-display').src = '/static/Graphs/Top Duration of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Tempo of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Top Tempo of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Valence of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Top Valence of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Liveness of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Top Liveness of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Acousticness of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Top Acousticness of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Speechiness of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Top Speechiness of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Energy of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Top Energy of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Danceability of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Top Danceability of Genres.png';
                }
            }
            else{
                button.textContent = "Switch to Top 10"; 
                if(currentGraph === "/static/Graphs/Popularity of Genres.png"){
                document.getElementById('image-display').src = "/static/Graphs/Popularity of Genres.png";
                }
                else if(currentGraph === '/static/Graphs/Duration of Genres.png' ){
                    document.getElementById('image-display').src = '/static/Graphs/Duration of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Tempo of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Tempo of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Valence of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Valence of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Liveness of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Liveness of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Acousticness of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Acousticness of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Speechiness of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Speechiness of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Energy of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Energy of Genres.png';
                }
                else if(currentGraph === '/static/Graphs/Danceability of Genres.png'){
                    document.getElementById('image-display').src = '/static/Graphs/Danceability of Genres.png';
                }

            }
        }

    // Handle the pie chart form submission (AJAX)
    document.getElementById('pie-chart-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission

    const selectedPieChart = document.getElementById('dropdown').value;

    // Send AJAX request for the selected pie chart
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'dropdown=' + encodeURIComponent(selectedPieChart)
    })
    .then(response => response.text())
    .then(data => {
        // Update the pie chart image dynamically
        const pieImage = document.getElementById('PieImage');
        pieImage.src = data;
    })
    .catch(error => console.error('Error updating pie chart:', error));
});


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
                songElement.innerHTML = `
                    <strong>Track Name:</strong> ${song.track_name} <br>
                    <strong>Artist:</strong> ${song.artists} <br>
                    <strong>Album:</strong> ${song.album_name} <br>
                    <strong>Popularity:</strong> ${song.popularity} <br>
                    <strong>Duration:</strong> ${song.duration_ms} ms <br>
                `;
                songsList.appendChild(songElement);
            });
        }
    })
    .catch(error => console.error('Error fetching data:', error));
    });

    </script>
</body>

</html>
```

### Flask App

```python
from flask import Flask, render_template, request, jsonify
import sqlite3
from waitress import serve

# Create a Flask application instance
app = Flask(__name__)

@app.route('/', methods=['POST'])
def update_pie_chart():
    selected_pie_chart = request.form.get('dropdown')

    # Map the selected pie chart to an image path (this is just an example)
    image_paths = {
        "Ratio of Explicit Songs": "/static/Graphs/Ratio%20of%20Explicit%20Songs.png",
        "Ratio of Major/Minor Songs": "/static/Graphs/Ratio%20of%20Major%20to%20Minor%20Songs.png",
        "Ratio of The Time Signatures of Songs": "/static/Graphs/Ratio%20of%20the%20Time%20Signature%20of%20Songs.png",
    }

    image_path = image_paths.get(selected_pie_chart, "/static/Graphs/default-image.png")

    return image_path

# Function to get 10 random songs based on genre
def get_random_songs(genre):
    conn = sqlite3.connect('music_genres.db')
    cursor = conn.cursor()
    
    # Query to get 5 random songs from the selected genre
    query = """
    SELECT * FROM tracks
    WHERE track_genre = ?
    ORDER BY RANDOM() 
    LIMIT 5;
    """
    
    cursor.execute(query, (genre,))
    songs = cursor.fetchall()
    
    conn.close()
    
    return songs

import random

@app.route('/', methods=['GET', 'POST'])
def home():
    selected_image = None  # Default to None to make sure we don't pass an undefined value

    if request.method == 'POST':
        if 'dropdown' in request.form:
            selected_graph = request.form.get('dropdown')
            graph_filename_map = {
                'Ratio of Explicit Songs': 'Graphs/Ratio of Explicit Songs.png',
                'Ratio of Major/Minor Songs': 'Graphs/Ratio of Major to Minor Songs.png',
                'Ratio of The Time Signatures of Songs': 'Graphs/Ratio of the Time Signature of Songs.png'
            }
            selected_image = graph_filename_map.get(selected_graph)

        elif 'genre' in request.form:
            genre = request.form['genre']
            songs = get_random_songs(genre)

            songs_data = []
            for song in songs:
                song_info = {
                    'track_name': song[4],
                    'artists': song[2],
                    'album_name': song[3],
                    'popularity': song[5],
                    'duration_ms': song[6],
                }
                songs_data.append(song_info)

            return jsonify(songs_data)

    # Default image if no selection is made
    if not selected_image:
        selected_image = 'Graphs/Ratio of Explicit Songs.png'

    # Get genres from the database
    conn = sqlite3.connect('music_genres.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT track_genre FROM tracks WHERE track_genre != 'track_genre'")
    genres = cursor.fetchall()
    conn.close()

    # Pie chart options
    options = [
        'Ratio of Explicit Songs',
        'Ratio of Major/Minor Songs',
        'Ratio of The Time Signatures of Songs'
    ]

    return render_template('index.html', genres=genres, options=options, selected_image=selected_image)

@app.route('/get_random_songs', methods=['POST'])
def get_random_songs_ajax():
    genre = request.form['genre']
    songs = get_random_songs(genre)
    
    # Convert songs to a list of dictionaries for easier handling on the front-end
    songs_data = []
    for song in songs:
        song_info = {
            'track_name': song[4],
            'artists': song[2],
            'album_name': song[3],
            'popularity': song[5],
            'duration_ms': song[6],
        }
        songs_data.append(song_info)
    
    return jsonify(songs_data)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
```

## Summary

For this program I create a 3-tiered web application by using html, css, javascript, flask, and an SQL database. I decided to add the ability for the user to select different pie charts or bar graphs to display. I also made it so the user can look at 5 different songs from a selected genre. This feature uses the SQL database I created to acheive this.

## Example Output

![Website 1](<SpotifyTopTracksWebsite1.png>)
![Website 1](<SpotifyTopTracksWebsite2.png>)

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
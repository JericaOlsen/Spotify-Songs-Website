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

from flask import Flask, render_template, request, jsonify
import sqlite3
from waitress import serve
import songPredictor
import Module9

# Create a Flask application instance
app = Flask(__name__)


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

# Function to get 5 random songs based on genre
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
            'track_id': song[1]
        }
        songs_data.append(song_info)
    
    return jsonify(songs_data)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)

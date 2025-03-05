import pandas as pd

def load_data():
    # Data initialization
    data = pd.read_csv('./data/raw/spotify_songs.csv')

    # Renaming columns
    data.columns = ['title', 
                'artist', 
                'genre', 
                'year', 
                'bpm', 
                'energy', 
                'danceability', 
                'loudness', 
                'liveness', 
                'valence', 
                'duration', 
                'acousticness', 
                'speechiness', 
                'popularity']
    
    return data
import os
import pandas as pd


def load_data():
    """
    Dynamically locate and load the Spotify songs CSV file from the root 'data/raw' folder.
    Returns:
        pd.DataFrame: The loaded data_loader with renamed columns.
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    file_path = os.path.join(project_root, 'data', 'raw', 'spotify_songs.csv')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}. Please verify the file location.")

    data = pd.read_csv(file_path)

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

import os
import pandas as pd
from functools import cache


#function to preprocess data
def preprocess_data(input_filepath: str, output_filepath: str):
    """
    Load raw data, preprocess it, and save it in a binary format (Feather) for fast loading.
    
    Parameters:
    input_filepath (str): Path to the raw data file.
    output_filepath (str): Path where the processed data will be saved.
    """
    # Load raw data
    df = pd.read_csv(input_filepath)

    # Example preprocessing steps
    df = df.dropna()  # Remove missing values
    df = df.drop_duplicates()  # Remove duplicate rows

    # Save processed data in Feather format
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    df.to_feather(output_filepath)
    print(f"Processed data saved to {output_filepath}")

    return df  


@cache
def load_data():
    """
    Dynamically locate and load the Spotify songs CSV file from the root 'data/raw' folder.
    Returns:
        pd.DataFrame: The loaded data_loader with renamed columns.
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    file_path = os.path.join(project_root, 'data', 'raw', 'spotify_songs.csv')
    processed_file = os.path.join(project_root, 'data', 'processed', 'processed_data.feather')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}. Please verify the file location.")

    preprocess_data(file_path, processed_file)

    data = pd.read_feather(processed_file)

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

    # This was generated using Chatgpt to map each subgenre to its parent genre
    genre_mapping = {
        # Pop
        'dance pop': 'Pop', 'pop': 'Pop', 'canadian pop': 'Pop', 'hip pop': 'Pop',
        'barbadian pop': 'Pop', 'australian pop': 'Pop', 'indie pop': 'Pop', 
        'art pop': 'Pop', 'colombian pop': 'Pop', 'acoustic pop': 'Pop', 
        'candy pop': 'Pop', 'french indie pop': 'Pop', 'danish pop': 'Pop',

        # Hip-Hop/Rap
        'detroit hip hop': 'Hip-Hop/Rap', 'atl hip hop': 'Hip-Hop/Rap', 'chicago rap': 'Hip-Hop/Rap',
        'canadian hip hop': 'Hip-Hop/Rap', 'hip hop': 'Hip-Hop/Rap', 'electronic trap': 'Hip-Hop/Rap',

        # Rock & Alternative
        'neo mellow': 'Rock/Alternative', 'british soul': 'Rock/Alternative', 
        'baroque pop': 'Rock/Alternative', 'celtic rock': 'Rock/Alternative', 
        'folk-pop': 'Rock/Alternative', 'alaska indie': 'Rock/Alternative', 
        'alternative r&b': 'Rock/Alternative', 'irish singer-songwriter': 'Rock/Alternative',
        'permanent wave': 'Rock/Alternative',

        # Electronic/Dance (EDM)
        'big room': 'Electronic/Dance', 'electro': 'Electronic/Dance', 
        'complextro': 'Electronic/Dance', 'house': 'Electronic/Dance', 
        'electropop': 'Electronic/Dance', 'australian dance': 'Electronic/Dance', 
        'belgian edm': 'Electronic/Dance', 'tropical house': 'Electronic/Dance',
        'electro house': 'Electronic/Dance', 'edm': 'Electronic/Dance', 
        'brostep': 'Electronic/Dance', 'downtempo': 'Electronic/Dance',

        # R&B & Soul
        'contemporary r&b': 'R&B/Soul', 'alternative r&b': 'R&B/Soul', 
        'canadian contemporary r&b': 'R&B/Soul', 'british soul': 'R&B/Soul',

        # Latin & Global
        'latin': 'Latin/Global', 'canadian latin': 'Latin/Global', 'moroccan pop': 'Latin/Global',

        # Country & Folk
        'contemporary country': 'Country/Folk', 'folk-pop': 'Country/Folk',

        # Other / Miscellaneous
        'metropopolis': 'Other', 'hollywood': 'Other', 'escape room': 'Other'
    }

    data['genre'] = data['genre'].map(genre_mapping).fillna('Other')

    return data

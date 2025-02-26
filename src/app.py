from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd


# Intialization
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Data initialization
data = pd.read_csv('./data/raw/spotify_songs.csv')

# Renaming columns
data.columns = ['title', 
              'artist', 
              'the genre of the track', 
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

# Extract top 6 artists by year sorted by popularity
top_artists_by_year = (
    data.groupby(['year', 'artist'])['popularity']
    .sum()
    .reset_index()
    .groupby('year')
    .apply(lambda x: x.nlargest(6, 'popularity'))
    .reset_index(drop=True)
)

# Create a list of HTML elements to display the top 6 artists
years = sorted(data['year'].unique())
default_year = 2010

# Top artists chart
artist_elements = html.Div(id='artist-list')

# Year Selector for Top Artists
year_dropdown = html.Div([
    html.H3("Year"),
    dcc.Slider(
        min=years[0], 
        max=years[-1], 
        step=1, 
        value=default_year, 
        marks={str(year): str(year) for year in years},
        id='year-dropdown',
        included=False
    )
])

@callback(
    Output('artist-list', 'children'),
    Input('year-dropdown', 'value')
)
def update_artist_list(selected_year):
    filtered_data = top_artists_by_year[top_artists_by_year['year'] == selected_year]
    
    return html.Div([
        html.H3(f"Top Artists in {selected_year}"),
        dbc.Row([
            dbc.Col([
                html.Div(
                        f"{rank}. {artist}"
                    ) for rank, artist in enumerate(filtered_data['artist'][:3], start=1)
                ], width=6),
            dbc.Col([
                html.Div(
                    f"{rank}. {artist}"
                    ) for rank, artist in enumerate(filtered_data['artist'][3:], start=4)
                ], width=6)
        ], style={'fontSize': '1.5rem'})
    ])

# Components
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Spotipy"),
            html.H3("Filters"),
            year_dropdown,
            html.H3("Widget2"),
            html.H3("Widget3"),
            html.H3("Widget4")
        ], width=4, style={'borderRight': 'solid 3px'}),
        dbc.Col([
            artist_elements,
            html.H3("Chart2"),
            html.H3("Chart3"),
            html.H3("Chart4")
        ], width=8)
    ], style={'marginTop': '10vh', 'border': 'solid 3px'})
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

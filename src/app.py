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

# Create a list of HTML elements to display the top 6 artists
years = sorted(data['year'].unique())
default_year = 2010

# Components

# Top artists chart
artist_elements = html.Div(id='artist-list')

# Selectors

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

# Song Duration Selector
song_duration = html.Div([
    html.H3("Song Duration (s)"),
    dcc.Input(id="duration_min", type="number", placeholder="Min Duration", debounce=True, value=0),
    dcc.Input(id="duration_max", type="number", placeholder="Max Duration", debounce=True, value=300)
])

# Callbacks

@callback(
    Output('artist-list', 'children'),
    Input('year-dropdown', 'value'),
    Input('duration_min', 'value'),
    Input('duration_max', 'value')
)
def update_artist_list(selected_year, selected_duration_min, selected_duration_max):
    # Apply filters on data first
    filtered_data = data[
        (data['year'] == selected_year) &
        (data['duration'] >= selected_duration_min) &
        (data['duration'] <= selected_duration_max)
    ].sort_values(by='popularity', ascending=False).head(6)
    
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

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Spotipy"),
            html.H3("Filters"),
            year_dropdown,
            song_duration,
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

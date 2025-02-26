from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import altair as alt
import pandas as pd

# Set Altair theme to dark
alt.theme.enable('carbong90')

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


# Components -----------------
# Top artists chart
artist_elements = html.Div(id='artist-list')

# Selectors ------------------
# Year Selector for Top Artists

years = sorted(data['year'].unique())
default_year = 2010

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

# Callbacks ----------
# Artist List Callback 
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

# Scatterplot Callback
@callback(
    Output('scatterplot', 'spec'),
    Input('year-dropdown', 'value'),
    Input('duration_min', 'value'),
    Input('duration_max', 'value')
)
def update_scatterplot(selected_year, selected_duration_min, selected_duration_max):
    # Apply filters on data
    filtered_data = data[
        (data['year'] == selected_year) &
        (data['duration'] >= selected_duration_min) &
        (data['duration'] <= selected_duration_max)
    ]

    return (
        alt.Chart(
            filtered_data, width='container'
        ).mark_point(filled=True, size=100).encode(
            x=alt.X('popularity', title='Popularity', scale=alt.Scale(zero=False)),
            y=alt.Y('danceability', title='Danceability', scale=alt.Scale(zero=False)),
            tooltip=[
                alt.Tooltip('title', title='Song Title'), 
                alt.Tooltip('artist', title='Artist'), 
                alt.Tooltip('popularity', title='Popularity'), 
                alt.Tooltip('danceability', title='Danceability'),
                alt.Tooltip('duration', title='Duration (Seconds)')
            ]
        ).properties(
            title=f'Danceability vs. Popularity in {selected_year}'
        ).configure_axis(
            labelFontSize=16,
            titleFontSize=20
        ).configure_title(
            fontSize=20
        ).to_dict()
    )

    
# App --------------
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
            dvc.Vega(id='scatterplot', spec={}, style={'width': '100%', 'marginTop': '1vh'}),
            artist_elements,
            html.H3("Chart3"),
            html.H3("Chart4")
        ], width=8)
    ], style={'marginTop': '10vh', 'border': 'solid 3px'})
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

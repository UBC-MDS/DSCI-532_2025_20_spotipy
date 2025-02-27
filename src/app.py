from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import altair as alt
import pandas as pd

# Set Altair theme to dark
alt.theme.enable('carbong90')

# Intialization
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

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


# Components -----------------
# Top artists chart
artist_elements = html.Div(id='artist_list')

# Scatterplot
scatterplot = dvc.Vega(id='scatterplot', spec={}, style={'width': '100%', 'marginTop': '1vh'})

# Selectors ------------------
# Year Selector for Top Artists

years = sorted(data['year'].unique())
default_year = 2010

year_dropdown = html.Div([
    html.H4("Year"),
    dcc.Slider(
        min=years[0], 
        max=years[-1], 
        step=1, 
        value=default_year, 
        marks={str(year): str(year) for year in years},
        id='year_dropdown',
        included=False
    )
], style={'marginBottom': '2.5vh'})

# Song Duration Selector
song_duration = html.Div([
    html.H4("Song Duration (s)"),
    dcc.Input(
        id="duration_min", 
        type="number", 
        placeholder="Min Duration", 
        debounce=True , 
        style={
            'backgroundColor': '#2a2a2a', 'color': 'white', 'border': 'solid white 1px', 'borderRadius': '3px', 'marginRight': '5px', 'padding': '3px', 'paddingLeft': '10px'
            }
        ),
    dcc.Input(
        id="duration_max", 
        type="number", 
        placeholder="Max Duration", 
        debounce=True, 
        style={'backgroundColor': '#2a2a2a', 'color': 'white', 'border': 'solid white 1px', 'borderRadius': '3px', 'padding': '3px', 'paddingLeft': '10px'
               }
        )
], style={'marginBottom': '2.5vh'})

# Beats Per Minute Selector
bpm_selector = html.Div([
    html.H4("Beats Per Minute"),
    dcc.RangeSlider(min=40, max=210, step=20, value=[60,140], id='bpm_range')
], style={'marginBottom': '2.5vh'})

# Genre Selector
genres = data['genre'].unique()

genre_selector = html.Div([
    html.H4("Genre"),
    dcc.Dropdown(
        id='genre_dropdown',
        options=[{"label" : genre, "value": genre} for genre in genres],
        multi=True,
        placeholder="Search and select genres...",
        searchable=True,
        style={'backgroundColor': '#2a2a2a'}
    )
], style={'marginBottom': '2.5vh'})

# Callbacks ----------------
# Artist List Callback 
@callback(
    Output('artist_list', 'children'),
    Input('year_dropdown', 'value'),
    Input('duration_min', 'value'),
    Input('duration_max', 'value'),
    Input('bpm_range', 'value'),
    Input('genre_dropdown', 'value')
)
def update_artist_list(selected_year, selected_duration_min, selected_duration_max, selected_bpm_range, selected_genres):
    filtered_data = data[
        (data['year'] == selected_year) &
        (data['duration'] >= (selected_duration_min if selected_duration_min is not None else 0)) &
        (data['duration'] <= (selected_duration_max if selected_duration_max is not None else data['duration'].max())) &
        (data['bpm'] >= selected_bpm_range[0]) &
        (data['bpm'] <= selected_bpm_range[1])
    ]
    
    if selected_genres:
        filtered_data = filtered_data[filtered_data['genre'].isin(selected_genres)]
    
    filtered_data = filtered_data.sort_values(by='popularity', ascending=False)['artist'].unique()[:6]
    
    return html.Div([
        html.H3(f"Top Artists in {selected_year}"),
        dbc.Row([
            dbc.Col([
                html.Div(
                        f"{rank}. {artist}"
                    ) for rank, artist in enumerate(filtered_data[:3], start=1)
                ], width=6),
            dbc.Col([
                html.Div(
                    f"{rank}. {artist}"
                    ) for rank, artist in enumerate(filtered_data[3:], start=4)
                ], width=6)
        ], style={'fontSize': '1.5rem'})
    ])

# Scatterplot Callback
@callback(
    Output('scatterplot', 'spec'),
    Input('year_dropdown', 'value'),
    Input('duration_min', 'value'),
    Input('duration_max', 'value'),
    Input('bpm_range', 'value'),
    Input('genre_dropdown', 'value')
)
def update_scatterplot(selected_year, selected_duration_min, selected_duration_max, selected_bpm_range, selected_genres):
    filtered_data = data[
        (data['year'] == selected_year) &
        (data['duration'] >= (selected_duration_min if selected_duration_min is not None else 0)) &
        (data['duration'] <= (selected_duration_max if selected_duration_max is not None else data['duration'].max())) &
        (data['bpm'] >= selected_bpm_range[0]) &
        (data['bpm'] <= selected_bpm_range[1])
    ]

    if selected_genres:
        filtered_data = filtered_data[filtered_data['genre'].isin(selected_genres)]

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
                alt.Tooltip('duration', title='Duration (Seconds)'),
                alt.Tooltip('bpm', title='BPM')
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
            html.H1("Spotipy", style={'borderBottom': 'solid #535353 3px', 'paddingBottom': '1rem', 'color': '#1ED760'}),
            html.H3("Filters", style={'marginBottom': '1.5vh'}),
            year_dropdown,
            bpm_selector,
            genre_selector,
            song_duration
        ], width=4, style={'borderRight': 'solid #535353 3px'}),
        dbc.Col([
            scatterplot,
            artist_elements
        ], width=8)
    ], style={'marginTop': '10vh'})
])

# Run the app
if __name__ == '__main__':
    app.run(debug=False)

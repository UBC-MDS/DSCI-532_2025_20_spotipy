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
artist_elements = html.Div(id='artist_list')

# Scatterplot
scatterplot = dvc.Vega(id='scatterplot', spec={}, style={'width': '100%', 'marginTop': '1vh'})

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
        id='year_dropdown',
        included=False
    )
], style={'marginBottom': '2.5vh'})

# Song Duration Selector
song_duration = html.Div([
    html.H3("Song Duration (s)"),
    dcc.Input(id="duration_min", type="number", placeholder="Min Duration", debounce=True, value=0),
    dcc.Input(id="duration_max", type="number", placeholder="Max Duration", debounce=True, value=300)
], style={'marginBottom': '2.5vh'})

# Beats Per Minute Selector
bpm_selector = html.Div([
    html.H3("Beats Per Minute"),
    dcc.RangeSlider(min=40, max=210, step=20, value=[60,140], id='bpm_range')
], style={'marginBottom': '2.5vh'})

# Callbacks ----------------
# Artist List Callback 
@callback(
    Output('artist_list', 'children'),
    Input('year_dropdown', 'value'),
    Input('duration_min', 'value'),
    Input('duration_max', 'value'),
    Input('bpm_range', 'value')
)
def update_artist_list(selected_year, selected_duration_min, selected_duration_max, selected_bpm_range):
    filtered_data = data[
        (data['year'] == selected_year) &
        (data['duration'] >= selected_duration_min) &
        (data['duration'] <= selected_duration_max) &
        (data['bpm'] >= selected_bpm_range[0]) &
        (data['bpm'] <= selected_bpm_range[1])
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
    Input('year_dropdown', 'value'),
    Input('duration_min', 'value'),
    Input('duration_max', 'value'),
    Input('bpm_range', 'value')
)
def update_scatterplot(selected_year, selected_duration_min, selected_duration_max, selected_bpm_range):
    filtered_data = data[
        (data['year'] == selected_year) &
        (data['duration'] >= selected_duration_min) &
        (data['duration'] <= selected_duration_max) &
        (data['bpm'] >= selected_bpm_range[0]) &
        (data['bpm'] <= selected_bpm_range[1])
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
            html.H3("Filters", style={'marginBottom': '2.5vh'}),
            year_dropdown,
            song_duration,
            bpm_selector,
            html.H3("Widget4")
        ], width=4, style={'borderRight': 'solid #535353 3px'}),
        dbc.Col([
            scatterplot,
            artist_elements
        ], width=8)
    ], style={'marginTop': '10vh'})
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

from dash import html, dcc
from data.data_loader import load_data

data = load_data()

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
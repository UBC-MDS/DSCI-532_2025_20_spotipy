from dash import html
import dash_bootstrap_components as dbc

footer = dbc.Container(
    [
        html.P("Spotipy Dashboard - An interactive visualization tool for exploring Spotify song data.",
               style={'textAlign': 'center'}),
        html.P("Created by: Yibin, Brian, Sam, Siddarth", 
               style={'textAlign': 'center'}),
        html.A("GitHub Repository", href="https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy", target="_blank", 
               style={'display': 'block', 'textAlign': 'center', 'color': '#1ED760', 'textDecoration': 'none'}),
        html.P("Last Updated: March 1, 2025", style={'textAlign': 'center'}),
    ],
    fluid=True,
    style={
        'padding': '1rem', 
        'borderTop': 'solid #535353 3px',
        'color': 'gray',
        'marginTop': '15vh'
        }
)

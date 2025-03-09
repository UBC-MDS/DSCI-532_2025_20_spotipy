from dash import Dash, html
import dash_bootstrap_components as dbc
import altair as alt

# Import our selectors
from components.selectors.year_dropdown_selector import year_dropdown
from components.selectors.bpm_selector import bpm_selector
from components.selectors.genre_selector import genre_selector
from components.selectors.song_duration_selector import song_duration
from components.selectors.axis_selector import y_axis_selector

# Import our UI components
from components.artist_list import artist_elements
from components.scatterplot import scatterplot
from components.footer import footer

# Import our callbacks
from callbacks.artist_callback import *  
from callbacks.scatterplot_callback import * 

# Set Altair theme to dark
alt.theme.enable('carbong90')

# Intialization
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], title='Spotipy')
server = app.server

# App Layout with Footer
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(
                "Spotipy", 
                style={
                    'borderBottom': 'solid #535353 3px', 
                    'paddingBottom': '1rem', 
                    'color': '#1ED760',
                    'textAlign': 'center'
                    }),
            dbc.Card(
                year_dropdown, body=True, style={'marginBottom': '1.5vh'}
            ),
            dbc.Card(bpm_selector, body = True, style={'marginBottom': '1.5vh'}),
            dbc.Card(genre_selector, body = True, style={'marginBottom': '1.5vh'}),
            dbc.Card(y_axis_selector, body = True, style={'marginBottom': '1.5vh'}),
            dbc.Card(song_duration, body = True, style={'marginBottom': '1.5vh'})
        ], width=4, style={'borderRight': 'solid #535353 3px'}),
        dbc.Col([
            dbc.Card(scatterplot, body=True, style={'marginBottom': '1.5vh'}),
            dbc.Card(artist_elements, body=True, style={'marginBottom': '1.5vh'})
        ], width=8)
    ], style={'marginTop': '10vh'}),
    footer
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

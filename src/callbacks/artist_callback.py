from dash import callback, Output, Input, html
import dash_bootstrap_components as dbc
from data.data_loader import load_data

data = load_data()

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
    
    filtered_data = filtered_data.sort_values(by='popularity', ascending=False)[['artist', 'popularity']].drop_duplicates('artist')[:6]
    
    def create_artist_row(artist, popularity, rank):
        return dbc.Row([
            dbc.Col(
                f"{artist}", 
                width=8,
                style={'textAlign': 'left'}
            ),
            dbc.Col(
                f"{popularity}%", 
                width=4,
                style={'textAlign': 'right'}
            )
        ], 
        style={
            'backgroundColor': get_artist_color(rank),
            'padding': '8px',
            'marginBottom': '8px',
            'marginRight': '1rem',
            'borderRadius': '4px',
            'color': 'white',
            'fontSize': '1.5rem',
            'fontWeight': 'bold'
        })
    
    def get_artist_color(rank):
        return f'hsl(145, 75%, {max(5, 40 - (rank - 1) * 4)}%)'

    return html.Div([
        html.H4(f"Top Artists in {selected_year}", style={'textAlign': 'left', 'marginBottom': '1rem'}),
        dbc.Row([
            dbc.Col([
                create_artist_row(artist, popularity, rank) for rank, (artist, popularity) in enumerate(
                    zip(filtered_data['artist'][:3], filtered_data['popularity'][:3]), 
                    start=1
                )
            ], width=6),
            dbc.Col([
                create_artist_row(artist, popularity, rank) for rank, (artist, popularity) in enumerate(
                    zip(filtered_data['artist'][3:], filtered_data['popularity'][3:]), 
                    start=4
                )
            ], width=6)
        ], style={'margin': '0.125rem'})
    ])

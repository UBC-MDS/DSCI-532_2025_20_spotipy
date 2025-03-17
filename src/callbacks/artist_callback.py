from dash import callback, Output, Input, html
import dash_bootstrap_components as dbc
from data_loader.data_loader import load_data

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
    
    # Deal with multiple songs by same artist by averaging the popularity
    filtered_data = (filtered_data.groupby('artist')['popularity']
                    .agg(['mean', 'count'])
                    .reset_index()
                    .sort_values(by='mean', ascending=False)
                    .head(6)
                    .rename(columns={'mean': 'popularity'}))
    
    def create_artist_row(artist, popularity, rank):
        return dbc.Row([
            dbc.Col(
                f"{artist}", 
                width=8,
                style={'textAlign': 'left'}
            ),
            dbc.Col(
                f"{popularity:.0f}%",
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
        return f'hsl(145, 75%, {max(5, 30 - (rank - 1) * 4)}%)'

    return html.Div([
        html.H4([
            "Most ",
            html.Span(
                "Popular",
                id="popularity-tooltip",
                style={
                    "textDecoration": "underline",
                    "cursor": "help",
                    "textUnderlineOffset": "5px"
                }
            ),
            f" Artists in {selected_year}"
        ], style={'textAlign': 'left', 'marginBottom': '1rem'}),
        dbc.Tooltip(
            "Popularity is calculated as the average popularity score across all songs by an artist in the selected filters.",
            target="popularity-tooltip",
            placement="right"
        ),
        dbc.Row([
            dbc.Col([
                create_artist_row(artist, popularity, rank) for rank, (artist, popularity) in enumerate(
                    zip(filtered_data['artist'][:3], filtered_data['popularity'][:3]), 
                    start=1
                )
            ], width=6, style={'paddingRight': '0.5rem'}),
            dbc.Col([
                create_artist_row(artist, popularity, rank) for rank, (artist, popularity) in enumerate(
                    zip(filtered_data['artist'][3:], filtered_data['popularity'][3:]), 
                    start=4
                )
            ], width=6, style={'paddingLeft': '0.5rem'})
        ], style={'margin': '0', 'width': '100%'})
    ], style={'width': '100%', 'paddingRight': '1rem'})

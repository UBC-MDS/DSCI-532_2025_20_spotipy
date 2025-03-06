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
    
    filtered_data = filtered_data.sort_values(by='popularity', ascending=False)['artist'].unique()[:6]
    
    return html.Div([
        html.H4(f"Top Artists in {selected_year}"),
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
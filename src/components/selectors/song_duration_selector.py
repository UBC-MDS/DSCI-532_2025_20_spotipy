from dash import html, dcc

# Song Duration Selector
song_duration = html.Div([
    html.H4("Song Duration (s)"),
    html.Div([
        dcc.Input(
            id="duration_min", 
            type="number", 
            placeholder="Min Duration", 
            debounce=True, 
            min=0,
            style={
                'backgroundColor': '#2a2a2a', 
                'color': 'white', 
                'border': 'solid white 1px', 
                'borderRadius': '3px', 
                'marginRight': '10px',
                'padding': '3px', 
                'paddingLeft': '10px',
                'width': '45%'
            }
        ),
        dcc.Input(
            id="duration_max", 
            type="number", 
            placeholder="Max Duration", 
            debounce=True, 
            min=0,
            style={
                'backgroundColor': '#2a2a2a',
                'color': 'white', 
                'border': 'solid white 1px', 
                'borderRadius': '3px', 
                'padding': '3px', 
                'paddingLeft': '10px',
                'width': '45%'
            }
        )
    ], style={'display': 'flex', 'flexDirection': 'row'})
], style={'marginBottom': '2.5vh'})
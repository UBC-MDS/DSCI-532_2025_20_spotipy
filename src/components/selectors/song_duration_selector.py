from dash import html, dcc

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
from dash import html, dcc
from data.data_loader import load_data

data = load_data()

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
    
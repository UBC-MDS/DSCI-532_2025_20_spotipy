from dash import html, dcc
from data_loader.data_loader import load_data

# Load dataset
data = load_data()

# Create Y-axis Selector
columns_for_selection = [col for col in data.columns if
                         col not in ['title', 'artist', 'genre', 'year', 'popularity']]  # Exclude non-numeric or irrelevant columns
default_y_axis = 'danceability'  # Default Y-axis column

y_axis_selector = html.Div([
    html.H4("Attribute"),
    dcc.Dropdown(
        id='y_axis_selector',
        options=[{'label': col.capitalize(), 'value': col} for col in columns_for_selection],
        value=default_y_axis,
        placeholder="Select a column for Y-axis"
    )
], style={'marginBottom': '2.5vh'})

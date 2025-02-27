from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc


# Intialization
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Components

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Spotipy"),
            html.H1("Filters"),
            html.H2("Widget1"),
            html.H2("Widget2"),
            html.H2("Widget3"),
            html.H2("Widget4")
        ], width=4),
        dbc.Col([
            html.H2("Chart1"),
            html.H2("Chart2"),
            html.H2("Chart3"),
            html.H2("Chart4")
        ], width=8)
    ], style={'marginTop': '10vh'}),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
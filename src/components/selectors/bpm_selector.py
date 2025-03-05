from dash import html, dcc

# Beats Per Minute Selector
bpm_selector = html.Div([
    html.H4("Beats Per Minute"),
    dcc.RangeSlider(min=40, max=210, step=20, value=[60,140], id='bpm_range')
], style={'marginBottom': '2.5vh'})
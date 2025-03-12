from dash import callback, Output, Input
import altair as alt
from data_loader.data_loader import load_data

data = load_data()

# Scatterplot Callback
@callback(
    Output('scatterplot', 'spec'),
    Input('y_axis_selector', 'value'),
    Input('year_dropdown', 'value'),
    Input('duration_min', 'value'),
    Input('duration_max', 'value'),
    Input('bpm_range', 'value'),
    Input('genre_dropdown', 'value')
)
def update_scatterplot(attribute, selected_year, selected_duration_min, selected_duration_max, selected_bpm_range, selected_genres):
    filtered_data = data[
        (data['year'] == selected_year) &
        (data['duration'] >= (selected_duration_min if selected_duration_min is not None else 0)) &
        (data['duration'] <= (selected_duration_max if selected_duration_max is not None else data['duration'].max())) &
        (data['bpm'] >= selected_bpm_range[0]) &
        (data['bpm'] <= selected_bpm_range[1])
    ]

    if selected_genres:
        filtered_data = filtered_data[filtered_data['genre'].isin(selected_genres)]

    return (
        alt.Chart(
            filtered_data, width='container'
        ).mark_point(filled=True, size=100, color='#1ED760').encode(
            x=alt.X('popularity', title='Popularity', scale=alt.Scale(zero=False)),
            y=alt.Y(attribute, title=f'{attribute.title()}', scale=alt.Scale(zero=False)),
            color=alt.Color('genre', title='Genre'),
            tooltip=[
                alt.Tooltip('title', title='Song Title'), 
                alt.Tooltip('artist', title='Artist'), 
                alt.Tooltip('popularity', title='Popularity'), 
                alt.Tooltip(attribute, title=attribute.title()),
                alt.Tooltip('duration', title='Duration (Seconds)'),
                alt.Tooltip('bpm', title='BPM')
            ]
        ).properties(
            title=f'{attribute.title()} vs. Popularity in {selected_year}'
        ).configure_axis(
            labelFontSize=20,
            titleFontSize=24
        ).configure_title(
            fontSize=24
        ).configure(
            background='#282828'
        ).to_dict()
    )
from dash import callback, Output, Input
import altair as alt
from data_loader.data_loader import load_data

data = load_data()
genre_color = alt.Color(
    'genre',
    title='Genre',
    scale=alt.Scale(
        domain=['Rock/Alternative', 'Hip-Hop/Rap', 'Pop', 'Electronic/Dance'],
        range=['#FF5733', '#33A1FF', '#FFC300', '#6A1B9A']
    )
)

# Calculate min and max values for each attribute to use for fixed scales
attribute_scales = {}
columns_for_scaling = [col for col in data.columns if col not in ['title', 'artist', 'genre', 'year']]  # Removed 'popularity' from exclusion
for col in columns_for_scaling:
    attribute_scales[col] = {
        'min': data[col].min(),
        'max': data[col].max()
    }

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
    
    # Check if there are no songs matching the criteria
    if filtered_data.empty:
        # Create an empty chart with a text annotation
        empty_chart = alt.Chart().mark_text(
            align='center',
            baseline='middle',
            fontSize=20,
            color='#999'
        ).encode(
            text=alt.value("No songs match your current filter criteria. Try adjusting your filters.")
        ).properties(
            width='container',
            height=300,
            title=f'{attribute.title()} vs. Popularity in {selected_year}'
        ).configure_axis(
            labelFontSize=20,
            titleFontSize=24
        ).configure_title(
            fontSize=24
        ).configure(
            background='#282828'
        )
        
        return empty_chart.to_dict()

    y_scale = alt.Scale(
        domain=[attribute_scales[attribute]['min'], attribute_scales[attribute]['max']],
        zero=False
    )
    
    x_scale = alt.Scale(
        domain=[attribute_scales['popularity']['min'], attribute_scales['popularity']['max']],
        zero=False
    )

    return (
        alt.Chart(
            filtered_data, width='container'
        ).mark_point(filled=True, size=100, color='#1ED760').encode(
            x=alt.X('popularity', title='Popularity', scale=x_scale),
            y=alt.Y(attribute, title=f'{attribute.title()}', scale=y_scale),
            color=genre_color,
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
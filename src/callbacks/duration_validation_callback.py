from dash import callback, Output, Input, State

# Duration validation callback
@callback(
    Output('duration_max', 'value'),
    Input('duration_max', 'value'),
    State('duration_min', 'value')
)
def validate_duration_max(max_value, min_value):
    # If max is less than min and both are not None, set max equal to min
    if max_value is not None and min_value is not None and max_value < min_value:
        return min_value
    return max_value
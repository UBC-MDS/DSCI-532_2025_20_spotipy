from dash import callback, Output, Input, State

# Duration validation callbacks
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

@callback(
    Output('duration_min', 'value'),
    Input('duration_min', 'value'),
    State('duration_max', 'value')
)
def validate_duration_min(min_value, max_value):
    # If min is greater than max and both are not None, set min equal to max
    if min_value is not None and max_value is not None and min_value > max_value:
        return max_value
    return min_value
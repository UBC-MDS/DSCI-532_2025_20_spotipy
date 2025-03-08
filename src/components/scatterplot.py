import dash_vega_components as dvc

# Scatterplot
scatterplot = dvc.Vega(
    id='scatterplot', 
    opt={"actions": False}, 
    spec={}, 
    style={'width': '100%', 'marginTop': '1vh'}
)
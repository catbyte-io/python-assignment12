from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

import pandas as pd


# Task 4: A Dashboard with Dash
# Load dataset
df = pldata.gapminder(return_type='pandas', indexed=False, datetimes=True)

# Create series of unique countries
countries = pd.Series(df['country'].unique())


# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="countries-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp", "figure"),
    [Input("countries-dropdown", "value")]
)
def update_graph(country):
    fig = px.line(df, x="date", y=country, title=f"{country} GDP")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 
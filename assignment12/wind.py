import pandas as pd
import plotly.express as px
import plotly.data as pldata


# Task 3: Interactive Visualizations with Plotly
df = pldata.wind(return_type='pandas')

print(f"{df.head(10)}")

# Replace any non digit character in 'strength' column with a decimal
df['strength'] = df['strength'].str.replace(r'\D', '.', regex=True)

# Convert to float
df['strength'] = pd.to_numeric(df['strength'])

# Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
fig = px.scatter(df, x='frequency', y='strength', color='direction')

fig.write_html("wind.html")
fig.show()

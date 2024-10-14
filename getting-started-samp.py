# Author: @infoseckp
# Built for: OU Weather and Climate Club
# License: GPU (General Public License)

import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Tree Species': ['Oak', 'Pine', 'Birch', 'Maple', 'Spruce'],
    'Carbon Sequestration (kg CO2/year)': [48, 35, 28, 40, 30]
}

df = pd.DataFrame(data)

# Create bar chart
fig = px.bar(
    df,
    x='Tree Species',
    y='Carbon Sequestration (kg CO2/year)',
    title='Carbon Sequestration Rates of Different Tree Species',
    labels={'Carbon Sequestration (kg CO2/year)': 'Carbon Sequestration (kg CO2/year)'}
)

fig.show()
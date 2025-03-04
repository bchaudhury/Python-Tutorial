import plotly.graph_objects as go
import pandas as pd
from copyreg import clear_extension_cache

# Load data from a CSV file
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['AAPL.Open'], high=df['AAPL.High'],
    low=df['AAPL.Low'], close=df['AAPL.Close'],
    increasing_line_color= 'cyan', decreasing_line_color= 'gray'
)])

# Update the layout
fig.update_layout(
    title=dict(text='The Great Recession'),
    yaxis=dict(
      title=dict(
        text='AAPL Stock'
        )
    ),
    shapes = [dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
        annotations=[dict(
        x='2016-12-09', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]
)

# Show the plot
fig.show()

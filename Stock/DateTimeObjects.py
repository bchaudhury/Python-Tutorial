import plotly.graph_objects as go
from datetime import datetime

# Create data arrays
open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
dates = [datetime(year=2024, month=10, day=10),
         datetime(year=2024, month=11, day=10),
         datetime(year=2024, month=12, day=10),
         datetime(year=2025, month=1, day=10),
         datetime(year=2025, month=2, day=10)]

# Create figure
fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=open_data, high=high_data,
                       low=low_data, close=close_data, name='Candlestick', showlegend=True, increasing_line_color='cyan', decreasing_line_color='gray', line=dict(width=1))])

# Add titles
fig.update_layout(
    title='Dummy Stock Price',
    yaxis_title='Price',
    xaxis_title='Month'
)

# Show figure
fig.show()
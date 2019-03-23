"""
    File name: heatmap.py
    Author: Harvey Barnhard
    Date created: 3/24/2019
    Date last modified: 3/23/2019
    Python Version: 3.7
"""

import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": go.Layout(title="hello world")
}, auto_open=True)
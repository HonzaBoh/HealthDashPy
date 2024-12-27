"""
Server setup, this happens after `register_callbacks()` is called and server can safely use this app to link callbacks to.
"""
from dash import Dash
from .layout import create_layout
from .data import data 

app = Dash(__name__)
server = app.server

# Build the layout using the data DataFrame
app.layout = create_layout(data)

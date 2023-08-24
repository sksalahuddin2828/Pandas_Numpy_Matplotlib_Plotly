import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from IPython.display import display, HTML
from ipywidgets import interact, widgets
from plotly.subplots import make_subplots

# Ingredients for the pizza
sauces = ['Tomato', 'Pesto', 'Alfredo', 'BBQ']
breads = ['Thin Crust', 'Regular', 'Whole Wheat', 'Gluten-Free']
cheeses = ['Mozzarella', 'Cheddar', 'Parmesan']

# Ensure all ingredient lists have the same length
max_len = max(len(sauces), len(breads), len(cheeses))
sauces = sauces + [''] * (max_len - len(sauces))
breads = breads + [''] * (max_len - len(breads))
cheeses = cheeses + [''] * (max_len - len(cheeses))

# Create a DataFrame for ingredient options
ingredient_options = pd.DataFrame({
    'Sauce': sauces,
    'Bread': breads,
    'Cheese': cheeses
})

# Create interactive dropdowns using ipywidgets
sauce_dropdown = widgets.Dropdown(options=ingredient_options['Sauce'])
bread_dropdown = widgets.Dropdown(options=ingredient_options['Bread'])
cheese_dropdown = widgets.Dropdown(options=ingredient_options['Cheese'])

# Function to update the pizza visualization
def update_pizza(sauce, bread, cheese):
    global selected_sauce, selected_bread, selected_cheese
    selected_sauce = sauce
    selected_bread = bread
    selected_cheese = cheese

    fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'xy'}, {'type': 'xy'}, {'type': 'xy'}]])
    
    # Create the pizza visualization
    pizza = go.Scatter(
        x=[0, 0.5, 1, 0], y=[0, 1, 0, 0],
        mode="lines", fill="toself",
        fillcolor="lightgrey"
    )
    
    # Highlight selected ingredients
    if selected_sauce:
        sauce_idx = ingredient_options[ingredient_options['Sauce'] == selected_sauce].index[0]
        fig.add_trace(go.Scatter(x=[0, 0.25, 0.25, 0],
                                 y=[0, 0.5, 1, 0], mode="lines", fill="toself",
                                 fillcolor="red", name="Sauce: " + selected_sauce))
    if selected_bread:
        bread_idx = ingredient_options[ingredient_options['Bread'] == selected_bread].index[0]
        fig.add_trace(go.Scatter(x=[0.25, 0.5, 0.75, 0.25],
                                 y=[0.5, 1, 0.5, 0.5], mode="lines", fill="toself",
                                 fillcolor="brown", name="Bread: " + selected_bread))
    if selected_cheese:
        cheese_idx = ingredient_options[ingredient_options['Cheese'] == selected_cheese].index[0]
        fig.add_trace(go.Scatter(x=[0.5, 1, 1, 0.75],
                                 y=[0, 0.5, 1, 0], mode="lines", fill="toself",
                                 fillcolor="yellow", name="Cheese: " + selected_cheese))
    
    fig.add_trace(pizza)
    fig.update_layout(
        showlegend=False, xaxis=dict(range=[-0.2, 1.2]), yaxis=dict(range=[-0.2, 1.2]),
        annotations=[
            dict(
                x=0.25, y=0.25, xref="x", yref="y",
                text="Sauce", showarrow=True, arrowhead=7, ax=0, ay=-40
            ),
            dict(
                x=0.625, y=0.75, xref="x", yref="y",
                text="Bread", showarrow=True, arrowhead=7, ax=0, ay=-40
            ),
            dict(
                x=0.875, y=0.25, xref="x", yref="y",
                text="Cheese", showarrow=True, arrowhead=7, ax=0, ay=-40
            )
        ],
        width=800, height=300
    )
    
    return fig

# Create interactive UI using ipywidgets interact function
interact(update_pizza, sauce=sauce_dropdown, bread=bread_dropdown, cheese=cheese_dropdown)

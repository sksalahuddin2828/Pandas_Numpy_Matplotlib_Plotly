import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define the operation table for Example 1
operation_table = pd.DataFrame({
    'a': ['a', 'b', 'c'],
    'b': ['b', 'a', 'c'],
    'c': ['c', 'c', 'a']
})

# Create a subplot for the operation table heatmap
fig_operation_table = make_subplots(rows=1, cols=1)
fig_operation_table.add_trace(
    go.Heatmap(
        z=operation_table.values,
        x=operation_table.columns,
        y=operation_table.index,
        colorscale='Viridis'
    )
)
fig_operation_table.update_layout(title_text="Operation Table")

# Check for inverses and create a DataFrame
inverses_data = []
for element in operation_table.columns:
    inverse = None
    for other_element in operation_table.columns:
        if operation_table.at[operation_table.index[0], element] == other_element and \
           operation_table.at[operation_table.index[0], other_element] == element:
            inverse = other_element
            break
    inverses_data.append({'Element': element, 'Inverse': inverse})
inverses_df = pd.DataFrame(inverses_data)

# Create a subplot for the inverses scatter plot
fig_inverses = make_subplots(rows=1, cols=1)
fig_inverses.add_trace(
    go.Scatter(
        x=inverses_df['Element'],
        y=inverses_df['Inverse'],
        mode='markers',
        text=inverses_df['Inverse'],
        marker=dict(size=10, color=inverses_df['Element'].astype('category').cat.codes, colorscale='Viridis')
    )
)
fig_inverses.update_layout(title_text="Inverses", xaxis_title="Element", yaxis_title="Inverse")

# Show the plots
fig_operation_table.show()
fig_inverses.show()

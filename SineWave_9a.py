import numpy as np
import plotly.graph_objects as go

x = np.linspace(-5, 5, 100)
y = np.sin(x)
z = np.cos(x)

fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines'
)])

fig.update_layout(title='3D Sine Wave')
fig.show()
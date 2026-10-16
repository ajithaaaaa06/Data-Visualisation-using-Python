
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 6, 4]

p1 = figure(title="Line Plot")
p1.line(x, y, color="blue", line_width=2)

p2 = figure(title="Scatter Plot")
p2.scatter(x, y, color="red", size=10)

p3 = figure(title="Bar Plot")
p3.vbar(x=x, top=y, width=0.5, color="green")

show(gridplot([[p1, p2], [p3]]))

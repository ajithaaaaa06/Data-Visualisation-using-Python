
from bokeh.plotting import figure, show
from bokeh.models import Title

x = [1, 2, 3, 4, 5]
y1 = [2, 5, 8, 6, 7]
y2 = [4, 6, 7, 5, 9]

p = figure(title="Line Graph",
           x_axis_label="X-axis",
           y_axis_label="Y-axis")

p.line(x, y1, color="blue", line_width=2,
       legend_label="Line 1")

p.line(x, y2, color="red", line_width=2,
       legend_label="Line 2")

#Adding Annotations
p.add_layout(Title(text="Annotation Example",
                   text_font_size="14px"), "above")

p.legend.location = "top_left"

show(p)

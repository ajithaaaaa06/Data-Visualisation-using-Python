import matplotlib.pyplot as plt

state = ['Assam', 'Manipur', 'Meghalaya', 'Mizoram',
         'Nagaland', 'Tripura', 'Nagaland']

forest_cover = [67353, 27692, 17280, 17321, 19240, 13464, 8073]

ex = [0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0]

plt.pie(
    forest_cover,
    labels=state,
    explode=ex,
    autopct="%0.2f%%",
    shadow=True,
    startangle=90,
)

plt.title("Forest Cover in States of India")
plt.legend(bbox_to_anchor=(1, 0.5))

plt.show()
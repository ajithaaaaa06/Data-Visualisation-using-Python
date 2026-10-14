import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a hexagon distribution plot
sns.jointplot(
    x="sepal_length",
    y="sepal_width",
    data=iris,
    kind="hex",
)

plt.show()
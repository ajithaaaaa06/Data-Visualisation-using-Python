
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Calculate correlation using numeric columns only
correlation_matrix = iris.select_dtypes(include="number").corr()

# Create heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")

plt.title("Heatmap of Feature Correlations in the Iris Dataset")
plt.show()

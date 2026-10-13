import matplotlib.pyplot as plt

# Sample data: Student grades
grades = [75, 82, 92, 88, 78, 90, 85, 95, 70, 87,
          93, 79, 81, 86, 89, 94, 73, 84, 91, 77]

# Create a histogram
plt.hist(
    grades,
    bins=5,
    edgecolor='black',
    color='skyblue'
)

# Customize labels and title
plt.xlabel('Grades')
plt.ylabel('Frequency')
plt.title('Grade Distribution in a Class')

# Display the plot
plt.show()
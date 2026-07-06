import matplotlib.pyplot as plt

# Data
labels = ["Apples", "Bananas", "Oranges", "Grapes"]
sizes = [30, 25, 20, 25]

# Create pie chart
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",   # Show percentages
    startangle=90        # Rotate so first slice starts at the top
)

plt.title("Fruit Distribution")
plt.axis("equal")        # Makes the pie chart a circle
plt.show()
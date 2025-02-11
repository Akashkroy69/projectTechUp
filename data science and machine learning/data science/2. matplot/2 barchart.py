import matplotlib.pyplot as plt

# Data: Programming languages and the number of students who like them
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C']
students_count = [40, 25, 15, 12, 8]

# Create the bar chart
plt.bar(languages, students_count, color=['blue', 'green', 'red', 'purple', 'orange'])

# Add labels and title
plt.xlabel("Programming Languages")
plt.ylabel("Number of Students")
plt.title("Favorite Programming Languages Among Students")

# Show the chart
plt.show()

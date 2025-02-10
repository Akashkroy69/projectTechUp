import seaborn as sns
import matplotlib.pyplot as plt  # Used to show the plots

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Display the first few rows
# print(iris.head())

# Scatter Plot
# Used to visualize relationships between two numerical variables.
sns.scatterplot(x="sepal_length", y="sepal_width", data=iris)




# Show the plot
plt.show()


# sns.scatterplot() → For relationships between two numbers
# sns.countplot() → For categorical data
# sns.histplot() → For distributions
# sns.boxplot() → For spread & outliers
# sns.pairplot() → For multiple variable relationships
# sns.heatmap() → For correlations
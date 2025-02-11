import seaborn as sns
import matplotlib.pyplot as plt  # Used to show the plots

# Load the Titanic dataset
titanic = sns.load_dataset("titanic")

print(titanic.head())

# Scatter Plot
# Used to visualize relationships between two numerical variables.
sns.regplot(x="age", y="fare", data=titanic,)
# markers=["o","s","D","^","P"]
# palette --> color of the hue variable : viridis,plasma,coolwarm,summer,autumn,winter,spring
plt.show()




# Note: The scatterplot() function is used to visualize relationships between two numerical variables.
# The x and y parameters specify the column names of the x and y variables.
# The data parameter specifies the dataset to use.
# The hue parameter specifies the column name of the variable to color the points by.
# Key Parameters to Remember

#     x and y: Define the axes.
#     hue: Colors points based on categories.
#     style: Changes marker shapes based on categories.
#     size: Adjusts point sizes.
#     palette: Defines the color scheme.
#     marker: Changes marker types.
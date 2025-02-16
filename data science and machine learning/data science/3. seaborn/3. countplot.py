import seaborn as sns
import matplotlib.pyplot as plt  # Used to show the plots

# Load the Titanic dataset
titanic = sns.load_dataset("titanic")
print(titanic.head())
# Count Plot
# Used to visualize the count of a categorical variable.
sns.countplot(x="sex", data=titanic, hue="class", palette="viridis",edgecolor="black",width=0.6,linewidth=2)
plt.show(  )


# Note:
# Count Plot in Seaborn

# A count plot is used to visualize the count of observations in each category. It is similar to a bar chart but
#  is explicitly designed to show the number of occurrences of each category in a categorical variable.
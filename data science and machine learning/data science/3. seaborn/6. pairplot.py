import seaborn as sns
import matplotlib.pyplot as plt  # Used to show the plots

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Pair Plot
# Used to visualize relationships between multiple numerical variables.
sns.pairplot(iris, hue="species", palette="viridis", diag_kind="hist",height=2,kind="scatter")
#kind : {‘scatter’, ‘kde’, ‘hist’, ‘reg’}
# diag_kind: hist, kde
plt.show()

# Note:
# Explanation:

#     The diagonal shows histograms of each feature (e.g., sepal_length, sepal_width).
#     The off-diagonal scatterplots show relationships between each pair of features.


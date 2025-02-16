import seaborn as sns
import matplotlib.pyplot as plt  # Used to show the plots

# Load the Titanic dataset
titanic = sns.load_dataset("titanic")
print(titanic.head())
print(titanic["class"].unique())

# histplot for catagorical data
# sns.histplot(titanic,x="embark_town",kde=True,hue="class")
#histplot for numerical data
sns.histplot(titanic,x="age",kde=True,hue="class",bins=8,multiple="stack")
#multiple : {“layer”, “dodge”, “stack”, “fill”}
# layer : Default value, draws the histogram on top of each other
# dodge : Draws the histogram next to each other
# stack : Stacks the histograms on top of each other
# fill : Stacks the histograms on top of each other and fills the area under the curve

# sns.histplot(titanic,x="age",kde=True,hue="class",bins=8,multiple="stack",cumulative=True)
#cumulative : bool, optional --> If True, then a histogram is computed where each bin gives 
# the counts in that bin plus all bins for smaller values. The last bin gives the total number 
# of datapoints.

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt  # Used to show the plots

# Load the Iris dataset
# data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #ex 1
# data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #ex 2
data = [1,6,8,13,17,19,28,34]

# hist plot
# Used to visualize the distribution of a numerical variable.
# The histplot in Seaborn is a powerful tool for visualizing the distribution of data. 
# It combines a histogram and optionally a kernel density estimate (KDE) to show how
#  frequently data points appear in a given range.

sns.histplot(data,kde=True)
# sns.histplot(data,bins= 5)
#palette: viridis,plasma, inferno, magma, cividis
#bins: 10,20,30,40,50--> number of bins
plt.show()
# Explanation:

#     The histogram divides the data into bins and counts how many values fall into each bin.
#     By default, Seaborn chooses an appropriate number of bins based on the data.
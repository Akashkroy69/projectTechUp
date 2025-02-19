import seaborn as sns
import matplotlib.pyplot as plt  # Used to show the plots
import numpy as np
# data = np.array([[1, 20, 3], [4, 50, 6], [7, 80, 9]]) #ex 1
# data = np.array([[1, 20, 3, 40], [4, 50, 6, 70], [7, 80, 9, 100]]) #ex 2
data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) #ex 3

# Heatmap
# Used to visualize the data in a 2D format.
# A heatmap is a two-dimensional graphical representation of data 
# where the individual values that are contained in a matrix are represented as colors.

# sns.heatmap(data) #simplest way
sns.heatmap(data, annot=True,fmt=".2f",cmap="plasma") #with annotation
# fmt: d, f, .2f, .3f, .4f, .5f, .6f, .7f, .8f, .9f, .10f
# cmap: viridis,plasma, inferno, magma, cividis,coolwarm
plt.show()
# The simplest way to create a heatmap is by using Seaborn with a 2D array of numbers.
# Explanation:

    # data: A 2D array representing the values for each cell in the heatmap.
    # The color intensity represents the value of each cell.
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")


## Matrix Plot
# For this to work, all data must be in a matrix format. meaning that the data must be in a 2D array-like structure.
# using .corr() to get the correlation matrix

# Only select numeric columns for correlation
tc = tips.corr(numeric_only=True)
print(tc)
sns.heatmap(tc, annot=False, cmap='Spectral')   
plt.show()

# Available cmap values include:
# Perceptually Uniform Sequential: ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
# Sequential: ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
# Sequential (2): ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper']
# Diverging: ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
# Cyclic: ['twilight', 'twilight_shifted', 'hsv']
# Qualitative: ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c']
# Miscellaneous: ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
fp = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(fp,cmap="magma", annot=False, fmt="d", linewidths=0.5, linecolor="white", cbar_kws={"orientation": "vertical"})
plt.show()



# cluster map is a matrix plot with clustering used for grouping similar data points together.
sns.clustermap(fp, cmap="coolwarm", annot=False, fmt="d", linewidths=0.5, linecolor="white", cbar_kws={"orientation": "vertical"})
plt.show()  
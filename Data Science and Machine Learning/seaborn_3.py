import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")


# sns.pairplot(iris, hue="species", palette="Set2", markers=["o", "s", "D"], diag_kind="kde")
# plt.show()

# g = sns.PairGrid(iris)
# g.map_diag(sns.displot)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot, cmap="Blues", shade=True)

# plt.show()


tips = sns.load_dataset("tips")
g = sns.FacetGrid(data=tips, col="time", row="sex", margin_titles=True)

g.map(sns.distplot, "total_bill")

plt.show()
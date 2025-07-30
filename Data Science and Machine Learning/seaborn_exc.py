import seaborn as sns
import matplotlib.pyplot as plt

titanic= sns.load_dataset("titanic")
sns.set_style("whitegrid")

# # Exerecise 1:
# sns.jointplot(x='fare', y='age', data= titanic, kind='scatter', cmap='twilight')
# plt.show()

# # Exercise 2:
# sns.displot(titanic['fare'], kde=False, bins=30, color='red', alpha=0.5)
# plt.show()

# # Exercise 3:
# sns.boxplot(x='class', y='age', data=titanic, palette='Set2')
# plt.show()

# # Exercise 4:
# sns.swarmplot(x='class', y='age', data=titanic, palette='twilight')
# plt.show()

# # Exercise 5:
# sns.countplot(x='sex', data=titanic, palette='gnuplot')
# plt.show()

# Exercise 6:
tit = titanic.corr(numeric_only=True)
sns.heatmap(tit, annot=False, cmap='coolwarm')
plt.show()
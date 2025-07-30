"""
Catrgorical plots with seaborn
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

# bar plot
sns.barplot(x="sex", y="total_bill", data=tips, palette="viridis", estimator=np.std, hue="smoker")
plt.show()

# count plot
sns.countplot(x="sex", data=tips, palette="pastel", hue="smoker")
plt.show()

# box plot
sns.boxplot(x="sex", y="total_bill", data=tips, palette="coolwarm", hue="smoker")
plt.show()

# violin plot
sns.violinplot(x="day", y="total_bill", data=tips, palette="Greens", hue="smoker", split=True)
plt.show()

# strip plot
sns.stripplot(x="day", y="total_bill", data=tips, palette="Set1", jitter=True, hue="smoker")
plt.show()

# swarm plot
sns.violinplot(x="day", y="total_bill", data=tips, palette="coolwarm")
sns.swarmplot(x="day", y="total_bill", data=tips, color="black", alpha=0.5)
plt.show()


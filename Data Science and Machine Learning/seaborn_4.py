"""
Regression Plots
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Linear Regression Plot
tips = sns.load_dataset("tips")
sns.lmplot(x="total_bill", y="tip", data=tips, hue="smoker", palette="coolwarm", markers=["o", "s"], scatter_kws={"s": 50})
plt.title("Linear Regression Plot")
plt.show()
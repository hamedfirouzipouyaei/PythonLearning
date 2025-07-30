"""
Distribution of a dataset using seaborn
"""

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# distribution of univariate data
sns.displot(tips["total_bill"], kde=True, bins= 30)

plt.show()

##joint distribution of two variables
# joint distribution with scatter plot with most density
sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde", fill=True)
plt.show()

#joint distribution with hexagonal binning
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex", gridsize=20)
plt.show()

#joint distribution with regression line
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg", color="g")
plt.show()



## Pair plot
sns.pairplot(tips, hue="sex", palette="coolwarm", markers=["o", "s"], diag_kind="kde")
plt.show()

## Rug plot
# kde means Kernel Density Estimate
sns.rugplot(tips["total_bill"], height=0.5, color="green")
plt.show()
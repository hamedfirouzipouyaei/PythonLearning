import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())


plt.figure(figsize=(10, 6))
# sns.set_style("whitegrid")
sns.set_context("talk")
sns.countplot(x='sex', data= tips)
sns.despine(left=True, bottom=True)

plt.show()
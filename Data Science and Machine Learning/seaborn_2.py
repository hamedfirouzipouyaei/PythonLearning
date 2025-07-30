import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 
tips = sns.load_dataset("tips")

root = tk.Tk()
root.title("Seaborn Visualization")

flights = sns.load_dataset("flights")


## Matrix Plot
# For this to work, all data must be in a matrix format. meaning that the data must be in a 2D array-like structure.
# using .corr() to get the correlation matrix

# Only select numeric columns for correlation
tc = tips.corr(numeric_only=True)
print(tc)
sns.heatmap(tc, annot=True, cmap='coolwarm')   
plt.show()
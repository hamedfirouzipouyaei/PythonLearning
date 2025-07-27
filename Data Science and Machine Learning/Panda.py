import numpy as np
import pandas as pd
from numpy.random import randn



list_ = ['a', 'b', 'c']
data_ = [10, 20, 30]
arr_  = np.array(data_)
dic_  = {'a': 10, 'b': 30, 'c':30}

print(pd.Series(data = data_))			# create a series of data
print(pd.Series(data = data_, index= list_))	# change the index of the series with custom index
print(pd.Series(data_, list_))			# creating a series without specifying the parameters

print(pd.Series(arr_))				# create a series from an array
print(pd.Series(dic_))				# create a series from dic. by recognizing keys as indexes


ser1 = pd.Series([1,2,3,4], ['USA','Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1,2,3,4], ['USA','Germany', 'USSR', 'Italy'])

print(ser1)
print(ser2)

print(ser1['USA'])
print(ser1 + ser2)				# adding two series together

# creating a dataframes
print("---------------DATAFRAME-----------------")
np.random.seed(101)
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print("Dataframe with random numbers:")
print(df)					# print the dataframe
print("Column W:")
print(df['W'])					# print a column of the dataframe
print("Column W and Z:")
print(df[['W', 'Z']])				# print multiple columns of the dataframe

#creating a new column
df['new'] = df['W'] + df['Z']
print("Dataframe with new column:")
print(df)

# Dropping a column
df.drop('new', axis=1, inplace=True)  # axis=1 means column and inplace=True means modify the original dataframe
print("Dataframe after dropping 'new' column:")
print(df)

print("Row A:")
print(df.loc['A']) # Accessing a row by label

print("Row at index position 2:")
print(df.iloc[2])  # Accessing a row by index position

print(df)
print(df.loc['B', 'Y']) # Accessing a specific value by label
print(df.iloc[1, 2])  # Accessing a specific value by index positions

print (df > 0)  # Boolean indexing to filter rows where values are greater than 0
print(df[df > 0])  # Displaying only the values greater than 0  

print("Selected df:")
print(df[df['W'] > 0])
print("Selected df with multiple conditions:")
print(df[df['W'] > 0][['Y', 'X']])  # Filtering with multiple conditions


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))  # Creating a hierarchical index
hier_index = pd.MultiIndex.from_tuples(hier_index)  # Converting to MultiIndex
df2 = pd.DataFrame(randn(6, 2), index=hier_index, columns=['A', 'B'])  # Creating a DataFrame with hierarchical index
print("DataFrame with hierarchical index:")
print(df2)


# Dealing with missing data
print("---------------MISSING DATA-----------------")
df3 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})
print("DataFrame with missing data:")
print(df3)
print("DataFrame after dropping rows with any missing data:")
print(df3.dropna())  # Dropping rows with any missing data
print("Drop on columns with any missing data:")
print(df3.dropna(axis=1))  # Dropping columns with any missing data
print("Filling missing data with 0:")
print(df3.fillna(0))  # Filling missing data with 0


# Grouping data
print("---------------GROUPING DATA-----------------")
df4 = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'], 'B': [1, 2, 3, 4]})
print("DataFrame before grouping:")
print(df4)
print("Grouped by column 'A':")
print(df4.groupby('A').sum()) # other aggregation functions can be used such as mean(), count(), std(), max(), min(), etc.

# Merging dataframes
print("---------------MERGING DATAFRAMES-----------------")
df5 = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'], 'C': [5, 6, 7, 8]})
print("DataFrame to merge:")
print(df5)
print("Merged DataFrame:")
print(pd.merge(df4, df5, on='A'))

# Concatenating dataframes
print("---------------CONCATENATING DATAFRAMES-----------------")
df6 = pd.DataFrame({'A': ['foo', 'bar'], 'D': [9, 10]})
print("DataFrame to concatenate:")
print(df6)
print("Concatenated DataFrame:")
print(pd.concat([df4, df6], axis=0))    
print("Concatenated DataFrame with axis=1:")
print(pd.concat([df4, df6], axis=1))  # Concatenating along columns

print("---------------READING AND WRITING DATA-----------------")
# Reading and writing data
df7 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df7.to_csv('data.csv', index=False)  # Writing DataFrame to CSV
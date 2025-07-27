import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
original_dir = os.getcwd()
os.chdir(script_dir)
ecom = pd.read_csv('Ecommerce Purchases')
print(ecom.head())
os.chdir(original_dir)

print("The number of rows in the dataframe is:", ecom.shape[0])
print("The number of columns in the dataframe is:", ecom.shape[1])

print("The average purchase price:", ecom['Purchase Price'].mean())
print("The highest purchase price:", ecom['Purchase Price'].max())
print("The lowest purchase price:", ecom['Purchase Price'].min())
print("The number of people haveing English as their prefered language:", ecom[ecom['Language'] =='en'].shape[0])
print("We have", ecom[ecom['Job'] == 'Lawyer'].shape[0], "Lawyers in the dataset.")
print(ecom[ecom['AM or PM'] == 'AM'].shape[0], "people made their purchase in the AM.")
print(ecom[ecom['AM or PM'] == 'PM'].shape[0], "people made their purchase in the PM.")
print("The most top 5 job titles are:")
print(ecom['Job'].value_counts().head(5))

print("The purchase price for Lot 90 WT", ecom[ecom['Lot'] == '90 WT']['Purchase Price'].values[0])
print("The email address of the person with the credit card number 4926535242672853 is:", 
      ecom[ecom['Credit Card'] == 4926535242672853]['Email'].values[0])
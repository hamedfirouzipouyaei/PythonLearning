"""
This script is an exercise in using pandas to manipulate data.
The SF salaries dataset is used to demonstrate various DataFrame operations,
including reading from and writing to different file formats such as CSV, Excel, JSON, and HTML.
"""

import numpy as np
import pandas as pd 
import os

# Set the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Script directory:", script_dir)

# Change to script directory to ensure we can find the CSV file
original_dir = os.getcwd()
os.chdir(script_dir)

# Reading the SF salaries dataset
sal = pd.read_csv('Salaries.csv')
print("SF Salaries DataFrame:")
print(sal.head())

# Change back to original directory
os.chdir(original_dir)

print("-----------------Number of entries in the DataFrame-----------------")
print(sal.info())

print("-----------------The average base pay-----------------")
# Convert BasePay to numeric, handling any non-numeric values
sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors='coerce')
print("The average base pay is:", sal['BasePay'].mean())

print("-----------------The highest amount of overtime pay-----------------")
# Convert OvertimePay to numeric, handling any non-numeric values
sal['OvertimePay'] = pd.to_numeric(sal['OvertimePay'], errors='coerce')
print("The highest amount of overtime pay is:", sal['OvertimePay'].max())

print("-----------------The job title of JOSEPH DRISCOLL-----------------")
print("The job title of JOSEPH DRISCOLL is:", sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].values[0])

print("-----------------The total pay of JOSEPH DRISCOLL including benefits-----------------")
print("The total pay of JOSEPH DRISCOLL including benefits is:", sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'].values[0])

print("-----------------The name of the employee with the highest total pay-----------------")
print("The name of the employee with the highest total pay is:", sal.loc[sal['TotalPayBenefits'].idxmax()]['EmployeeName'])
print(sal.loc[sal['TotalPayBenefits'].idxmax()])

print("-----------------The name of the employee with the lowest total pay-----------------")
print("The name of the employee with the lowest total pay is:", sal.loc[sal['TotalPayBenefits'].idxmin()]['EmployeeName'])
print(sal.loc[sal['TotalPayBenefits'].idxmin()])

print("-----------------The average base pay per year-----------------")
average_basepay_per_year = sal.groupby('Year')['BasePay'].mean()
print(average_basepay_per_year)

print("------------------The number of unique job titles-----------------")
print("The number of unique job titles is:", sal['JobTitle'].nunique())

print("-----------------The top 5 most common job titles-----------------")
five_most_common_job_titles = sal['JobTitle'].value_counts().head(5)
print("The top 5 most common job titles are:")
print(five_most_common_job_titles)

print("-----------------The number of job titles represented by only one person in 2013-----------------")
job_title_count_2013 = sal[sal['Year'] == 2013]['JobTitle'].value_counts()
one_person_job_titles_2013 = job_title_count_2013[job_title_count_2013 == 1]
print("The number of job titles represented by only one person in 2013 is:", len(one_person_job_titles_2013))

print("-----------------The number of people have the word Chief in their job title-----------------")
chief_job_titles = sal[sal['JobTitle'].str.contains('Chief', case=False, na=False)]
print("The number of people who have the word 'Chief' in their job title is:", len(chief_job_titles))   


print("-----------------------------------------Just for some more test:")
interseted_name = sal[sal['Year']==2013]
print(interseted_name)
print("The base pay mean:")
interseted_name_mean = interseted_name['BasePay'].mean()
print(interseted_name_mean)
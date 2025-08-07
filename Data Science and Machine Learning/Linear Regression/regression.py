import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('USA_Housing.csv')

# print(df.head())
print(df.info())
print(df.describe())

# sns.pairplot(df)
# plt.show()

# sns.displot(df['Price'], kde=True)
# plt.show()

# sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
# plt.show()

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 
         'Avg. Area Number of Bedrooms', 'Area Population']]

Y = df['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=101)  # 60% training and 40% testing

from sklearn.linear_model import LinearRegression

lm = LinearRegression() # Create a Linear Regression model (instantiate the class/object)
lm.fit(X_train, Y_train) # Fit the model to the training data
print("Coefficients:", lm.coef_) # Print the coefficients of the model
print("Intercept:", lm.intercept_) # Print the intercept of the model

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficients'])
print(cdf)

# Predicting the test set results
predictions = lm.predict(X_test)
plt.scatter(Y_test, predictions)
plt.show()

# Plotting the residuals
sns.displot((Y_test - predictions), bins=50, kde=True)
plt.show()

# Evaluation metrics
from sklearn import metrics 
print("Mean Absolute Error:", metrics.mean_absolute_error(Y_test, predictions))
print("Mean Squared Error:", metrics.mean_squared_error(Y_test, predictions))   
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(Y_test, predictions)))
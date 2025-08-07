import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Ecommerce Customers')

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)


# sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=df, kind='scatter', color='purple')
# plt.show()

# sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=df, kind='scatter')
# plt.show()

# sns.jointplot(x='Time on App', y='Length of Membership', data=df, kind='hex', color='green')
# plt.show()

# sns.pairplot(df)
# plt.show()

# sns.lmplot(x='Yearly Amount Spent', y='Length of Membership', data=df, palette='coolwarm')
# plt.show()


Y = df['Yearly Amount Spent']
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101) 

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, Y_train)
print("Coefficients:", lm.coef_)
print("Intercept:", lm.intercept_)

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficients'])
print(cdf)

predictions = lm.predict(X_test)
plt.scatter(Y_test, predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()

# Plotting the residuals
sns.displot((Y_test - predictions), bins=50, kde=True)
plt.xlabel('Residuals')
plt.ylabel('Frequency') 
plt.show()

from sklearn import metrics 
print("Mean Absolute Error:", metrics.mean_absolute_error(Y_test, predictions))
print("Mean Squared Error:", metrics.mean_squared_error(Y_test, predictions))   
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(Y_test, predictions)))

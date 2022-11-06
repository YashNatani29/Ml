# Implementation of Normal equation in multivariable linear regression
import numpy as np
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


X,y = datasets.fetch_california_housing(return_X_y=True)
x_zero=np.ones((X.shape[0], 1))
X=np.concatenate((x_zero,X),axis=1)
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.75)


thetas = np.dot(np.dot(np.linalg.inv(np.dot(X_train.T, X_train)),X_train.T),Y_train)

# model evaluation for training set
y_train_predict = np.dot(X_train,thetas)
rmse = (np.sqrt(metrics.mean_squared_error(Y_train, y_train_predict)))
r2 = metrics.r2_score(Y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test_predict = np.dot(X_test,thetas)
rmse = (np.sqrt(metrics.mean_squared_error(Y_test, y_test_predict)))
r2 =metrics.r2_score(Y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))


plt.style.use('fivethirtyeight')
plt.subplot(2, 1, 1)
plt.scatter(np.arange(X_train.shape[0]), y_train_predict - Y_train,color = "green", s = 10, label = 'Train data')
plt.hlines(y = 0, xmin = 0, xmax = X_train.shape[0], linewidth = 2,colors='red')
plt.title("Residual errors")
plt.legend(loc = 'upper right')
plt.subplot(2, 1, 2)
plt.scatter(np.arange(X_test.shape[0]), y_test_predict - Y_test,color = "blue", s = 10, label = 'Test data')
plt.hlines(y = 0, xmin = 0, xmax = X_train.shape[0], linewidth = 2,colors='red')
plt.legend(loc = 'upper right')
plt.show()
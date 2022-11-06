import numpy as np
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

X,y = datasets.load_boston(return_X_y=True)
print(X)
x_zero=np.ones((X.shape[0], 1))
X=np.concatenate((x_zero,X),axis=1)
X_train,X_test,Y_train,Y_test = X[:50,:],X[400:,:],y[:50],y[400:]
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

Standardisation = StandardScaler()
X_train= Standardisation.fit_transform(X_train)

# Y_train=np.dot(Y_train,np.ones((Y_train.shape[0], 1)))
# Y_test=np.dot(Y_test,np.ones((Y_train.shape[0], 1)))


L,iteration = 0.0001, 1000
n = float(X_train.shape[0])
thetas =  np.zeros((X_train.shape[1], 1))
cost=np.ones(iteration)
# Performing Gradient Descent
for j in range(iteration):
    Y_pred = np.dot(X_train,thetas)
    for i in range(0, X_train.shape[1]):
        D_m = (-2 / n) * np.sum(X_train[...,i].ravel() * (Y_pred-Y_train))
        print("j=",j,"i=",i)
        thetas[i] = thetas[i] - L * D_m
        cost[i]=(1/n)*np.sum(np.square(Y_pred-Y_train))
plt.plot(cost)
plt.show()





# # model evaluation for training set
# y_train_predict = np.dot(X_train,thetas)
# rmse = (np.sqrt(metrics.mean_squared_error(Y_train, y_train_predict)))
# r2 = metrics.r2_score(Y_train, y_train_predict)
#
# print("The model performance for training set")
# print("--------------------------------------")
# print('RMSE is {}'.format(rmse))
# print('R2 score is {}'.format(r2))
# print("\n")
#
# # model evaluation for testing set
# y_test_predict = np.dot(X_test,thetas)
# rmse = (np.sqrt(metrics.mean_squared_error(Y_test, y_test_predict)))
# r2 =metrics.r2_score(Y_test, y_test_predict)
#
# print("The model performance for testing set")
# print("--------------------------------------")
# print('RMSE is {}'.format(rmse))
# print('R2 score is {}'.format(r2))
#
#
#
# plt.style.use('fivethirtyeight')
# plt.subplot(2, 1, 1)
# plt.scatter(np.arange(X_train.shape[0]), y_train_predict - Y_train,color = "green", s = 10, label = 'Train data')
# plt.hlines(y = 0, xmin = 0, xmax = X_train.shape[0], linewidth = 2,colors='red')
# plt.title("Residual errors")
# plt.legend(loc = 'upper right')
# plt.subplot(2, 1, 2)
# plt.scatter(np.arange(X_test.shape[0]), y_test_predict - Y_test,color = "blue", s = 10, label = 'Test data')
# plt.hlines(y = 0, xmin = 0, xmax = X_train.shape[0], linewidth = 2,colors='red')
# plt.legend(loc = 'upper right')
#
# plt.show()
# Implementation of gradient descent in multivariable linear regression(Ridge)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('HousingData.csv')
dataset = dataset.fillna(0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

z = dataset.iloc[:].values
z = sc.fit_transform(z)
X = z[:, 0:-1]
y = z[:, -1]

m = X.shape[0]
ones = np.ones((m, 1))
X = np.concatenate((ones, X), axis=1)

def LinReg_with_gradient_descent(X, y, alpha, epoch,lam):

  n = X.shape[1]
  Theta = np.ones(n)
  h = np.dot(X, Theta)

  cost = np.ones(epoch)
  for i in range (0, epoch):
    Theta[0] = Theta[0] - (alpha / X.shape[0]) * sum(h-y)
    for j in range(0, n):
      Theta[j]= Theta[j]*(1-(lam*(alpha/ X.shape[0])) ) - (alpha/ X.shape[0]) * sum((h-y) * X[:, j])
    h  = np.dot(X, Theta)
    cost[i] = 1/(2*m) * sum(np.square(h-y))
  return cost, Theta

cost, theta = LinReg_with_gradient_descent(X, y, 0.01, 2000,0.001)

print(theta)
print("\nLowest cost =" + str(np.min(cost)))
print("Cost after 2000 iterations = " + str(cost[-1]))
py = np.dot(X,theta)
rss = np.sum(np.square(y - py))
tss = np.sum(np.square(y - np.mean(y)))
print("\nR square:", 1 - rss / tss)

plt.plot(cost)
plt.xlabel("Epoch (number of iteration)")
plt.ylabel( "Cost or Loss")
plt.show()

# Implementation of gradient descent in simple linear regression
import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("data.csv")
X = df['x']
Y = df['y']
plt.scatter(X, Y, color='b')


m,c,L,iteration = 0,0, 0.0001, 1000
n = float(len(X))

# Performing Gradient Descent
for i in range(iteration):
    Y_pred = m * X + c
    D_m = (-2 / n) * sum(X * (Y - Y_pred))
    D_c = (-2 / n) * sum(Y - Y_pred)
    m = m - L * D_m
    c = c - L * D_c

print(m, c)
Y_pred = m*X + c
plt.plot(X,Y_pred, color='red')
plt.xlabel("X")
plt.ylabel( "Y")
plt.show()
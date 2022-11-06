import matplotlib.pyplot as plt
import random
import numpy as np


# function to calculate total
def total(a):
    c = [a[0]]
    for j in range(1, 10):
        k = c[j - 1] + a[j]
        c.append(k)
    return c


india = []
england = []

# Generating random scores
for i in range(0, 10):
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    england.append(m)
    india.append(n)
print('India => ', india)
print('England=> ', england)

x1 = np.arange(0, 10, 1)

# Calculating total after each wicket
y1 = total(india)
y2 = total(england)

# plotting the india points
plt.plot(x1, y1, '-ob', label="India")
# plotting the England points
plt.plot(x1, y2, '-or', label="England")

# naming the x axis
plt.xlabel('Wickets')
# naming the y axis
plt.ylabel('Runs')
# giving a title to my graph
plt.title('Performance')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

import matplotlib.pyplot as plt
import pandas
from scipy import stats

df = pandas.read_csv("data.csv")
x = df['sqft_lot']
y = df['price']

slope, intercept, r, p, stderror = stats.linregress(x, y)


def parthlinreg(q):
    return slope * q + intercept


linregmodel1 = list(map(parthlinreg, x))



plt.plot(x, linregmodel1, '-r', label="linear regression")
plt.scatter(x, y)
plt.xlabel('sqft_lot')
plt.ylabel('Price')
plt.title('House Price.')
plt.legend()
plt.show()


a = int(input("Enter sqft_lot:"))
print("Predicted house price:", parthlinreg(a))
import statistics

import numpy as np

x = np.random.rand(100)
print("\nx is : ", x)
print("\nMINIMUM OF x: ", np.min(x))
print("LOWER QUARTILE OF x: ", np.quantile(x, .25))
print("MEDIAN OF x: ", np.median(x))
print("UPPER QUARTILE OF x: ", np.quantile(x, .75))
print("MAXIMUM OF x: ", np.max(x))
print("MEAN OF x: ", np.mean(x))
print("MODE IS: ", statistics.mode(x))
print("VARIANCE OF x: ", np.var(x))
print("STANDARD DEVIATION OF x: ", np.std(x))
print("RANGE OF x: ", np.max(x) - np.min(x))

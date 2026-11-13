import numpy as np
import matplotlib.pyplot as plt

m = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(m.mean(), m.sum(), m.max(), m.min())
print(m.mean(axis=1))   # мөрөөр
print(m.mean(axis=0))   # баганаар

plt.bar(["М1","М2","М3"], m.mean(axis=1))
plt.show()
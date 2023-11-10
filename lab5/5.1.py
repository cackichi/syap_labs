# y = (sin(pi/6-1)*sin(pi/6-1)+(3+x*x)^(1/4)-lg(x^3-1)*lg(x^3-1)*lg(x^3-1))/(arcsin(x/2) - 1,756*10^(-2))
# при x = 1,6453
import numpy as np

x = 1.6453
y = (np.sin(np.pi/6 - 1)**2 + (3 + x*x)**(1/4) - np.log10(x**3-1)**3)/(np.arcsin(x/2) - 1.756e-2)
print("Ответ: " + y.__str__())

# 1.2

rows = 12
column1 = np.ones(rows)
NVariant = 10
column2 = np.random.randint(NVariant, NVariant + 12, rows)
column3 = np.random.randint(60, 83, rows)
X = np.column_stack((column1, column2, column3))
print()
print(X)
Y = np.random.uniform(13.5, 18.6, rows)
print()
print(Y)
A = np.linalg.inv(X.T @ X) @ X.T @ Y
print()
print(A)

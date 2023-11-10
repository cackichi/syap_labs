import numpy as np
import matplotlib.pyplot as plt

x_val = 3.567
a_val = np.arange(-5, 12.5, 0.5)

def f(x, a):
    return 1/np.tan(x)**3 + 2.24*a*x

y_val = f(x_val, a_val)

for a, y in zip(a_val, y_val):
    print(f"a: {a:.2f}, f(x): {y:.4f}")

max_val = np.max(y_val)
min_val = np.min(y_val)
mean_val = np.mean(y_val)
count_el = len(y_val)
print("Max val: ", max_val)
print("Min val: ", min_val)
print("Mean val: ", mean_val)
print("Count: ", count_el)

if count_el % 2 == 0:
    sorted_val = np.sort(y_val)[::-1]
else:
    sorted_val = np.sort(y_val)

print("Sorted values:\n")
for sorted_val in sorted_val:
    print(sorted_val)

plt.figure(figsize=(10,6))
plt.plot(a_val, y_val, marker='o', label='f(x)')
plt.axhline(y=mean_val, color='r', linestyle='--', label='Mean values')
plt.title("Graph of f(x)")
plt.xlabel('a')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
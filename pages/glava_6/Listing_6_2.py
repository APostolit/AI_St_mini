# Листинг 6.2
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker=".")
plt.xlabel('Подпись к оси X') # подпись оси х
plt.ylabel('Подпись к оси Y')  # подпись оси y
plt.show()
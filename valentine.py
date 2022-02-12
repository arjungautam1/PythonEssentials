import numpy as np
import matplotlib.pyplot as plt

x_coords = np.linspace(-200, 200, 600)
y_coords = np.linspace(-200, 200, 600)

heart_x = []
heart_y = []

for y in y_coords:
    for x in x_coords:
        if ((x * 0.01) ** 2 + (y * 0.01) ** 2 - 1) ** 3 - (x * 0.01) ** 2 * (y * 0.01) ** 3 <= 0:
            heart_x.append(x)
            heart_y.append(y)

plt.scatter(heart_x, heart_y, c="red")
plt.text(0.5, 0.5, "Happy Valentine's Day \n My Love", horizontalalignment="center", verticalalignment="center",
         color="white")
plt.axis("off")
plt.show()

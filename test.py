import matplotlib.pyplot as plt
import numpy as np

print("ok")
print("ok2")
#export DISPLAY=localhost:10.0

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Plot of sin(x)")
plt.show()

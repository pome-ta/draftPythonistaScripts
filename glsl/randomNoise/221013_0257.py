
import numpy as np
import matplotlib.pyplot as plt


def fract(x: float) -> float:
  return x - np.floor(x)


def fractSin11(x: float) -> float:
  return fract(1e3 * math.sin(x))



l = np.arange(0.0, 10.0, 0.001, dtype=np.float32)

plt.plot(np.sin(l * np.pi))
plt.show()

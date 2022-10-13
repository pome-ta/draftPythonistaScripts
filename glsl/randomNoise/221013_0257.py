import numpy as np
import matplotlib.pyplot as plt


def fract(x: float) -> float:
  return x - np.floor(x)


def fractSin11(x: float) -> float:
  return fract(1e3 * math.sin(x))


def view_plot(data):
  plt.plot(np.sin(l * np.pi))
  plt.show()

if __name__ == '__main__':
  q: float = 1e5
  #m: list = [math.sin((i / (n / 1e2)) * math.pi) for i in range(int(n))]
  lpy: list = [i / (q / 1e2) for i in range(int(q))]
  lnp = np.arange(0.0, 10.0, 0.001, dtype=np.float32)
  uint32 = lnp.astype(np.uint32)
  

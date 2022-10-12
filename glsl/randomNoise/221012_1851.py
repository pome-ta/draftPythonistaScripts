# ヒストグラム
# legacy
import math
import matplotlib.pyplot as plt


def fract(x: float) -> float:
  return x - math.floor(x)


def fractSin11(x: float) -> float:
  return fract(1e3 * math.sin(x))


n: float = 1e5
#m: list = [math.sin((i / (n / 1e2)) * math.pi) for i in range(int(n))]
l: list = [i / (n / 1e2) for i in range(int(n))]
m: list = [fractSin11(j) for j in l]

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.hist(m)
ax2.plot(m)

if __name__ == '__main__':
  plt.tight_layout()
  plt.show()


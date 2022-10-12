# ヒストグラム
# hash1d
import math
import matplotlib.pyplot as plt


def fract(x: float) -> float:
  return x - math.floor(x)


def fractSin11(x: float) -> float:
  return fract(1e3 * math.sin(x))


def uhash11(n):
  n ^= (n << 1)  # 1 左シフトして XOR
  n ^= (n >> 1)  # 1 右シフトして XOR
  n *= k  # 算術積
  n ^= (n << 1)  # 1 左シフトして XOR
  return n * k  # 算術積


def hash11(p):
  n = p
  #return uhash11(n) / UINT_MAX


k: int = 0x456789ab  # 算術積に使う大きな桁数の定数
UINT_MAX: int = 0xffff_ffff  # 符号なし整数の最大値

q: float = 1e5
#m: list = [math.sin((i / (n / 1e2)) * math.pi) for i in range(int(n))]
l: list = [i / (q / 1e2) for i in range(int(q))]
m: list = [hash11(j) for j in l]

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.hist(m)
ax2.plot(m)

if __name__ == '__main__':
  plt.tight_layout()
  plt.show()


import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core import util

# Mencetak plot random
# import matplotlib.pyplot as plt
# import numpy as np

# med = []
# for i in range(1000):
#     data = [util.random() for i in range(0,10000)]
#     med.append(np.average(data))

# plt.scatter(list(range(0,1000)),med)
# plt.savefig("random.png")

# Mencetak tiga bilangan
print(util.random())
print(util.random())
print(util.random())
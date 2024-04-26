import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use("seaborn-v0_8-whitegrid")

import numpy as np

a = np.random.normal(size=50)
#plt.plot(a)
#plt.show()

x = np.linspace(0, 10, 100)

plt.plot(x, np.cos(x), marker="*", color="b")
plt.plot(x, np.sin(x), marker="o", color="r")
#plt.show()

# creiamo una figura con due pannelli
# La funzione restiruisce due riferimenti all'oggetto figure e all'oggetto axes

fig, ax = plt.subplots(2)

# usiamo il riferimento ad axes per i plot
ax[0].plot(x, np.cos(x), marker="*", color="b")
ax[0].plot(x, np.tan(x), marker=".", color="g")
ax[1].plot(x, np.sin(x), marker="o", color="r")
plt.show()

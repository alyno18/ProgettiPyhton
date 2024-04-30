import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use("seaborn-v0_8-whitegrid")

import numpy as np

a = np.random.normal(size=50)
# plt.plot(a)
# plt.show()

x = np.linspace(0, 10, 40)
ax = plt.axes()
ax.plot(x, np.cos(x), marker="o", linestyle="None", color="r", label="coseno")
ax.set(title="Funzione coseno", xlabel="x", ylabel="cos(x)", xlim=(0, 10), ylim=(-2, 2))
ax.legend()

# plt.plot(x, np.cos(x), marker="*", color="b", label="coseno", linestyle="-")
# plt.plot(x, np.sin(x), marker="o", color="r", label="tangente")
# plt.title("Coseno e tangente")
# plt.xlabel("x")
# plt.ylabel("cos(x) e tan(x)")
# plt.legend()

plt.show()


# creiamo una figura con due pannelli
# La funzione restiruisce due riferimenti all'oggetto figure e all'oggetto axes

# fig, ax = plt.subplots(2)

# usiamo il riferimento ad axes per i plot
# ax[0].plot(x, np.cos(x), marker="*", color="b")
# ax[0].plot(x, np.tan(x), marker=".", color="g")
# ax[1].plot(x, np.sin(x), marker="o", color="r")
# plt.show()


rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000*rng.rand(100)
plt.scatter(x, y, c=colors,s=sizes, alpha=0.3, cmap="viridis")
plt.colorbar()
plt.show()


def f(x, y):
    return np.sin(x)**5 + np.cos(3+y*x)*np.cos(x)


x1 = np.linspace(-5, 5, 50)
y1 = np.linspace(-5, 5, 50)
X1, Y1 = np.meshgrid(x1, y1)
Z1 = f(X1, Y1)

fig, ax = plt.subplots(1)
contour_img = ax.contour(X1, Y1, Z1, cmap="RdGy")
ax.clabel(contour_img, inline=True, fontsize=8)
fig.colorbar(contour_img, ax=ax)
plt.show()


mean = [0, 0]
cov = [[1, 1], [1, 2]]
x2, y2, = np.random.multivariate_normal(mean, cov, 1000000).T
fig, ax = plt.subplots(1)

hist2d, sedges, yedges, hist_image = ax.hist2d(x2, y2, cmap="Blues", alpha=0.9, density=True, bins=256)
fig.colorbar(hist_image, ax=ax)
plt.show()


fig = plt.figure()
ax = plt.axes(projection="3d")

zline = 2*np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, "gray")

zdata = 2*15 * np.random.random(1000)
xdata = np.cos(zdata) + 0.1*np.random.random(1000)
ydata = np.sin(zdata) + 0.1*np.random.random(1000)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap="Greens")

plt.show()


fig = plt.figure()
ax = plt.axes(projection="3d")


def f3(x, y):
    return x**2 + y**2


x3 = np.linspace(-6, 6, 40)
y3 = np.linspace(-6, 6, 40)
X3, Y3 = np.meshgrid(x3, y3)
Z3 = f3(X3, Y3)
ax.contour3D(X3, Y3, Z3, 50, cmap="binary")

plt.show()


import seaborn as sea
sea.set()

iris = sea.load_dataset("iris")
print(iris.head)
sea.pairplot(iris, hue="species", height=2.5)
sea.boxplot(iris, x="species", y="sepal_length")

plt.show()

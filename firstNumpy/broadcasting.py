import numpy as np

a = np.array([1, 2, 3])
print("shape di a: ", a.shape)
b = np.array([[1, 2, 3], [4, 5, 6]])
print("shape di b: ", b.shape)
c = a + b
print(c)
print("shape di c: ", c.shape)

d = np.zeros(shape=(2, 1, 1))
e = np.ones(shape=(2, 3, 4))
f = d + e
print("f: ", f)
print("shape di f: ", f.shape)

x = np.arange(4)
y = np.arange(4)

xx, yy = np.meshgrid(x, y)
print(xx)
print(yy)


def f(x, y):            # funzione che implementa z = f(x, y) = x^2 + y
    return x**2+y


print(f(xx, yy))


a1 = np.array([0, 0, 1, 1])
b1 = np.array([1, 1, 0, 0])
print("a1 dot a1: ", np.dot(a1, a1))
print("a1 dot b1: ", np.dot(a1, b1))
print("b1 dot b1: ", np.dot(b1, b1))

c1 = 2 * np.diag(np.ones(4))
print("c1 dot a1: ", np.dot(c1, a1))
print("c1 dot b1: ", np.dot(c1, b1))

d1 = np.ones(shape=(4, 4))
print("c1 dot d1: ", np.dot(c1, d1))

A = np.random.normal(size=(4, 4))
eigenvalues, eigenvectors = np.linalg.eig(A)
print("autovalori: ", eigenvalues)
print("autovettori: ", eigenvectors)
print("determinante di A: ", np.linalg.det(A))
print("inversa di A: ", np.linalg.inv(A))

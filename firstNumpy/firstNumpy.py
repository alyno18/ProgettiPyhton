import numpy as np

a = np.array([1, 2, 3, 4])
lista1 = [1, 2, 3, 4]
tupla1 = (1, 2, 3, 4)
b = np.array(lista1)
c = np.array(tupla1)
a1 = np.zeros(shape=(3, 3))
print("a1:\n", a1)
b1 = np.ones(shape=(2, 2))
print("b1:\n", b1)
c1 = np.diag(b1)
print("c1:\n", c1)
d1 = np.empty(shape=(3, 3))
print("d1:\n", d1)
e1 = np.eye(4) #np.identity
print("e1:\n", e1)

import numpy as np

a = np.array([1, 2, 3, 4])
lista1 = [1, 2, 3, 4]
tupla1 = (1, 2, 3, 4)

b = np.array(lista1)
c = np.array(tupla1)

a1 = np.zeros(shape=(3, 3))
print("a1: ", a1)
print("Size di a1:", a1.size)
print("Shape di a1:", a1.shape)
print("Data type di a1:", a1.dtype)

b1 = np.ones(shape=(3, 3), dtype=np.float64)
print("b1:\n", b1)
print("Size di b1:", b1.size)
print("Shape di b1:", b1.shape)
print("Data type di b1:", b1.dtype)

c1 = np.diag(b1)
print("c1:\n", c1)
print("Size di c1:", c1.size)
print("Shape di c1:", c1.shape)
print("Data type di c1:", c1.dtype)

d1 = np.empty(shape=(3, 3))
print("d1:\n", d1)
print("Size di d1:", d1.size)
print("Shape di d1:", d1.shape)
print("Data type di d1:", d1.dtype)

e1 = np.eye(4) #np.identity
print("e1:\n", e1)
print("Size di e1:", e1.size)
print("Shape di e1:", e1.shape)
print("Data type di e1:", e1.dtype)

print("-----------------------------------------------------------------------")

print(np.arange(start=10, stop=50, step=10))

print(np.arange(start=10.0, stop=11.0, step=0.1))

print(np.linspace(start=10, stop=50, num=10))

print(np.diag(np.arange(6)))

print("-----------------------------------------------------------------------")

print(np.random.uniform(low=0.0, high=10.0, size=(3, 3)))

print(np.random.normal(loc=0.0, scale=10.0, size=(3, 3)))

print(np.random.randint(low=0, high=10, size=(3, 3)))

print("-----------------------------------------------------------------------")

d = np.arange(9)
e = d.reshape(3, 3)
print("d:\n", d)
print("e:\n", e)

f = e.ravel()
print("f:\n", f)

print("-----------------------------------------------------------------------")

tensor_1 = np.random.normal(loc=1.0, scale=2.0, size=(2, 3, 3))
print("tensor_1:\n", tensor_1)
print("tensor_1(ravel):\n", tensor_1.ravel())


a11 = np.random.uniform(size=(3, 3))
a11_vec = a11.ravel()
print("a1:\n", a11)
print("Size di a11:", a11.size)
print("Shape di a11:", a11.shape)
print("Data type di a11:", a11.dtype)

print("primo for a11:")
for el in a11_vec:
    print(el)

print("secondo for a11:")
for i in range(a11_vec.size):
    print(a11[1])

print("terzo for a11:")
for el in a11:
    print("el: ", el)

print("-----------------------------------------------------------------------")

a22 = np.random.uniform(size=(2, 3, 4))
print(a22)
for el1 in a22:
    for el2 in el1:
        print("el2: ", el2)

list1 = [
    [1, 2, 3],
    [3, 4, 5]
]

print("-----------------------------------------------------------------------")

print(list1[0][1])
print("a22:\n", a22)
print("singolo elemento: ", a22[0, 2, 1])
a22[0, 2, 1] = 0.0
print("a22 modificato:\n", a22)
print("più elementi: ", a22[0, 2, 0:2])

print("-----------------------------------------------------------------------")

a23 = np.random.normal(size=(3, 3))
print("a23 prima slicing:\n", a23)
b23 = a23[:, 0:2]
print("b23:\n", b23)
b23[0, 0] = 0.0
print("a23 dopo slicing:\n", a23)
print("b23:\n", b23)

print("-----------------------------------------------------------------------")

a33 = np.ones(shape=(3000, 3000))
b33 = np.ones(shape=(3000, 3000))+2
print("a33:\n", a33)
print("a44:\n", b33)
print("somma:\n", a33+b33)
print("pre modifica:\n", a33 == b33)
b33[0, 0] = 1.0
print("dopo modifica:\n", a33 == b33)
print(np.array_equal(a33, b33))

print("-----------------------------------------------------------------------")

import time
start = time.time()
c33 = a33+b33
stop = time.time()
print("tempo di a33+a44: ", stop - start)

result = np.empty(shape=(3000, 3000))
start1 = time.time()
for i in range(3000):
    for j in range(b33[i].size):
        result[i, j] = a33[i, j] + b33[i, j]

stop1 = time.time()
print("tempo di a33+a44 con for: ", stop1 - start1)

print("-----------------------------------------------------------------------")

a44 = np.random.normal(loc=0.0, scale=10.0, size=(3, 3))
print(a44.sum())
print(a44.mean())
print(a44.sum(axis=1))

print("-----------------------------------------------------------------------")

a55 = np.random.normal(loc=0.0, scale=10.0, size=(2,2))
a55[1][1] = 20.0
print("a66:\n", a55)
b55 = np.random.normal(loc=0.0, scale=10.0, size=(2))
b55[1] = 10.0
print("b66:\n", b55)
print("somma:\n", a55+b55)

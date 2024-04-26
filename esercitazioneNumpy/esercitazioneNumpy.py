import numpy as np


# 1. Creare un vettore di zero di dimensione 10
a = np.zeros(shape=(10,))
print("a: ", a)


# 2. Creare un vettore di dimensione 6 con valori a zero tranne per il quinto che è impostato a 1
b = np.zeros(shape=(6,))
b[4] = 1
b11 = np.array([0., 0., 0., 0., 1., 0.])
print("b: ", b)
print("b11: ", b11)


# 3. Creare un vettore con valori compresi tra 8 e 39 (inclusi)
c = np.arange(8, 40)
print("c: ", c)


# 4. Invertire l'ordine degli elementi di un vettore
d = np.flip(c)
d1 = c[::-1]
print("c reverse con flip: ", d)
print("c reverse con sliding: ", d1)


# 5. Creare un ndarray con valori [1,4,1,0,4,0] e trovare gli elementi non nulli
e = np.array([1, 4, 1, 0, 4, 0])
print(e[np.nonzero(e)])


# 6. Creare un ndarray 2x5x3 con valori casuali campionati da una distribuzione normale
f = np.random.normal(size=(2, 5, 3))
print("f: ", f)
# 7. Trovare il valore massimo, minimo e medio sull’array dell’esempio 6.
print("max: ", np.max(f))
print("min: ", np.min(f))
print("medio: ", np.mean(f))
# 8. Creare una matrice 10x10 e riempirla con un pattern a scacchiera (1, 0, 1, 0…)
g = np.zeros(shape=(10, 10), dtype=int)
g[1::2, ::2] = 1
g[::2, 1::2] = 1
print(g)
# 9. Moltiplicare una matrice 7x2 per una matrice 2x6
h = np.random.normal(size=(7, 2))
h1 = np.random.normal(size=(2, 6))
print("moltiplicazione matrice 7x2 per una matrice 2x6: ", np.dot(h, h1))
# alternativa con @
print("moltiplicazione matrice 7x2 per una matrice 2x6 alternativa con @: ", h @ h1)
# 10. Trovare i valori comuni tra due ndarray
a11 = np.array([1, 2, 3, 4, 5])
a12 = np.array([4, 5, 6, 7, 8])
print(np.intersect1d(a11, a12))
# 11. Calcolare ((A+B)\*(-A/2)), dove A e B sono ndarray
# 12. Dati due ndarray con valori random A e B, controllare se sono uguali
# 13. Creare un ndarray random di dimensione 10 e sostituire l'elemento con valore massimo con 0
# 14. Trovare il valore più vicino di un ndarray a uno scalare dato
# 15. Considerare un ndarray con valori random e shape (100,2) che rappresenta delle coordinate cartesiane, calcolare
# le distanze punto-punto
# 16. Sottrarre la media di ogni riga di un ndarrat a se stesso

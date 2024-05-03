import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sea

df = pd.read_csv("iris.data", names=["sepal_length",
                                     "sepal_width", "petal_length", "petal_width", "category"])

print(df.head())
iris_versicolor = df[df.category == "iris-versicolor"]
# sea.pairplot(iris_versicolor)
# plt.show()

serie = pd.Series(0.0, index=range(100))
print(serie)

months = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto"]
days = [31, 28, 31, 30, 31, 30, 31, 31]
s = pd.Series(days, index=months)
print(s)
print(s["febbraio"])
print("iloc prima della modifica: ", s.iloc[1])
s.iloc[1] = 29
print("iloc dopo la modifica: ", s.iloc[1])
print(s["gennaio":"marzo"])
print("head:\n", s.head(3))
print("tail:\n", s.tail(2))
print("operazioni matematiche")
print("s+5:\n", s+5)
print("s*3:\n", s*3)

index1 = ["a", "b", "c", "d"]
value1 = [1, 3, 4, 5]

index2 = ["a", "b", "c", "d"]
value2 = [10, 30, 40, 52]
s1 = pd.Series(value1, index=index1)
s2 = pd.Series(value2, index=index2)
print(s1+s2)


index = ["a", "b", "c", "d", "e", "f", "g", "h"]
value = [31, 28, 31, 30, 31, 30, 31, 31]
s3 = pd.Series(value, index=index)


def my_func(x, param):
    print("elemento della serie: ", x)
    return x**2 + param

print(s3.apply(my_func, args=(5, )))
s3.plot(color="pink")
plt.show()


index4 = range(50)
values4 = np.random.normal(size=(50, ))
s4 = pd.Series(values4, index=index4)
s4.plot(kind="box")
plt.show()


data = {
    "Jobs": pd.Series(["Engineer", "Doctor"], index=["first", "second"]),
    "Cities": pd.Series(["Rome", "Paris"], index=["second","third"])
}

df1 = pd.DataFrame(data)
print("df1: \n", df1)
print("index: ", df1.index)
print("columns: ", df1.columns)
print("shape: ", df1.shape)

data1 = {
    "column1": [2, 4, 5, 5, 7],
    "column2": [3, 3, 10, 3, 12]
}

df2 = pd.DataFrame(data1)
print("df2: \n", df2)
print("index: ", df2.index)
print("columns: ", df2.columns)
print("shape: ", df2.shape)

df3 = pd.DataFrame(data1, index=range(10, 15))
print("df3 (range(10, 15)): \n", df3)
print("index: ", df3.index)
print("columns: ", df3.columns)
print("shape: ", df3.shape)

print("--------------------------------------------------------------------------")


df4 = pd.read_csv("iris.data", header=None,
                  names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"])
print(df4.head())

sepal_col = df4["Sepal length"]
print("sepal_col: \n", sepal_col)
print("Sepal Length and Species: \n", df4[["Sepal length", "Species"]])
print("loc: \n", df4.loc[0])
print("iloc: \n", df4.iloc[0:6])

print("--------------------------------------------------------------------------")

pd.plotting.scatter_matrix(df4, alpha=0.7)
plt.show()

corr = df4.corr(numeric_only=True)
sea.heatmap(corr, annot=True)
plt.show()

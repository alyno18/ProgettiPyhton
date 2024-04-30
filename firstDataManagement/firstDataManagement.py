import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

df = pd.read_csv("iris.data", names=["sepal_length",
                                     "sepal_width", "petal_length", "petal_width", "category"])

print(df.head())
iris_versicolor = df[df.category == "iris-versicolor"]
sea.pairplot(iris_versicolor)
plt.show()


s = pd.Series(0.0, index=range(100))
print(s)


months = ["gennaio", "febbraio", "marzo", "aprile"]
days = [31, 28, 31, 30]
s = pd.Series(days, index=months)
print(s)
print(s["febbraio"])
print(s.iloc[1])
s.iloc[1] = 29
print(s.iloc[1])

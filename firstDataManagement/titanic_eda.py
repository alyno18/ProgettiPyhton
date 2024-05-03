import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sea


pd.set_option("display.expand_frame_repr", False)
df = pd.read_csv("train.csv")
print(df.head())
print(df.info())
print(df.describe())

sea.heatmap(df.isnull())
plt.show()

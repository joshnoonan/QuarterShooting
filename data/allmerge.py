import pandas as pd

a = pd.read_csv("all1718.csv")
b = pd.read_csv("all1819.csv")
merged = a.merge(b)
merged.to_csv("reg1719.csv")


import pandas as pd
df=pd.read_csv("../Data/titanic.csv")
print(df.info())
print(df.dtypes)
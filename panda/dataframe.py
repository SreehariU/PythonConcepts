import pandas as pd

#Creating dataframe
df=pd.DataFrame({"Name" :["Sreehari","Rahul","Aryan"],
                 "Age" :[18,19,20],
                 "branch" :["CSE","CSD","AI"]})
print(df["Name"])
print(df["Age"].max())
print(type(df))
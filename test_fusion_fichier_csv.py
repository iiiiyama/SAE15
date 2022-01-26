import pandas as pd

df = pd.concat(
    map(pd.read_csv, ['netflix-1.csv', 'netflix-2.csv','netflix-3.csv','netflix-4.csv','netflix-5.csv']), ignore_index=True)
print(df)
df.to_csv("test.csv")
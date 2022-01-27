import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv("test.csv")
compteur = 0
counter = 0
while True:
    compteur += 1
    try:
        for i in range (0, 11):
            read = pd.isnull(df.iloc[compteur, i])
            if read == True:
                compteur += 1
                counter += 1
            compteur += 1
    except IndexError:
        break
    except:
        compteur += 1
    compteur += 1

print(df.isnull().sum())
print("")
print("il y a", counter, "valeurs manquantes")
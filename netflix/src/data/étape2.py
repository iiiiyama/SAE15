import pandas as pd
import os

vmanquante = 0
vaberrante = 0
vmanquantecol = 0
counter = 0
dellist = []

os.chdir("../../output")

read = pd.read_csv('test.csv')

while True:
    counter += 1
    try:
        added : any = read.iloc[counter, 6]
        reversed: int = int(read.iloc[counter, 7])
        nothing, added = added.split(",")
        added = int(added)
    except IndexError :
        break
    except:
        dellist.append(counter)
        vmanquante += 1
        vmanquantecol += 1
    if added < reversed :
        vaberrante += 1
        print(added, reversed, f"--> valeur abérante ligne s{counter}")
        dellist.append(counter)
    for i in range (0, 11):
        cellcheck = pd.isnull(read.iloc[counter, i])
        if cellcheck == True:
            vmanquante += 1

read.drop(read.index[dellist], inplace=True)
read.to_csv('test_corrige.csv', index=False)

total = vaberrante + vmanquantecol

os.remove("test.csv")
calc = lambda x: x * 100/counter

print(f"nombre de valeur manquantes totales : {vmanquante}\n"
      f"pourcentage :  {calc(vmanquante):.2f}\n"
      f"nombre de valeurs  manquantes (colonne 6 et 7):{vmanquantecol}\n"
      f"pourcentage : {calc(vmanquantecol):.2f}\n"
      f"nombre de valeurs aberrantes (colonne 6 et 7):{vaberrante}\n"
      f"pourcentage : {calc(vaberrante):.2f}\n"
      f"total d'erreur (colonne 6 et 7):{total}\n"
      f"pourcentage d'erreur total : {calc(total):.3f}\n")

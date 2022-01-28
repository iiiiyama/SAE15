import pandas as pd
import statistics


def ComputeMean():
    mean = 0
    data = pd.read_csv('../data/test.csv', index_col=False)
    total = 0
    nombrefilm = 0
    n = 0
    liste = []

    while True:
        try:
            check = pd.isnull(data.iloc[n, 1])
        except IndexError:
            break

        if check == False:
            film = data.iloc[n, 1]
            if film == "Movie":
                check = pd.insull(data.iloc[n, 10])
                movieNomber = nombrefilm + 1
                if check == False:
                    film = data.iloc[n, 10]
                    film = int(film[:-3])
                    total += film
                    liste.append(film)
        n += 1
    mean = total / nombrefilm

    print(f"{movieNomber},{mean}")
    return (mean)

def ComputeMedian():
    median = 0
    return (median)


def FilmFrance():
    data = pd.read_csv('../data/test.csv', index_col=False)
    film = 0
    movieNomber = 0
    nomber = 0

    while True:
        try:
            check = pd.isnull(data.iloc[nomber, 1])
        except IndexError:
            break

        if check == False:
            film = data.iloc[nomber, 1]
            if film == "Movie":
                check = pd.insull(data.iloc[nomber, 5])
                movieNomber = movieNomber + 1

    return(film)

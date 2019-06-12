import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt
sns.set()

df=pd.read_csv('Z:\__naj\GAMES\gdp_data.csv')
# try index_col = 0
n = len(df)

def pick_countries(k):
    countries = {}
    while len(countries) < k:
        x = random.randint(0,n-1)
        if df["COUNTRY"][x] not in countries:
            countries[df["COUNTRY"][x]] = round(df.iloc[x][1],1)
    return countries

def declare_countries(countries):
    print()
    print('YOUR COUNTRIES ARE:')
    print()
    i = 1
    for country in countries:
        print('M' + str(i) + ': ' + country)
        i+=1


def main():
    print("###############################################")
    print("### WELCOME TO THE COUNTRY GDP TRADING GAME ###")
    print("### NB: ALL VALUES ARE IN BILLION USD ###")
    print()
    print("HOW MANY COUNTRIES DO YOU WANT TO TRADE?")
    print()
    k = int(input())
    countries = pick_countries(k)
    declare_countries(countries)
    print()
    print("ONCE YOU ARE HAPPY INPUT 'Y'. ENTER ANYTHING ELSE TO RE-ROLL.")
    print()
    while input()!="Y":
        countries = pick_countries(k)
        declare_countries(countries)
        print()
        print("ONCE YOU ARE HAPPY, INPUT 'Y'. ENTER ANYTHING ELSE TO RE-ROLL.")
        print()
    print()
    print("COMMENCE TRADING!")
    print()
    print("ENTER 'SETTLE' TO SETTLE WHEN YOU'RE READY")
    print()
    while input()!="SETTLE":
        pass
    #improve this below with a proper settlement procedure
    print()
    print(countries)


# NOW TRYING USING DATA FRAMES INSTEAD OF DICTIONARY!

def pick_countries2(k):
    countries = df.sample(k,replace=False)
    return countries

def declare_countries2(countries):
    print()
    print('YOUR COUNTRIES ARE:')
    print()
    i = 1
    for index, row in countries.iterrows():
        print('M' + str(i) + ': ' + row["COUNTRY"])
        i+=1

def main2():
    print()
    print("###############################################")
    print()
    print("WELCOME TO THE COUNTRY GDP TRADING GAME")
    print()
    print("NB: ALL VALUES ARE IN BILLION USD")

    print("NB: ALL VALUES ARE ROUNDED TO 1 DP")

    print("NB: ALL VALUES ARE AS OF 2017")
    print()
    print("###############################################")
    print()
    print("HOW MANY COUNTRIES DO YOU WANT TO TRADE?")
    print()
    k = int(input())
    countries = pick_countries2(k)
    declare_countries2(countries)
    print()
    print("ONCE YOU ARE HAPPY INPUT 'Y'. ENTER ANYTHING ELSE TO RE-ROLL.")
    print()
    while input()!="Y":
        countries = pick_countries2(k)
        declare_countries2(countries)
        print()
        print("ONCE YOU ARE HAPPY, INPUT 'Y'. ENTER ANYTHING ELSE TO RE-ROLL.")
        print()
    print()
    print("COMMENCE TRADING!")
    print()
    print("ENTER 'SETTLE' TO SETTLE WHEN YOU'RE READY")
    print()
    while input()!="SETTLE":
        pass
    #improve this below with a proper settlement procedure
    print()
    settle2(countries)


def settle2(countries):
    print()
    print('##### FLAT PRICE SETTLES #####')
    print()
    i = 1
    for index, row in countries.iterrows():
        print('M' + str(i) + ': ' + str(round(row["GDP_US_BN"],1)) + ' (' + row["COUNTRY"] + ')')
        i+=1
    print()
    print('##### SPREAD SETTLES #####')
    print()
    for i in range(1,len(countries)):
        for j in range(i+1,len(countries)+1):
            spd = round(countries.iloc[i-1]["GDP_US_BN"] - countries.iloc[j-1]["GDP_US_BN"],1)
            print('M' + str(i) + ' - M' + str(j) + ': ' + str(spd))
    print()
    print('##### STRIP SETTLES #####')
    print()
    print("FULL STRIP: " + str(round(countries['GDP_US_BN'].mean(),1)))
    print()
    sns.barplot(x="COUNTRY",y="GDP_US_BN",data=countries)
    plt.show()


main2()


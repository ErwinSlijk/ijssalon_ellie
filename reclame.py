from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting:.2f} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

print()

def inkomsten_totaal(inkomsten):
    totaal = inkomsten
    bedrag = totaal / 100 * 9
    print (f"Het totaal van alle inkomsten van deze week is {totaal} euro, ")
    print (f"waarover {bedrag} euro btw betaald dient te worden.")
inkomsten_totaal(220 + 430 + 125 + 160 + 205 + 90 + 345)

print()

mijn_lijst_2 = [220, 430, 125, 160, 205, 90, 345]
def laag_en_hoog(mijn_lijst):
    max_num = max(mijn_lijst_2)
    min_num = min(mijn_lijst_2)
    print(f"Op een topdag verdiende we {max_num:.2f} euro")
    print(f"Op de slechste dag verdiende we {min_num:.2f} euro")
laag_en_hoog(mijn_lijst_2)

print()

def gemiddelde(mijn_lijst):
    inkomsten = mijn_lijst
    bedrag = inkomsten / 7
    print (f"De gemiddelde inkomsten deze week zijn {bedrag:.2f} euro.")
gemiddelde(220 + 430 + 125 + 160 + 205 + 90 + 345)

print()

mijn_lijst_3 = [10, 5, 3, 2, 1, 2, 9]
def meervoudig(invoer_lijst):
    max_num = max(invoer_lijst)
    min_num = min(invoer_lijst)
    print(f"De hoogste waarde is {max_num}")
    print(f"De laagste waarde is {min_num}")
meervoudig(mijn_lijst_3)

print()

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

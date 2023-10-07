from helper import *

mijn_dict = {
    "vis" : 10,
    "vlees" : 25,
    "overig" : 15
}

def presenteer():
    for k, v in mijn_dict.items():
        print (f"{k} : {v} euro")
presenteer()

print(26 * "=")

totaal_inkomsten = som(mijn_dict)
print(f"totaal : {totaal_inkomsten}")

print()
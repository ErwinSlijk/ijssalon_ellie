def mijn_functie_1(a, b, c, d): 
    return a * a, b * b, c * c, d * d
print(mijn_functie_1(2, 4, 10, 12))

print()

def mijn_functie_2(a, b, c, d):
    lijst_1 = [a + 2.7, a - 3.3, a + 23.7, a - 8.3]
    string_list = list(map(int, lijst_1))
    print(string_list)
    lijst_2 = [b + 1.8, b - 2.2, b + 11.8, b - 5.2]
    string_list = list(map(int, lijst_2))
    print(string_list)
    lijst_3 = [c + 4.5, c - 5.5, c + 39.5, c - 8.5]
    string_list = list(map(int, lijst_3))
    print(string_list)
    lijst_4 = [d + 19.80, d - 20.20, d + 1899.80, d - 95.15]
    string_list = list(map(int, lijst_4))
    print(string_list)
mijn_functie_2(12.3, 12.2, 10.5, 100.20)

print()
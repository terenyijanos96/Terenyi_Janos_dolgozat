import random


def beker():
    i = 1
    lista = []
    while i <= 3:
        szam = int(input(f"Kérem az {i}. páros számot! "))
        while szam % 2 != 0:
            szam = int(input(f"Ez nem PÁROS! Kérem az {i}. páros számot! "))
        lista.append(szam)

        i += 1

    return lista


def legkisebb(lista):
    i = 1
    minimum = lista[0]
    min_index = 0
    while i < len(lista):
        if lista[i] < minimum:
            minimum = lista[i]
            min_index = i
        i += 1
    print(f"{min_index + 1}. lépésben adta meg a legkisebb páros számot, melynek értéke: {minimum}", end="\n\n")


def veletlen_generator():
    lista = []
    i = 0
    while i < 13:
        veletlen = int(random.random() * 191) - 40
        lista.append(veletlen)
        i += 1

    print(f"2. a) A lista: {lista}")

    return lista


def ketjegyuek_szama(lista):
    i = 0
    c = 0
    while i < len(lista):
        if (10 <= lista[i] <= 99) or (-10 >= lista[i] >= -99):
            c += 1
        i += 1

    print(f"2. b) A kétjegyű számok száma: {c}")
    return c


def paros_osszege(lista):
    osszeg = 0
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            osszeg += lista[i]
        i += 1

    return osszeg


def paratlan_osszege(lista):
    osszeg = 0
    i = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            osszeg += lista[i]
        i += 1

    return osszeg


def paros_vagy_paratlan_osszege_nagyobb(paros, paratlan):
    if paros > paratlan:
        print(f"2. e) A párosok összege {paros} > a páratlanok összege {paratlan}", end="\n\n")
    elif paratlan > paros:
        print(f"2. e) A páratlanok összege {paratlan} > a párosok összege {paros}", end="\n\n")
    else:
        print(f"2. e) A párosok és a páratlanok összege egyenlő! {paros}", end="\n\n")


def stadionok_beolvasasa():
    nevek = []
    helyszin = []
    hanyas = []
    eloszor = []
    utoljara = []

    f = open("stadionok.txt", "r", encoding="utf-8")
    tartalom = f.readlines()

    i = 1
    while i < len(tartalom):
        lista = tartalom[i].strip().split(";")
        nevek.append(lista[0])
        helyszin.append(lista[1])
        hanyas.append(lista[2])
        eloszor.append(lista[3])
        utoljara.append(lista[4])
        i += 1

    f.close()
    return nevek, helyszin, hanyas, eloszor, utoljara


def csapatok_darabja(hanyas):
    osszeg = 0
    i = 0
    while i < len(hanyas):
        osszeg += int(hanyas[i])
        i += 1

    print(f"A csapatok darabszáma: {osszeg}", end="\n\n")

def new_yorki_csapatok(nevek, helyszin, hanyas):
    i = 0
    while i < len(helyszin):
        if helyszin[i] == "New York":
            print(f"Stadion neve: {nevek[i]}; csapatok száma: {hanyas[i]}")
        i+=1


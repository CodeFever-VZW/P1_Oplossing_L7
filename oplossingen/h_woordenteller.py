def lees_tekst():
    return input("Voer een tekst in: ")


def tel_woorden(tekst):
    woorden = tekst.split()
    woord_frequentie = {}

    for woord in woorden:
        if woord in woord_frequentie:
            woord_frequentie[woord] += 1
        else:
            woord_frequentie[woord] = 1

    return woord_frequentie


def toon_resultaat(frequenties):
    print("Woordfrequenties:")
    for woord, frequentie in frequenties.items():
        print(f"{woord}: {frequentie}")


def vraag_tekst_en_tel_woorden():
    tekst = lees_tekst()
    frequenties = tel_woorden(tekst)
    toon_resultaat(frequenties)


vraag_tekst_en_tel_woorden()
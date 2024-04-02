import random

def betoverde_dieren():
    dieren = {
        "Vuurdraak": "ademt vuur",
        "Waterelf": "beheerst water",
        "Luchthond": "kan vliegen"
    }

    print("Welkom in het Betoverde Bos!")
    print("In dit magische bos leven verschillende betoverde dieren met speciale krachten.")

    while True:
        print("\nWat wil je doen?")
        print("1. Bekijk betoverde dieren")
        print("2. Voeg een nieuw betoverd dier toe")
        print("3. Stoppen")

        keuze = input("Voer het nummer van je keuze in: ")

        if keuze == "1":
            toon_betoverde_dieren(dieren)
        elif keuze == "2":
            voeg_nieuw_dier_toe(dieren)
        elif keuze == "3":
            print("Bedankt voor het verkennen van het Betoverde Bos!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

def toon_betoverde_dieren(dieren):
    print("\nBetoverde dieren in het bos:")
    for dier, kracht in dieren.items():
        print(f"{dier}: {kracht}")

def voeg_nieuw_dier_toe(dieren):
    nieuw_dier = input("Voeg een nieuw betoverd dier toe: ")
    nieuwe_kracht = input(f"Wat is de kracht van {nieuw_dier}? ")

    dieren[nieuw_dier] = nieuwe_kracht

    print(f"Je hebt succesvol een nieuw betoverd dier '{nieuw_dier}' met kracht '{nieuwe_kracht}' toegevoegd!")

betoverde_dieren()
# Het woordenboek met Nederlandse woorden en hun Engelse vertalingen
woordenboek = {
    "hond": "dog",
    "kat": "cat",
    "huis": "house",
    "boom": "tree",
    "auto": "car"
}

# Vraag de gebruiker om een Nederlands woord in te voeren
woord = input("Voer een Nederlands woord in: ")

# Zoek het woord op in het woordenboek en druk de Engelse vertaling af
if woord in woordenboek:
    print(f"De Engelse vertaling van '{woord}' is '{woordenboek[woord]}'")
else:
    print("Dit woord staat niet in het woordenboek.")
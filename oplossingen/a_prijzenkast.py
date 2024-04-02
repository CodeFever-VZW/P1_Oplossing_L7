prijzenkast = ("knuffelbeer", "gameconsole", "fiets")

print("Welkom bij de prijzenkast van de tv-show!")
print("Achter één van de dozen staat een verrassing. Kies doos 1, 2 of 3 en ontdek wat je gewonnen hebt!\n")

print("1. Doos 1")
print("2. Doos 2")
print("3. Doos 3")

nummer = int(input("\nGeef het nummer van de doos waar je op wilt drukken (1, 2 of 3): "))

if nummer in (1, 2, 3):
    gewonnen_voorwerp = prijzenkast[nummer - 1]
    print("Gefeliciteerd! Je hebt gewonnen: ", gewonnen_voorwerp)
else:
    print("Ongeldig nummer. Kies een nummer tussen 1 en 3.")
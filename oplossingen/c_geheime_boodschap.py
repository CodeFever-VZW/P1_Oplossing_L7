geheime_boodschap = (5, 0, 17, 19, 18, 26, 0, 17, 4, 26, 2, 14, 12, 8, 13, 6, 27)
alfabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '.', '?')

# Ontcijfer de geheime boodschap en print het volledige bericht
bericht = ""
for getal in geheime_boodschap:
    bericht += alfabet[getal]

# Schrijf jouw code hier!

print("Ontcijferde geheime boodschap:")
print(bericht)
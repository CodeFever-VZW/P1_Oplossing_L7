geheime_boodschap = (19, 8, 9, 3, 26, 21, 14, 14, 17, 26, 3, 8, 2, 19, 8, 14, 13, 0, 17, 8, 4, 18, 27)
alfabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '.', '?')

# Ontcijfer de geheime boodschap en print het volledige bericht
bericht = ""
for getal in geheime_boodschap:
    bericht += alfabet[getal]

# Schrijf jouw code hier!

print("Ontcijferde geheime boodschap:")
print(bericht)
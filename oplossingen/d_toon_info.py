persoonsdata = {
	"Naam": "John",
	"Leeftijd": "25",
	"Favoriete kleur": "blauw"
}

zin = persoonsdata["Naam"] + " is " + persoonsdata["Leeftijd"] + " jaar oud en zijn favoriete kleur is: " + persoonsdata["Favoriete kleur"]
print(zin)

print(f"{persoonsdata['Naam']} is {persoonsdata['Leeftijd']} jaar oud en zijn favoriete kleur is: {persoonsdata['Favoriete kleur']}")
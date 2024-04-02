contacten = {
	"Jan": "1234567890",
	"Alice": "9876543210",
	"Bob": "5555555555",
	"Emma": "1111111111",
	"Michael": "2222222222"
}

def welkom():
   print("Welkom bij de Telefoonboek App!")

def vraag_naam():
   return input("Voer een naam in (of 'stop' om te stoppen): ")

def toon_telefoonnummer(naam, contacten):
   if naam in contacten:
       telefoonnummer = contacten[naam]
       print("Telefoonnummer van " + naam + ": " + telefoonnummer)
   else:
       voeg_telefoonnummer_toe(naam, contacten)

def voeg_telefoonnummer_toe(naam, contacten):
    contacten[naam] = input("Voer het telefoonnummer in: ")
    print(f"Telefoonnummer van {naam} is toegevoegd.")

def raadpleeg_telefoonboek(contacten):
   welkom()
   wil_doorgaan = True
   while wil_doorgaan:
       naam = vraag_naam()
       if naam == "stop":
           wil_doorgaan = False
       else:
           toon_telefoonnummer(naam, contacten)

raadpleeg_telefoonboek(contacten)
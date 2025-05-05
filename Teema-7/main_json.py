import json

andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
json_string = json.dumps(andmed, indent=2, sort_keys=True) #formateerimine (file, indent=2, sort_keys=True)
print(json_string)

#Lisame failisse
with open("Teema-7//Andmet.json", 'w') as f:
    json.dump(andmed, f)

#Loeme JSON failist
with open("Teema-7//Andmet.json", 'r') as f:
    andmed_failist = json.load(f)
print(andmed_failist)

klass = {
"opetaja": "Tamm",
"opilased": [
{"nimi": "Mari", "hinne": 5},
{"nimi": "Juri", "hinne": 4}
] }
with open("Teema-7//klass.json", "w") as f:
    json.dump(klass, f, indent=2)

#Ülesanne
import requests

linn = input("Sisesta linna nimi: ")
api_voti = ""
url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&lang=et"
vastus = requests.get(url)
andmed = vastus.json()
if andmed.get("cod") != "404" and "main" in andmed and "weather" in andmed:
    peamine = andmed["main"]
    temperatuur = peamine["temp"]
    niiskus = peamine["humidity"]
    kirjeldus = andmed["weather"][0]["description"]
    tuul = andmed["wind"]["speed"]
    print(f"\nIlm linnas {linn}:")
    print(f"Temperatuur: {temperatuur}°C")
    print(f"Kirjeldus: {kirjeldus.capitalize()}")
    print(f"Niiskus: {niiskus}%")
    print(f"Tuule kiirus: {tuul} m/s")
else:
    print("Linna ei leitud. Palun kontrolli nime õigekirja.")
with open("Teema-7//ilm.json", "w", encoding="utf-8") as f:
    json.dump(andmed, f, ensure_ascii=False, indent=4)


#keerulised andmed
with open("Teema-7//andmed_keerulised.json", "r", encoding="utf-8") as f:
    andmed = json.load(f)

sisestatud_nimi = input("Nimi: ")

if andmed.get("nimi", "Võti ei ole!") == sisestatud_nimi:
    print(f"\nAutod kasutajal {sisestatud_nimi}:")
    for auto in andmed.get("autod", []):
        print(f"- {auto['muudel']} ({auto['varv']}, {auto['joud']} hj), number: {auto['number']}")
else:
    print("Sellega nimega kasutajat ei leitud!")


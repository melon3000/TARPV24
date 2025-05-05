#-----------------------
#MILAN PETROVSKI TARPV24 



import math
from random import *

#-----------------------
#1
print("Tere maailm!")
nimi = input("Mis on sinu nimi? ").capitalize()
print(f"Tere maailm!, Tervitan sind {nimi}!")
vanus=int(input("Kui vana sa oled? "))
print(f"Tere maailm!, Tervitan sind {nimi}! sa oled {vanus} aastat vana.")


#-----------------------
#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16
kas_käib_kooli = True
print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja {eesnimi} on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuja {kas_käib_kooli} on {type(kas_käib_kooli)}")


#-----------------------
#3
kommide_arv=randint(10,100)
print(f"Laua peal on {kommide_arv} kommid")
mitu=int(input("Mitu tahad süüja? "))
print(f"Laua peal on jäänud {kommide_arv - mitu}")


#-----------------------
#4
pikkus = float(input("Sisestage puu pikkus: "))
diaameter = pikkus / 3.14
diaameter = round(diaameter, 1)
print(diaameter)


#-----------------------
#5
M = int(input("Sisestage maatukki pikkus (m): "))
N = int(input("Sisestage maatukki laius (m): "))
c = round(math.sqrt(M**2 + N**2), 1)
print(f"Diagonaal on ~ {c} meetrid")


#-----------------------
#6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
kiirus = round(kiirus, 1)
print(f"Sinu kiirus oli ~ {kiirus} km/h")


#-----------------------
#7
int1 = int(input("Sisestage arv 1 "))
int2 = int(input("Sisestage arv 2 "))
int3 = int(input("Sisestage arv 3 "))
int4 = int(input("Sisestage arv 4 "))
int5 = int(input("Sisestage arv 5 "))

keskmine = (int1 + int2 + int3 + int4 + int5) / 5
print(f"Keskmine on {keskmine} arv!")


#-----------------------
#8
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print("  ^^ "" ^^  ")


#-----------------------
#9
aaa = float(input("Sisestage kolmnurga a: "))
bbb = float(input("Sisestage kolmnurga b: "))
ccc = float(input("Sisestage kolmnurga c: "))
p = (aaa+bbb+ccc)
print(f"Teie kolmnurga umbermood on {p}")


#-----------------------
#10
komissioon = 0.1
phind = float(input("Sisestage pitsa hind: "))
maksa = (phind + phind*komissioon) / 2
print(f"Sina ja sober peab maksma {maksa} euro")
#-----------------------
#MILAN PETROVSKI TARPV24


from datetime import *
from calendar import *
import math

tana = date.today() #datetime
print(f"Tere! Täna on {tana}")

# 27/12/2022
tana_ = tana.strftime("%d/%m/%Y")
print(f"Tere! Täna on {tana_}")

# # December 27, 2022
# tana_ = tana.strftime("%B %d, %y")
# print(f"Tere! Täna on {tana_}")

# # 12/27/22
# tana = tana.strftime("%m/%d/%y")
# print(f"Tere! Täna on {tana}")

# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
# print(f"Tere! Täna on {tana}")


#-----------------------
#ÜL 1
print("\n-----ÜL1-----")

paevadekogus = monthrange(2025, 1)[1]
print(f"Jaanuaris on {paevadekogus} päeva!")

paevad = tana.day
onjaanud = paevadekogus - paevad
print(f"Jaanuaris on jaanud {onjaanud} päeva!")

aastatoday = int(tana.strftime("%Y"))
aastalopuni = 365 - monthrange(aastatoday,1)[1] + onjaanud
print(f"Aasta lõpuni on jaanud {aastalopuni} päeva!")


#-----------------------
#ÜL 2
print("\n-----ÜL2-----")

arvutus1 = 3 + 8 / (4 - 2) * 4
print(f"sulgudega = {arvutus1}")
arvutus1 = 3 + 8 / 4 - 2 * 4
print(f"sulgudeta = {arvutus1}")


#-----------------------
#ÜL 3
print("\n-----ÜL3-----")

try:
    Raadius = float(input("Sisestage Raadius: "))
    Pindala_Ruut = round(math.sqrt(2*Raadius), 2)
    Pindala_Ring = round(math.pi * math.sqrt(Raadius), 2)
    umbermõõt_ruut = round(8 * Raadius, 2)
    umbermõõt_ring = round(2 * math.pi * Raadius, 2)
    print(f"\nRuudu pindala   = {Pindala_Ruut} | Ringi pindala   = {Pindala_Ring}")
    print(f"Ruudu ümbermõõt = {Pindala_Ruut} | Ringi ümbermõõt = {umbermõõt_ring}")
except:
    print("Sisesta ujukomaarud!")


#-----------------------
#ÜL4
print("\n-----ÜL4-----")

d = 2.575 #mündi d sm
maaR = 6378 #maa raadius km
maaR *= 100000 #maa radius sm
Pmaa = 2 * math.pi * maaR #maa umbermõõt
kogus = Pmaa / d
eur = kogus * 2

print(f"Maa ekvaatori ümbermõõt on {Pmaa} km.")
print(f"Selle katmiseks läheks vaja umbes {int(kogus): ,d} 2 euro mündi.")
print(f"See maksab {int(eur): ,d}  euro.")


#-----------------------
#ÜL5
print("\n-----ÜL5-----")

a ="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2, b, a*2, b, a*4)


#-----------------------
#ÜL6
print("\n-----ÜL6-----")

laulusonad_1 = """Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?"""

laulusonad_2 = """Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""

print(laulusonad_1.upper())
print()
print(laulusonad_2.upper())


#-----------------------
#ÜL7
print("\n-----ÜL7-----")
try:
    pikkus = float(input("Sisesta ristküliku pikkus: "))
    laius = float(input("Sisesta ristküliku laius: "))
    if pikkus > 0 and laius > 0:
        print("Pindala ja ümbermõõdu arvutamine: ")
        umermood = 2 * (pikkus + laius)
        pindala = pikkus * laius
        print(f"Ristküliku ümbermõõt on {umermood}")
        print(f"Ristküliku pindala on {pindala}")
    else:
        print("Arvud peavad olema suurem kui 0!")
except ValueError:
    print("Sisesta ujukomaarud!")


#-----------------------
#ÜL8
print("\n-----ÜL8-----")

try:
    benz = float(input("Sisestage tangitud kütuse liitrid: "))
    kmläbi = float(input("Sisestage läbitud kilomeetrid: "))
    if benz > 0 and kmläbi < 1:
        print("Teil on auk bensiinipaagis.")
    else:
        keskmine_rais = (benz / kmläbi) * 100

        print(f"Teie keskmine rais on {keskmine_rais} L, 100km kohta. ")
except:
    print("Sisestage ainult arvud / ujukomaarvud ")


#-----------------------
#ÜL9
print("\n-----ÜL9-----")

try:
    kiirus = 29.9
    MINS = float(input("Sisestage aeg minutites (M): "))

    if MINS > 0:
        kaugus = round(kiirus * (MINS / 60), 2)
        print(f"Rulluisutaja jõuab {kaugus} km {MINS} minutiga.")
    else:
        print("Aeg peab olema positiivne arv!")
except:
    print("Palun sisestage ainult arvud!")


#-----------------------
#ÜL10
print("\n-----ÜL10-----")

try:
    MINS2 = int(input("Sisestage aeg minutites (M): "))
    if MINS2 > 0:
        tundid = MINS2 // 60
        minutid = MINS2 % 60
        print(f"Aeg on {tundid}:{minutid}")
    else:
        print("Aeg peab olema positiivne arv!")
except:
    print("Palun sisestage õiged arvud!") 
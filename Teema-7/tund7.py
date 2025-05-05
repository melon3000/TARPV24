"""#Tekst failist salvestame järjendisse
def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

#Järjendite elemendid salvestame failisse
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()
    return jarjend

list_=Loe_failist("bob.txt")
for x in list_:
    print(x)

list_=["Ann","Kati","Mari"]
Kirjuta_failisse("bob.txt", list_)
list2_= Loe_failist("bob.txt")
print(list2_)

with open("bob.txt", "r", encoding="utf-8-sig") as f:
    print(f.read())"""

from random import  *
def failist_to_dict(f:str):
    riik_pealinn={}#sõnastik {"Riik":"Pealinn"}
    pealinn_riik={}#sõnastik {"Pealinn":"Riik"}
    riigid=[] #järjend, kus talletakse riigide nimetused
    file=open(f,'r', encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-') #k-võti, v-väärtus
        riik_pealinn[k]=v #täidame riik_pealinn
        pealinn_riik[v]=k #täidame pealinn_riik
        riigid.append(k)
    file.close()
    return riik_pealinn, pealinn_riik,riigid
    #käivitame loodud funktsion
riik_pealinn, pealinn_riik, riigid=failist_to_dict("riigid.txt")

print("""MENUU:
1) RIIK - PEALINN
2) PEALINN - RIIK
3) RIIGID
""")
valik = int(input(">"))

if valik == 1:
    #riik_pealinn
    with open("riigid.txt", "r", encoding="utf-8-sig") as f:
        print(f.read())

elif valik ==2:
    #pealinn_riik
    print("PEALINN             RIIK")
    print("")
    for r,p  in pealinn_riik.items():
        print(f"{r:20}{p}")

elif valik == 3:
    #riigid
    print("RIIGID")
    print("")
    for i in range(len(riigid)):
        print(riigid[i])


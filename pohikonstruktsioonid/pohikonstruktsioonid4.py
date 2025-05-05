#-----------------------
#MILAN PETROVSKI TARPV24
#Praktiline töö: "Matemaatika"

import math
import os #Konsooli kustutamise funktsiooni eest
from random import *

while True:
    try:
        os.system('cls') 
        tehed = ["+", "-", "*", "/"]
        while True:
            print("""┌Vali tase: 
├ 1 - Lihtne
├ 2 - Keskmine
├ 3 - Raske """)

            try:
                valitud_tase = int(input("└$ "))
                if valitud_tase in [1, 2, 3]:
                    print(f"\n » Valitud tase: {valitud_tase}")
                    break
                else:
                    print("Vale tase! Palun vali 1, 2 või 3.")
            except ValueError:
                print("Palun sisesta kehtiv number (1, 2 või 3).")

        if valitud_tase == 1:
            NUMS=[randint(1, 10),randint(1, 5),randint(1, 5)]
            OPERATS=tehed[:2]
        elif valitud_tase == 2:
            NUMS=[randint(1, 50),randint(1, 5),randint(1, 5)]
            OPERATS=tehed[:3]
        elif valitud_tase == 3:
            NUMS=[randint(1, 50),randint(1, 50),randint(1, 50)]
            OPERATS=tehed[2:4]
        else:print("Vale tase!")
        
        print("\n┌Valitud operatsioonid > ",OPERATS)

        operation1 = choice(OPERATS)
        operation2 = choice(OPERATS)
        print("└Pannud operatsioonid  > ",[operation1, operation2])

        ulesanne = f"{NUMS[0]} {operation1} {NUMS[1]} {operation2} {NUMS[2]}"
        Uresult = eval(ulesanne)
        if Uresult % 1 == 0:
            ulesanne_lahend = round(Uresult)
        else:
            ulesanne_lahend = round(Uresult,2)
    
        if valitud_tase == 3 and Uresult % 1 != 0:
            print(f"\n » Ülesanne: [{ulesanne}] ümardage kuni sajandikeni.")

        else:
            print(f"\n » Ülesanne: [{ulesanne}]")

        while True:
            try:
                vastus = float(input("\nVastus > "))
                if (vastus == ulesanne_lahend):
                    print("Õige vastus!")
                    break
                elif (vastus != ulesanne_lahend):
                    print("Vale vastus!")
                print("Õige vastus oli", ulesanne_lahend)
            except ValueError:
                    print("Palun sisesta  number.")

        mang = input(str("\nMangi uuesti? [Y/N] > "))
        if mang.lower() != "y":
            exit()

    except Exception as e:
        print(f"Viga: {e}")
        break

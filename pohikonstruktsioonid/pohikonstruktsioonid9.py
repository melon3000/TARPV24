from time import sleep
#--------------------
#v4 2
summa = 0
while True:
    try:
        p=int(input("Mitu korda kordame? "))
        if p<0:
            print("Sisetage positiivne number! ")
            pass
        else:   
            break
    except ValueError:
        print("Sisetage ainult numbrid!")
       
while True:
    try:
        arv = float(input(f"Sisesta arv: "))
        if arv < 0:
            summa += arv   
        elif arv > 0:
            pass
        p-=1
        if p == 0: break

    except ValueError:
        print("Sisetage ainult numbrid!")
print(f"Summa on {summa}\n")
sleep(3)

#--------------------
#v5 3
for õ in range(20):
    print(f"Soritab eksamit {õ+1}. Õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")

#--------------------
#v1 4

aeg = 0.2
while True:
    try:
        kokku = int(input("\nKotlettide arv: "))
        panni_maht = int(input("Panni maht: "))
        break
    except ValueError:
        print("\Sisetage ainult numbrid\n")

while True:
    if kokku == 0:
        break

    print(f"Jai {kokku} kotlettid.")
    if kokku <= panni_maht: panni_maht = kokku

    print(f"Robot valmistab {panni_maht} kotletit\n")
    sleep(aeg * 2)
    
    kokku -= panni_maht
    break

#--------------------
#v5 1
while True:
    try:
        a = float(input("Sisetage trapetside pikkus cm: "))
        b = float(input("Sisetage trapetside laius cm: "))
        h = float(input("Sisetage trapetside korgus cm: "))
        break
    except ValueError:
        print("Sisetage ainult numbrid!")

s = (a + b) * h / 2
print(f"Trapetside pindala on {s} cm.\n")

#--------------------
#v2 1

N = []
while True:
    try:
        kord = int(input("Kui palju numbreid tahate sisestada?: "))
        i = 1
        while i <= kord:
            try:
                number = float(input(f"Sisestage {i}. number: "))
                N.append(number)
                i += 1
            except ValueError:
                print("Sisestage ainult numbrid!")
        print(f"Maksimaalne number on > {round(max(N))}.\n")
        break
    except ValueError:
        print("Sisestage ainult numbrid!")


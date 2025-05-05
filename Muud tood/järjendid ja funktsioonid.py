import random

def sport():
    sportlased = []
    tulemused = []

    sportlasteArv = int(input("Sisesta sportlaste arv: "))
    
    for i in range(sportlasteArv):
        name = input(f"Sisesta {i+1} sportlase nimi: ")
        sportlased.append(name)

        results = [random.randint(1, 100) for j in range(3)]
        max_result = max(results)
        tulemused.append(max_result)

    while True:
        print("\n1. Teada n parimaid tulemusi")
        print("2. Korraldage nimekiri punktide kasvavas järjekorras")
        print("3. Sisestage ühe või mitme sportlase nimi ja näidake tema / nende tulemust")
        print("4. Diskvalifitseerida sportlased, kelle tulemused on antud künnisest halvemad")
        print("5. Väljund")
        
        choice = input("Vali: ")

        if choice == "1":
            n = int(input("Sisesta parimate tulemuste arv: "))
            for i in range(len(tulemused)):
                for j in range(i + 1, len(tulemused)):
                    if tulemused[i] < tulemused[j]:
                        tulemused[i], tulemused[j] = tulemused[j], tulemused[i]
                        sportlased[i], sportlased[j] = sportlased[j], sportlased[i]
            for i in range(min(n, len(sportlased))):
                print(f"{i + 1}. {sportlased[i]}: {tulemused[i]}")

        elif choice == "2":
            for i in range(len(tulemused)):
                for j in range(i + 1, len(tulemused)):
                    if tulemused[i] > tulemused[j]:
                        tulemused[i], tulemused[j] = tulemused[j], tulemused[i]
                        sportlased[i], sportlased[j] = sportlased[j], sportlased[i]

            print("\nNimekiri punktide kasvavas järjekorras:")
            for i in range(len(sportlased)):
                print(f"{i + 1}. {sportlased[i]}: {tulemused[i]}")

        elif choice == "3":
            names = input("Sisesta sportlaste nimed: ").split(",")
            names = [name.strip() for name in names]
            for name in names:
                if name in sportlased:
                    index = sportlased.index(name)
                    print(f"{name}: {tulemused[index]}")
                else:
                    print(f"Sportlane {name} ei leitud.")


        elif choice == "4":
            threshold = int(input("Sisestage diskvalifitseerimise künnis: "))
            disqualified = []
            for i in range(len(sportlased)):
                if tulemused[i] < threshold:
                    disqualified.append(i)

            for i in reversed(disqualified):
                sportlased.pop(i)
                tulemused.pop(i)
            
            print("\nPärast diskvalifitseerimist:")
            for name, result in zip(sportlased, tulemused):
                print(f"{name}: {result}")

        elif choice == "5":
            break

        else:
            print("Vale valik, proovige uuesti.")

sport()

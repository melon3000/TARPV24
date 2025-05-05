while True:
    print("\n")
    print(" Valige toiming │")
    print("┌───────────────┘")
    print("├ 1. islower")
    print("├ 2. isupper")
    print("├ 3. swapcase")
    print("├ 4. isalpha")
    print("├ 5. isdigit")
    print("├ 6. isspace")
    print("├ 7. strip")
    print("├ 8. replace")
    print("├ 9. find")
    print("├ 0. split")

    choice = input("└Sisestage number » ")

    if choice == '1':
        t = input("Sisestage tekst: ")
        if t.islower():  
            print("Tekst on kirjutatud väiketähtedega")
        else:
            print("Tekst pole kirjutatud suurtähtedega")


    if choice == '2':
        t = input("Sisestage tekst: ")
        if t.isupper():  
            print("Tekst on kirjutatud suurtähtedega")
        else:
            print("Tekst on kirjutatud väiketähtedega")

    elif choice == '3':
        t = input("Sisestage tekst: ")
        print("Muudetud tekst:", t.swapcase())

    elif choice == '4':
        t = input("Sisestage tekst: ")
        if t.isalpha():
            print("Tekst sisaldab ainult tähti.")
        else:
            print("Tekst sisaldab mitte ainult tähti.")

    elif choice == '5':
        t = input("Sisestage tekst: ")
        if t.isdigit():
            print("Tekst sisaldab ainult numbreid.")
        else:
            print("Tekst ei sisalda ainult numbreid.")

    elif choice == '6':
        t = input("Sisestage tekst: ")
        if t.isspace():
            print("Tekst sisaldab ainult tühikuid.")
        else:
            print("Tekst sisaldab muid märke peale tühikute.")

    elif choice == '7':
        t = input("Sisestage tekst: ")
        print("Tekst ilma tühikuteta alguses ja lõpus:", t.strip())

    elif choice == '8':
        t = input("Sisestage tekst: ")
        old = input("Sisestage osa, mida asendada: ")
        new = input("Sisestage uus osa: ")
        print("Muudetud tekst:", t.replace(old, new))

    elif choice == '9':
        t = input("Sisestage tekst: ")
        search = input("Sisestage otsitav alamtekst: ")
        index = t.find(search)
        if index != -1:
            print(f"Esimene esinemine leiti positsioonil {index}.")
        else:
            print("Alamteksti ei leitud.")

    elif choice == '0':
        t = input("Sisestage tekst, et jagada sõnadeks: ")
        print("Sõnad tekstis:", t.split())

    else:
        print("Vale valik! Proovige uuesti.")

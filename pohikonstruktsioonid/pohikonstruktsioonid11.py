sõne_list = []

while True:
    print("\nValige toiming nimekirjaga:")
    print("1. Lisa element nimekirja lõppu (append)")
    print("2. Laienda nimekirja (extend)")
    print("3. Sisesta element nimekirja (insert)")
    print("4. Eemalda element väärtuse järgi (remove)")
    print("5. Eemalda element indeksi järgi (pop)")
    print("6. Leia elemendi indeks (index)")
    print("7. Arvuta elementide arv (count)")
    print("8. Sorteeri nimekiri (sort)")
    print("9. Pööra nimekiri (reverse)")
    print("10. Kopeeri nimekiri (copy)")
    print("11. Puhasta nimekiri (clear)")

    choice = input("Sisestage number: ")

    if choice == '1':
        while True:
            try:
                t = input("Sisestage element nimekirja lisamiseks: ")
                if t.isalpha():
                    sõne_list.append(t)
                    break
                else:
                    print("Viga! Sisestage ainult tekst.")
            except Exception as e:
                print(f"Viga: {e}. Proovige uuesti.")
        print("Nimekiri pärast lisamist:", sõne_list)

    elif choice == '2':
        while True:
            try:
                ext_list = input("Sisestage nimekiri, et lisada koma järgi: ").split(',')
                ext_list = [item.strip() for item in ext_list]
                sõne_list.extend(ext_list)
                break
            except Exception as e:
                print(f"Viga: {e}. Proovige uuesti.")
        print("Nimekiri pärast laiendamist:", sõne_list)

    elif choice == '3':
        while True:
            try:
                t = input("Sisestage element sisestamiseks: ")
                indx = int(input("Sisestage indeks sisestamiseks: "))
                if 0 <= indx <= len(sõne_list):
                    sõne_list.insert(indx, t)
                    break
                else:
                    print("Viga! Indeks on väljaspool lubatud vahemikku.")
            except ValueError:
                print("Viga! Sisestage õige indeks.")
        print("Nimekiri pärast sisestamist:", sõne_list)

    elif choice == '4':
        while True:
            try:
                t = input("Sisestage element kustutamiseks: ")
                if t in sõne_list:
                    sõne_list.remove(t)
                    break
                else:
                    print("Viga! Elementi ei leitud.")
            except Exception as e:
                print(f"Viga: {e}. Proovige uuesti.")
        print("Nimekiri pärast elemendi kustutamist:", sõne_list)

    elif choice == '5':
        while True:
            try:
                indx = int(input("Sisestage elemendi indeks kustutamiseks: "))
                if 0 <= indx < len(sõne_list):
                    removed_item = sõne_list.pop(indx)
                    print(f"Kustutatud element: {removed_item}")
                    break
                else:
                    print("Viga! Indeks on väljaspool lubatud vahemikku.")
            except ValueError:
                print("Viga! Sisestage õige indeks.")
        print("Nimekiri pärast elemendi kustutamist:", sõne_list)

    elif choice == '6':
        while True:
            try:
                t = input("Sisestage element indeksi leidmiseks: ")
                if t in sõne_list:
                    index = sõne_list.index(t)
                    print(f"Elemendi '{t}' indeks: {index}")
                    break
                else:
                    print("Viga! Elementi ei leitud.")
            except Exception as e:
                print(f"Viga: {e}. Proovige uuesti.")

    elif choice == '7':
        while True:
            try:
                t = input("Sisestage element arvestamiseks: ")
                count = sõne_list.count(t)
                print(f"Elemendi '{t}' arv: {count}")
                break
            except Exception as e:
                print(f"Viga: {e}. Proovige uuesti.")

    elif choice == '8':
        while True:
            try:
                sort_order = input("(sisestage 'y' kasvavas järjekorras või 'n' kahanevas järjekorras): ")
                sort_order = sort_order.lower()
                if sort_order == 'y':
                    sõne_list.sort()
                    print("Nimekiri on sorteeritud kasvavas järjekorras.")
                    break
                elif sort_order == 'n':
                    print("Sorteerimine on tühistatud.")
                    break
                else:
                    print("Viga! Sisestage 'y' või 'n'.")
            except Exception as e:
                print(f"Viga: {e}. Proovige uuesti.")
        print("Nimekiri pärast sorteerimist:", sõne_list)

    elif choice == '9':
        sõne_list.reverse()
        print("Nimekiri pärast pööramist:", sõne_list)

    elif choice == '10':
        copy_list = sõne_list.copy()
        print("Nimekirja koopia:", copy_list)

    elif choice == '11':
        sõne_list.clear()
        print("Nimekiri on tühjendatud.")

    else:
        print("Vale valik! Proovige uuesti.")

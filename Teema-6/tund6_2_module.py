from os import system
from random import choice
#
def loo_sonastik():
    try:
        with open('sonastik.txt', 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            """lines = [
                "est = ['liim', 'koer', 'kass', 'maja', 'auto', 'päike']",
                "rus = ['клей', 'собака', 'кошка', 'дом', 'машина', 'солнце']",
                "eng = ['glue', 'dog', 'cat', 'house', 'car', 'sun']"
                ]"""

        est = eval(lines[0].strip()[5:]) #['liim', 'koer', 'kass', 'maja', 'auto', 'päike']
        rus = eval(lines[1].strip()[5:]) #['клей', 'собака', 'кошка', 'дом', 'машина', 'солнце']
        eng = eval(lines[2].strip()[5:]) #['glue', 'dog', 'cat', 'house', 'car', 'sun']

        sonastik = []
        for e, r, g in zip(est, rus, eng):
            sonastik.append({'est': e, 'rus': r, 'eng': g})

        return sonastik

    except FileNotFoundError:
        print("Fail sonastik.txt pole leitud, loome tühi sonastik.")
        return []
    except Exception as e:
        print(f"Viga faili loemisel - {e}")
        return []

def salvestada_sonastik(sonastik):
    est_list = []
    rus_list = []
    eng_list = []

    print(sonastik)
    for sona in sonastik: #[{'est': 'liim', 'rus': 'клей', 'eng': 'glue'}
        est_list.append(sona['est'])
        rus_list.append(sona['rus'])
        eng_list.append(sona['eng'])

    est = f"est = {str(est_list)}"
    rus = f"rus = {str(rus_list)}"
    eng = f"eng = {str(eng_list)}"

    with open('sonastik.txt', 'w', encoding='utf-8') as f:
        f.write(est + '\n')
        f.write(rus + '\n')
        f.write(eng + '\n')

def otsi_sona(sonastik, sona):
    found = False
    for entry in sonastik:
        for key, value in entry.items():
            if value == sona:
                print(f"est: {entry['est']}")
                print(f"rus: {entry['rus']}")
                print(f"eng: {entry['eng']}")
                found = True
                break
        if found:
            break

    if not found:
        print("Sõna ei leitud!")

def lisa_sona(sonastik):
    est = input("Sisesta eesti keeles: ").strip()
    rus = input("Sisesta vene keeles: ").strip()
    eng = input("Sisesta inglise keeles: ").strip()
   
    sonastik.append({'est': est, 'rus': rus, 'eng': eng})
    print("Sõna lisatud!")
    
    salvestada_sonastik(sonastik)
    return sonastik

def paranda_sona(sonastik):
    sona = input("Sisesta sõna, mida soovid parandada: ").strip()

    found = False
    for entry in sonastik:
        if sona == entry['est'] or sona == entry['rus'] or sona == entry['eng']:
            print(f"Leiti: {entry}")
            print(f"Kas soovid seda parandada? (Jah/Ei)")

            choice = input().strip().lower()
            if choice == 'jah':
                if sona == entry['est']:
                    new_est = input("Sisesta uus eesti sõna: ").strip()
                    entry['est'] = new_est
                elif sona == entry['rus']:
                    new_rus = input("Sisesta uus vene sõna: ").strip()
                    entry['rus'] = new_rus
                else:
                    new_eng = input("Sisesta uus ingliskeelne sõna: ").strip()
                    entry['eng'] = new_eng

                print("Sõna on parandatud!")
                
                salvestada_sonastik(sonastik)
                found = True
                break

    if not found:
        print("Sõna ei leitud!")

def kuva_sonad(sonastik):
    print(f"{'EST':10}|{'RUS':10}|{'ENG':10}")
    for i in sonastik:
        print(f"{i['est']:10}|{i['rus']:10}|{i['eng']:10}")

def vali_keelte_suund():
    while True:
        try:
            keel = int(input("Vali keel: |1 - EST|2 - RUS|3 - ENG| > "))
            if 1 <= keel <= 3:
                return keel
            else:
                print("Vali 1-3!")
        except ValueError:
            print("Vali 1-3!")

def testi_teadmisi(sonastik):
    keel = vali_keelte_suund()
    
    languages = {1: 'est', 2: 'rus', 3: 'eng'}
    source_language = languages[keel]

    used_words = []
    for i in range(len(sonastik)):
        random_word = choice([word for word in sonastik if word not in used_words])
        used_words.append(random_word)

        target_language = choice([lang for lang in ['est', 'rus', 'eng'] if lang != source_language])

        word_to_translate = random_word[source_language]
        target_word = random_word[target_language]
        guess = input(f"Tõlgi sõna '{word_to_translate}' {target_language} keelde: ")

        if guess.lower() == target_word.lower():
            print("Õige!")
        else:
            print(f"Vale! Õige vastus on: {target_word}")

def kuva_tulemus():
    print("Testi lõpptulemus: kõik vastused on õiged!")

def kysi_kasutajalt_sisestus(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Sisend ei tohi olla tühi. Proovi uuesti.")

def kuva_menuu(sonastik):
    print("\nVali tegevus:")
    print("1. Otsi sõna")
    print("2. Lisa uus sõna")
    print("3. Paranda sõna")
    print("4. Kuvada kõik sõnad")
    print("5. Testi teadmisi")
    print("6. Välju")

    choice = input("Vali tegevus (1-6): ")
    system('cls')
    if choice == '1':
        sona = input("Sisesta otsitav sõna: ").strip()
        otsi_sona(sonastik, sona)
    elif choice == '2':
        sonastik = lisa_sona(sonastik)
    elif choice == '3':
        paranda_sona(sonastik)
    elif choice == '4':
        kuva_sonad(sonastik)
    elif choice == '5':
        testi_teadmisi(sonastik)
    elif choice == '6':
        print("Head aega!")
        exit()
    else:
        print("Vale valik. Palun vali tegevus vahemikus 1-6.")

sonastik = loo_sonastik()

while True:
    kuva_menuu(sonastik)

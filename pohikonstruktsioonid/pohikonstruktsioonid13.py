from random import randint
from os import system
from time import sleep

pointsPlayer1 = []
pointsPlayer2 = []

#nimed
player1 = ""
player2 = ""

print("""Kivi-paber-käärid
VALIGE KELLEGA TE MÄNGITE:
    1 - ROBOT.
    2 - INIMESEGA.
""")

while True:
    try:
        playerChoiceToPlayWith = int(input("Valige kellega te mängite: "))
        if playerChoiceToPlayWith not in [1, 2]:
            print("Sisestage number (1 või 2).")
            continue
        break
    except ValueError:
        print("Sisestage number (1 või 2).")

system('cls')

if playerChoiceToPlayWith == 2:
    player1 = input(f"Mängija 1, sisesta oma nimi: ")
    player2 = input(f"Mängija 2, sisesta oma nimi: ")

elif playerChoiceToPlayWith == 1:
    player1 = input(f"Mängija 1, sisesta oma nimi: ")
    player2 = "Robot"
system('cls')

while True:
    while True:
        try:
            player1_choice = int(input(f"""{player1} Valige:
[1 - Kivi]
[2 - Käärid]
[3 - Paber]
> """))
            if player1_choice not in [1, 2, 3]:
                print("Palun vali kehtiv valik (1, 2 või 3).")
                continue
            break
        except ValueError:
            print("Sisestage kehtiv number (1, 2 või 3).")

    if playerChoiceToPlayWith == 1:
        player2_choice = randint(1, 3)
        print(f"Robot valis: {player2_choice}")
    
    elif playerChoiceToPlayWith == 2:
        while True:
            try:
                player2_choice = int(input(f"""{player2} Valige:
[1 - Kivi]
[2 - Käärid]
[3 - Paber]
> """))
                if player2_choice not in [1, 2, 3]:
                    print("Palun vali kehtiv valik (1, 2 või 3).")
                    continue
                break
            except ValueError:
                print("Sisestage kehtiv number (1, 2 või 3).")

    if player1_choice == player2_choice:
        print("Viik!")
    elif (player1_choice == 1 and player2_choice == 2) or (player1_choice == 2 and player2_choice == 3) or (player1_choice == 3 and player2_choice == 1):
        print(f"Mängija {player1} võitis!")
        pointsPlayer1.append(1)
    else:
        print(f"Mängija {player2} võitis!")
        pointsPlayer2.append(1)

    print(f"\nSkorid: {player1}: {len(pointsPlayer1)} | {player2}: {len(pointsPlayer2)}\n")

    while True:
        play_again = input("Kas soovite mängida veel? (y/n): ").lower()
        if play_again == "y":
            system('cls')
            break
        elif play_again == "n":
            print("Mäng on lõppenud!")
            exit()
        else:
            print("Palun sisesta 'y' või 'n'.")

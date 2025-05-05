#enumerate
from random import choice
from os import system

width = 50
height = 30

system(f'mode {width},{height}')
system('title WORDLE @melon3000')

toGuessWords = ['PYTHON', 'CODE', 'LIST', 'VARIABLE', 'TYPE', 'TTHK']
toGuessWord = choice(toGuessWords)
hiddenWord = ['_'] * len(toGuessWord)
usedLett = "" 

tries = 0
max_tries = 6

#COLORS
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

while tries < max_tries:
    system('cls')
    print(f"Kasutatud tähed: {usedLett}")
    print("")
    print(f"{' '.join(hiddenWord):^{width}}")
    guess = input(f"Siseta {len(toGuessWord)} tähe sõna: ").upper()

    if len(guess) != len(toGuessWord):
        print(f"Palun siseta {len(toGuessWord)} tähed.")
        continue

    for letter in guess:
        if letter not in usedLett:
            if letter in toGuessWord:
                usedLett += f"{YELLOW}{letter}{RESET} "
            else:
                usedLett += f"{letter} "

    for i in range(len(toGuessWord)):
        if guess[i] == toGuessWord[i]:
            hiddenWord[i] = guess[i]

    if ''.join(hiddenWord) == toGuessWord:
        system('cls')
        print(f"Võitja! Sõna oli: {toGuessWord}")
        break

    tries += 1

    if tries == max_tries:
        system('cls')
        print(f"Mäng lõppeb! Sõna oli: {toGuessWord}")

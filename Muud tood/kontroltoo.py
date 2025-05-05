# 4 Вариант 
import random


# 1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зверьков.
# Между двумя соседними зверьками также имеется пустой (из пробелов) столбец.
# Разрешается вывести пустой столбец после последнего зверька.
# Для упрощения рисования скопируйте зверька из примера в среду разработки.
#   ^---^
#  ( o o )
#   ! = !/)

print("Esimene ülesanne┐")
print("────────────────┘")

while True:
    try:
        n = int(input("Kui palju loomi te tahate nähta?: "))
        
        if 1 <= n <= 9:
            for i in range(3):
                for j in range(n):
                    if i == 0:
                        print(f"{'   ^---^':10}", end="")
                    elif i == 1:
                        print(f"{'  ( o o )':10}", end="")
                    else:
                        print(f"{'   ! = !/)':10}", end="")
                print()
            break
        else:
            print("Palun sisestage number 1-9.")
    except ValueError:
        print("VIGA: Sisestage ainult numbrid!")


# 2 Вывести степени натуральных чисел, не превосходящие данного числа n*100. Пользователь задает показатель степени и число n.

print("\nTeine ülesanne┐")
print("──────────────┘")

while True:
    try:
        arv = float(input("Mis arvu sa tahad tõsta N astmeni?: "))
        aste = int(input("Milleni asteni?: "))

        for i in range(1, aste + 1):
            result = arv ** i
            if result < arv * 100:
                print(f"{arv} astes {i} = {result}.")
            else:
                print(f"Lõpp, sest tulemus on suurem kui {round(arv*100)}")
                break 

        break 

    except ValueError:
        print("Sisestage ainult numbrid!")


# 3 Известны оценки по физике каждого из учеников класса. Определить минимальную и максимальную оценки.
# (Оценки и количество учеников получаем случайным образом)
print("\nKolmas ülesanne┐")
print("───────────────┘")

students = random.randint(5, 30)

hinded = [random.randint(1, 5) for i in range(students)]

min_hinne = min(hinded)
max_hinne = max(hinded)
print(f"Hinded: {hinded}")
print(f"Minimaalne hinne: {min_hinne}")
print(f"Maskimaalne hinne: {max_hinne}")


# 4 Одноклеточная амеба каждые 3 часа делится на 2 клетки.
#  Определить, сколько клеток будет через 3, 6, 9, ..., 24 часа, если первоначально была одна амеба.
print("\nNeljas ülesanne┐")
print("───────────────┘")

ameeb_count = 1
aeg = 3

while True:
    if aeg <= 24:
        print(f"{aeg} tundi = {ameeb_count} ameebid")
        aeg += 3
        ameeb_count *= 2
    else:
        break


# 5 Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.
# Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней. Оформите решение через цикл, используя только вычитание.
print("\nViies ülesanne┐")
print("──────────────┘")

while True:
    try:
        kokku = int(input("\nKotlettide arv: "))
        panni_maht = int(input("Panni maht: ")) 
        break
    except ValueError:
        print("\nSisestage ainult numbrid\n")

praadimiskorrad = 0

while kokku > 0:
    kokku -= panni_maht
    praadimiskorrad += 1

print(f"Kokku tuleb praadida {praadimiskorrad} korda.")

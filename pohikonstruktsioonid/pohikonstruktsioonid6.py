#-----------------------
#10 Praktilist ulessaned
#-----------------------

import math
import os

#-----------------------
#1

print("n1")
print("-----------------------")
counter_arv = 0

for i in range(15):
    while True:
        try:
            arv = float(input(f"Sisesta {i+1}. arv » "))
            break
        except ValueError:
            print("Kirjuta ainult numbrid")

    if arv == int(arv):
        counter_arv += 1

print(f"Täisarvude kogus: {counter_arv}")

#-----------------------
#2

print("\n2")
print("-----------------------")

while True:
    try:
        number_till = int(input("Siseta number: "))
        if number_till > 0:
            summa_arv = 0

            for i in range(1, number_till + 1):
                summa_arv += i
            print(f"Summa on {summa_arv}.")
            break

        else:
            print("Siseta arv mis on rohkem kui 0.")

    except Exception as EXC:
        print(f"VIGA: {EXC}")

#-----------------------
#3

print("\n3")
print("-----------------------")

summa = 0

while True:
    try:
        for i in range(1, 8+1):
            number = int(input(f"Sisesta {i} number » "))
            
            if number > 0:
                summa += number

        print(f"Summa » {summa}") 
        break
    except ValueError:
        print("Sisesta ainuld numbrid!")

#-----------------------
#4

print("\n4")
print("-----------------------")

a_sqrts = 10
while True:
    if a_sqrts <= 20:
        print(f" [Ruut {a_sqrts} on]  > {a_sqrts * a_sqrts}")
        a_sqrts += 1
    else:
        break

#-----------------------
#5

print("\n5")
print("-----------------------")

N_SUM = 0
while True:

    N = int(input("Mitu numbrit soovite lisada? » "))

    if N >= 1:
        for i in range(1, N +1):
            while True:
                try:
                    N_NUM = float(input(f"Sisesta {i} arv » "))
                    break
                except ValueError:
                    print("Siseta ainult numbrid. ")

            if N_NUM < 0:
                N_SUM += N_NUM
        break

print(f"Summa: {N_SUM}")

#-----------------------
#6

print("\n6")
print("-----------------------")

while True:
    try:
        N = int(input("Sisestage arvude arv » "))

        negative_count = 0
        positive_count = 0
        zero_count = 0

        for i in range(N):
            num = int(input(f"Sisestage number {i+1} » "))
            if num < 0:
                negative_count += 1
            elif num > 0:
                positive_count += 1
            else:
                zero_count += 1

        print(f"Negatiivsete arvude arv: {negative_count}")
        print(f"Positiivsete arvude arv: {positive_count}")
        print(f"Nullide arv: {zero_count}")
        
        break

    except ValueError:
        print("Kirjuta ainult numbrid! Püüa uuesti.")

#-----------------------
#7

print("\n7")
print("-----------------------")

while True:
    try:
        A = int(input("Sisesta arv A » "))
        B = int(input("Sisesta arv B » "))
        K = int(input("Sisesta arv K » "))

        for i in range(A, B + 1):
            if i % K == 0:
                print(i)

        break
    except Exception as EXC:
         print(f"VIGA: {EXC}")

#-----------------------
#8

print("\n8")
print("---------------------")

print("Tollid | Sentimeetrid")
print("---------------------")

for toll in range(1, 21):
    cm = toll * 2.5
    print(f"{toll:6} | {cm:12.2f}")

#-----------------------
#9

print("\n9")
print("---------------------")

while True:
    try:
        S = float(input("Sisestage algne summa eur » "))
        N = int(input("Sisestage aastate arv » "))
        p = 3
        A = S * (1 + p / 100) ** N
        break

    except ValueError:
        print(f"Siseta ainult numbrid!")


print(f"Summa pärast {N} aastat on: {A:.2f} eurot")

#-----------------------
#10

print("\n10")
print("---------------------")

while True:
    try:
        for i in range(1, 11):
            num1 = float(input("Sisesta esimine arv » "))
            num2 = float(input("Sisesta teise arv » "))

            if num1 > num2:
                print(f"Suurem on {num1}")
            elif num2 > num1:
                print(f"Suurem on {num2}")     
        break
    except ValueError:
        print(f"Kirjuta ainult numbrid!")
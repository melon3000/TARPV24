from module import * 


#artimetic funktsiooni kasutamine
a = float(input("Sisesta arv 1: "))
b = float(input("Sisesta arv 2: "))
c = input("Sisesta operatsioon: ")
v=arithmetic(a, b, c)
print(v)

#is_year_leap funktsiooni kasutamine
aasta = int(input("Sisesta aasta"))
v=is_year_leap(aasta)
if v == True:
    print(f"{aasta} on liigaasta")
else:
    print(f"{aasta} ei ole liigaasta")

#square funktsiooni kasutamine
S,P,d=square(float(input("sisesta külg")))
print(S,P,d)

#is_prime funktsiooni kasutamine
print(is_prime(500))
#lists

from random import randint

sõne = "Programmeerimine"
print(sõne)

sõne_list = list(sõne)
print(sõne_list)

sõne_list.reverse()
print(sõne_list)

print(sõne_list.index("P"))

print(len(sõne_list))
print(len(sõne))

sõne_list_count = sõne_list.count("m")
for m in range(sõne_list_count):
    sõne_list.remove("m")

tähed=randint(1, 10)

for i in range(tähed):
    while True:
        try:
            t = input(f"Sisestsa {i + 1} täht: ")
            if t.isalpha(): break
        except:
            print("On vaja täht!")
    sõne_list.append(t)
print(sõne_list)

tähed=randint(1, 5)

for i in range(tähed):
    while True:
        try:
            t = input(f"Sisestsa {i + 1} täht: ")
            if t.isalpha(): break
        except:
            print("On vaja täht!")

    while True:
        try:
            indx = input("Sisestsa index: ")
            if indx.isnumeric() & int(indx)<len(sõne_list): break
        except:
            print("On vaja täht!")
    sõne_list.insert(int(indx), t)
print(sõne_list)

def function(e):
    return len(e)
sõne_list.sort(reverse=True, key=function)
print(sõne_list)

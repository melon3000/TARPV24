print("*** MÄNG ARVUDEGA ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Siseta täisarv => ")))
        break
    except ValueError:
         print("See pole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("On mõtettu jagada 0-ga")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu paaritu arvu")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0:
            if b % 2 == 0:
                    paaris =+ 1
            else:
                    paaritu =+ 1
            b = b // 10
    
    print("Paaris arvud:",paaris)
    print("Paaritu arvud:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Ümberpöörame* sisestatud number")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number
    print("*Pöörtud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Kontrollime Sirakuz-i teoreem"))
    print()
    if c % 2 == 0:
        print(c, " - чётное число. Делим на 2.")
    else:
        print(c, " - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
            if c % 2 == 0:
                print('{:>4}'.format(round(c))," - Paarisarv, Jagame 2.")
                c = c / 2
            else:
                print('{:>4}'.format(round(c))," - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
                c=(3*c + 1)
    print()
    print("Hüpotees kehtib")
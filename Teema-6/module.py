from datetime import datetime

def arithmetic(number_1:float, number_2:float, operation:str)->any:
    """Lihne kalkulaator
    + - liitmine
    - - lahutamine 
    * - korrutamine
    / - jagamnine
    :param float number_1: Sisend kasutajalt, mingi ujukomaarv
    :param float number_2: Sisend kasutajalt, mingi ujukomaarv
    :param str operation: Sisend kasutajalt, aritmeetili tehe
    :rtype: Määrata tyyp(float või str)
    """
    if operation in ["+", "-", "*", "/"]:
        if number_1==0 and operation=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(number_1)+operation+str(number_2))
    else:
        vastus="Tundmatu tehe"
    return vastus


def is_year_leap(year:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigasta False kui on tavaline aasta.
    :param int year: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus 
    """
    if year % 4 == 0:
        vastus = True
    else:
       vastus = False
    return vastus


def square(side:float)->any:
    """
     Arvutab ruudu omadused, sh pindala, perimeeter ja diagonaali pikkuse.
    :param float side: Ruudu külje pikkus
    :return: Kolm väärtust, mis on ruudu pindala, perimeeter ja diagonaal
    :rtype: tuple
    """
    S=side**2
    P=side*4
    d=2**(1/2)*side
    s_list=[S,P,d]
    return S,P,d


def season(month:int)->str:
    """
    Leiab astaaja.
    :param int month: huvitav kuu
    :return: Tagastab aastaaja nime konkreetsel kuul
    :rtype: string
    """
    if month in [12,1,2]:
        v = "talv"
    elif month in [3,4,5]:
        v = "kevad"
    elif month in [6,7,8]:
        v = "suvi"
    elif month in [9,10,11]:
        v = "sügis"
    return v


def seasonv2(month:int)->str:
    """
    Leiab astaaja.
    :param int month: huvitav kuu
    :return: Tagastab aastaaja nime konkreetsel kuul
    :rtype: string
    """
    k=int(input("Sisesta kuu number: "))
    while True:
        if k in range(1,13):
            break
        else:
             k=int(input("Sisesta kuu number: "))
        return season(k)


def bank(eur:float, years:int)->float:
    """
    Leiab 1.10*eur / aasta.
    :param float eur: summa 
    :param int years: aastat
    :return: Tagastab intress
    :rtype: float
    """
    for i in range(years):
        eur *= 1.10
    return eur


def is_prime(number:float)->bool:
    """
    Kontrollib, kas number on algarv.
    Funktsioon tagastab True, kui number on algarv, vastasel juhul False.
    :param int n: kontrollitav arv
    :return: True, kui arv on algarv, False vastasel juhul
    :rtype: bool
    """

    if 0 <= number < 1001:
        if number in [0,1]:
            pass
        else:
            for i in range(2,number):
                if number % i == 0:
                    return False
                else:
                    return True



def date(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

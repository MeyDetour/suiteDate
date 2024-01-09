def isgood(result):
    return 2000 < result < 2050


def iflow(result):
    return result < 2000


def calcul(a, b, puissance):
    result = 0
    for k in range(a, b + 1):
        result += k ** puissance
    return result


def verify(puissance):
    a = 1
    b = 2
    for k in range(30):

        print(a, b, isgood(calcul(a, b, puissance)), iflow(calcul(a, b, puissance)))
        while isgood(calcul(a, b, puissance)) or iflow(calcul(a, b, puissance)):
            print(a, b, calcul(a, b, puissance))
            if isgood(calcul(a, b, puissance)):
                liste.append((a, b, puissance))
            b += 1
        print(liste)
        a += 1
        b = a + 1
    return liste

def run():
    for k in range(11):
        verify(k)
    return liste

liste = []  # renvoie un tuple avec resultat (a,b,puissance)

print(run())

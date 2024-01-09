def isgood(result):
    return 2000 < result < 3000
def iflow(result):
    return result<2000

def calcul(a, b, puissance):
    result = 0
    for k in range(a, b + 1):
        result += k ** puissance
    return result


def verify(puissance):
    liste = []  # renvoie un tuple avec resultat (a,b,puissance)
    a = 1
    b = 1
    while isgood(calcul(a,b,puissance)) or iflow(calcul(a,b,puissance))  :
        print(calcul(a,b,puissance))



print(calcul(2, 9, 3))

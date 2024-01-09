def isgood(result):
    return min < result < max


def iflow(result):
    return result < min

def ifhight(result):
    return result < max
def calcul(a, b, puissance):
    result = 0
    for k in range(a, b + 1):
        result += k ** puissance
    return result


def verify(puissance):
    a = 1
    b = 2

    while ifhight(a ** puissance + (a + 1) ** puissance):

        while isgood(calcul(a, b, puissance)) or iflow(calcul(a, b, puissance)):
            print(a, b, puissance, calcul(a, b, puissance))
            if isgood(calcul(a, b, puissance)):
                print(a, b, calcul(a, b, puissance))
                liste.append((a, b, puissance,calcul(a, b, puissance)))

            b += 1
        print(a, b, calcul(a, b, puissance))
        print(liste)
        a += 1
        b = a + 1

    return liste

def affichage():

    for tuple in liste:
        print(tuple)
        texte = ""
        for k in range(tuple[0],tuple[1]+1):
            texte += f"{k}^{tuple[2]} + "
        texte += f"=> ={tuple[3]}"
        print(texte)
        print("  ")

def run():
    for k in range(2, 11):
        verify(k)
    return liste

max = 2050
min = 2000
liste = []  # renvoie un tuple avec resultat (a,b,puissance)
run()
affichage()

l = []
print("\nVeuillez entrer une série d'entier se terminant par '.'")

while 1 :
    try :
        n = int(input("\nEntrer un nombre : "))
        l.append(n)
    except ValueError :
        break

print("\nLa liste avant :",l)

i = 0 # indice début
j = len(l) - 1 # indice fin

while i < j :

    if l[i] < 0 and l[j] < 0 :
        i += 1

    elif l[i] < 0 and l[j] >= 0 :
        i += 1
        j -= 1

    elif l[i] >= 0 and l[j] >= 0 :
        j -= 1

    else : # i < 0 and j < 0
        l[i] , l[j] = l[j] , l[i]
        i += 1
        j -= 1

print("\nLa liste après :",l)

# Version optimisé :

""" while i < j:
    while l[i] < 0:
        i += 1
    while l[j] >= 0:
        j -= 1
    if i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1 """
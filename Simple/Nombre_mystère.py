from random import randint
from time import sleep

print("\nBienvenue dans ce jeu du nombre mystère , vous devez trouver un nombre compris dans un intervalle donné avec le moins de tentative possible")
r = "oui"
l = [] # la liste qui contiendra le nombre de tentatives de chaque partie

while r == "oui" : # la réponse de l'utilisateur pour savoir s'il veut continuer à jouer (de base elle est initialisée à oui)

    print("\nVoulez vous définir vous même l'intervalle ? (oui/non)")
    while 1 :
        ru = input("\nVotre réponse : ")
        if ru not in ("oui", "non") :
            print("\n💡 Veuillez répondre par 'oui' ou 'non'")
        else : 
            break

    if ru == "oui" :
        bi = int(input("\nEntrer la borne inférieure : "))
        while 1 :
            bs = int(input("\nEntrer la borne supérieure : "))
            if bs <= bi :
                print("\n💡 Veuillez entrer une valeur strictement supérieure à",bi)
            else : 
                break
    
    else :
        bi = randint(0,10000)
        bs = randint(bi+1,10000)
        print("\nGénrération de l'intervalle ...")
        sleep(3) # za3ma ...
    
    x = randint(bi,bs)
    print(f"\n{bi} < X < {bs}")

    t = 0
    while 1 :
        y = int(input("\nVeuillez entrer un nombre : "))
        t += 1
        if y < x :
            print(f"\n{y} plus petit que X")
        elif y > x :
            print(f"\n{y} plus grand que X")
        else :
            print("\nBravo vous avez trouvé le nombre mystère",x,"en",t,"tentative ✨")
            break
    l.append(t)
    
    print("\nVoulez vous lancer une nouvelle partie ? (oui/non)\n")
    while 1 :
        r = input("Votre réponse : ")
        if r not in ("oui", "non") :
            print("\n💡 Veuillez répondre par 'oui' ou 'non'\n")
        else : 
            break

m = format(sum(l)/len(l),".2f") # calcul de la moyenne des tentatives

print("\nMerci d'avoir joué voici votre score : ")
for i, v in enumerate(l) :
    print(f"\nPartie {i+1} : {v} tentatives")
print("\nLa moyenne des tentatives =",m,"\n")
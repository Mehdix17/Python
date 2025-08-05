from random import choice 
nbrP = 0 # nombre de partie jouées
nbrPG = 0 # nombre de partie gagnée
r = "oui" # la réponse de l'utilisateur pour savoir s'il veut continuer à jouer (de base elle est initialisée à oui)

print("\nEntrer votre nom pour commencer à jouer 🙂")
name = input("Votre nom : ")
print("\nBienvenue dans ce jeu "+name+" voici les règles 📜 : \nPierre > ciseaux \nciseaux > feuille \nfeuille > pierre \n")
print("Commençons par une première partie 🎲")

while r == "oui" :
    nbrP += 1 # incrémentation du nombre de partie
    while 1 :
        nbrM = int(input("\nVeuillez choisir le nombre de manches gagnantes de cette partie : "))
        if nbrM <= 0 : print("\n💡 Veuillez chosir un nombre positif non nul \n")
        else : break
    print("\nLe premier à",nbrM,"gange ✅")

    dic = {
        1 : "Pierre 🪨" ,
        2 : "Feuille 📃" ,
        3 : "Ciseaux ✂️" ,
    }
    scu = 0 #intialisation du score de l'utilisateur
    sco = 0 #initialistion du score de l'ordinateur

    while scu != nbrM and sco != nbrM :

        while 1 :
            print("\nQue voulez vous jouer ? \n1) Pierre 🪨\n2) Feuille 📃\n3) Ciseaux ✂️\n")
            cu = int(input("Votre choix : ")) #cu = choix utilisateur
            if cu not in dic.keys() :
                print("\n💡 Veuillez choisir l'une des 3 propistions (1-2-3)")
            else : break
        co = choice([1,2,3]) #co = choix ordinateur

        if cu == 1 and co == 3 or cu == 2 and co == 1 or cu == 3 and co == 2 : #cas de victoire
            scu += 1 #incrémentation du score de l'utilisateur
        elif cu == 3 and co == 1 or cu == 1 and co == 2 or cu == 2 and co == 3 : #cas de defaite
            sco += 1 #incrémentation du score de l'ordinateur

        # en cas d'égalitée on ne fait rien

        print() # pour sauter une ligne
        print(name,":",dic.get(cu)) #retourne la valeur stockée dans le dictionnaire
        print("Ordinateur :",dic.get(co))
        print("Score :",scu,"-",sco)

        if scu == nbrM : 
            print("\nBravo",name,"vous avez remporté cette partie ✨ \n")
            nbrPG += 1 # incrémentation du nombre de parties gagnées
        elif sco == nbrM :
            print("\nDommage vous avez perdu cette partie 💔 \n")

    print("Voulez vous lancer une nouvelle partie ? (oui/non)")
    while 1 :
        r = input("\nVotre réponse : ")
        if r not in ["oui","non"] :
            print("\n💡 Veuillez réponde par 'oui' ou 'non'")
        else : break

pv = nbrPG // nbrP * 100 # calcul du pourcentage de victoire
print(f"\nVoici votre score {name} : \nParties gagnées : {nbrPG} 🏆\nParties perdues : {nbrP-nbrPG} 🔪"
      +f"\nPourcentage de victoire : {pv} % 🔥\n")

from Voyage import voyage_frais

print("\nBienvenue dans ce programme qui calcul le coût total de votre voyage")

while 1 :
    v = input("\nVeuillez entrer le nom de la ville : ")
    if v not in ["Paris","Barcelone","Tunis","Tokyo","New york"] :
        print("\nVeuillez saisir l'une de ces villes : \nParis \nBarcelone \nTunis \nTokyo \nNew york")
    else : 
        break

while 1 :
    n = int(input("\nVeuillez entrer le nombre de nuits passé a l'hôtel : "))
    if n <= 0 :
        print("\nVeuillez entrer un nombre naturel non nul")
    else :
        break

while 1 :
    j = int(input("\nVeuillez entrer le nombre de jours de la location voiture : "))
    if j < 0 :
        print("\nVeuillez entrer un nombre naturel")
    else :
        break

while 1 :
    a = int(input("\nVeuillez entrer d'autres frais s'il y'en a : "))
    if a < 0 :
        print("\nVeuillez entrer un nombre naturel")
    else :
        break

print("\nLe coût total de votre voyage =",voyage_frais(v,j,n,a),"$ \n")


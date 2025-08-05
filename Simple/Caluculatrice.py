print("\nBienvenue dans ce programme !")
r = "o"
while r == "o" :
    print("\nVeuillez choisir une opération : \n1) Addition \n2) Soustraction \n3) Multiplication  \n4) Division \n5) Quitter le programme \n")
    c = int(input("Votre réponse : "))
    match c :
        case 1 : 
            x = int(input("Veuilez entrer le 1er nombre : "))
            y = int(input("Veuilez entrer le 2e nombre : "))
            print("Le résulat = ",x+y)
            
        case 2 : 
            x = int(input("Veuilez entrer le 1er nombre : "))
            y = int(input("Veuilez entrer le 2e nombre : "))
            print("Le résulat = ",x-y)
            
        case 3 : 
            x = int(input("Veuilez entrer le 1er nombre : "))
            y = int(input("Veuilez entrer le 2e nombre : "))
            print("Le résulat = ",x*y)
            
        case 4 : 
            x = int(input("Veuilez entrer le 1er nombre : "))
            y = int(input("Veuilez entrer le 2e nombre : "))
            if y == 0 :
                print("Division par 0 impossible")
            else :
                print("Le résulat = ",format(x/y,".2f"))
            
        case 5 : 
            print("Fin du programme")
            exit()

        case _ : print("Choix incorrect")
    print("\nVoulez vous continuer ? o/n ")
    r = input("Votre réponse : ")
print("Fin du programme")




  


   



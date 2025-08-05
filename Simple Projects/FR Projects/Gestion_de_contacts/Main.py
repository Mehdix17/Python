from contact import *
from carnet_contact import *

menu = "\n* * * * * * *  Menu * * * * * * *\n*                               *\n*  1) Ajouter un contact 📞     * \n*                               *\n*  2) Modifier un contact ✏️     * \n*                               *\n*  3) Rechercher un contact 🔎  * \n*                               *\n*  4) Supprimer un contact ❌   * \n*                               *\n*  5) Afficher le répertoire 📒 * \n*                               *\n*  6) Afficher la corbeille 🗑️   * \n*                               *\n*  7) Quitter le programme ⚙️    * \n*                               *\n* * * * * * * * * * * * * * * * *"
print("\nBienvenue dans votre géstionnaire de contacts")
carnet = CarnetContacts()

while 1 :
    
    print(menu)
    while 1 :
        try :
            choix =  int(input("\nVotre choix : "))
            if choix not in range(1,8) :
                print("\n💡 Veuillez choisir l'une des 7 options")
            else :
                break
        except ValueError :
            print("\n💡 Veuillez choisir l'une des 7 options")

    match choix :
        
        case 1 :
            carnet.ajouter_contact()

        case 2 :
            carnet.modifier_contact()

        case 3 :
            carnet.rechercher_contact()

        case 4 :
            carnet.supprimer_contact()

        case 5 :
            carnet.afficher_repertoire()

        case 6 :
            carnet.afficher_corbeille()

        case 7 :
            print("\nFin du programme.")
            exit()


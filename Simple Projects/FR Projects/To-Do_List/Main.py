from taskManager import *

menu = """
* * * * * * * * * *  Menu * * * * * * * * * * * 
*                                             *
*   1) Ajouter un tâche ✏️                     *
*                                             *
*   2) Afficher la liste des tâches 📒        *
*                                             *
*   3) Marquer une tâche comme terminée ✅    * 
*                                             *
*   4) Quitter le programme ⚙️                 *
*                                             *
* * * * * * * * * * * * * * * * * * * * * * * *
""" 

print("\nBienvenue dans votre géstionnaire de tâches")
tasks = TaskManager()

while 1 :
    
    print(menu)
    while 1 :
        try :
            choix =  int(input("\nVotre choix : "))
            if choix not in range(1,5) :
                print("\n💡 Veuillez choisir l'une des 4 options")
            else :
                break
        except ValueError :
            print("\n💡 Veuillez choisir l'une des 4 options")

    match choix :
        
        case 1 :
            tasks.ajouter_tache()

        case 2 :
            tasks.afficher_taches()

        case 3 :
            tasks.marquer_tache()

        case 4  :
            print("\nFin du programme.")
            exit()
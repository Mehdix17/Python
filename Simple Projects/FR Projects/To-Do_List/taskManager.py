import os

class TaskManager :
    
    def __init__(self) :
        self.CheminFichier = r"To-Do_List\tasks.txt"

# 1) ajouter une tâche 

    def ajouter_tache(self) :
        t = input("\nVeuillez entrer une tâche : ")
        with open(self.CheminFichier,"a") as file :
            file.write(t+"\n")        
        print("\nTâche ajoutée ✅")

# 2) afficher la liste des tâches

    def afficher_taches(self) :
        if os.path.getsize(self.CheminFichier) == 0 :
            print("\nAucune tâche disponible ❌")
        else :
            print("\nListe des tâches :")
            with open(self.CheminFichier,"r") as file :
                for index , line in enumerate(file,start = 1) :
                    print(f"\n{index}\ {line.strip()}")

# 3) marquer une tâche comme terminée

    def marquer_tache(self) :
        if os.path.getsize(self.CheminFichier) == 0 :
            print("\nAucune tâche disponible ❌")
        else :
            while 1 :
                try :
                    num = int(input("\nVeuillez le numéro de la tâche : "))
                    if num in range(1,self.lignes_fichiers()+1) :
                        self.maj_fichier(num) # mise à jour du fichier
                        print("\nTâche marquée ✅")
                        break
                    else :
                        print("\nNuméro de tâche incorrecte ❌")
                except ValueError :
                    print("\nNuméro de tâche incorrecte ❌")

# fonction qui compte le nombre de lignes d'un fichier

    def lignes_fichiers(self):
        with open(self.CheminFichier, "r") as file:
            cpt = 0
            for _ in file:
                cpt += 1
            return cpt
    
# fonction qui met à jour un fichier

    def maj_fichier(self,x) :
        
        with open(self.CheminFichier, "r") as file : # Lire le contenu du fichier
            lignes = file.readlines()

        del lignes[x-1] # supprimer la ligne spécifique

        with open(self.CheminFichier, "w") as file : # Réécrire le contenu mis à jour dans le fichier
            for ligne in lignes :
                file.write(ligne)
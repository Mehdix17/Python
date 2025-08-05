from contact import *

class CarnetContacts :

    def __init__(self) :
        self.liste = []
        self.liste_numéro = [] # liste qui contiendra tous les numéros, utile pour vérifier l'unicité des numéros
        self.corbeille = [] # liste qui contiendra tous les contacts supprimés

# 1) Ajouter un nouveau contact

    def ajouter_contact(self) : 
        
        while 1 : # boucle de vérification du nom
            n = input("\nNom : ")
            tempo_n = n.replace(" ","") # pour gérer le cas particulier où le nom est composé
            if not tempo_n.isalpha() :  # car isalpha() renvoie "False" s'il y'a des espaces dans le nom
                print("\nNom incorrecte ❌")
            else :
                break

        while 1 : # boucle de vérification du prénom
            p = input("\nPrénom : ")
            tempo_p = p.replace(" ","") # même chose pour le prénom
            if not tempo_p.isalpha() :
                print("\nPrénom incorrecte ❌")
            else :
                break      
        
        while 1 : # boucle de vérification du numéro
            num = input("\nNuméro : ")
            if num.isdigit() and (num.startswith("05") or num.startswith("06") or num.startswith("07")) and len(num) == 10 :
                if num in self.liste_numéro :
                    print("\nCe numéro appartient déjà à un contact ❌")
                else :
                    break
            else : # numéro entré par l'utilisateur ne respecte pas toutes les conditions
                print("\n💡 Veuillez entrer un numéro à 10 chiffres commençant par 05 ou 06 ou 07")
        
        contact = Contact(n,p,num)
        self.liste.append(contact)
        self.liste_numéro.append(num)

# 2) Modifier un contact

    def modifier_contact(self) :
            
            c = input("\nVeuillez entrer le numéro du contact à modifier : ")
            trouvé = False
            
            if c.isdigit() : # cas d'un numéro
                for i in self.liste :
                    if i.numero == c :
                        print("\nVoici le contact correspondant : \n",i)
                        trouvé = True
                        self.liste_numéro.remove(i.numero) # enlever le numéro de la liste pour le remplacer après par le nouveau              
                        break
                
                if trouvé == True :

                    while 1 : # boucle de vérification du nouveau nom
                        i.nom = input("\nNouveau nom : ")
                        tempo_n = i.nom.replace(" ","") # pour gérer le cas particulier où le nom est composé
                        if not tempo_n.isalpha() :  # car isalpha() renvoie "False" s'il y'a des espaces dans le nom
                            print("\nNom incorrecte ❌")
                        else :
                            break

                    while 1 : # boucle de vérification du nouveau prénom
                        i.prenom = input("\nNouveau prénom : ")
                        tempo_p = i.prenom.replace(" ","") # même chose pour le prénom
                        if not tempo_p.isalpha() :
                            print("\nPrénom incorrecte ❌")
                        else :
                            break      
                    
                    while 1 : # boucle de vérification du nouveau numéro
                        i.numero = input("\nNouveau numéro : ")
                        if i.numero.isdigit() and (i.numero.startswith("05") or i.numero.startswith("06") or i.numero.startswith("07")) and len(i.numero) == 10 :
                            if i.numero in self.liste_numéro :
                                print("\nCe numéro appartient déjà à un contact ❌")
                            else :
                                self.liste_numéro.append(i.numero) # mise à jour du numéro dans la liste de numéros
                                print("\nContact modifié ✏️")
                                break
                        else : # numéro entré par l'utilisateur ne respecte pas toutes les conditions
                            print("\n💡 Veuillez entrer un numéro à 10 chiffres commençant par 05 ou 06 ou 07")
            
            else :
                print("\nNuméro incorrecte ❌")
                trouvé = True # pour éviter d'afficher le prochain message après celui-ci

            if trouvé == False :
                print("\nNuméro introuvable ❌")

# 3) Rechercher un contact par son nom ou numéro de téléphone

    def rechercher_contact(self) :
        
        c = input("\nVeuillez entrer le nom ou le numéro du contact à rechercher : ")
        tempo_c = c.replace(" ","") # pour gérer le cas particulié où l'on cherche un nom composé
        trouvé = False
        
        if c.isdigit() : # cas d'un numéro
            for i in self.liste :
                if i.numero == c :
                    print("\nVoici le contact correspondant : \n",i)
                    trouvé = True
                    break
        
        elif tempo_c.isalpha() : # cas d'un nom
            tempo = []
            for i in self.liste :
                if i.nom == c :
                    tempo.append(i)  # liste qui contient tous les contacts ayant un nom = c
                    trouvé = True
            if len(tempo) == 1 :
                print(f"\nVoici le contact correspondant : \n",tempo[0])
            elif len(tempo) > 1 :
                print(f"\nVoici la liste des contacts correspondants : ")
                for i , j in enumerate(tempo) :
                    print(f"\nContact {i+1} : \n{j}")
        
        else : # ni un numéro ni un nom (alphanumérique)
            print("\nNom ou numéro incorrecte ❌")
            trouvé = True # pour éviter d'afficher le prochain message après celui-ci

        if trouvé == False :
            print("\nNom ou numéro introuvable ❌")

# 4) Supprimer un contact par son nom ou numéro de téléphone

    def supprimer_contact(self) : 
        
        c = input("\nVeuillez entrer le nom ou le numéro du contact à supprimer : ")
        tempo_c = c.replace(" ","") # pour gérer le cas particulié où l'on cherche un nom composé
        trouvé = False
        
        if c.isdigit() : # cas d'un numéro
            for i in self.liste :
                if i.numero == c :
                    self.corbeille.append(i) # ajouter à la corbeille avant de supprimer
                    self.liste.remove(i)
                    self.liste_numéro.remove(c)
                    print("\nContact supprimé ✅")
                    trouvé = True
                    break
        
        elif tempo_c.isalpha() : # cas d'un nom
            contacts = [contact for contact in self.liste if contact.nom == c] # liste temporaire
            if len(contacts) > 1 : # plusieurs contacts qui ont le même nom
                trouvé = True
                print("\nPlusieurs contacts correspondent au nom :",c)
                for i , j in enumerate(contacts) :
                    print(f"\nContact {i+1} : \n{j}")
                while 1 :        
                    print("\nVoulez-vous tous les supprimer ?")
                    reponse = input("\nVotre réponse : ") 
                    if reponse not in ["oui","non"] :
                        print("\n💡 Veuillez répondre par oui ou non")   
                    else :
                        break
                if reponse == "oui" :
                    self.corbeille.extend(contacts) # ajouter à la corbeille avant de mettre à jour la liste
                    self.liste = [contact for contact in self.liste if contact.nom != c] # mise à jour de la liste
                    for i in contacts :
                        self.liste_numéro.remove(i.numero) # mise à jour de la liste des numéros
                    print("\nContacts supprimés ✅")
                else :
                    print(f"\n💡 Pour supprimer l'un des {len(contacts)} contacts précedents il vous suffit d'entrer son numéro")
                
            elif len(contacts) == 1 : # un seul contact correspondant
                trouvé = True
                self.corbeille.append(contacts[0]) # ajouter à la corbeille avant de mettre à jour la liste
                self.liste.remove(contacts[0]) # mise à jour de la liste
                self.liste_numéro.remove(contacts[0].numero) # mise à jour de la liste des numéros
                print("\nContact supprimé ✅")

        else : # ni un numéro ni un nom (alphanumérique)
            print("\nNom ou numéro incorrecte ❌")
            trouvé = True # pour éviter d'afficher le prochain message après celui-ci

        if trouvé == False : # aucun contact correspondant
            print("\nNom ou numéro introuvable ❌")

# 5) Afficher la liste de tous les contacts

    def afficher_repertoire(self) :
        if len(self.liste) == 0 :
            print("\nAucun contact enregistré ❌") 
        else :
            print(f"\n{len(self.liste)} contacts enregistrés 📒")
            for i , j in enumerate(self.liste) :
                print(f"\nContact {i+1} : \n{j}")

# 6) Affihcher la corbeille :
 
    def afficher_corbeille(self) :
        if len(self.corbeille ) == 0 :
            print("\nCorbeille vide 🗑️")
        else :
            print("\nLa corbeille contient :",len(self.corbeille),"contacts")
            for i , j in enumerate(self.corbeille) :
                print(f"\nContact {i+1} : \n{j}")
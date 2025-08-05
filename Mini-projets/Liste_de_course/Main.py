from Stock import *
from commande import Commande
import datetime
from random import choice

print("\nBienvenue dans notre magasin !")

choix = affiche_menu()

while 1 : # la boucle principale du programme, pour en sortir il faut choisir la 7e option      
    
    match choix :
        
        case 1 :
            if len(panier) > 0 :
                print("\nVotre panier 🧺")
                affiche_panier()
                facture = calcul_facture()
                print("\nPrix total =",facture,"$")
                
                while 1 :
                    print("\nVoulez vous payez maintenant ? 💵")
                    c1 = input("\nVotre réponse : ")
                    if c1 not in ["oui", "non"] :
                        print("\n💡 Veuillez répondre par 'oui' ou 'non'")
                    else :
                        if c1 == "oui" :
                            while 1 :
                                carte = input("\nVeuillez entrer votre carte de crédit : ")
                                if carte.isdigit() == False or len(carte) != 16 :
                                    print("\n💡 Le numéro de carte de crédit doit comprendre 16 chiffres")
                                else :
                                    while 1 :
                                        code = choice(range(10000,100000)) # génération d'un numéro de commande unique sur 5 chiffres
                                        if code not in historique_code :
                                            date = datetime.date.today().strftime("%d/%m/%Y")
                                            heure = datetime.datetime.now().time().strftime("%H:%M")
                                            commande = Commande(code,panier.copy(),facture,date,heure) # création de la commande
                                            historique.append(commande) # sauvegarde de la commande dans l'historique
                                            historique_code.append(code) # sauvegarde du code de la commande
                                            panier.clear() # on vide le panier pour la prochaine commande
                                            print("\nPaiement effectué avec succès 💵")
                                            break
                                    print("\nVoici votre numéro de commande :",code,"🎟️")
                                    break
                            break
                        else :
                            break # on sort de la boucle et l'utilisateur revient au menu principal

            else : # panier vide
                print("\nVotre panier est vide pour l'instant, voulez vous le remplir ?")
                while 1 :
                    c2 = input("\nVotre réponse : ")
                    if c2 not in ["oui", "non"] :
                        print("\n💡 Veuillez répondre par 'oui' ou 'non'")
                    else : break
                if c2 == "non" :
                    choix = affiche_menu()
                else :
                    choix = 2
                continue # pour sauter directement a case 2                   

        case 2 :
            print("\nVoici la liste de nos produits : ")
            print(Produits)
            print("\nPour ajouter un produit à votre panier il suffit d'entrer son nom")
            print("\n💡 Vous pouvez arrêter la saisi à tout moment en entrant 'stop'")
            while 1 :
                p = input("\nEntrer le nom du produit : ")
                if p == "stop" :
                    break
                elif p not in stock.keys() :
                    print("\nProduit indisponible ❌")
                else :
                    panier.append(p)
                    print(f"\n{p} a bien été ajouté au panier ✅")

        case 3 :
            if len(panier) == 0 :
                print("\nImpossible de supprimer car votre panier est vide")
            else :
                print("\nPour supprimer un produit de votre panier il suffit d'entrer son nom")
                print("\n💡 pour quitter entrer 'stop'")
                print("\n💡 pour vider tout le panier entrer 'clear'")
                while 1 :
                    p = input("\nEntrer le nom du produit à supprimer : ")
                    if p == "clear" :
                        panier.clear()
                        print("\nLe panier a bien été vidé ✅")
                        break
                    elif p == "stop" :
                        break
                    elif p not in set(panier) :
                        print("\nCe produit n'existe pas dans votre panier ❌")
                    else :
                        if panier.count(p) > 1 :
                            print(f"\nil semblerait que ce produit ({p}) soit présent dans votre panier en plusieurs exemplaires ({panier.count(p)})")
                            print("Voulez vous supprimer toutes ses occurences ?")
                            while 1 :
                                reponse = input("\nVotre réponse : ")
                                if reponse not in ["oui", "non"] :
                                    print("\n💡 Veuillez répondre par 'oui' ou 'non'")
                                else :
                                    break
                            if reponse == "oui" :
                                while p in panier :
                                    panier.remove(p)
                                print(f"\nToutes les occurences du produit '{p}' on été supprimé du panier ✅") 
                            else : # la reponse = non donc on ne supprime qu'une seule occurence du produit
                                panier.remove(p)
                                print(f"\n'{p}' a bien été supprimé du panier ✅") 
                        else : # il existe qu'une seule occurence de ce produit dans le panier
                            panier.remove(p)
                            print(f"\n'{p}' a bien été supprimé du panier ✅") 
        
        case 4 :
            print("\nVoici la liste de tout nos produits disponibles : ")
            print(Produits)
            
        
        case 5 :
            if len(historique) == 0 :
                print("\nAucune commande disponible pour le moment")
            else :
                print("\n💡 Pour annuler une commande il suffit d'entrer son numéro")
                print("\n💡 pour revenir au menu principal entrer 'back'")
                while 1 :
                    try :
                        c3 = int(input("\nNuméro de la commande : "))
                        if c3 == "back" :
                            break
                        elif c3 not in historique_code :
                            print("\nNuméro de commande incorrecte ❌")
                        else :
                            historique = [commande for commande in historique if commande.code != c3] 
                            # mise a jour de l'historique en utilisant une compréhension de liste
                            print("\nCommande annulée ✅")
                            break
                    except ValueError :
                        print("\n💡 Veuillez entrer votre numéro de commande unique sur 5 chiffres")
        
        case 6 :
            if len(historique) == 0 :
                print("\n📂 L'historique est vide pour l'instant")
            else :
                print("\nVoici votre historique des commandes : ")
                for h in historique :
                    print(f"\nCode : {h.code} 🎟️")
                    print(f"\nPanier : {h.p}")
                    print(f"\nFacture : {h.facture} $")
                    print(f"\nDate : {h.date}")
                    print(f"\nHeure : {h.heure}")
        case 7 :
            print("\nAvant de quitter pouvez-vous nous donner une note sur 5 ?\n\n1) oui je veux bien \n\n2) Non merci")
            while 1 :
                try :
                    c4 = int(input("\nVotre choix : "))
                    if c4 not in [1,2] :
                        print("\n💡 Veuillez choisir l'une des 2 options")
                    else : 
                        break
                except ValueError :
                    print("\n💡 Veuillez choisir l'une des 2 options")
            if c4 == 1 :
                while 1 :
                    try :
                        note = int(input("\nVotre note : "))
                        if note not in range(1,6) :
                            print("\n💡 Donnez une note entre 1 et 5 ⭐")
                        else : 
                            break
                    except ValueError :
                        print("\n💡 Donnez une note entre 1 et 5 ⭐")
                if note == 5 :
                    print("\nMerci d'avoir de nous avoir mis 5 ⭐ voici un cadeau pour vous remercier : ")
                    print("\nBon de réduction de 10 % 🎁")
                else :
                    print("\nNous vous remercions Merci d'avoir pris de votre temps")

            print("\nFin du programme")
            exit()

    choix = affiche_menu()
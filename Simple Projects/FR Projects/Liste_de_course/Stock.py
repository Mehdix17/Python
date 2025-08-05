menu = "* * * * * * * * * * * * * * * * * * * * * *\n*                                         *\n*  1) Consulter votre panier 🧺           *\n*                                         *\n*  2) Ajouter un produit au panier ✅     *\n*                                         *\n*  3) Supprimer un produit du panier ↩️    *\n*                                         *\n*  4) Check les produits disponibles 📦   *\n*                                         *\n*  5) Annuler votre commande ❌           *\n*                                         *                                     \n*  6) Check l'historique des commandes 📜 *\n*                                         *                                     \n*  7) Quitter le programme 🤖             *\n*                                         *                                     \n* * * * * * * * * * * * * * * * * * * * * *"
Produits = "\n  Alimentation                  Vetements                   Produits electromenagers             Produits electroniques   \n"+"\nPomme 🍎    : 2.5           Pantalon 👖    : 50.0           Réfrigérateur 🧊   : 600.0          PC portable 💻     : 800.0\n" +"\nOrange 🍊   : 1.8           T-shirt 👕     : 20.0           Machine à laver 🧼 : 400.0          Smartphone 📱      : 500.0\n" +"\nCarotte 🥕  : 1.0           veste 🧥       : 60.0           Cuisinière 🔥      : 500.0          Casque audio 🎧    : 100.0 \n"+"\nTomate 🍅   : 2.0           Chapeau 👒     : 25.0           Micro-ondes 🔳     : 120.0          Appareil photo 📷  : 350.0 \n"+"\nPatate 🥔   : 1.2           Casquette 🧢   : 15.0           Lave-vaisselle 🍽️   : 250.0          Téléviseur 📺      : 700.0 \n"+"\nPain 🥖     : 2.5           Chaussures 👟  : 40.0           Cafetière ☕       : 80.0           Console de jeux 🎮 : 500.0 \n"+"\nChocolat 🍫 : 3.0           Chaussettes 🧦 : 5.0            Grille-pain 🍞     : 30.0           Imprimante 🖨️       : 150.0 \n"
panier = [] # liste qui contient tout les produits achetés
facture = 0 # le prix final à payer
historique = [] # liste d'objets (commandes)
historique_code = [] # Liste qui contient tout les numéros de commandes
code = 0 # code unique pour chque commande
heure = 0 # l'heure de la commande
date = 0 # l'heure de la commande

# Les fonctions utilisées dans Main

def affiche_menu() :
        print()
        print(menu)
        while 1 :
            try : # pour éviter que le programme s'arrête lorsque l'utilisateur entre autre chose qu'un nombre
                choix = int(input("\nVotre choix : "))
                if choix not in range(1,8) :
                    print("\n💡 Veuillez choisir l'une des 7 options")
                else : 
                    return choix
            except ValueError :
                print("\n💡 Veuillez choisir l'une des 7 options") # dans le cas win l'utilisateur entre autre chose qu'un nombre
    
def affiche_panier() :
    for i in set(panier) : # la fonction set permet d'éliminer les doublons
        prix = format(panier.count(i) * stock.get(i),".2f") # Produit x Quantité = Prix
        print(f"\n{i} x {panier.count(i)} = {prix} $") 

def calcul_facture() :
    facture = 0 # c'est le prix final à payer
    for i in set(panier) : # la fonction set permet d'éliminer les doublons
        facture += panier.count(i) * stock.get(i) # calcul de la facture
    return facture

# Le dictionnaire qui contient tout les produits

stock = {   "Pomme"            : 2.5 ,
            "Orange"           : 1.8 ,
            "Fraise"           : 4.0 ,
            "Carotte"          : 1.0 ,
            "Patate"           : 1.2 ,
            "Tomate"           : 2.0 ,
            "Pain"             : 2.5 ,
            "Frommage"         : 3.5 ,
            "Viande"           : 5.0 ,
            "Poulet"           : 4.0 ,
            "Chocolat"         : 3.0 ,
            "Pantalon"         : 50.0 ,
            "T-shirt"          : 20.0 ,
            "Veste"            : 60.0 ,
            "Chapeau"          : 25.0 ,
            "Casquette"        : 15.0 ,
            "Chaussures"       : 40.0 ,
            "Chaussettes"      : 5.0  ,
            "Réfrigérateur"    : 600.0 ,
            "Machine à laver"  : 400.0 ,
            "Cuisinière"       : 500.0 ,
            "Micro-ondes"      : 120.0 ,
            "Lave-vaisselle"   : 250.0 ,
            "Cafetière"        : 80.0  ,
            "Grille-pain"      : 30.0  ,
            "PC portable"      : 800.0 ,
            "Smartphone"       : 500.0 ,
            "Casque audio"     : 100.0 ,
            "Appareil photo"   : 350.0 ,
            "Montre connectée" : 200.0 ,
            "Téléviseur"       : 700.0 ,
            "Console de jeux"  : 500.0 ,
            "Imprimante"       : 150.0
}
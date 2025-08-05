class Contact :
    
    def __init__(self,nom,prenom,numero) :
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        print("\nContact créé ✅")

    def __str__(self) :
        return f"\nNom = {self.nom}\n \nPrénom = {self.prenom}\n \nNuméro = {self.numero}"
    
        


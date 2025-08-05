print("\nLe but de ce programme est de convertir un nombre décimal donné en un nombre binaire")
while 1 :
    n = int(input(("\nVeuillez entrer un nombre positif : ")))
    if n < 0 :
        continue
    else : 
        break

x = n # stocker la valeur décimal
ord = 0 # l'ordre
b = 0 # le nombre binaire

while n != 0 :
    r = n % 2 # le reste
    p = 10 ** ord # la puissance
    b = b + r * p
    ord += 1
    n //= 2

print(f"\n{x} en binaire = {b}\n")
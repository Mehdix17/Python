l = [] # liste qui contiendra les n premiers nombres premiers
k = 0 # compteur qui s'incrémente à chaque nombre premier
x = 2 # 2 est le premier des nombres premiers

print("\nCe programme affiche les n premiers nombres premiers")

while 1 :
    try :
        n = int(input("\nEntrer n : "))
        if n < 1 :
            print("\n💡 Veuillez entrer un nombre strictement positif")
        else :
            break
    except ValueError :
        print("\n💡 Veuillez entrer un nombre strictement positif")

while k != n : # k peut être remplacé par len(l)
    premier = True
    for i in range(2,x//2+1) : # il suffit de chercher de 2 jusqu'a la moitié d'un nombre pour savoir si ce dernier est premier ou non
        if x % i == 0 :
            premier = False
            break
    if premier == True :
        l.append(x)
        k += 1
    x += 1

print(f"\nLes {n} premiers nombres premiers sont : ")
for i in l :
    print(i)


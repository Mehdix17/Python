l = []

print("\nVeuillez entrer une série de nombres , entrer '.' pour arrêter")
while 1 :
    x = input("\nEntrer un nombre : ")
    if x == "." :
        break
    else :
        l.append(int(x))

while 1 :
    print(f"\nVeuillez entrer un nombre m < {len(l)} : ",end="")
    y = int(input())
    if y < len(l) :
        break

k = list(reversed(sorted(l)))
print("\nLes",y,"plus grands nombres de la liste :")
for i in range(y) :
    print(k[i])
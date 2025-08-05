def mult(j) :
    for i in range(1,11) :
        print(f"\n{j} * {i} = {j*i}")

while 1 :
    x = int(input("\nVeuillez entrer un nombre : "))
    print("\nLa table de multiplication de",x,": ")
    mult(x)


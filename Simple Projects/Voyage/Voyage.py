def hotel_frais(n) : # paramètre = nombre de nuit
    return n * 90

def vol_frais(v) : # paramètre = ville
    match v :
        case "Paris" : return 200
        case "New york" : return 300
        case "Tokyo" : return 350
        case "Tunis" : return 100
        case "Barcelone" : return 250

def location_voiture_frais(j) : # paramètre = nombre de jour
    coût = j * 35
    if j < 3 :
        return coût
    elif j < 7 :
        return coût - 20
    else :
        return coût - 50

def voyage_frais(v,j,n,a) : # paramètre = ville, jours, nuits, autres frais
    return (vol_frais(v) + location_voiture_frais(j) + hotel_frais(n) + a)
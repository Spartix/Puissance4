from interface.grille import Grille,Ligne,Dessin

def print_grille(grille:Grille):
    global Dessin
    total = ""
    for lst in grille:
        lst:Ligne;
        for elt in lst:
            total += str(Dessin[elt])
        total += "\n"
    return total


def place(grille:Grille,player:int,position:int):
    boucle = len(grille) - 1 
    while boucle > 0:
        lst:Ligne = grille[boucle]
        if(lst[position] == 0):
            lst[position] = player
            return True
        boucle -= 1
    return False
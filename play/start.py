from interface.grille import Grille,Ligne,Dessin

def print_grille(grille:Grille):
    global Dessin;
    
    """
    Fonction print_grille , affichant la grille
    grille(Grille): grille à afficher
    >>> print_grille([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    X.....\nX.....\nX.....\nX.....\n......\n......\n
    """
    assert(type(grille) == list)
    assert(len(grille) == 6)
    assert(len(grille[0]) == 6) 
    assert(type(Dessin) == list)
    assert(len(Dessin) == 3)
    
    total = ""
    for lst in grille:
        lst:Ligne;
        for elt in lst:
            total += str(Dessin[elt])
        total += "\n"
    return total


def place(grille:Grille,player:int,position:int) -> bool:
    """
    Fonction place pour placer un jeton dans le puissance4
    grille(Grille): grille de puissance4 à comparer
    player(int): Joueur actuel jouant
    position(int): Position de la colone joué
    return(bool): Le jeton a été placer avec success
    
    Exemples:
    >>> place([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],1,0)
    True
    """
    assert(type(grille) == list)
    assert(len(grille) == 6)
    assert(len(grille[0]) == 6)
    assert(type(player) == int)
    assert(type(position) == int)
    assert(position <= 6)
    assert player == 1 or player == 2
    boucle = len(grille) - 1 
    while boucle > 0:
        lst:Ligne = grille[boucle]
        if(lst[position] == 0):
            lst[position] = player
            return True
        boucle -= 1
    return False
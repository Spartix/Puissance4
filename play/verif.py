from interface.grille import Grille,Ligne
from typing import Tuple


def horizontal(grille:Grille) -> Tuple[bool,int]:
    for lst in grille:
        lst:Ligne;
        compare:int = 0
        nb_compare:int = 0
        for elt in lst:
            if compare != 0:
                if compare == elt:
                    nb_compare += 1
                else:
                    compare = elt
                    nb_compare = 0
                if nb_compare == 4 and compare != 0:
                    return True,elt
        return False,0
    
    
def vertical(grille:Grille):
    index = 0
    compare = 0
    nb_compare = 0
    while index < 6:
        for i in range(7):
            if compare == grille[i][index]:
                nb_compare += 1
            else:
                nb_compare = 1
                compare = grille[i][index]
            if nb_compare == 4 and compare != 0:
                return True,compare
        index += 1
    return False,0
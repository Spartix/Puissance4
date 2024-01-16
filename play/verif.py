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
                if nb_compare == 4:
                    return True,elt
        return False,0
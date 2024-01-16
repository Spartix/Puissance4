from utils.grille import Gen
from interface.grille import Grille
from typing import List

Dessin = [" ","X","O"]

def play() -> None:
    grille:Grille = Gen()
    print(print_grille(grille))


def print_grille(grille:Grille):
    global Dessin
    total = ""
    for lst in grille:
        lst:List[int];
        for elt in lst:
            total += str(Dessin[elt])
        total += "\n"
    return total




play()
from interface.grille import Grille,Ligne
from typing import Tuple


def horizontal(grille:Grille) -> Tuple[bool,int]:
    for lst in grille:
        lst:Ligne;
        compare:int = 0
        nb_compare:int = 0
        for elt in lst:
            if compare == elt:
                nb_compare += 1
            else:
                compare = elt
                nb_compare = 1
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


def diagonale_droit(grille:Grille,start_ligne:int,start_colone):
    comaprer = 0
    nb_compare = 0
    for _ in range(6):
        if(grille[start_ligne][start_colone] == comaprer):
            nb_compare += 1
        else:
            comaprer = grille[start_ligne][start_colone]
        start_ligne -= 1
        start_colone +=1
        
    
def diagonale_gauche(grille:Grille,start:int):
    compare = 0
    nb_compare = 0
    while start > 0:
            print(f"found {grille[start][start]} in {start,start}")
            if compare == grille[start][start]:
                nb_compare += 1
            else:
                compare = grille[start][start]
                nb_compare = 1
            if nb_compare == 4 and compare != 0 :
                return True,compare
            start -= 1
    return False,0

def diagonale(grille:Grille):
    for i in range(3):
        if diagonale_droit(grille,i)[0]:
            return diagonale_droit(grille,i)
    for caca in range(5):
        for proute in range(5):
            diagonale_droit(caca,proute)
    return False,0
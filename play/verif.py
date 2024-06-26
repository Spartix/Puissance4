from interface.grille import Grille,Ligne
from typing import Tuple


def horizontal(grille:Grille) -> Tuple[bool,int]:
    '''
    Fonction horizontal retournant si il y a un gagnant et lequel
    grille(Grille): grille a comparer
    return (tuple(bool,int)): le tuple gagner ou non ainsi que le gagant
    '''
    assert(type(grille) == list)
    assert(type(grille[0]) == list)
    assert(type(grille[0][0] == int))
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
    
    
def vertical(grille:Grille) -> tuple:
    '''
    Fonction veritcal retournant si il y a un gagnant et lequel
    grille(Grille): grille a comparer
    return (tuple(bool,int)): le tuple gagner ou non ainsi que le gagant
    '''
    assert(type(grille) == list)
    assert(type(grille[0]) == list)
    assert(type(grille[0][0] == int))
    index = 0
    compare = 0
    nb_compare = 0
    while index < 6:
        for i in range(7):
            try:
                if compare == grille[i][index]:
                    nb_compare += 1
                else:
                    nb_compare = 1
                    compare = grille[i][index]
                if nb_compare == 4 and compare != 0:
                    return True,compare
            except:
                pass
        index += 1
    return False,0


def diagonale_droit(grille:Grille,start_colone:int):
    """
    Fonction diagonal droit donnant le numéro du joueur qui a gagné si et seulment si il a 4 jetons alignés en diagonal de droite a gauche
    grille(Grille): grille de puissance 4 à comparer
    return (tuple(bool,int)): retourne un tuple contenant si il y a un gagnant et lequel
    Exemples:
    >>> diagonale_droit([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    False,0
    >>> diagonale_droit([[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,1,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[1,0,0,0,0,0]])
    False,0
    """
    assert(type(grille) == list)
    assert(type(grille[0]) == list)
    assert(type(grille[0][0] == int))
    nb_compare = 0
    comparer = 0
    grille.reverse()
    for lst in grille:
        lst:Ligne;
        if(start_colone > 5):
            grille.reverse()
            return False,0
        if lst[start_colone] == comparer:
            nb_compare += 1
        else:
            comparer = lst[start_colone]
            nb_compare = 1
        start_colone += 1
        if( nb_compare == 4 and comparer != 0):
            grille.reverse()
            return True,comparer
    grille.reverse()
    return False,0

def diagonale_droit_hauteur(grille:Grille,starter:int):
    """
    Fonction diagonal droit donnant le numéro du joueur qui a gagné si et seulment si il a 4 jetons alignés en diagonal de droite a gauche
    grille(Grille): grille de puissance 4 à comparer
    return (tuple(bool,int)): retourne un tuple contenant si il y a un gagnant et lequel
    Exemples:
    >>> diagonale_droit_hauteur([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    False,0
    >>> diagonale_droit_hauteur([[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,1,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[1,0,0,0,0,0]])
    False,0
    """
    assert(type(grille) == list)
    assert(type(grille[0]) == list)
    assert(type(grille[0][0] == int))
    nb_compare = 0
    comparer = 0
    colone = 0
    grille.reverse()
    for _ in range(4):
        if grille[starter][colone] == comparer:
            nb_compare += 1
        else:
            comparer = grille[starter][colone];nb_compare = 1
        if nb_compare == 4 and comparer != 0:
            return True,comparer
        starter += 1
        colone += 1
    grille.reverse()
    return False,0

def diagonale_gauche(grille, start_colonne):
    """
    Fonction diagonal gauche donnant le numéro du joueur qui a gagné si et seulment si il a 4 jetons alignés en diagonal de gauche a droite
    grille(Grille): grille de puissance 4 à comparer
    return (tuple(bool,int)): retourne un tuple contenant si il y a un gagnant et lequel
    Exemples:
    >>> diagonale_gauche([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    False,0
    >>> diagonale_gauche([[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,1,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[1,0,0,0,0,0]])
    False,0
    """
    assert(type(grille) == list)
    assert(type(grille[0]) == list)
    assert(type(grille[0][0] == int))
    nb_compare = 0
    comparer = 0
    grille.reverse()
    for lst in grille:
        if start_colonne < 0:
            grille.reverse()
            return False, 0
        if lst[start_colonne] == comparer:
            nb_compare += 1
        else:
            comparer = lst[start_colonne]
            nb_compare = 1
        start_colonne -= 1 
        if nb_compare == 4 and comparer != 0:
            grille.reverse()
            return True, comparer
    grille.reverse()
    return False, 0

def diagonale_gauche_hauteur(grille, starter):
    """
    Fonction diagonal donnant le numéro du joueur qui a gagné si et seulment si il a 4 jetons alignés en diagonal de gauche a droite
    grille(Grille): grille de puissance 4 à comparer
    return (tuple(bool,int)): retourne un tuple contenant si il y a un gagnant et lequel
    Exemples:
    >>> diagonale_gauche_hauteur([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    False,0
    >>> diagonale_gauche_hauteur([[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,1,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[1,0,0,0,0,0]])
    False,0
    """
    assert(type(grille) == list)
    assert(type(grille[0]) == list)
    assert(type(grille[0][0] == int))
    nb_compare = 0
    comparer = 0
    colonne = 5  
    grille.reverse()
    for _ in range(4):
        if starter >= len(grille) or colonne < 0:  
            grille.reverse()
            return False, 0
        if grille[starter][colonne] == comparer:
            nb_compare += 1
        else:
            comparer = grille[starter][colonne]
            nb_compare = 1
        if nb_compare == 4 and comparer != 0:
            grille.reverse()
            return True, comparer
        starter += 1
        colonne -= 1 
    grille.reverse()
    return False, 0


def diagonale(grille:Grille):
    """
    Fonction diagonal donnant le numéro du joueur qui a gagné si et seulment si il a 4 jetons alignés en diagonal
    grille(Grille): grille de puissance 4 à comparer
    return (tuple(bool,int)): retourne un tuple contenant si il y a un gagnant et lequel
    Exemples:
    >>> diagonale([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    False,0
    >>> diagonale([[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,1,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[1,0,0,0,0,0]])
    True,1
    """
    assert(type(grille) == list)
    assert(len(grille) == 6)
    assert(len(grille[0]) == 6)
    for i in range(3):
        if diagonale_droit(grille,i)[0]:
            return diagonale_droit(grille,i)
        if diagonale_droit_hauteur(grille,i)[0]:
            return diagonale_droit_hauteur(grille,i)
        if diagonale_gauche_hauteur(grille,i)[0]:
            return diagonale_gauche_hauteur(grille,i)
        if diagonale_gauche(grille,i)[0]:
            return diagonale_gauche(grille,i)  
        # print(diagonale_droit(grille,i))
        # print(diagonale_droit_hauteur(grille,i))
    return False,0

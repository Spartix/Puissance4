from play.verif import diagonale, horizontal, vertical
from utils.grille import Gen
from interface.grille import Grille
from play.start import *


def question(player:int) -> int:
    """
    fonction question demandant au joueur quelle colone veut il choisir pour placer son jeton
    player(int): numero du joueur (1 ou 2)
    return (int): reponse a la question
    """
    assert type(player) == int
    assert player <= 2
    
    try:
        retour = int(input(f"Joueur {player} quel colone voulez vous entrer votre jeton\n >")) - 1
        if retour > 6:
            return question(player)
        return retour
    except:
        question(player)

def play() -> None:
    """
    fonction jouer permettant de démarrer le puissance4
    """
    grille:Grille = Gen()
    actuel:int = 1
    while not win(grille):
        print(print_grille(grille))
        print(f"Le joueur {actuel} joue...")
        joue = question(actuel)
        place(grille,actuel,joue)
        if(actuel == 1):
            actuel =    2
        else:
            actuel = 1
    print(f"le joueur {winner(grille)} a gagné")
        
        
def win(grille:Grille) -> bool:
    """
    fonction win donnant si un joueur a gagné
    grille (Grille): grille du puissance4
    Exemples:
    >>> win([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    False
    >>> win([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    True
    """
    assert(type(grille) == list)
    assert(len(grille) == 6)
    assert(len(grille[0]) == 6) 
    return vertical(grille)[0] or horizontal(grille)[0] or diagonale(grille)[0]


def winner(grille:Grille) -> int:
    """
    Fonction winner donnant le numero du joueur gagnant
    grille (Grille): Grille du puissance 4 contenant le jeu à comparer
    return (int): retourne le numero du joueur gagnant
    Exemples:
    >>> winner([[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    1
    >>> winner([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    0
    """
    assert(type(grille) == list)
    assert(len(grille) == 6)
    assert(len(grille[0]) == 6) 
    lst = ([vertical(grille), horizontal(grille),diagonale(grille)])
    lst.sort(key=lambda info: info[0],reverse=True)
    return lst[0][1]

play()
"""gtest =[
          [0, 0, 0, 0, 0, 0],
          [0, 0, 2, 1, 0, 0], 
          [0, 2, 1, 0, 1, 0], 
          [2, 1, 0, 1, 2, 0], 
          [0, 0, 1, 2, 0, 2], 
          [0, 0, 2, 0, 0, 1]
          ]"""
"print(Gen())"
"print(diagonale(gtest))"


from play.verif import diagonale, horizontal, vertical
from utils.grille import Gen
from interface.grille import Grille
from play.start import *


def question(player:int) -> str:
    try:
        retour = int(input(f"Joueur {player} quel colone voulez vous entrer votre jeton\n >")) - 1
        if retour > 6:
            return question(player)
        return retour
    except:
        question(player)

def play() -> None:
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
    return vertical(grille)[0] or horizontal(grille)[0]


def winner(grille:Grille):
    lst = ([vertical(grille), horizontal(grille)])
    lst.sort(key=lambda info: info[0],reverse=True)
    return lst[0][1]


"play()"
gtest = [
         [0, 0, 2, 0, 0, 0],
         [0, 0, 1, 0, 2, 0],
         [1, 0, 1, 1, 2, 2],
         [0, 1, 1, 1, 0, 2],
         [0, 0, 1, 0, 2, 0],
         [1, 0, 0, 1, 0, 1]
         ]
print(diagonale(gtest))

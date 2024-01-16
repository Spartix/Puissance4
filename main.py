from play.verif import horizontal
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
    while not win(grille)[0]:
        print(print_grille(grille))
        print(f"Le joueur {actuel} joue...")
        joue = question(actuel)
        place(grille,actuel,joue)
        if(actuel == 1):
            actuel =    2
        else:
            actuel = 1
        
        
        
def win(grille:Grille) -> bool:
    return horizontal(grille)
    return False

play()
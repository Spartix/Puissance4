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
    actuel = 1
    while not win(grille):
        print(print_grille(grille))
        print(f"Le joueur {actuel} joue...")
        joue = question(actuel)
        place(grille,actuel,joue)
        
        
def win(grille:Grille):
    return False

play()
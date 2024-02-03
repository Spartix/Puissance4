from typing import List
from utils.color import colors
class Grille:
    List[List[int]]
    
class Ligne:
    List[int]

Dessin:List[str] = [f"{colors.reset()}●",f"{colors.player(1)}●{colors.reset()}",f"{colors.player(2)}●{colors.reset()}"]
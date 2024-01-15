from ctypes import List
from utils.grille import Gen

def play() -> None:
    grille:List[List[int]] = Gen()
    print(grille)
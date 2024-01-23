from interface.grille import Grille
def Gen() -> Grille:
    lst = list()
    for _ in range(6):
        lss = list()
        for _ in range(6):
            lss.append(0)
        lst.append(lss)
    return lst

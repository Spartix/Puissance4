from interface.grille import Grille
def Gen() -> Grille:
    """
    Fonction generant la grille du puissance4
    return (Grille): list de list contenant les parametres du puissance4
    """
    lst = list()
    for _ in range(6):
        lss = list()
        for _ in range(6):
            lss.append(0)
        lst.append(lss)
    return lst

from random import choice

color = ["\033[32m","\033[33m","\033[31m",""]
class colors:
    """
    Classs colors permettant d'avoir une couleur demander , sois aleatoire sois pré choisis
    """
    def random():
        """
        return (str): couleurs aleatoire parmis la list color=
        """
        return choice(colors)
    def player(player:int): 
        """
        player(int): joueur dont on veut connaitre sa couleur
        return (str): couleurs choisi parmis la list color
        Exemples:
        >>> colors.player(1)
        \033[33m
        """
        return color[player]
    def reset():
        """
        return (str): couleur reset
        >>> colors.reset()
        \033[0m
        """
        return "\033[0m"
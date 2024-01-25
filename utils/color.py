from random import choice
class color:
    
    def random():
        colors = ["\033[2;31;43m"]
        return choice(colors)
    
    reset = "\033[0m"
        
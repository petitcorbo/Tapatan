
# [0]–[1]–[2] #
#  | \ | / |  #
# [3]–[4]–[5] #
#  | / | \ |  #
# [6]–[7]–[8] #


# Actualisation graphique
# Placement
# Deplacement
# Sauvegarde / Chargement


def afficher(tab):
    print(tab[0:3])
    print(tab[3:6])
    print(tab[6:9])


def creer_tableau():
    tab = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    return tab


def changer_joueur():
    return joueur


def placement(tab, sur=0):
    pass


def deplacement(tab, de=0, a=1):
    pass


def main():
    global deplacement_possible
    deplacement_possible = [
        [1, 3, 4], [0, 2, 4], [1, 5, 4],
        [0, 6, 4], [0, 1, 2, 3, 5, 6, 7, 8], [2, 8, 4],
        [3, 7, 4], [6, 8, 4], [5, 7, 4]
        ]
    tab = creer_tableau()
    
    placement(tab, sur=0)
    
    deplacement(tab, de=0, a=1)
    


if __name__ == '__main__': main()

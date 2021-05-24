##### Ce fichier n'est pas a prendre en compte #####

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
    global joueur
    if joueur == 1:
        joueur = 2
    elif joueur == 2:
        joueur = 1


def placement(tab, sur=0):
    if tab[sur] == 0:
        tab[sur] = joueur


def deplacement(tab, de=0, a=1):
    if tab[a] == 0 and tab[de] == joueur:
        if a in deplacement_possible[de] :
            tab[a] = tab[de]
            tab[de] = 0


def tour(tab):
    while True:
        if tab.count(0) > 3:
            sur = int(input("Sur"))
            placement(tab, sur=sur)
        else:
            de = int(input("De"))
            a = int(input("a"))
            deplacement(tab, de=de, a=a)
        
        if verifie_victoire(tab):
            break
        changer_joueur()
        afficher(tab)
    

def verifie_victoire(tab):
    for sub in victoire_possible:
        if tab[sub[0]] == tab[sub[1]] == tab[sub[2]] and tab[sub[0]] != 0:
            print("victoire")
            return True


def main():
    global deplacement_possible, victoire_possible, joueur
    deplacement_possible = [
        [1, 3, 4], [0, 2, 4], [1, 5, 4],
        [0, 6, 4], [0, 1, 2, 3, 5, 6, 7, 8], [2, 8, 4],
        [3, 7, 4], [6, 8, 4], [5, 7, 4]
        ]
    
    victoire_possible = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    tab = creer_tableau()
    joueur = 1
    tour(tab)
    


if __name__ == '__main__': main()

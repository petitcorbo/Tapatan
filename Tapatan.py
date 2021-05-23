#########################
# Projet Tapatan DLBI   #
#########################
# Marwane Grosjacques   #
# Alexandre Mihet       #
# Sarah Louis El Khoury #
# Eryne Guenet          #
# Emma Leroy pardonche  #
#########################

# https://github.com/uvsq22006204/Tapatan #


## Importation ##

import tkinter as tk

## Parametres ##

Longueur, Hauteur = 700, 700 # Du canevas

taille = 2 * Hauteur / 3 # Taille du plateau
rayon = 30 # Rayon des intersections

couleur_canevas = "white"
couleur_intersection = "grey"
couleur_joueurs = {1: "red", 2: "blue"}

## Variables ##

x, y = Longueur / 2, Hauteur / 2 # Milieu du canevas
disposition_jetons = []

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

## Fonctions ##

def creer_plateau():
    Canevas.create_line(50,y,Longueur-50,y,fill="black",width=4)
    Canevas.create_line(50,50,Longueur-50,50,fill="black",width=4)
    Canevas.create_line(50,50,50,Hauteur-50,fill="black",width=4)
    Canevas.create_line(50,50,Longueur-50,Hauteur-50,fill="black",width=4)
    Canevas.create_line(50,Hauteur-50,Longueur-50, Hauteur-50,fill="black",width=4)
    Canevas.create_line(Longueur-50,50,Longueur-50,Hauteur-50,fill="black",width=4)
    Canevas.create_line(50,Hauteur-50,Longueur-50,50,fill="black",width=4)
    Canevas.create_line(x,50,x, Hauteur-50,fill="black",width=4)


def creer_intersections():
    intersections = []
    intersections.append(Canevas.create_oval(50-rayon,50-rayon, 50+rayon, 50+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(x-rayon,50-rayon,x+rayon, 50+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(Longueur-50-rayon,50-rayon,Longueur-50+rayon,50+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(50-rayon,y-rayon, 50+rayon, y+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(x-rayon,y-rayon,x+rayon, y+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(Longueur-50-rayon,y-rayon,Longueur-50+rayon,y+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(50-rayon,Hauteur-50-rayon, 50+rayon, Hauteur-50+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(x-rayon,Hauteur-50-rayon,x+rayon, Hauteur-50+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(Longueur-50-rayon,Hauteur-50-rayon,Longueur-50+rayon,Hauteur-50+rayon, fill=couleur_intersection,width=4))
    return intersections


def actualiser_tableau():
    global disposition_jetons
    for p in disposition_jetons:
        Canevas.delete(p)
    disposition_jetons = []
    for i, pion in enumerate(tab):
        if pion == 1:
            p = Canevas.create_oval(Canevas.coords(intersections[i]), fill="red", width=4, tags="pion")
            disposition_jetons.append(p)
        elif pion == 2:
            p = Canevas.create_oval(Canevas.coords(intersections[i]), fill="blue", width=4, tags="pion")
            disposition_jetons.append(p)


def actualiser_historique():
    historique.append(tab.copy())


def changer_joueur():
    global joueur
    if joueur == 1:
        joueur = 2
    elif joueur == 2:
        joueur = 1


def tour():
    actualiser_tableau()
    if verifie_victoire():
        Mafenetre.after(2000, recommencer_manche)
        return
    actualiser_historique()
    if verifie_egalite():
        Mafenetre.after(2000, recommencer_manche)
        return
    changer_joueur()
    label_tour.config(text="C'est au tour du joueur " + str(joueur), fg=couleur_joueurs[joueur])
    if tab.count(0) == 3:
        Canevas.unbind("<Button-1>")
        Canevas.tag_bind("pion", "<Button-1>", deplacement_clic)


# Placement #

def clic_placement(event):
    """les joueurs posent un jeton a tour de role sur une intersection libre du plateau"""
    for i, inter in enumerate(intersections):
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3]:
            placement(i)


def placement(sur=0):
    if tab[sur] == 0:
        tab[sur] = joueur
        tour()


# Deplacement #

def deplacement_clic(event):
    actualiser_tableau()
    for i, inter in enumerate(intersections):
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3]:
            pion = Canevas.find_closest(event.x, event.y)[0]
            Canevas.itemconfig(pion, outline="green")
            Canevas.bind("<Button-1>", lambda event, i=i: deplacement_clic_bis(event, i))


def deplacement_clic_bis(event, i):
    for j, inter in enumerate(intersections):
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3]:
            deplacement(i, j)


def deplacement(de=0, a=1):
    if tab[a] == 0 and tab[de] == joueur:
        if a in deplacement_possible[de] :
            tab[a] = tab[de]
            tab[de] = 0
            tour()


# Victoire / Egalité #

def verifie_victoire():
    for sub in victoire_possible:
        if tab[sub[0]] == tab[sub[1]] == tab[sub[2]] and tab[sub[0]] != 0:
            label_tour.config(text="Victoire du joueur " + str(joueur), fg=couleur_joueurs[joueur])
            score[joueur-1] += 1
            return True


def verifie_egalite():
    if historique.count(tab) == 3:
            label_tour.config(text="Egalité")
            return True

# Sauvegarde / Chargement #

def sauvegarder():
    """Sauvegarde la partie en cour"""
    pass


def charger():
    """Charge une partie à partir d'unf fichier"""
    pass


# Menu #

def recommencer_partie():
    """Recommence une nouvelle partie"""
    global score
    score = [0, 0]
    recommencer_manche()


def recommencer_manche():
    """Recommence une nouvelle manche"""
    global joueur, tab, historique
    joueur = 1
    tab = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    historique = []
    actualiser_tableau()
    label_tour.config(text="C'est au tour du joueur " + str(joueur), fg=couleur_joueurs[joueur])
    label_score_1.config(text="Joueur 1: " + str(score[0]))
    label_score_2.config(text="Joueur 2: " + str(score[1]))


def quitter():
    Mafenetre.quit()


## GUI ##

Mafenetre = tk.Tk()
Mafenetre.title("Jeu du Tapatan")
Mafenetre.resizable(False, False)

# Canevas #
Canevas = tk.Canvas(Mafenetre, width=Longueur, height=Hauteur, bg=couleur_canevas)
Canevas.bind("<Button-1>", clic_placement)
Canevas.grid(row=1, column=0, rowspan=7)

# Plateau #
creer_plateau()
intersections = creer_intersections()
intersections_bis = intersections.copy()

# Menu #
menu = tk.Label(Mafenetre, text="MENU", font=("bold", 50))
menu.grid(row=0, column=1)

bouton_sauvegarder = tk.Button(Mafenetre, text="Sauvegarder", font=("bold", 30), command=sauvegarder, relief="groove")
bouton_sauvegarder.grid(row=1, column=1, sticky="ew")

bouton_recharger = tk.Button(Mafenetre, text="Recharger", font=("bold", 30), command=charger, relief="groove")
bouton_recharger.grid(row=2, column=1, sticky="ew")

bouton_recommencer = tk.Button(Mafenetre, text="Recommencer", font=("bold", 30), command=recommencer_partie, relief="groove")
bouton_recommencer.grid(row=3, column=1, sticky="ew")

bouton_quitter = tk.Button(Mafenetre, text="Quitter", font=("bold", 30), command=quitter, relief="groove")
bouton_quitter.grid(row=4, column=1, sticky="ew")

label_tour = tk.Label(Mafenetre, text="C'est au tour du joueur 1",  font=("bold", 30))
label_tour.grid(row=0, column=0)

label_score = tk.Label(Mafenetre, text="SCORE",  font=("bold", 30, "underline"))
label_score.grid(row=5, column=1)

label_score_2 = tk.Label(Mafenetre, text="Joueur 1: 0",  font=("bold", 30))
label_score_2.grid(row=6, column=1)

label_score_1 = tk.Label(Mafenetre, text="Joueur 2: 0",  font=("bold", 30))
label_score_1.grid(row=7, column=1)


recommencer_partie()

## Fin ##
Mafenetre.mainloop()

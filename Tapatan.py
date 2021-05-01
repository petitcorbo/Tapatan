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

## Variables ##

x, y = Longueur / 2, Hauteur / 2 # Milieu du canevas
disposition_jetons = []
compteur = 0

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
    intersections.append(Canevas.create_oval(Longueur-50-rayon,y-rayon,Longueur-50+rayon,y+rayon, fill=ouleur_intersection,width=4))
    intersections.append(Canevas.create_oval(50-rayon,Hauteur-50-rayon, 50+rayon, Hauteur-50+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(x-rayon,Hauteur-50-rayon,x+rayon, Hauteur-50+rayon, fill=couleur_intersection,width=4))
    intersections.append(Canevas.create_oval(Longueur-50-rayon,Hauteur-50-rayon,Longueur-50+rayon,Hauteur-50+rayon, fill=couleur_intersection,width=4))
    return intersections



# Placement #

def placement(event):
    """les joueurs posent un jeton a tour de role sur une intersection libre du plateau"""
    global compteur, disposition_jetons
    
    if compteur%2 != 0:
        couleurjeton = "blue"
    else:
        couleurjeton = "red"
    
    for inter in intersections:
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3] and compteur < 6:
            compteur += 1
            disposition_jetons.append(Canevas.create_oval(Canevas.coords(inter), fill=couleurjeton))
            intersections.remove(inter)
            tour.config(text="C'est au tour du joueur "+ str(compteur%2 +1))


# Deplacement #

def deplacement():
    pass


# Sauvegarde / Chargement #

def sauvegarder():
    """Sauvegarde la partie en cour"""
    pass


def charger():
    """Charge une partie à partir d'unf fichier"""
    pass


# Menu #

def recommencer():
    """Recommence une nouvelle partie"""
    global disposition_jetons, compteur, intersections
    compteur = 0
    for jeton in disposition_jetons:
        Canevas.delete(jeton)
    intersections = intersections_bis.copy()
    tour.config(text="C'est au tour du joueur 1")


def quitter():
    Mafenetre.quit()


## GUI ##

Mafenetre = tk.Tk()
Mafenetre.title("Jeu du Tapatan")
Mafenetre.resizable(False, False)

# Canevas #
Canevas = tk.Canvas(Mafenetre, width=Longueur, height=Hauteur, bg=couleur_canevas)
Canevas.bind("<Button-1>", placement)
Canevas.grid(row=1, column=0, rowspan=5)

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

bouton_recommencer = tk.Button(Mafenetre, text="Recommencer", font=("bold", 30), command=recommencer, relief="groove")
bouton_recommencer.grid(row=3, column=1, sticky="ew")

bouton_quitter = tk.Button(Mafenetre, text="Quitter", font=("bold", 30), command=quitter, relief="groove")
bouton_quitter.grid(row=4, column=1, sticky="ew")

tour = tk.Label(Mafenetre, text="C'est au tour du joueur 1",  font=("bold", 30))
tour.grid(row=0, column=0)

## Fin ##
Mafenetre.mainloop()

#########################
# Projet Tapatan DLBI   #
#########################
# Marwane Grosjacques   #
# Alexandre Mihet       #
# Sarah Louis El Khoury #
# Eryne Guenet          #
# Emma Leroy pardonche  #
#########################

"https://github.com/uvsq22006204/Tapatan"

'''
[0]–[1]–[2]
 | \ | / |
[3]–[4]–[5]
 | / | \ |
[6]–[7]–[8]
'''

# Importation #

import tkinter as tk
from tkinter import filedialog
import random

# Parametres #

Longueur, Hauteur = 700, 700  # Du canevas

taille = 3 * Hauteur // 8  # Taille du plateau
rayon = 25  # Rayon des intersections
epaisseur = 2  # Des lignes

couleur_joueurs = {1: "red", 2: "blue"}
couleur_fg = 'white'
couleur_bg = 'black'
couleur_afg = 'white'
couleur_abg = 'grey'
couleur_intersection = 'black'

bouton_bd = 3
bouton_relief = 'groove'
font = ('bold', '30')

# Variables #

x, y = Longueur / 2, Hauteur / 2  # Milieu du canevas
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

# Fonctions #


def creer_plateau():
    '''Crée les lignes du plateau'''
    s = taille
    w = epaisseur

    Canevas.create_rectangle(x - s, y - s, x + s, y + s, outline=couleur_fg, fill=couleur_bg, width=w)
    Canevas.create_line(x, y - s, x, y + s, fill=couleur_fg, width=w)  # | #
    Canevas.create_line(x - s, y, x + s, y, fill=couleur_fg, width=w)  # - #
    Canevas.create_line(x - s, y + s, x + s, y - s, fill=couleur_fg, width=w)  # / #
    Canevas.create_line(x - s, y - s, x + s, y + s, fill=couleur_fg, width=w)  # \ #


def creer_intersections():
    '''Crée les intersections où l'on peut placer les pions'''
    s = taille
    w = epaisseur
    r = rayon

    intersections = []
    for n in range(9):
        x_o, y_o = x - s + s * (n % 3), y - s + s * (n // 3)
        inter = Canevas.create_oval(x_o - r, y_o - r, x_o + r, y_o + r, outline=couleur_fg, fill=couleur_bg, width=w)
        intersections.append(inter)
    return intersections


def actualiser_tableau():
    '''Actualise le tableau selon la variable tab'''
    global disposition_jetons
    for p in disposition_jetons:  # Enleve tous les pions
        Canevas.delete(p)

    disposition_jetons = []
    for i, pion in enumerate(tab):  # Pose tous les pions
        if pion == 1:
            p = Canevas.create_oval(Canevas.coords(intersections[i]), outline=couleur_fg, fill="red", width=2, tags="pion")
            disposition_jetons.append(p)
        elif pion == 2:
            p = Canevas.create_oval(Canevas.coords(intersections[i]), outline=couleur_fg, fill="blue", width=2, tags="pion")
            disposition_jetons.append(p)


def actualiser_historique():
    historique.append(tab.copy())


def changer_joueur():
    '''Passe du joueur 1 au joueur 2 et inversement'''
    global joueur
    if joueur == 1:
        joueur = 2
    elif joueur == 2:
        joueur = 1


def tour():
    '''Assemble les différentes fonctions nécessaires pour faire un tour'''
    actualiser_tableau()
    if verifie_victoire():
        Canevas.unbind('<Button-1>')
        Canevas.tag_unbind('pion', '<Button-1>')
        score[joueur - 1] += 1

        if score[joueur - 1] == 3:
            Canevas.itemconfig(label_tour, text="Le joueur " + str(joueur) + " a gagné la partie!", fill=couleur_joueurs[joueur])
            racine.after(2000, menu)
        else:
            Canevas.itemconfig(label_tour, text="Le joueur " + str(joueur) + " a gagné la manche.", fill=couleur_joueurs[joueur])
            racine.after(2000, recommencer_manche)
        return

    actualiser_historique()
    if verifie_egalite():
        Canevas.unbind('<Button-1>')
        Canevas.tag_unbind('pion', '<Button-1>')
        Canevas.itemconfig(label_tour, text="Egalité", fill=couleur_fg)
        racine.after(2000, recommencer_manche)
        return

    changer_joueur()
    Canevas.itemconfig(label_tour, text="C'est au tour du joueur " + str(joueur), fill=couleur_joueurs[joueur])
    if IA_1.get() and (joueur == 1):
        IA()
    elif IA_2.get() and (joueur == 2):
        IA()
    elif tab.count(0) == 3:
        Canevas.unbind("<Button-1>")
        Canevas.tag_bind("pion", "<Button-1>", deplacement_clic)


# Placement #


def clic_placement(event):
    '''Recupere l'emplacement cliqué puis place un pion à cet emplacement'''
    for i, inter in enumerate(intersections):
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3]:
            placement(i)


def placement(sur=0):
    '''Place le pion d'un joueur a l'emplacement donné si possible'''
    if tab[sur] == 0:
        tab[sur] = joueur
        tour()
        return True
    return False


# Deplacement #


def deplacement_clic(event):
    '''Premier clique: Recupere l'emplacement initial d'un pion puis attend un deuxième clique'''
    actualiser_tableau()
    for i, inter in enumerate(intersections):
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3]:
            pion = Canevas.find_closest(event.x, event.y)[0]
            Canevas.itemconfig(pion, outline="green2")
            Canevas.bind("<Button-1>", lambda event, i=i: deplacement_clic_bis(event, i))


def deplacement_clic_bis(event, i):
    '''Deuxième clique: recupere l'emplacement final et deplace le pion'''
    for j, inter in enumerate(intersections):
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3]:
            deplacement(i, j)


def deplacement(de=0, a=1):
    '''Deplace un pion choisi a l'emplacement donné si possible'''
    if tab[a] == 0 and tab[de] == joueur:
        if a in deplacement_possible[de]:
            tab[a] = tab[de]
            tab[de] = 0
            tour()
            return True
    return False


# Victoire / Egalité #


def verifie_victoire():
    '''Renvoie True si il y a victoire'''
    for sub in victoire_possible:
        if tab[sub[0]] == tab[sub[1]] == tab[sub[2]] and tab[sub[0]] != 0:
            return True


def verifie_egalite():
    '''Renvoie True si il y a egalité'''
    if historique.count(tab) == 3:
        return True


# Sauvegarde / Chargement #


def sauvegarder():
    '''Sauvegarde la partie en cours dans un fichier'''
    pys = filedialog.asksaveasfile(mode='w', defaultextension='.pys')
    if pys is None:
        return

    pys.write(str(score[0]) + '\n')
    pys.write(str(score[1]) + '\n')
    pys.write(str(joueur) + '\n')
    for sub in historique:
        pys.write("".join([str(i) for i in sub]) + '\n')

    pys.close()


def charger():
    '''Charge une partie à partir d'un fichier'''
    global score, joueur, tab, historique

    pys = filedialog.askopenfile(title="Select save file", filetypes=(("Save files", '*.pys'), ("all files", '*.*')))
    if pys is None:
        return
    content = pys.readlines()

    score = [int(content[0]), int(content[1])]
    joueur = int(content[2])
    historique = []
    for sub in content[3:-1:]:
        tab = [int(i) for i in sub.strip()]
        actualiser_historique()
    tab = [int(i) for i in content[-1].strip()]

    pys.close()

    commencer(True)
    Canevas.bind('<Button-1>', clic_placement)
    Canevas.itemconfig(label_score_1, text=score[0] * "|", fill=couleur_joueurs[1])
    Canevas.itemconfig(label_score_2, text=score[1] * "|", fill=couleur_joueurs[2])


# IA #


def IA():
    '''
    IA:
    Détecte automatiquement si c'est la phase de placement ou de déplacement;
    L'IA joue un coup gagnant ou bloque un coup gagnant si il y en a;
    Sinon elle joue un coup aléatoire
    '''
    A = [i for i, sub in enumerate(tab) if sub == joueur]  # Pions de l'IA
    X = [i for i, sub in enumerate(tab) if sub == (joueur % 2 + 1)]  # Pions du joueur adverse

    if tab.count(joueur) < 3:  # Placement

        for sub in victoire_possible:

            inter = list(set(A).intersection(sub))
            if len(inter) == 2:

                for pos in sub:
                    if placement(pos):
                        print("IA gagne")
                        return

            inter = list(set(X).intersection(sub))
            if len(inter) == 2:

                for pos in sub:
                    if placement(pos):
                        print("IA bloque une victoire")
                        return

        else:
            print("IA joue aléatoirement")
            pos = 4
            while not placement(pos):
                pos = random.randint(0, 8)

    else:  # Deplacement

        for sub in victoire_possible:

            inter = list(set(A).intersection(sub))
            if len(inter) == 2:  # L'IA regarde si elle a une victoire proche

                for pos in A:
                    for f_p in sub:
                        if pos not in inter and f_p not in inter:
                            for move in deplacement_possible[pos]:
                                if move == f_p:
                                    if deplacement(pos, move):
                                        print("IA gagne")
                                        return

            inter = list(set(X).intersection(sub))
            if len(inter) == 2:  # L'IA regarde si l'adversaire a une victoire proche

                for pos in A:
                    for f_p in sub:
                        if f_p not in inter:
                            if deplacement(pos, f_p):
                                print("IA bloque une victoire")
                                return

        else:
            print("IA joue aléatoirement")
            pos = random.choices(A)[0]
            move = random.choices(deplacement_possible[pos])[0]

            while not deplacement(pos, move):
                pos = random.choices(A)[0]
                move = random.choices(deplacement_possible[pos])[0]


# Menu #

def recommencer_partie():
    '''Recommence une nouvelle partie'''
    global score
    score = [0, 0]
    recommencer_manche()


def recommencer_manche():
    '''Recommence une nouvelle manche'''
    global joueur, tab, historique
    if 'historique' in globals():
        joueur = (len(historique) % 2 + joueur) % 2 + 1
    else:
        joueur = 2
    tab = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    Canevas.bind('<Button-1>', clic_placement)
    Canevas.itemconfig(label_score_1, text=score[0] * "|", fill=couleur_joueurs[1])
    Canevas.itemconfig(label_score_2, text=score[1] * "|", fill=couleur_joueurs[2])
    historique = []
    tour()


def commencer(continuer=False):
    '''Commence ou continue une partie'''
    global intersections, intersections_bis
    global label_tour, label_score_1, label_score_2
    frame_main.grid_forget()

    creer_plateau()
    intersections = creer_intersections()
    intersections_bis = intersections.copy()

    label_tour = Canevas.create_text(x, 25, text="", font=font)
    label_score_1 = Canevas.create_text(Longueur // 4, Hauteur - 30, text="|||", font=font, fill=couleur_bg)
    Canevas.create_rectangle(Canevas.bbox(label_score_1), outline=couleur_fg)
    label_score_2 = Canevas.create_text(3 * Longueur // 4, Hauteur - 30, text="|||", font=font, fill=couleur_bg)
    Canevas.create_rectangle(Canevas.bbox(label_score_2), outline=couleur_fg)

    racine.bind('<Escape>', lambda evt: frame_pause.grid(row=0, column=0))

    if continuer:
        tour()
    else:
        recommencer_partie()


def reprendre():
    '''Quitte le menu pause'''
    frame_pause.grid_forget()


def menu():
    '''Reviens au menu principal'''
    racine.unbind('<Escape>')
    Canevas.unbind('<Button-1>')
    Canevas.tag_unbind('pion', '<Button-1>')
    Canevas.delete('all')
    frame_pause.grid_forget()
    frame_main.grid(row=0, column=0)


def quitter():
    '''Quitte le jeu'''
    racine.quit()


def main_menu():
    '''Création du menu principal'''
    global frame_main
    frame_main = tk.Frame(racine, bg=couleur_bg)

    tk.Label(
        frame_main, text="TAPATAN", bg=couleur_bg, fg=couleur_fg,
        font=('Yu Gothic', '40', 'underline'), relief='flat', pady=20
    ).grid(row=0, column=0, sticky='we')

    tk.Button(
        frame_main, command=commencer,
        text="Commencer", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=1, column=0, sticky='we')

    tk.Button(
        frame_main, command=charger,
        text="Charger", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=2, column=0, sticky='we')

    tk.Button(
        frame_main, command=quitter,
        text="Quitter", bg=couleur_bg, fg='red',
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=3, column=0, sticky='we')

    frame_main.grid(row=0, column=0)


def options():
    '''Création du menu d'options'''
    global IA_1, IA_2
    IA_1, IA_2 = tk.IntVar(), tk.IntVar()

    frame_option = tk.LabelFrame(frame_main, text="Ordinateur", bg=couleur_bg, fg=couleur_fg, font=font)

    tk.Checkbutton(
        frame_option, selectcolor='black', variable=IA_1,
        text="Joueur 1", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_bg, activeforeground=couleur_fg,
        font=font, bd=bouton_bd, relief='flat', justify='center'
    ).grid(row=0, column=0, sticky='we')

    tk.Checkbutton(
        frame_option, selectcolor='black', variable=IA_2,
        text="Joueur 2", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_bg, activeforeground=couleur_fg,
        font=font, bd=bouton_bd, relief='flat', justify='center'
    ).grid(row=1, column=0, sticky='we')

    frame_option.grid(row=4, column=0, sticky='we')


def pause():
    '''Création du menu pause'''
    global frame_pause
    frame_pause = tk.LabelFrame(racine, text="Pause", bg=couleur_bg, fg=couleur_fg, font=font)

    tk.Button(
        frame_pause, command=reprendre,
        text="Reprendre", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=1, column=0, sticky='we')

    tk.Button(
        frame_pause, command=sauvegarder,
        text="Sauvegarder", bg=couleur_bg, fg=couleur_fg,
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=2, column=0, sticky='we')

    tk.Button(
        frame_pause, command=menu,
        text="Menu", bg=couleur_bg, fg='red',
        activebackground=couleur_abg, activeforeground=couleur_afg,
        font=font, bd=bouton_bd, relief=bouton_relief
    ).grid(row=3, column=0, sticky='we')

    frame_pause.tkraise()


# Main #

racine = tk.Tk()
racine.title("Tapatan")
racine.resizable(False, False)

Canevas = tk.Canvas(racine, width=Longueur, height=Hauteur, bg=couleur_bg, bd=0)
Canevas.grid(row=0, column=0)

main_menu()
options()
pause()

racine.mainloop()

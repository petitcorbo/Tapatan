# Marwane Grosjacques
# Eryne Guenet
# Sarah Louis El Khoury
# Alexandre Mihet
# Emma le roy pardonche



import tkinter as tk



# Création de la fenêtre principale
Mafenetre = tk.Tk()
Mafenetre.title("Jeu du Tapatan")
# Création d'un widget Canvas
Longueur = 700
Hauteur = 700

x = Longueur / 2
y = Hauteur / 2

taille = 2*Hauteur / 3 # 200

rayon = 30

disposition_jetons =[]
compteur = 0
intersections = []


#Fonctions 
def sauvegarder():
    pass

def recharger():
    pass

def recommencer():
    global disposition_jetons, compteur, intersections
    compteur = 0
    for jeton in disposition_jetons:
        Canevas.delete(jeton)
    intersections = intersectionsbis.copy()
    tour.config(text="C'est au tour de : Joueur 1")

def quitter():
    Mafenetre.destroy()

def Placement(event):
    """les joueurs posent un jeton a tour de role sur une intersection libre du plateau"""
    global compteur, disposition_jeton

    if compteur%2 != 0:
        couleurjeton = "blue"
    else:
        couleurjeton = "red"
        
    for inter in intersections:
        if Canevas.coords(inter)[0] < event.x < Canevas.coords(inter)[2] and Canevas.coords(inter)[1] < event.y < Canevas.coords(inter)[3] and compteur < 6:
            compteur +=1
            disposition_jetons.append(Canevas.create_oval(Canevas.coords(inter), fill = couleurjeton))
            intersections.remove(inter)
            tour.config(text="C'est au tour de : Joueur "+ str(compteur%2 +1))

Canevas = tk.Canvas(Mafenetre, width = Longueur, height =Hauteur, bg ="white")
Canevas.bind()

Canevas.grid(row = 1, column = 0, rowspan = 5)

Canevas.create_line(50,y,Longueur-50,y,fill="black",width=4)

Canevas.create_line(50,50,Longueur-50,50,fill="black",width=4)

Canevas.create_line(50,50,50,Hauteur-50,fill="black",width=4)

Canevas.create_line(50,50,Longueur-50,Hauteur-50,fill="black",width=4)

Canevas.create_line(50,Hauteur-50,Longueur-50, Hauteur-50,fill="black",width=4)

Canevas.create_line(Longueur-50,50,Longueur-50,Hauteur-50,fill="black",width=4)

Canevas.create_line(50,Hauteur-50,Longueur-50,50,fill="black",width=4)

Canevas.create_line(x,50,x, Hauteur-50,fill="black",width=4)


intersections.append(Canevas.create_oval(50-rayon,50-rayon, 50+rayon, 50+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(x-rayon,50-rayon,x+rayon, 50+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(Longueur-50-rayon,50-rayon,Longueur-50+rayon,50+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(50-rayon,y-rayon, 50+rayon, y+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(x-rayon,y-rayon,x+rayon, y+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(Longueur-50-rayon,y-rayon,Longueur-50+rayon,y+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(50-rayon,Hauteur-50-rayon, 50+rayon, Hauteur-50+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(x-rayon,Hauteur-50-rayon,x+rayon, Hauteur-50+rayon, fill="grey",width=4))
intersections.append(Canevas.create_oval(Longueur-50-rayon,Hauteur-50-rayon,Longueur-50+rayon,Hauteur-50+rayon, fill="grey",width=4))

intersectionsbis = intersections.copy()

bouton_sauvegarder = tk.Button(Mafenetre, text="Sauvegarder", font=("bold", 30), command=sauvegarder, relief="groove")
bouton_recharger = tk.Button(Mafenetre, text="Recharger", font=("bold", 30), command=recharger,relief="groove")
bouton_recommencer = tk.Button(Mafenetre, text="Recommencer", font=("bold", 30), command=recommencer, relief="groove")
bouton_quitter = tk.Button(Mafenetre, text="Quitter", font=("bold", 30), command=quitter, relief="groove")

bouton_sauvegarder.grid(row=1, column=1, sticky="ew")
bouton_recharger.grid(row=2, column=1, sticky="ew")
bouton_recommencer.grid(row=3, column=1, sticky="ew")
bouton_quitter.grid(row=4, column=1, sticky="ew")

Canevas.bind("<Button-1>", Placement)
menu = tk.Label(Mafenetre, text="MENU", font=("bold", 50))
menu.grid(row=0, column=1)
tour = tk.Label(Mafenetre, text="C'est au tour de : Joueur 1",  font=("bold", 30))
tour.grid(row=0, column=0)
tk.Button(Mafenetre)




Mafenetre.mainloop()



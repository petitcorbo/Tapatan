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
Longueur = 500
Hauteur = 500

x = Longueur / 2
y = Hauteur / 2

taille = 2*Hauteur / 3 # 200

rayon = 30

Canevas = tk.Canvas(Mafenetre, width = Longueur, height =Hauteur, bg ="white")
Canevas.bind()

Canevas.grid(row =0, column = 0, rowspan = 1)

Canevas.create_line(50,y,Longueur-50,y,fill="black",width=4)

Canevas.create_line(50,50,Longueur-50,50,fill="black",width=4)

Canevas.create_line(50,50,50,Hauteur-50,fill="black",width=4)

Canevas.create_line(50,50,Longueur-50,Hauteur-50,fill="black",width=4)

Canevas.create_line(50,Hauteur-50,Longueur-50, Hauteur-50,fill="black",width=4)

Canevas.create_line(Longueur-50,50,Longueur-50,Hauteur-50,fill="black",width=4)

Canevas.create_line(50,Hauteur-50,Longueur-50,50,fill="black",width=4)

Canevas.create_line(x,50,x, Hauteur-50,fill="black",width=4)

Canevas.create_oval(50-rayon,50-rayon, 50+rayon, 50+rayon, fill="grey",width=4)

Canevas.create_oval(x-rayon,50-rayon,x+rayon, 50+rayon, fill="grey",width=4)

Canevas.create_oval(Longueur-50-rayon,50-rayon,Longueur-50+rayon,50+rayon, fill="grey",width=4)

Canevas.create_oval(50-rayon,y-rayon, 50+rayon, y+rayon, fill="grey",width=4)

Canevas.create_oval(x-rayon,y-rayon,x+rayon, y+rayon, fill="grey",width=4)

Canevas.create_oval(Longueur-50-rayon,y-rayon,Longueur-50+rayon,y+rayon, fill="grey",width=4)

Canevas.create_oval(50-rayon,Hauteur-50-rayon, 50+rayon, Hauteur-50+rayon, fill="grey",width=4)

Canevas.create_oval(x-rayon,Hauteur-50-rayon,x+rayon, Hauteur-50+rayon, fill="grey",width=4)

Canevas.create_oval(Longueur-50-rayon,Hauteur-50-rayon,Longueur-50+rayon,Hauteur-50+rayon, fill="grey",width=4)

menu = tk.Label(Mafenetre, text="MENU", font=("bold", 50))
menu.grid(row=0, column=1)


tk.Button(Mafenetre)

Mafenetre.mainloop()
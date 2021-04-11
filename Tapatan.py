# Marwane Grosjacques
# Eryne Guenet
# Lou Delattre
# Sarah Louis El Khoury
# Alexandre Mihet
# Emma le roy pardonche



import tkinter as tk



# Création de la fenêtre principale
Mafenetre = tk.Tk()
Mafenetre.title("Jeu du Tapatan")
# Création d'un widget Canvas
Largeur = 300
Hauteur = 300
Canevas = tk.Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ="white")

Canevas.bind()
Canevas.pack(padx =5, pady =5)
Canevas.create_line(0,150,300,150,fill="black",width=4)

Canevas.create_line(0,300,300,0,fill="black",width=4)

Canevas.create_line(150,300,150,0,fill="black",width=4)

Canevas.create_line(0,0,300,300,fill="black",width=4)

Canevas.create_line(0,4,300,4,fill="black",width=4)

Canevas.create_line(4,4,4,300,fill="black",width=4)

Canevas.create_line(300,0,300,300,fill="black",width=4)

Canevas.create_line(0,300,300,300,fill="black",width=4)


tk.Button(Mafenetre)

Mafenetre.mainloop()
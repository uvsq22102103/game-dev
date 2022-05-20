##############
# LIBRAIRIES #


import tkinter as tk
import random as rd


###########################
# VARIABLES ET CONSTANTES #


GRILLE = 50
DIM = 500
ECART = DIM/GRILLE
apple_c = [rd.randint(0,50), rd.randint(0,50)]
snake_c = [25,25]


#############
# FONCTIONS #


##########################################
# CORPS DU PROGRAMME + FENETRE GRAPHIQUE #

root = tk.Tk()
root.title("Snake")
canvas = tk.Canvas(root, height=DIM, width=DIM, bg= "#118811")
canvas.grid()

apple = canvas.create_oval(apple_c[0]*ECART,apple_c[1]*ECART,
                           apple_c[0]*ECART+ECART,apple_c[1]*ECART+ECART,
                           fill="red")

snake = canvas.create_oval(apple_c[0]*ECART,apple_c[1]*ECART,
                           apple_c[0]*ECART+ECART,apple_c[1]*ECART+ECART,
                           fill="red")

root.mainloop()
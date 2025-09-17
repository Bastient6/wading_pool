import turtle
toto = turtle . Screen ()
toto . bgcolor ("black")
titi = turtle . Turtle ()
titi . color ("red")
for i in range (3):
    titi . right (90)
    titi . circle (42)
toto . exitonclick ()

#va créer une fenêtre noir et va dessiner 3 cercle rouge chacun 
#deplacé de 90° et la page reste ouverte jusqu'à ce qu'un click soit fait.
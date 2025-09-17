import turtle

def draw_polygon(side):
    corner = 360 / side
    size = 1000 / side
    toto = turtle.Screen()
    toto.bgcolor("black")
    titi = turtle.Turtle()
    titi.color("red")
    for i in range(side):
        titi.forward(size)
        titi.right(corner)
    toto . exitonclick ()
    
draw_polygon(1000)
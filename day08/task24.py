import turtle

def draw_spiral():
    toto = turtle.Screen()
    toto.bgcolor("black")
    titi = turtle.Turtle()
    titi.color("red")
    for i in range(200):
        titi.forward(i)
        titi.right(10)
    toto.exitonclick ()
    
draw_spiral()
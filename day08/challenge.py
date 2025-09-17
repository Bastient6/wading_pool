import turtle

def draw_spiral():
    toto = turtle.Screen()
    toto.bgcolor("black")
    titi = turtle.Turtle()
    titi.color("red")
    for i in range(200):
        for j in range(4):
            titi.forward(i * 5)
            titi.right(90)
        titi.right(10)
    toto.exitonclick ()
    
draw_spiral()
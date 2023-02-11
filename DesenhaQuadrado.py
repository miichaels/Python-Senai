import turtle;
def desenhaQuadrado(t, tam):
    for i in range(4):
        t.forward(tam);
        t.left(90);
dq = turtle.Screen();
dq.bgcolor("lightgreen");
jan = turtle.Turtle();
desenhaQuadrado(jan, 50);
jan.penup();
jan.goto(100,100);
jan.pendown();
desenhaQuadrado(jan, 75);
dq.exitonclick();
import turtle
def desenhaBarra(t, altura):
    t.begin_fill(); #Comece preenchendo o perfil
    t.left(90)
    t.forward(altura);
    t.write(" " + str(altura));
    t.right(90);
    t.forward(40);
    t.right(90);
    t.forward(altura);
    t.left(90);
    t.end_fill(); #Para de preencher o perfil
xs = [48,117,200,240,160,260,220] #Aqui vão os dados
alturamax = max(xs);
numbarras = len(xs);
moldura = 10;
tess = turtle.Turtle();  #Crie tess e inicializa alguns de seus atributos
tess.color("blue");
tess.fillcolor("red");
tess.pensize(3);
wn = turtle.Screen();
wn.bgcolor("lightgreen");
wn.setworldcoordinates(0-moldura,0-moldura,40*numbarras+moldura,alturamax+moldura);
for a in xs:
    desenhaBarra(tess, a);
wn.exitonclick();

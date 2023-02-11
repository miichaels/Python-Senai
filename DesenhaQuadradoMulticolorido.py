import turtle
def desenhaQuadradoMulticolorido(t , tam):
    for i in ["red" , "purple", "hotpink", "blue"]:
        t.color(i);
        t.forward(tam);
        t.left(90);
dq = turtle.Screen();    #Inicializa a janela e seus atributos
dq.bgcolor("black");
tess = turtle.Turtle();   #Cria tess e seus atributos
tess.pensize(3);
tamanho = 20;           #Tamanho do menor quadrado
for i in range(22):
    desenhaQuadradoMulticolorido(tess, tamanho);
    tamanho = tamanho + 10;  #Aumenta o tamanho para a próxima vez
    tess.forward(10);        #Move tess um pouco à frente
    tess.right(18)           #e dá uma virada nela
dq.exitonclick();           
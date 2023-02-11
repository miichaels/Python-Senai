def variacao(arg, *vartup):
    print("Primeiro argumento: ", arg);
    for item in vartup:
        print("O outro argumento", item);
    return;
variacao(10);
variacao("Pão de Queijo", "Café");
variacao("Brincando", "Com os argumentos", "Seguindo mais ainda");

print("");
print("--------------------------------------------------------------");
print("");
#--------------------------------------------------------------


def imprimeLinha(numero):
    for n in range(1, numero +1):
        print((' {} ').format(n), end = '');
    print();

def imprimeSequencia(numero):
    for numero in range(numero + 1):
        imprimeLinha(numero);

numero = input("Digite um número: ");
imprimeSequencia(int(numero));
def valorPagamento():
    diario = [];

    while True:
        val = float(input("Valor da prestação: "));
        atr = int(input("Dias atrasados: "));
        multa = 0.03;
        multa_dia = 0.001 * atr
        total = int(val+(val*multa_dia)+(val*multa));
        print(f"O valor a ser pago é R${total}.");
        diario.append(total)

        continuar = input("Continuar? S/N: ").upper();
        if continuar == "N":
            break;

    
    print(f"As prestações pagas de hoje foram {diario}");
    print("Encerrado");

valorPagamento();
arquivo = open(input('Nome do arquivo a ser editado:'), 'r');
texto = arquivo.readlines();
texto.append(input("Insira o texto:"));
arquivo = open(input("Nome do arquivo a ser editado:"), "w");
arquivo.writelines(texto);
arquivo.close();

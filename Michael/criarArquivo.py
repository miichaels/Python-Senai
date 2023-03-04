arquivo = open('texto.txt', 'a') #Cria um arquivo dentro da pasta de destino do arquivo

arquivo.write('manipulando arquivos \n') #Escreve dentro do arquivo criado

varios = list();
varios.append("brincando \n");
varios.append("com manipulação \n");
varios.append("de arquivos \n");
varios.append("usando Python \n");

arquivo.writelines(varios);

arquivo = open("texto.txt", "r")
print(arquivo.readline()) #Le a primeira linha
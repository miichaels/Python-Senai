import os
diretorio = "C:/Users/Aluno/OneDrive - SESISENAISP - Escolas/Documentos/Michael/destino";
extencao = ".jfif";

for nomearquivo in os.listdir(diretorio):
    if nomearquivo.endswith(extencao):
        os.remove(os.path.join(diretorio, nomearquivo))
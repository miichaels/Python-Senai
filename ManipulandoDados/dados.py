import shutil
import os

origem = 'C:/Users/Aluno/OneDrive - SESISENAISP - Escolas/Documentos/Michael/origem';
destino = "C:/Users/Aluno/OneDrive - SESISENAISP - Escolas/Documentos/Michael/destino";
extencao = ".jfif";

for nomearquivo in os.listdir(origem):
    #if nomearquivo.endwith(extencao): 
        #origem = os.path.join(origem, nomearquivo)
        #destino = os.paths.join(destino, nomearquivo)
        shutil.copy(os.path.join(origem,nomearquivo), (os.path.join(destino, nomearquivo)))

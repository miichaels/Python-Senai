#importar o modulo
from pytube import YouTube, streams
from pytube.cli import on_progress

#Para inserir URL do vídeo do Youtube
link = input("Insira o link: ") # inserir o link entre as aspas

#mostrar o progresso de download
yt = YouTube(link, on_progress_callback= on_progress)

#mostrar o titulo do video
print("Titulo = ", yt.title)

#mostrar que o download iniciou
print("Baixando...")

#para baixar a maior resolução do vídeo
ys =yt.streams.get_highest_resolution()
ys.download()
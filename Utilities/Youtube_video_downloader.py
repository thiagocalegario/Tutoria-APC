from pytube import YouTube
# Função para baixar o vídeo
def baixar_video(url):
    try:
        # Cria uma instância do objeto YouTube com a URL do vídeo
        video = YouTube(url)

        # Seleciona o formato do vídeo a ser baixado (no exemplo, escolhemos o formato MP4)
        formato = video.streams.get_highest_resolution()

        # Define o local onde o vídeo será salvo (no exemplo, utilizamos o diretório atual)
        local_salvar = "/Users/IBM/Downloads/ytvideos"

        # Faz o download do vídeo
        formato.download(local_salvar)

        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro durante o download:", str(e))

# Exemplo de uso
url_video = input("Digite aqui o link do vídeo: ")  # Insira aqui a URL do vídeo que você deseja baixar
baixar_video(url_video)
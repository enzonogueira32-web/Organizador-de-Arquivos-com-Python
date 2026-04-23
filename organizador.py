import os
import shutil

pasta = input("Digite o Caminho da Pasta: ")

tipos_arquivos = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Documentos": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Audios": [".mp3", ".wav"]
}

# Criar pastas
for tipo in tipos_arquivos:
    os.makedirs(os.path.join(pasta, tipo), exist_ok=True)

os.makedirs(os.path.join(pasta, "Outros"), exist_ok=True)

arquivos = os.listdir(pasta)

for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_arquivo):
        nome, extensao = os.path.splitext(arquivo)

        movido = False

        for tipo, extensoes in tipos_arquivos.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(pasta, tipo, arquivo)
                shutil.move(caminho_arquivo, destino)
                movido = True
                break

        if not movido:
            destino = os.path.join(pasta, "Outros", arquivo)
            shutil.move(caminho_arquivo, destino)

print("Arquivos organizados com sucesso")
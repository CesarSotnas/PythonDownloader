from pytube import YouTube
import sys

link = input(str('Link para download: '))
print('Baixando link')
YouTube(link).streams.get_highest_resolution().download()


# É necessário ter esses pacotes instalados:
    # pip install pytube
    # pip install pywin32
    # pip install pyinstaller

# Após instalação, rodar o seguinte comando:
    # pyinstaller --onefile "nome do arquivo.py"
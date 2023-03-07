from tkinter import *

janela_inicial = Tk()
janela_inicial.title('Python Downloader')

# Mudando Ícone
janela_inicial.iconbitmap('./imagens/python_icon.ico') 
janela_inicial.geometry('450x400+200+100')
janela_inicial.resizable(True, True)

# Opções de dimensão e configração da janela:
# janela_inicial.minsize(450, 400)
# janela_inicial.maxsize(950, 700)
# janela_inicial.state('zoomed')
# janela_inicial.state('iconic')
# janela_inicial['bg'] = 'green'

def cmd_click(mensagem):
    print(mensagem)

# Criando botão
cmd = Button(janela_inicial, text = 'Executar', command = lambda: cmd_click('Nova mensagem'))
cmd.pack()

# Criando Label
label_1 = Label(janela_inicial, text = 'Este é o label 1')
label_1.pack()

janela_inicial.mainloop()
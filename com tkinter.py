import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import time

tempo_inicio = None

perguntas = [
    ("Qual a função do barramento de dados em um computador?", #P1
     {'A': "Controlar os dispositivos externos", 'B': "Gerenciar a execução de programas",
      'C': "Transportar informações entre os componentes", 'D': "Armazenar dados em cache"}, 'C'),

    ("Qual das alternativas representa corretamente um dos pilares do pensamento computacional?", #P2
     {'A': "Compactação de dados", 'B': "Análise estatística", 'C': "Decomposição", 'D': "Normalização"}, 'C'),

    ("Qual é a saída do seguinte código Python?\nprint(type([1,2,3]))", #P3
     {'A': "<class 'tuple'>", 'B': "<class 'int'>", 'C': "<class 'set'>", 'D': "<class 'list'>"}, 'D'),

    ("Qual das linguagens abaixo é mais usada para estruturar o conteúdo de páginas web?", #P4
     {'A': "HTML", 'B': "Python", 'C': "SQL", 'D': "JavaScript"}, 'A'),

    ("A abstração, no pensamento computacional, refere-se a:", #P5
     {'A': "Converter algoritmos em imagens", 'B': "Representar aspectos essenciais e ignorar os irrelevantes",
      'C': "Eliminar dados úteis do problema", 'D': "Transformar linguagem natural em linguagem de máquina"}, 'B'),

    ("Qual estrutura de controle em Python é usada para repetição com condição?", #P6
     {'A': "if", 'B': "def", 'C': "try", 'D': "while"}, 'D'),

    ("O que é a unidade lógica e aritmética (ULA)?", #P7
     {'A': "Parte do processador que executa operações matemáticas e lógicas", 'B': "Controlador de entrada e saída",
      'C': "Um registrador de propósito geral", 'D': "Um tipo de memória cache"}, 'A'),

    ("O que o seguinte trecho de código imprime?\nprint('oi'*3)", #P8
     {'A': "oioioi", 'B': "oi*3", 'C': "3oi", 'D': "Erro de execução"}, 'A'),

    ("Qual das tecnologias a seguir é usada para tornar páginas web interativas?", #P9
     {'A': "CSS", 'B': "XML", 'C': "JavaScript", 'D': "PHP"}, 'C'),

    ("Qual componente armazena temporariamente as instruções e dados usados pelo processador?", #P10
     {'A': "Disco rígido", 'B': "Cache", 'C': "Placa de vídeo", 'D': "Unidade de disco óptico"}, 'B')

#Mensagem para Simão: Se quiser adicionar mais perguntas, ve se bota na parte das imagens_perguntas,
#coloca um PhotoImage(file="Nome da imagem"),As imagem é sequencial, se quiser mudar alguma coisa ja deixei os P(perguntas) marcados.
#OBS: Dei espaço pras perguntas porque tava tudo muito junto
#Parte do codigo tem como base do canal do youtube do "Usando Python | João Futi Muanda", tutorial de como fazer um quiz,
#só peguei base dos botão e PhotoImage lá, e as background e font
#O Codemy.com tbm é um canal massa, mas ta em ingles, tem coisa de interface que vi lá, dá uma olhada tbm se tiver tempo


]


BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"
BUTTON_COLOR = "green"
BUTTON_TEXT_COLOR = "yellow"
FONT = ("Arial", 14, "bold")


janela = tk.Tk()
janela.title("Quiz de Programação")
janela.geometry("900x600")
janela.config(bg=BACKGROUND_COLOR)
janela.option_add('*font', 'arial')

imagens_perguntas = [
    PhotoImage(file="Dados.png"), #P1
    PhotoImage(file="pensamento.png"), #P2
    PhotoImage(file="programacao.png"), #P3
    PhotoImage(file="sites.png"), #P4
    PhotoImage(file="pensamento.png"), #P5
    PhotoImage(file="python.png"), #P6
    PhotoImage(file="Dados.png"), #P7
    PhotoImage(file="programacao2.png"), #P8
    PhotoImage(file="sites.png"), #P9
    PhotoImage(file="Dados.png") #P10
]

pergunta_atual = 0


app_icon = PhotoImage(file='IconeLogo.png')
app_label = tk.Label(janela, image=app_icon, bg=BACKGROUND_COLOR)
app_label.pack(pady=10)


imagem_pergunta_label = tk.Label(janela, bg=BACKGROUND_COLOR)
imagem_pergunta_label.pack()

tempo_label = tk.Label(janela, text="Tempo: 0s", bg=BACKGROUND_COLOR, fg="black", font=("Comic Sans", 18))


question_label = tk.Label(janela, text="", wraplength=650, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=FONT, justify="center")
question_label.pack(pady=20)
question_label.config(text="Bem-vindo ao Quiz de Programação!\nClique em 'Iniciar Quiz' para começar.")


frame_opcoes = tk.Frame(janela, bg=BACKGROUND_COLOR)

botoes = []
for i in range(4):
    btn = tk.Button(frame_opcoes, text="", width=35, height=5, wraplength=250,
                    bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Arial", 12, "bold"),
                    command=lambda i=i: verificar_resposta(i))
    botoes.append(btn)
    row = i // 2
    col = i % 2
    btn.grid(row=row, column=col, padx=30, pady=30)


btn_iniciar = tk.Button(janela, text="Iniciar Quiz", width=30, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,font=("Arial", 14, "bold"), command=lambda: iniciar_quiz())
btn_iniciar.pack(pady=5)

btn_creditos = tk.Button(janela, text="Créditos", width=30, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,font=("Arial", 14, "bold"), command=lambda: mostrar_creditos())
btn_creditos.pack(pady=5)

btn_recomecar = tk.Button(janela, text="Recomeçar", width=30, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,font=("Arial", 14, "bold"), command=lambda: iniciar_quiz())
btn_creditos.pack(pady=5)


def atualizar_tempo():
    if tempo_inicio is not None:
        tempo_atual = int(time.time() - tempo_inicio)
        minutos = tempo_atual // 60
        segundos = tempo_atual % 60
        tempo_label.config(text=f"Tempo: {minutos:02d}:{segundos:02d}")
        janela.after(1000, atualizar_tempo)



def iniciar_quiz():
    global pergunta_atual, tempo_inicio

    if tempo_inicio is None:
        tempo_inicio = time.time()

    pergunta_atual = 0
    btn_iniciar.pack_forget()
    btn_creditos.pack_forget()
    btn_recomecar.pack_forget()
    app_label.pack_forget()
    imagem_pergunta_label.pack()
    frame_opcoes.pack(pady=10)
    proxima_pergunta()
    tempo_label.place(x=10, y=10)
    atualizar_tempo()


def proxima_pergunta():
    global pergunta_atual
    if pergunta_atual < len(perguntas):
        pergunta, opcoes, _ = perguntas[pergunta_atual]
        question_label.config(text=pergunta)
        imagem_atual = imagens_perguntas[pergunta_atual]
        imagem_pergunta_label.config(image=imagem_atual)
        imagem_pergunta_label.image = imagem_atual

        keys = list(opcoes.keys())
        for i, btn in enumerate(botoes):
            chave = keys[i]
            btn.config(text=f"{chave}) {opcoes[chave]}", state=tk.NORMAL)
    else:
        finalizar_quiz()


def verificar_resposta(botao_idx):
    global pergunta_atual
    _, opcoes, correta = perguntas[pergunta_atual]
    keys = list(opcoes.keys())
    resposta_escolhida = keys[botao_idx]
    if resposta_escolhida == correta:
        pergunta_atual += 1
        proxima_pergunta()
    else:
        messagebox.showinfo("Resposta Incorreta", "Você errou! Infelizmente você vai recomeçar.")
        iniciar_quiz()


def finalizar_quiz():


    tempo_total = int(time.time() - tempo_inicio)
    minutos = tempo_total // 60
    segundos = tempo_total % 60

    question_label.config(text=f"Parabéns, você concluiu o Quiz! Fique feliz pelo que aprendeu.\nTempo Total do Quiz: {minutos} minutos e {segundos} segundos")
    for btn in botoes:
        btn.config(text="", state=tk.DISABLED)
    frame_opcoes.pack_forget()
    imagem_pergunta_label.pack_forget()
    btn_recomecar.pack(pady=10)
    app_label.pack(pady=10)
    tempo_label.place_forget()


def mostrar_creditos():
    tempo_label.place_forget()
    messagebox.showinfo("Créditos", "Desenvolvido por Guilherme e Guilherme\nUm é Guilherme Simão, e o Outro é Guilherme Marques")



frame_opcoes.pack_forget()

janela.mainloop()

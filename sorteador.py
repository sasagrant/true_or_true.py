import random
import tkinter as tk

perguntas = [
    "Mana você é ygona?",
    "Se pudesse jantar com qualquer pessoa no mundo, viva ou morta, quem seria?",
    "Se pudesse viajar para qualquer lugar agora, para onde iria?",
    "O que mais te atrai em uma pessoa?",
    "Se tivesse que escolher um filme para representar sua vida, qual seria?",
    "Qual foi o momento mais feliz da sua vida?",  
    "Qual é o seu maior medo?",  
    "O que você mais valoriza em uma amizade?",  
    "Se pudesse reviver um dia do seu passado, qual seria?",  
    "Qual foi a coisa mais louca que você já fez?",  
    "Se você pudesse ter um superpoder, qual seria?",  
    "Você acredita em destino ou coincidência?",  
    "Se você tivesse uma máquina do tempo, iria para o passado ou para o futuro?",  
    "O que você mudaria no mundo se pudesse?",  
    "Se sua vida fosse uma música, qual seria?",   
    "O que você mais gosta em você mesmo(a)?",  
    "Se fosse escrever uma carta para seu eu do passado, o que diria?",  
    "Qual habilidade você gostaria de aprender instantaneamente?",  
    "O que você acha que te torna único(a)?",  
    "Se pudesse viver em qualquer época da história, qual escolheria?",  
    "Qual é o seu maior sonho?",  
    "Se você ganhasse na loteria hoje, qual seria a primeira coisa que faria?",  
    "Qual memória da infância te faz sorrir até hoje?",  
    "Se você pudesse passar um dia na pele de outra pessoa, quem seria?",  
    "Você prefere planejar ou viver no improviso?",  
    "Qual foi o melhor conselho que já recebeu?",  
    "O que você gostaria que as pessoas lembrassem sobre você?",  
    "Se pudesse apagar um único momento da vida, apagaria?",  
    "Você acredita em vidas passadas?",  
    "Qual seria seu emprego dos sonhos, sem se preocupar com dinheiro?",  
    "Se você pudesse dominar qualquer instrumento musical, qual seria?",  
    "Qual personagem de filme ou série mais parece com você?",  
    "Qual sua maior realização até hoje?",  
    "Se pudesse mudar algo em você, mudaria?",  
    "Qual o hábito mais estranho que você tem?",  
    "Se pudesse viver em qualquer lugar do mundo, onde moraria?",  
    "Qual sua forma preferida de demonstrar carinho?",  
    "Se pudesse criar uma lei que todos tivessem que seguir, qual seria?",  
    "Qual foi o momento mais desafiador da sua vida?",  
    "Você prefere amar ou ser amado(a)?",  
    "Se você fosse um animal, qual seria e por quê?",  
    "Qual foi o melhor elogio que já recebeu?",  
    "O que mais te inspira no mundo?",  
    "Se sua vida fosse um livro, qual seria o enredo?",  
    "Você acredita em alma gêmea?",  
    "Se pudesse trocar de vida com alguém por um dia, quem seria?",  
    "O que você faz para se acalmar em momentos difíceis?",  
    "Qual foi a decisão mais importante que já tomou?",  
    "Se tivesse que escolher só uma comida para comer o resto da vida, qual seria?",  
    "Se o amor tivesse uma cor, qual seria pra você?",  
    "Você já se apaixonou à primeira vista?",  
    "Como você sabe que está apaixonado(a)?",  
    "Qual o gesto mais romântico que alguém já fez por você?",  
    "Qual o seu tipo de date perfeito?",  
    "Você acredita que os opostos se atraem?",  
    "O que você mais gosta de fazer a dois?",  
    "O que você considera uma traição?",  
    "Você acredita que amor à distância funciona?",  
    "O que faz você se sentir mais conectado(a) com alguém?",  
    "Você acha que existe 'a pessoa certa' ou somos nós que fazemos dar certo?",  
    "O que é mais importante para você: química ou conexão emocional?",  
    "Você já escreveu uma carta de amor?",  
    "Qual a sua maior prova de amor que já fez ou faria por alguém?",  
    "O que você procura em um relacionamento?",  
    "O que não pode faltar na parte emocional de um namoro?",  
    "Você prefere declarações públicas ou momentos íntimos?",  
    "Se pudesse descrever o amor em uma palavra, qual seria?",  
    "Qual música resume seu jeito de amar?",  
    "Você prefere muitos momentos pequenos ou um grande gesto romântico?",  
    "O que você mais sente falta quando está longe de quem ama?",  
    "Você acredita que o amor pode mudar uma pessoa?",  
    "Qual o momento mais marcante que já viveu em um relacionamento?",  
    "Qual foi seu primeiro crush famoso?",  
    "Você se considera ciumento(a)?",  
    "Qual seria o presente ideal que alguém poderia te dar?",   
    "Como você demonstra ciúmes quando sente?",  
    "Você acredita em reencontros do destino?",  
    "Você perdoaria uma traição?",  
    "O que mais te faz sentir saudade em um relacionamento?",  
    "Qual sua opinião sobre demonstrações de afeto em público?",  
    "Qual foi o elogio mais inesquecível que alguém já te fez?",  
    "Você acredita que amor de novela pode existir na vida real?",  
    "Você prefere intensidade ou estabilidade em um relacionamento?",  
    "Qual seria a viagem romântica dos seus sonhos?",  
    "Você já escreveu poesia ou texto inspirado em alguém que ama?",  
    "Você acredita que o primeiro amor nunca se esquece?",  
    "Como você imagina o amor daqui a 10 anos?",   
    "Qual parte do corpo você acha mais atraente em alguém?",  
    "Você acredita que tempo cura tudo?",  
]

perguntas_restantes = perguntas.copy()
perguntas_sorteadas = []

def sortear_pergunta():
    global perguntas_restantes, perguntas_sorteadas
    if not perguntas_restantes:
        perguntas_restantes = perguntas.copy()
        perguntas_sorteadas.clear()
    pergunta = random.choice(perguntas_restantes)
    perguntas_restantes.remove(pergunta)
    perguntas_sorteadas.append(pergunta)
    pergunta_label.config(text=pergunta)

def voltar_pergunta():
    if len(perguntas_sorteadas) > 1:
        pergunta_atual = perguntas_sorteadas.pop()
        perguntas_restantes.insert(0, pergunta_atual)
        pergunta_label.config(text=perguntas_sorteadas[-1])

root = tk.Tk()
root.title("Verdade ou Verdade")
root.geometry("1200x600")

fundo_imagem = tk.PhotoImage(file="D:/Avila/Área de Trabalho/true_or_true.py/capavv.png")
fundo_label = tk.Label(root, image=fundo_imagem)
fundo_label.place(relwidth=1, relheight=1)

titulo_label = tk.Label(root, text="VERDADE OU VERDADE?", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#000000")
titulo_label.pack(pady=10)

pergunta_label = tk.Label(root, text="Clique para sortear uma pergunta", wraplength=1000, 
                          font=("Calibri", 20, "bold"), pady=10, bg="#000000", fg="white")
pergunta_label.pack(pady=110)

botao_style = {"font": ("Calibri", 12, "bold"), "fg": "white", "bg": "#2b48ac", "activebackground": "#111111", "width": 20, "height": 0,
                "borderwidth": 5, "highlightthickness": 0, "padx": 0, "pady": 0, "bd": 5}

sortear_botao = tk.Button(root, text="Sortear Pergunta", command=sortear_pergunta, **botao_style)
sortear_botao.pack(pady=0)

voltar_botao = tk.Button(root, text="Voltar", command=voltar_pergunta, **botao_style)
voltar_botao.pack(pady=10)
root.mainloop()
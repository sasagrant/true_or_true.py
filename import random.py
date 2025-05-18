import random
import tkinter as tk

# Lista de perguntas
perguntas = [
    "Qual foi o momento mais feliz da sua vida?",
    "Se pudesse viajar para qualquer lugar agora, para onde iria?",
    "O que mais te atrai em uma pessoa?",
    "Se tivesse que escolher um filme para representar sua vida, qual seria?",
    "O que te faz sentir realmente vivo(a)?",
    "Se pudesse jantar com qualquer pessoa no mundo, viva ou morta, quem seria?",
    "Qual é o seu maior medo?",
    "O que você mais valoriza em uma amizade?",
    "Se pudesse reviver um dia do seu passado, qual seria?",
    "Qual foi a coisa mais louca que você já fez?"
]

# Listas para controle de perguntas
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

# Criar a interface gráfica
root = tk.Tk()
root.title("Sorteador de Perguntas")
root.geometry("600x400")
root.configure(bg="#2C3E50")  # Cor de fundo

# Adicionando imagem de fundo
bg_image = tk.PhotoImage(file="D:/Users/Avila/Downloads/viarcane.png")  # Insira o caminho correto da sua imagem
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Estilo do rótulo da pergunta
pergunta_label = tk.Label(root, text="Clique no botão para sortear uma pergunta", wraplength=500, 
                          font=("Arial", 14, "bold"), pady=20, bg="#2C3E50", fg="white")
pergunta_label.pack(pady=20)

# Estilo dos botões com bordas arredondadas e efeito de brilho
botao_style = {
    "font": ("Arial", 12, "bold"), 
    "fg": "white", 
    "bg": "#9B59B6",  # Roxo
    "activebackground": "#8E44AD",  # Cor do botão quando pressionado
    "activeforeground": "white",  # Cor do texto quando pressionado
    "relief": "flat",  # Remover bordas retas
    "borderwidth": 3,  # Borda mais espessa para destacar
    "highlightthickness": 0,  # Remover borda de destaque
    "width": 20, 
    "height": 2,
    "padx": 20, 
    "pady": 10
}

sortear_botao = tk.Button(root, text="Sortear Pergunta", command=sortear_pergunta, **botao_style)
sortear_botao.pack(pady=10)

voltar_botao = tk.Button(root, text="Voltar", command=voltar_pergunta, **botao_style)
voltar_botao.pack(pady=10)

root.mainloop()

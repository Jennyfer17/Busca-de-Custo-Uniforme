import tkinter as tk

def selecionar_opcao(opcao_selecionada):
    print(f"Opção selecionada: {opcao_selecionada}")

janela = tk.Tk()
janela.title("Exemplo de OptionMenu")

opcoes = ["Opção 1", "Opção 2", "Opção 3"]
opcao_var = tk.StringVar(janela)
opcao_var.set(opcoes[0])  # Valor padrão

# Criar o OptionMenu
option_menu = tk.OptionMenu(janela, opcao_var, *opcoes, command=selecionar_opcao)
option_menu.pack()

janela.mainloop()
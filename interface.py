import tkinter as tk
from tkinter import ttk
from main import buscar_caminho_otimo


class InterfaceUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Busca de Itinerário")

        # Variáveis para armazenar os dados inseridos pelo usuário
        self.criterio_var = tk.StringVar()
        self.peso_var = tk.DoubleVar()
        self.localidade1_var = tk.StringVar()
        self.localidade2_var = tk.StringVar()

        # Criar e posicionar os widgets na interface
        self.criar_widgets()

    def criar_widgets(self):
        # Rótulos
        tk.Label(self.root, text="Critério:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.root, text="Peso:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.root, text="Localidade 1:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.root, text="Localidade 2:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

        # Entradas
        ttk.Entry(self.root, textvariable=self.criterio_var).grid(row=0, column=1, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.peso_var).grid(row=1, column=1, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.localidade1_var).grid(row=2, column=1, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.localidade2_var).grid(row=3, column=1, padx=10, pady=5)

        # Botão para calcular o itinerário
        ttk.Button(self.root, text="Calcular Itinerário", command=self.calcular_itinerario).grid(row=4, column=0, columnspan=2, pady=10)

    def calcular_itinerario(self):
        # Obter os dados inseridos pelo usuário
        criterio = self.criterio_var.get()
        peso = self.peso_var.get()
        localidade1 = self.localidade1_var.get()
        localidade2 = self.localidade2_var.get()


        # Chamar a função para calcular o itinerário
        itinerario_otimo = buscar_caminho_otimo(localidade1, localidade2, peso, criterio)

        # Mostrar o itinerário na interface
        mostrar_itinerario(itinerario_otimo)


# Inicializar a interface
root = tk.Tk()
interface = InterfaceUsuario(root)
root.mainloop()

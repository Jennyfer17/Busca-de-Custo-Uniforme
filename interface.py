import tkinter as tk
from tkinter import ttk
from main import buscar_caminho_otimo


class InterfaceUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Busca de Itinerário")
        self.root.configure(bg='beige')

        # Variáveis para armazenar os dados inseridos pelo usuário
        
        self.criterio_var = tk.StringVar()
        self.peso_var = tk.DoubleVar()
        self.localidade1_var = tk.StringVar()
        self.localidade2_var = tk.StringVar()

        # Criar e posicionar os widgets na interface
        self.criar_widgets()

    def criar_widgets(self):
        # Rótulos
        tk.Label(self.root, text="Critério:",bg='beige').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.root, text="Peso:", bg='beige').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.root, text="Localidade 1:", bg='beige').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.root, text="Localidade 2:", bg='beige').grid(row=3, column=0, padx=10, pady=5, sticky="e")

        # Entradas
        #ttk.Entry(self.root, textvariable=self.criterio_var).grid(row=0, column=1, padx=10, pady=5)
        #ttk.Entry(self.root, textvariable=self.peso_var).grid(row=1, column=1, padx=10, pady=5)
        #ttk.Entry(self.root, textvariable=self.localidade1_var).grid(row=2, column=1, padx=10, pady=5)
        #ttk.Entry(self.root, textvariable=self.localidade2_var).grid(row=3, column=1, padx=10, pady=5)

        # Menus suspensos (OptionMenu)
        criterios_opcoes = ["C1", "C2", "C3"]  # Substitua com as opções reais
        teste = ttk.OptionMenu(self.root, self.criterio_var, criterios_opcoes[0], *criterios_opcoes).grid(row=0, column=1, padx=10, pady=5)
        #ttk.Entry(self.root, textvariable=self.peso_var).grid(row=1, column=1, padx=10, pady=5)
        pesos_opcoes = [1, 2,3,4,5]  # Substitua com as opções reais
        ttk.OptionMenu(self.root, self.peso_var, pesos_opcoes[0], *pesos_opcoes).grid(row=1, column=1, padx=10, pady=5)
        
        localidades_opcoes = ["beira", "inhambane", "maputo", "quelimane", "tete",
                              "xai-xai", "nampula", "dondo", "songo"] 
        ttk.OptionMenu(self.root, self.localidade1_var, localidades_opcoes[0], *localidades_opcoes).grid(row=2, column=1, padx=10, pady=5)
        ttk.OptionMenu(self.root, self.localidade2_var, localidades_opcoes[0], *localidades_opcoes).grid(row=3, column=1, padx=10, pady=5)

        # Botão para calcular o itinerário
        ttk.Button(self.root, text="Calcular Itinerário", command=self.calcular_itinerario).grid(row=4, column=0, columnspan=2, pady=10)

         # Botão para limpar o percurso
        ttk.Button(self.root, text="Limpar", command=self.limpar_percurso).grid(row=6, column=0, columnspan=2, pady=10)

        # Widget de texto para mostrar o percurso
        tk.Label(self.root, text="Percurso:", bg='#F0F0F0').grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.texto_percurso = tk.Text(self.root, height=4, width=50, wrap="word", bg='white', relief="solid", borderwidth=1)
        self.texto_percurso.grid(row=5, column=1, padx=10, pady=5, sticky="w")


    def calcular_itinerario(self):
        # Obter os dados inseridos pelo usuário
        criterio = self.criterio_var.get()
        peso = self.peso_var.get()
        localidade1 = self.localidade1_var.get()
        localidade2 = self.localidade2_var.get()


        # Chamar a função para calcular o itinerário
        itinerario_otimo = buscar_caminho_otimo(localidade1, localidade2, peso, criterio)

        percurso = '\n'.join(str(via) for via in itinerario_otimo)
        #self.percurso_var.set(percurso)

        # Limpar o texto existente no widget de texto
        self.texto_percurso.delete(1.0, tk.END)

        # Adicionar o percurso ao widget de texto
        self.texto_percurso.insert(tk.END, percurso + '\n')

        # Mostrar o itinerário na interface
        #mostrar_itinerario(itinerario_otimo) 


    def limpar_percurso(self):
        # Limpar o texto existente no widget de texto
        self.texto_percurso.delete(1.0, tk.END)

# Inicializar a interface
root = tk.Tk()
largura = 600
altura = 500
posicao_x = 100
posicao_y = 50
root.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")
interface = InterfaceUsuario(root)
root.mainloop()

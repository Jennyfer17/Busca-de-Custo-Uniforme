from Via import *
from Caracteristicas import *
from redeViaria import *
from queue import PriorityQueue
import csv

def calcular_Distancia(via):
    return via.distancia

def mostrar_itinerario(itinerario):
    if itinerario:
        print("O Itinerario optimo a seguir é: ")
        for via in itinerario:
            print(via)
    else:
        print("Itinerario nao encontrado")


rede_viaria = redeViaria()

def ler_Vias ():
    with open("Road_network.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            codigo = row["code"]
            localidade1 = row["local1"]
            localidade2 = row["local2"]
            distancia = float(row["distance"])
            piso = int(row["ground"])
            portagem = float(row["portage"])
            velocidade = float(row["speed"])
            
            rede_viaria.adicionar_via(Via(codigo, localidade1, localidade2, distancia, Caracteristicas(piso, portagem, velocidade)))

#funcao para calcular custo do Criterio 03
def calcular_custo(via):
    peso_distancia = 1
    peso_portagem = 0.1
    peso_velocidade_media = 0.01
    peso_consumo_medio = 0.05

    custo = (peso_distancia * via.distancia + 
            peso_portagem * via.caracteristicas.portagem + peso_velocidade_media * via.caracteristicas.velocidade_media +
            peso_consumo_medio * (via.distancia / via.caracteristicas.velocidade_media))
    return custo

#funcao de busca de custo uniforme
def buscar_caminho_otimo(localidade_inicial, localidade_final, piso, criterio):

    fila_prioridade = PriorityQueue()
    visitados = set()

    fila_prioridade.put((0, localidade_inicial, []))  # (custo, localidade, caminho)

    while not fila_prioridade.empty():
        custo_atual, local_atual, caminho_atual = fila_prioridade.get()

        if local_atual == localidade_final:
            return caminho_atual

        if local_atual in visitados:
            continue
        visitados.add(local_atual)

        if criterio == "C1":
            for via in rede_viaria.obter_vias_adjacentes_pela_distancia(local_atual):
                if via.caracteristicas.piso >= piso:
                    novo_custo = custo_atual + via.distancia
                    fila_prioridade.put((novo_custo, via.localidade2, caminho_atual + [(via.codigo, local_atual, via.localidade2)]))

        if criterio == "C2":
            for via in rede_viaria.obter_vias_adjacentes_pela_duracao(local_atual):
                if via.caracteristicas.piso >= piso:
                    novo_custo = custo_atual + via.distancia / via.caracteristicas.velocidade_media
                    fila_prioridade.put((novo_custo, via.localidade2, caminho_atual + [(via.codigo, local_atual, via.localidade2)]))

        if criterio == "C3":
            for via in rede_viaria.obter_vias_adjacentes_pelo_custo(local_atual):
                if via.caracteristicas.piso >= piso:
                    novo_custo = custo_atual + calcular_custo(via)
                    fila_prioridade.put((novo_custo, via.localidade2, caminho_atual + [(via.codigo, local_atual, via.localidade2)]))
    return None


# criterio = "C1"
# localidade_inicial = "Maputo"
# localidade_final = "Xai-xai"
# piso = 4
# # ler_Vias()
# # itinerario_otimo = buscar_caminho_otimo(localidade_inicial, localidade_final, piso, criterio)

# # # itinerario02 = calcular_itinerario02('dondo','beira','distancia')

# # mostrar_itinerario(itinerario_otimo)
# # mostrar_itinerario02(itinerario02)      

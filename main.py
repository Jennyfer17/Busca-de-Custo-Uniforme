from Via import *
from Caracteristicas import *
from redeViaria import *
from queue import PriorityQueue
# from interface import InterfaceUsuario

# vias = [Via('a4','beira','inhambane',65, Caract(5,500,130)),
#         Via('a1','beira','quelimane',70, Caract(5,500,130)),
#         Via('n1','beira','quelimane',70, Caract(5,500,90)),
#         Via('n109','beira','quelimane',60, Caract(5,0,70)),
#         Via('n10','beira','tete',50, Caract(5,500,130)),
#         Via('ip1', 'beira','xai-xai',30, Caract(2,0,60)),
#         Via('n6', 'quelimane','nampula',70, Caract(4,0,100)),
#         Via('n23', 'tete','maputo',130, Caract(3,0,80)),
#         Via('n35', 'tete','dondo',25, Caract(2,0,60)),
#         Via('ic1', 'tete','songo',55, Caract(3,0,80)),
#         Via('n31', 'xai-xai','tete',25, Caract(1,0,50)),
#         Via('ip1', 'xai-xai', 'songo',45, Caract(3,0,90)),
#         Via('n6', 'nampula', 'vilanculos',70, Caract(2,0,70)),
#         Via('n18', 'vilanculos','Inhambane',50, Caract(2,0,60)),
#         Via('n19', 'vilanculos','vilareal',40, Caract(2,0,60)),
#         Via('n35', 'dondo', 'Inhambane',40, Caract(2,0,60)),
#         Via('a4', 'Inharrime','Inhambane',40, Caract(1,400,120)),
#         Via('ip2', 'Inharrime','maputo', 65, Caract(2,0,60))]

# def calcular_itinerario(loc_inicial,loc_final,categoria):
#     fila = PriorityQueue()
#     fila.put((0,loc_inicial,[]))

#     while not fila.empty():
#         custo_atual, local_atual, caminho_atual = fila.get()

#         if local_atual == loc_final:
#             return caminho_atual
        
#         for via in vias:
#             if via.loc1 == local_atual:
#                 if categoria == 'distancia':
#                     novo_custo = custo_atual + calcular_Distancia(via)

#                 novo_caminho = caminho_atual + [(via.cod, via.loc1, via.loc2)]
#                 fila.put((novo_custo,via.loc2,novo_caminho))

#     return None

# def calcular_itinerario02(loc_inicial,loc_final,categoria):
#     fila = PriorityQueue()
#     fila.put((0,loc_inicial,[]))

#     while not fila.empty():
#         custo_atual, local_atual, caminho_atual = fila.get()

#         if local_atual == loc_final:
#             return caminho_atual
        
#         for via in vias:
#             if via.loc1 == local_atual:
#                 if categoria == 'distancia':
#                     novo_custo = custo_atual + calcular_Distancia(via)

#                 novo_caminho = caminho_atual + [(via.cod, via.loc2, via.loc1)]
#                 fila.put((novo_custo,via.loc1,novo_caminho))
#     return None

def calcular_Distancia(via):
    return via.distancia

# def mostrar_itinerario(itinerario):
#     if itinerario:
#         print("Itinerario optimo")
#         for via in itinerario:
#             print(via)
#     else:
#         print("Itinerario nao encontrado")
def mostrar_itinerario(itinerario):
    if itinerario:
        print("O Itinerario optimo a seguir é: ")
        for via in itinerario:
            print(via)
    else:
        print("Itinerario nao encontrado")


# def mostrar_itinerario02(itinerario):
#     if itinerario:
#         print("Itinerario optimo")
#         for via in itinerario:
#             print(via)
#     else:
#         print("Itinerario nao encontrado")

# Exemplo de uso
rede_viaria = redeViaria()

            #codigo, localidade1, localidade2, distancia, (piso, portagem, velocidade media)
via_a4 = Via('a4','beira','inhambane',65, Caracteristicas(5,500,130))
via_a1 = Via('a1','beira','quelimane',70, Caracteristicas(5,500,130))

rede_viaria.adicionar_via(via_a4)
rede_viaria.adicionar_via(via_a1)
rede_viaria.adicionar_via(Via('a4','maputo','inhambane',80, Caracteristicas(5,500,130)))
rede_viaria.adicionar_via(Via('a1','inhambane','tete',70, Caracteristicas(2,500,130)))
rede_viaria.adicionar_via(Via('n1','beira','quelimane',70, Caracteristicas(5,500,90)))
rede_viaria.adicionar_via(Via('n109','maputo','inhambane',60, Caracteristicas(5,300,70)))
rede_viaria.adicionar_via(Via('n10','beira','tete',50, Caracteristicas(5,500,130)))
rede_viaria.adicionar_via(Via('ip1', 'beira','xai-xai',30, Caracteristicas(2,0,60)))
rede_viaria.adicionar_via(Via('n6', 'quelimane','nampula',70, Caracteristicas(4,0,100)))
rede_viaria.adicionar_via(Via('n23', 'tete','maputo',130, Caracteristicas(3,0,80)))
rede_viaria.adicionar_via(Via('n35', 'tete','dondo',25, Caracteristicas(2,0,60)))
rede_viaria.adicionar_via(Via('ic1', 'tete','songo',55, Caracteristicas(3,0,80)))



def calcular_custo(via):
    # Parâmetros de ponderação (podem ser ajustados conforme necessário)
    peso_distancia = 1
    peso_portagem = 0.1
    peso_velocidade_media = 0.01
    peso_consumo_medio = 0.05

    custo = (peso_distancia * via.distancia + 
            peso_portagem * via.caracteristicas.portagem + peso_velocidade_media * via.caracteristicas.velocidade_media +
            peso_consumo_medio * (via.distancia / via.caracteristicas.velocidade_media))
    return custo


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
# itinerario = calcular_itinerario('maputo','tete','distancia')
criterio = "C3"
localidade_inicial = "maputo"
localidade_final = "inhambane"
piso = 3
itinerario_otimo = buscar_caminho_otimo(localidade_inicial, localidade_final, piso, criterio)

# itinerario02 = calcular_itinerario02('dondo','beira','distancia')

mostrar_itinerario(itinerario_otimo)
# mostrar_itinerario02(itinerario02)      

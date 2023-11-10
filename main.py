from Via import *
from Caract import *
from queue import PriorityQueue

vias = [Via('a4','beira','inhambane',65, Caract(5,500,130)),
        Via('a1','beira','quelimane',70, Caract(5,500,130)),
        Via('n1','beira','quelimane',70, Caract(5,500,90)),
        Via('n109','beira','quelimane',60, Caract(5,0,70)),
        Via('n10','beira','tete',50, Caract(5,500,130)),
        Via('ip1', 'beira','xai-xai',30, Caract(2,0,60)),
        Via('n6', 'quelimane','nampula',70, Caract(4,0,100)),
        Via('n23', 'tete','maputo',130, Caract(3,0,80)),
        Via('n35', 'tete','dondo',25, Caract(2,0,60)),
        Via('ic1', 'tete','songo',55, Caract(3,0,80)),
        Via('n31', 'xai-xai','tete',25, Caract(1,0,50)),
        Via('ip1', 'xai-xai', 'songo',45, Caract(3,0,90)),
        Via('n6', 'nampula', 'vilanculos',70, Caract(2,0,70)),
        Via('n18', 'vilanculos','Inhambane',50, Caract(2,0,60)),
        Via('n19', 'vilanculos','vilareal',40, Caract(2,0,60)),
        Via('n35', 'dondo', 'Inhambane',40, Caract(2,0,60)),
        Via('a4', 'Inharrime','Inhambane',40, Caract(1,400,120)),
        Via('ip2', 'Inharrime','maputo', 65, Caract(2,0,60))]

def calcular_itinerario(loc_inicial,loc_final,categoria):
    fila = PriorityQueue()
    fila.put((0,loc_inicial,[]))

    while not fila.empty():
        custo_atual, local_atual, caminho_atual = fila.get()

        if local_atual == loc_final:
            return caminho_atual
        
        for via in vias:
            if via.loc1 == local_atual:
                if categoria == 'distancia':
                    novo_custo = custo_atual + calcular_Distancia(via)

                novo_caminho = caminho_atual + [(via.cod, via.loc1, via.loc2)]
                fila.put((novo_custo,via.loc2,novo_caminho))

    return None

def calcular_itinerario02(loc_inicial,loc_final,categoria):
    fila = PriorityQueue()
    fila.put((0,loc_inicial,[]))

    while not fila.empty():
        custo_atual, local_atual, caminho_atual = fila.get()

        if local_atual == loc_final:
            return caminho_atual
        
        for via in vias:
            if via.loc1 == local_atual:
                if categoria == 'distancia':
                    novo_custo = custo_atual + calcular_Distancia(via)

                novo_caminho = caminho_atual + [(via.cod, via.loc2, via.loc1)]
                fila.put((novo_custo,via.loc1,novo_caminho))
    return None

def calcular_Distancia(via):
    return via.dist

# def mostrar_itinerario(itinerario):
#     if itinerario:
#         print("Itinerario optimo")
#         for via in itinerario:
#             print(via)
#     else:
#         print("Itinerario nao encontrado")
def mostrar_itinerario(itinerario):
    if itinerario:
        print("Itinerario optimo")
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

itinerario = calcular_itinerario('dondo','beira','distancia')
itinerario02 = calcular_itinerario02('dondo','beira','distancia')

mostrar_itinerario(itinerario)
# mostrar_itinerario02(itinerario02)

       
        
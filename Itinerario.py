from queue import PriorityQueue

class Via:

    def __init__(self, cod, loc1, loc2, distancia):
        self.cod = cod
        self.loc1 = loc1
        self.loc2 = loc2
        self.distancia = distancia

    
vias = [Via('a4','maputo','beira',1), 
        Via('a1','maputo', 'nampula', 2),
        Via('b1','maputo','inhambane',10),
        Via('b2','beira','nampula',10), 
        Via('b3','beira','inhambane',3),
        Via('b3','nampula','inhambane',1)]

def calcular_itinerario(loc_inicial, loc_final):
    fila = PriorityQueue()
    fila.put((0,loc_inicial,[]))

    while not fila.empty():
        custo_atual, local_atual, caminho_atual = fila.get()

        if local_atual == loc_final:
            return caminho_atual
        
        for via in vias:
            if via.loc1 == local_atual:
                novo_custo = custo_atual + via.distancia
                novo_caminho = caminho_atual + [(via.cod, via.loc1, via.loc2)]

                fila.put((novo_custo, via.loc2, novo_caminho))

    return None

itinerario = calcular_itinerario('maputo','inhambane')

if itinerario:
    print("Itinerario Optimo")
    for via in itinerario:
        print(via)
else:
    print("Nao foi possivel encontrar itinerario.")


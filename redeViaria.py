class redeViaria:
    def __init__(self):
        self.vias = []

    def adicionar_via(self, via):
        self.vias.append(via)

    def obter_vias_adjacentes(self, localidade):
        return [via for via in self.vias if via.localidade1 == localidade]

    def obter_vias_adjacentes_pela_distancia(self, localidade):
            vias_adjacentes = [via for via in self.vias if via.localidade1 == localidade]
            vias_adjacentes_ordenadas = sorted(vias_adjacentes, key=lambda via: via.distancia)
            return vias_adjacentes_ordenadas
    
    def obter_vias_adjacentes_pela_duracao(self, localidade):
            vias_adjacentes = [via for via in self.vias if via.localidade1 == localidade]
            vias_adjacentes_ordenadas = sorted(vias_adjacentes, key=lambda via: via.distancia / via.caracteristicas.velocidade_media)        
            return vias_adjacentes_ordenadas
    
    def obter_vias_adjacentes_pelo_custo(self, localidade):
            vias_adjacentes = [via for via in self.vias if via.localidade1 == localidade]

            peso_distancia = 1
            peso_portagem = 0.1
            peso_velocidade_media = 0.01
            peso_consumo_medio = 0.05

            vias_adjacentes_ordenadas = sorted(vias_adjacentes, key=lambda via: (peso_distancia * via.distancia + 
            peso_portagem * via.caracteristicas.portagem + peso_velocidade_media * via.caracteristicas.velocidade_media +
            peso_consumo_medio * (via.distancia / via.caracteristicas.velocidade_media)))
            return vias_adjacentes_ordenadas

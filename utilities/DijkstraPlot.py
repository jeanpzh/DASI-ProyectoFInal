import heapq as h
class DijkstraPlot:
    def __init__(self, G, origen):
        self.G = G
        self.origen = origen
        self.pasos_finales = []  # Lista para almacenar las aristas finales del camino más corto
        self.descartados = []    # Lista para almacenar las aristas descartadas
        self.predecesores = {}   # Para rastrear el predecesor de cada nodo
        
    def get_shortest_path(self):
        distancias = {node: float('inf') for node in self.G}
        distancias[self.origen] = 0
        cola = []
        h.heappush(cola, (0, self.origen))
        visitados = {node: False for node in self.G}
        self.predecesores = {node: None for node in self.G}  # Inicializar los predecesores
        
        while cola:
            d, u = h.heappop(cola)
            if visitados[u]:
                continue
            visitados[u] = True
            for v, peso in self.G[u]:
                if not visitados[v]:
                    nueva_distancia = d + peso
                    if nueva_distancia < distancias[v]:
                        distancias[v] = nueva_distancia
                        self.predecesores[v] = u  
                        h.heappush(cola, (nueva_distancia, v))
                    else:
                        self.descartados.append((u, v))  
        
        return distancias

    def path_rebuild(self, destino):
        camino = []
        nodo_actual = destino
        while nodo_actual is not None and self.predecesores[nodo_actual] is not None:
            camino.append((self.predecesores[nodo_actual], nodo_actual))
            nodo_actual = self.predecesores[nodo_actual]
        camino.reverse()  # Revertir para obtener el camino desde el origen al destino
        return camino
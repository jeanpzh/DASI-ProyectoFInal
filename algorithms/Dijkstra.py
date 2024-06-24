import heapq as h
class Dijkstra:
    def __init__(self, G, origen, destino):
        self.G = G
        self.origen = origen
        
    def get_shortest_path(self):
        distancias = {node: float('inf') for node in self.G}
        distancias[self.origen] = 0
        cola = []
        h.heappush(cola, (0, self.origen))
        visitados = {node: False for node in self.G}
        
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
                        h.heappush(cola, (nueva_distancia, v))
                       
        return distancias




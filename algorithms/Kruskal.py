class Kruskal:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.conjunto = {i: i for i in graph.keys()}
        self.altura = {node: 0 for node in graph.keys()}
        self.solucion = []
        self.aristas = []

    def fusionar(self, u, v):
        raiz_u = self.buscar(u)
        raiz_v = self.buscar(v)
        if raiz_u != raiz_v:
            if self.altura[raiz_u] > self.altura[raiz_v]:
                self.conjunto[raiz_v] = raiz_u
            elif self.altura[raiz_u] < self.altura[raiz_v]:
                self.conjunto[raiz_u] = raiz_v
            else:
                self.conjunto[raiz_v] = raiz_u
                self.altura[raiz_u] += 1

    def buscar(self, k):
        if self.conjunto[k] != k:
            self.conjunto[k] = self.buscar(self.conjunto[k])
        return self.conjunto[k]

    def kruskal(self):
        self.aristas.sort(key=lambda x: x[2])  

        for u, v, peso in self.aristas:
            if self.buscar(u) != self.buscar(v):
                self.solucion.append((u, v, peso))
                self.fusionar(u, v)

        return self.solucion
    def lista_de_aristas(self):
        
        for nodo, adyacentes in self.graph.items():
            for adyacente, peso in adyacentes:
                if (adyacente, nodo, peso) not in self.aristas:  
                    self.aristas.append((nodo, adyacente, peso))
        return self.aristas
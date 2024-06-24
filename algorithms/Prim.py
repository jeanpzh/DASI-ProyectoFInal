
import heapq

class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.parent = {node: None for node in graph}
        self.key = { node: float('inf') for node in graph}
        self.mst_set = {node: False for node in graph}

    def prim(self):
    #
        start_node = next(iter(self.graph))
        self.key[start_node] = 0
        self.parent[start_node] = None
        pq = [(0, start_node)]
        while pq:
            _, u = heapq.heappop(pq)
            self.mst_set[u] = True

            for v, w in self.graph[u]:
                if not self.mst_set[v] and self.key[v] > w:
                    self.key[v] = w
                    self.parent[v] = u
                    heapq.heappush(pq, (w, v))

    def get_mst_edges(self):
        mst_edges = []
        for v, u in self.parent.items():
            if u is not None:
                mst_edges.append((u, v))
        return mst_edges





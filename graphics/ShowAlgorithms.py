
from algorithms.Prim import Prim
from utilities.DrawGraphics import draw_algorithm , draw_dijkstra
from utilities.DijkstraPlot import DijkstraPlot
from data.data import distritos , pos
from algorithms.Kruskal import Kruskal
def algorithms_options(option):
    
    if option == 1:
        P = Prim(distritos)
        P.prim()
        h = draw_algorithm(distritos, pos , P.get_mst_edges() , 'blue' , 11 , 'Prim algorithm')
        h
    elif option == 2:
        K = Kruskal(distritos)
        K.lista_de_aristas()
        K1 = K.kruskal()
        
        g = draw_algorithm(distritos, pos, K1 , 'red' , 11 , 'Kruskal algorithm')
        g
    elif option == 3:
        d = DijkstraPlot(distritos, "Santa Rosa" )
        d.get_shortest_path()
        pasos_finales = d.path_rebuild('Pucusana')
        descartados = d.descartados
        draw_dijkstra(distritos, pos, pasos_finales, descartados, 'blue', 'black', 10, 'Dijkstra Algorithm Result')
    else:
        print("Opcion no valida")
        return
    return

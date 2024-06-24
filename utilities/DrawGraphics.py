import matplotlib.pyplot as plt
import networkx as nx


def draw_algorithm(graph, pos, algorithm, color, font_size, title, delay=0.5):
    G = nx.Graph()
    
    for node, edges in graph.items():
        for adjacent, weight in edges:
            G.add_edge(node, adjacent, weight=weight)   
    
    plt.ion()  
    fig, ax = plt.subplots(figsize=(12, 12))
      
    
   
    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.state('zoomed') 
    
    for i in range(len(algorithm) + 1):
        plt.clf()  
        
        # Dibujar el grafo completo
        nx.draw(G, pos, with_labels=True, node_color='yellow', edge_color='black', node_size=700, font_size=font_size, font_weight='bold')
        
        # Dibujar las aristas del algoritmo hasta el paso actual
        nx.draw_networkx_edges(G, pos, edgelist=algorithm[:i], edge_color=color, width=2)
        
        # Dibujar etiquetas de las aristas
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.title(title)
        plt.pause(delay)
        
        # Verificar si la ventana ha sido cerrada
        if not plt.fignum_exists(fig.number):
            break
    
    plt.ioff()  # Modo interactivo off
    plt.show()


def draw_dijkstra(graph, pos, pasos_finales, descartados, color_final, color_descartado, font_size, title):
    G = nx.Graph()
    
    for node, edges in graph.items():
        for adjacent, weight in edges:
            G.add_edge(node, adjacent, weight=weight)   
    
 
    

    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.state('zoomed') 
    
    plt.clf() 
    
    # Dibujar el grafo completo
    nx.draw(G, pos, with_labels=True, node_color='yellow', edge_color='black', node_size=700, font_size=font_size, font_weight='bold')
    
    # Dibujar las aristas descartadas
    nx.draw_networkx_edges(G, pos, edgelist=descartados, edge_color=color_descartado, width=2, style='dashed')
    
    # Dibujar las aristas finales del camino más corto
    nx.draw_networkx_edges(G, pos, edgelist=pasos_finales, edge_color=color_final, width=2)
    
    # Dibujar etiquetas de las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title(title)
    plt.show()

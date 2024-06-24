import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utilities.AlgorithmCounter import test_kruskal, test_prim

def show_graphics(replicas):
    prim_times = []
    kruskal_times = []
    
    # Ejecutamos los algoritmos (kruskal y prim) y lo almacenamos en arrays 
    for _ in range(replicas):
        prim_times.append(test_prim())
        kruskal_times.append(test_kruskal())
    
    # Calculamos el promedio de los tiempos de ejecución de cada algoritmo, para tener un numero representativo
    prim_avg = sum(prim_times) / len(prim_times)
    kruskal_avg = sum(kruskal_times) / len(kruskal_times)
    
    # Promedio movil con ventana de tamaño 20 para suavizar la grafica
    w_size = 20
    w = np.ones(w_size)/w_size
    prim_mov_avg = np.convolve(prim_times,w, mode='valid')
    kruskal_mov_avg = np.convolve(kruskal_times, w, mode='valid')
    
    # Subplots para mostrar los resultados
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfico de barras para los promedios
    axs[0].bar(['Prim', 'Kruskal'], [prim_avg, kruskal_avg])
    axs[0].set_title('Tiempo de ejecución promedio')
    axs[0].set_ylabel('Tiempo')
    
    # Diagrama de promedio móvil
    axs[1].plot(prim_mov_avg, label='Prim')
    axs[1].plot(kruskal_mov_avg, label='Kruskal')
    axs[1].set_title('Promedio móvil de tiempos de ejecución')
    axs[1].set_ylabel('Tiempo')
    axs[1].legend()
    
    plt.tight_layout()
    plt.show()



from algorithms.Kruskal import Kruskal
from algorithms.Prim import Prim
from data.data import distritos 
import time

def counter_time(func, *args ):
    inicio = time.perf_counter()
    result = func(*args)  
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio:.8f} segundos")
    return fin - inicio

def prim_alg():
   prim = Prim(distritos)
   prim.prim()
   
def test_prim():
   return counter_time(prim_alg)

def test_kruskal():
   
   K = Kruskal(distritos)
   K.lista_de_aristas()
   return counter_time(K.kruskal)


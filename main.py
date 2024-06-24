from graphics.GraphicTime import show_graphics
from graphics.ShowAlgorithms import algorithms_options

if __name__ == '__main__':
   print("Selecciona una opción:")
   print("1. Visualizar algoritmos")
   print("2. Visualizar gráficos de tiempo")
   print("3. Cerrar")
   option = int(input())
   if option == 1:
       print("Selecciona un algoritmo:")
       print("1. Prim")
       print("2. Kruskal")
       print("3. Dijkstra")

       option2 = int(input())
       if option2 == 1:
           algorithms_options(1)
       elif option2 == 2:
           algorithms_options(2)
       elif option2 == 3:
           algorithms_options(3)
       else:
            print("Opción no válida")
   elif option == 2:
      print("Selecciona el numero de veces que desea ejecutar los algoritmos:")
      intentos = int(input())
      show_graphics(intentos)
   elif option == 3:
      print("Saliendo...")
   else:
      print("Opción no válida")
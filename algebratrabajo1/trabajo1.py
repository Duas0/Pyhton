import numpy as np

def matrizElevadoaN(adj_matrix, longitud):
    result_matrix = np.linalg.matrix_power(adj_matrix, longitud)
    return result_matrix

if __name__ == "__main__":
    grafoEnMatriz = np.array([[0, 1, 0, 1, 1],[1, 0, 1, 0, 0],[0, 1, 0, 1, 0],[1, 0, 1, 0, 1],[1, 0, 0, 1, 0]])
    nombreNodos = ["A", "B", "C", "D", "E"]
    longitud = 3

    try:
        resultado = matrizElevadoaN(grafoEnMatriz, longitud)
        print(f"Caminos con longitud {longitud} entre los nodos:")
        for indexfila, columna in enumerate(resultado):
            for indexelemento, elemento in enumerate(columna):
                print(f"El número de caminos con longitud {longitud} entre los nodos: ", nombreNodos[indexfila], nombreNodos[indexelemento] , "es ", elemento)
    except Exception as e:
        print(f"Error: {e}")
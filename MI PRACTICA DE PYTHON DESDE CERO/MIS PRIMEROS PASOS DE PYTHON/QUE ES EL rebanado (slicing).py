# Ejercicio de rebanado (slicing) de listas en Python

def mostrar_ejercicio():
    # Definimos la lista
    fruits = ['Python', 'Py', 'Anaconda', 'CPython', 'Dragon']

    # Mostramos la lista original
    print("Lista original:", fruits)

    # Mostramos los índices para mejor comprensión
    print("\nÍndices:     0        1      2          3         4")
    print("           Python    Py   Anaconda   CPython   Dragon")

    # Realizamos el rebanado y mostramos el resultado
    resultado = fruits[1:3]
    print("\nResultado de fruits[1:3]:", resultado)

    # Explicación del resultado
    print("\nExplicación:")
    print("- Comienza en índice 1 (incluido)")
    print("- Termina en índice 3 (no incluido)")
    print("- Por lo tanto, toma los elementos en posición 1 y 2")

    # Opciones de respuesta
    print("\nOpciones:")
    print("A. ['Py', 'Anaconda']")
    print("B. ['Py', 'Anaconda', 'CPython']")
    print("C. ['Python', 'Py', 'Anaconda']")
    print("D. None")

    print("\nRespuesta correcta: A")


# Ejecutar el ejercicio
if __name__ == "__main__":
    mostrar_ejercicio()
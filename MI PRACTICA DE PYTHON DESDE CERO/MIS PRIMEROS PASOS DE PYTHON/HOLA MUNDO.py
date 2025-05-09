# 1. Conceptos Básicos
#- El código comienza con ejemplos básicos de `print()` para mostrar texto en la consola:

#¡Hola, Mundo!
#Para mostrar cualquier cosa en la consola, o en la parte inferior, podemos usar el comando print, y entre paréntesis poner lo que queremos:

#print("texto")
#print(variable)
#print(f"texto {variable}")

print("Hola Mundo")
print("Hola desde Pujili")

# 2. Variables
# - Se muestran ejemplos de declaración y uso de variables:

#Las variables son "cajones" en donde podemos almacenar información.
# Podemos guardar textos, números, símbolos, o incluso listas o arreglos enteros de valores.

#Veamos la forma más simple de declarar una variable:

variable = 11
variable2 = 4

# - Se demuestra la interpolación de strings usando f-strings:

print(f"El valor de mi variable es {variable} y el variable2 es {variable2}")


#Las variables pueden cambiar fácilmente de valor
miVariable = 14
otraVariable = 74

#¿Qué pasa si ahora imprimimos el resultado?
# Rellena con el comando que creas conveniente, por ejemplo:
print(otraVariable)

# 3. Operaciones Matemáticas
# - Se realizan cálculos matemáticos básicos:
#Las variables también pueden tener "cuentas" asociadas.
x = 20
y = 4
ecuacion = x**2 + y
print(f"F(x) = {ecuacion}")

# 4. Uso de Bibliotecas
# - Se importa la biblioteca para usar constantes matemáticas como π (pi): `math`
#Las bibliotecas nos permiten expandir las posibilidades de lo que hace Python,
# lo único que debemos hacer es "traerlas" a nuestro programa para aprovechar sus funciones

import math
# ¿Math es una biblioteca que tiene funcionalidades bastante
# poderosas para operaciones matemáticas
# Cuanto vale "pi"?
pi = math.pi

#Comprobamos si es cierto...

print(pi)

#Ejercicio: ¡Calculemos el área de un círculo!

radio = 15
areaCirculo = pi * (radio**2)   #rellenar con nuestra ecuación
print(f"El área para un círculo de radio {radio} cm es de {areaCirculo} cm^2")

# 5. Listas
# - Se muestra cómo crear y manipular listas:
# Las listas son conjuntos de valores que me permiten almacenar mucha información

# Se declaran parecido a una variable, pero cada elemento se separa por una coma,

# y todo el conjunto se encierra entre corchetes

# Ejemplo: miLista = [5,4,3,2,1]

planetas = ["Mercurio","Venus","Tierra","Marte","Júpiter","Saturno","Urano","Neptuno"]
numeros = [2,6,7,2]

# Si quiero ver un elemento de la lista, basta con poner el número del elemento entre corchetes.

# Ejemplo: miLista[0]

# Nota: En Python, los elementos se cuentan a partir del cero, así que cuando nos referimos a miLista[0], me trae el primer elemento (5)

# ¿Cuál es el segundo planeta del sistema solar?
print(planetas[0]) #rellenar

# ¡Python admite números negativos! Si quiero el último elemento de una lista, basta con poner miLista[-1]

# ¿Cual es el último planeta del sistema solar?

var: str = planetas[-1]
print(planetas[-1])

# El comando "append" nos permite agregar elementos en una lista.

planetas.append("Plutón")
# ¿Cuál es el último planeta del sistema solar?
# Kjaskdajsdkajsdkasd
var = planetas[-1]
print(planetas[-1])

# 6. Bucles y Cálculos
# - Se usa un bucle `for` para calcular valores de una función:
# Ejercicio: Ejecutemos el siguiente código. ¿Qué es lo que hace?

x = [-5,-4,-3,-2,-1,0,1,2,3,4,7,8,9,10]
y = 1
fx = [] #lista vacía

for elemento in x:
    fx.append(elemento**6 + y)

print(f"F(x) = {fx}")

# 7. Gráficos
# - Se utiliza para crear gráficos: `matplotlib`
# Graficar con Python
# para graficar rápidamente con python, podemos apoyarnos en la biblioteca MatPlotLib

import matplotlib.pyplot as plt

#Lo único que necesitamos para graficar, es decirle qué es lo que queremos en el eje X, y en el eje Y

plt.plot(
    x,  # primero el eje X
    fx,  # luego el eje Y
    )


plt.style.use("ggplot")
plt.plot(
    x, # primero el eje X
    fx, # luego el eje Y
    )




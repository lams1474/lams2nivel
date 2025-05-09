# Importación de bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definición de parámetros
radius = 1
num_points = 50  # Faltaba el operador de asignación '='

# Crear puntos para el círculo
theta = np.linspace(0, 2 * np.pi, num_points)  # Faltaba el operador de asignación '=' y '*'

# Calcular coordenadas x e y
x = radius * np.cos(theta)  # Faltaba el operador de multiplicación '*'
y = radius * np.sin(theta)  # Faltaba el operador de multiplicación '*'

# Crear la figura y el eje
fig, ax = plt.subplots()  # Faltaba el operador de asignación '='

# Dibujar los puntos
ax.scatter(x, y, color='black', s=50)

# Configurar los límites del gráfico
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# Configurar aspecto y ejes
ax.set_aspect('equal')
ax.axis('off')

# Añadir título
plt.title("Circle pattern plot")

# Mostrar el gráfico
plt.show()  # Faltaba esta línea para mostrar el gráfico
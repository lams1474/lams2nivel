# Importar solo colorama que ya está instalado
from colorama import Fore, init

# Inicializar colorama
init()

def crear_banner(texto):
    """Crea un banner simple con ASCII art"""
    ancho = len(texto) + 4
    borde = '*' * ancho
    return f"""
{borde}
* {texto} *
{borde}
"""

# Crear el texto estilizado
mensaje = crear_banner('LAMS1474')

# Imprimir el texto en color verde
print(Fore.GREEN + mensaje)

# Resetear el color
print(Fore.RESET)
# tablero.py

# Definición del tablero
Colores = ["Rojo", "Verde", "Azul", "Amarillo"]

# Diccionario para almacenar posiciones clave
Casillas_Especiales = {
    "Seguros": [5, 12, 17, 22, 29, 34, 41, 46, 53, 58, 65],  # Ajusta si es necesario
    "Carcel": {  # Ubicación de la cárcel por color
        "Rojo": 0,
        "Verde": 17,
        "Azul": 34,
        "Amarillo": 51
    },
    "Llegada": {  # Primer casilla de llegada por color
        "Rojo": 69,
        "Verde": 77,
        "Azul": 85,
        "Amarillo": 93
    }
}

def es_casilla_especial(casilla):
    """
    Verifica si una casilla es especial (seguro, cárcel o llegada).
    """
    for tipo, ubicaciones in Casillas_Especiales.items():
        if isinstance(ubicaciones, list) and casilla in ubicaciones:
            return tipo
        elif isinstance(ubicaciones, dict):
            for color, posicion in ubicaciones.items():
                if casilla == posicion:
                    return f"{tipo} ({color})"
    return None

def inicializar_tablero():
    """
    Inicializa el tablero con las casillas y sus propiedades.
    """
    tablero = []
    for color in Colores:
        for n in range(17):
            if n == 0:
                tablero.append([[], color, [], []])  # Casilla de cárcel
            elif n == 5 or n == 12:
                tablero.append(["Seguro", color, [], []])  # Casilla de seguro
            else:
                tablero.append([n, color, [], []])  # Casilla normal
    return tablero
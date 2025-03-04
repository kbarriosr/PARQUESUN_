import pygame


# Última casilla de llegada para cada color
zona_de_llegada = {
    "Rojo": 76,
    "Verde": 84,
    "Azul": 92,
    "Naranja": 100
}


# Primera casilla de llegada para cada color
inicio_zona_de_llegada = {
    "Rojo": 69,
    "Verde": 77,
    "Azul": 85,
    "Naranja": 93
}


def verificar_victoria(color, fichas):
    """
    Verifica si un jugador ha ganado al coronar sus 4 fichas.
    
    :param color: Color del jugador.
    :param fichas: Lista de fichas en juego. Cada ficha es una tupla (color, posición).
    :return: True si el jugador gana, False de lo contrario.
    """
    # Obtener la última casilla de llegada para el color dado
    ultima_casilla = zona_de_llegada[color]
    
    # Inicializar el contador de fichas coronadas
    fichas_coronadas = 0
    
    # Conteo de cuántas fichas del jugador están en la última casilla de llegada
    for ficha in fichas:
        # ficha[0] es el color y ficha[1] es la posicion
        if ficha[0] == color and ficha[1] == ultima_casilla:
            fichas_coronadas += 1
    
    # Retorno True si el jugador ha coronado 4 fichas, False de lo contrario
    return fichas_coronadas == 4


def mover_ficha(ficha, pasos):
    """
    Mueve una ficha y valida si está en la zona de llegada.
    
    :param ficha: Una tupla (color, posición).
    :param pasos: Número de casillas a mover.
    :return: Nueva posición de la ficha.
    """
    # Desempaquetar la tupla para obtener el color y la posición actual de la ficha
    color, posicion_actual = ficha
    
    # Obtener la primera y última casilla de la zona de llegada para el color dado
    primera_casilla = inicio_zona_de_llegada[color]
    ultima_casilla = zona_de_llegada[color]
    
    # Verificar si la ficha ya está en la zona de llegada
    if posicion_actual >= primera_casilla:
        # Verificar si el movimiento se pasa de la última casilla de llegada
        if posicion_actual + pasos > ultima_casilla:
            print(f"La ficha {color} en {posicion_actual} no puede moverse {pasos} casillas.")
            return ficha  # La ficha no se mueve
        else:
            # Movimiento válido en la  zona de llegada
            return (color, posicion_actual + pasos)
    
    # Si la ficha no está en la zona de llegada moverla normal
    nueva_posicion = posicion_actual + pasos
    return (color, nueva_posicion)
# reglas.py
from fichas import enviar_a_carcel

def verificar_captura(ficha, nueva_posicion, tablero):
    """
    Verifica si una ficha captura a otra en la nueva posición.
    """
    for otra_ficha in tablero[nueva_posicion][2]:  # Fichas en la casilla
        if otra_ficha["color"] != ficha["color"]:
            print(f"La ficha {ficha['id']} ha capturado a la ficha {otra_ficha['id']}.")
            enviar_a_carcel(otra_ficha)
            return True
    return False

def verificar_victoria(fichas, color):
    """
    Verifica si un jugador ha ganado (todas sus fichas están en la zona de llegada).
    """
    for ficha in fichas[color]:
        if ficha["posicion"] != "llegada":
            return False
    return True
# fichas.py
from tablero import es_casilla_especial

def inicializar_fichas():
    """
    Inicializa las fichas para cada color.
    """
    colores = ["rojo", "azul", "verde", "amarillo"]
    fichas = {color: [] for color in colores}

    for color in colores:
        for i in range(1, 5):  # 4 fichas por color
            fichas[color].append({"id": i, "posicion": "carcel", "color": color})  # Inicialmente en la cárcel
    return fichas

def elegir_ficha(fichas, color):
    """
    Permite al jugador elegir qué ficha mover.
    """
    fichas_disponibles = [ficha for ficha in fichas[color] if ficha["posicion"] != "carcel"]
    if not fichas_disponibles:
        print("No hay fichas disponibles para mover.")
        return None

    print(f"Fichas disponibles para el color {color}:")
    for i, ficha in enumerate(fichas_disponibles):
        print(f"{i + 1}. Ficha {ficha['id']} en posición {ficha['posicion']}")

    try:
        eleccion = int(input("Elige una ficha para mover (1, 2, 3, 4): ")) - 1
        if 0 <= eleccion < len(fichas_disponibles):
            return fichas_disponibles[eleccion]
        else:
            print("Elección inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None

def enviar_a_carcel(ficha):
    """
    Envía una ficha a la cárcel.
    """
    ficha["posicion"] = "carcel"
    print(f"La ficha {ficha['id']} del color {ficha['color']} ha sido enviada a la cárcel.")

def mover_ficha(ficha, pasos, tablero):
    """
    Mueve una ficha en el tablero.
    """
    if ficha["posicion"] == "carcel":
        print("La ficha está en la cárcel y no puede moverse.")
        return None

    posicion_actual = ficha["posicion"]
    nueva_posicion = posicion_actual + pasos

    # Verificar si la ficha llega a una casilla especial
    tipo_casilla = es_casilla_especial(nueva_posicion)
    if tipo_casilla:
        print(f"La ficha {ficha['id']} ha caído en una casilla especial: {tipo_casilla}")

    # Actualizar la posición de la ficha en el diccionario
    ficha["posicion"] = nueva_posicion
    return nueva_posicion
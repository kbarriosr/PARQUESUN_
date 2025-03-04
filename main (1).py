import pygame
from dados import lanzar_dados, verificar_sacar_ficha
from tablero import inicializar_tablero, es_casilla_especial
from fichas import inicializar_fichas, mover_ficha, elegir_ficha, enviar_a_carcel
from reglas import verificar_captura, verificar_victoria
from dibujar import draw_board, draw_fichas  # Importar las funciones de dibujo

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parchís")

# Función para elegir el dado
def elegir_dado(dado_1, dado_2):
    """
    Permite al jugador elegir cuál dado usar para mover.
    """
    print(f"Resultado de los dados: {dado_1}, {dado_2}")
    try:
        eleccion = int(input("Elige el dado que deseas usar (1 o 2): "))
        if eleccion == 1:
            return dado_1
        elif eleccion == 2:
            return dado_2
        else:
            print("Elección inválida. Por favor, elige 1 o 2.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return None

# Inicializar el tablero y las fichas
tablero = inicializar_tablero()
fichas = inicializar_fichas()  # Asegúrate de que esto devuelva un diccionario con las posiciones iniciales

# Bucle principal del juego
victoria = False
while not victoria:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    screen.fill((255, 255, 255))  # Rellenar la pantalla con color blanco

    # Dibujar el tablero y las fichas
    draw_board(screen)  # Dibujar el tablero
    draw_fichas(screen, fichas)  # Dibujar las fichas (con las posiciones actualizadas)

    # Actualizar la pantalla
    pygame.display.flip()

    for color in fichas.keys():
        print(f"Es turno del color {color}")
        print("Presiona Enter para lanzar los datos...")

        # Esperar a que el jugador presione Enter
        esperando_enter = True
        while esperando_enter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Verificar si se presionó Enter
                        esperando_enter = False

        # Lanzar los dados
        dado_1, dado_2 = lanzar_dados()
        print(f"Resultado de los dados: {dado_1}, {dado_2}")

        # Verificar si se debe sacar una ficha de la cárcel
        if verificar_sacar_ficha(dado_1, dado_2, any(ficha["posicion"] == "carcel" for ficha in fichas[color])):
            print("Se debe sacar una ficha de la cárcel.")
            # Sacar una ficha de la cárcel
            for ficha in fichas[color]:
                if ficha["posicion"] == "carcel":
                    ficha["posicion"] = 0  # Mover la ficha a la posición inicial
                    print(f"La ficha {ficha['id']} ha sido sacada de la cárcel.")
                    break  # Sacar solo una ficha
            continue  # Terminar el turno sin permitir avanzar

        # Mover fichas según el resultado de los dados
        ficha_a_mover = elegir_ficha(fichas, color)
        if ficha_a_mover:
            dado_elegido = elegir_dado(dado_1, dado_2)
            if dado_elegido is not None:
                print(f"Movimiento de {dado_elegido} pasos para la ficha {ficha_a_mover['id']}.")
                nueva_posicion = mover_ficha(ficha_a_mover, dado_elegido, tablero)
                if nueva_posicion is not None:
                    if verificar_captura(ficha_a_mover, nueva_posicion, tablero):
                        print("¡Captura realizada!")

        # Verificar si el jugador ha ganado
        if verificar_victoria(fichas, color):
            print(f"¡El color {color} ha ganado la partida!")
            victoria = True
            break

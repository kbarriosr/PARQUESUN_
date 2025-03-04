import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 800
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parchís")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Dimensiones del tablero
BOARD_SIZE = 600  # Tamaño del tablero (cuadrado grande)
CELL_SIZE = BOARD_SIZE // 3  # Tamaño de cada cárcel (3x3 casillas)
OFFSET_X = (WIDTH - BOARD_SIZE) // 2  # Centrar el tablero horizontalmente
OFFSET_Y = (HEIGHT - BOARD_SIZE) // 2  # Centrar el tablero verticalmente

# Grosor del marco
THICKNESS = 5

# Dibujar el tablero
def dibujar_tabl(pantalla):
    # Dibujar el cuadrado grande (tablero principal)
    pygame.draw.rect(pantalla, BLACK, (OFFSET_X, OFFSET_Y, BOARD_SIZE, BOARD_SIZE), THICKNESS)

    # Dibujar las cárceles en cada esquina
    tamanioc = CELL_SIZE  # Tamaño de cada cárcel
    color_carcel = [RED, BLUE, GREEN, YELLOW]  # Colores de las cárceles

    # Cárcel roja (esquina superior izquierda)
    pygame.draw.rect(pantalla, color_carcel[0], (OFFSET_X, OFFSET_Y, tamanioc, tamanioc), THICKNESS)
    # Cárcel azul (esquina superior derecha)
    pygame.draw.rect(pantalla, color_carcel[1], (OFFSET_X + BOARD_SIZE - tamanioc, OFFSET_Y, tamanioc, tamanioc), THICKNESS)
    # Cárcel verde (esquina inferior izquierda)
    pygame.draw.rect(pantalla, color_carcel[2], (OFFSET_X, OFFSET_Y + BOARD_SIZE - tamanioc, tamanioc, tamanioc), THICKNESS)
    # Cárcel amarilla (esquina inferior derecha)
    pygame.draw.rect(pantalla, color_carcel[3], (OFFSET_X + BOARD_SIZE - tamanioc, OFFSET_Y + BOARD_SIZE - tamanioc, tamanioc, tamanioc), THICKNESS)

    # Dibujar los cuadrados entre las cárceles (divididos en rectángulos)
    ancho = CELL_SIZE // 3  # Ancho de cada rectángulo
    alto = CELL_SIZE // 7  # Alto de cada rectángulo

    # Cuadrado superior (entre cárcel roja y azul) - Líneas extendidas
    for i in range(3):  # 3 columnas
        for j in range(7):  # 7 filas
            x = OFFSET_X + tamanioc + i * ancho
            y = OFFSET_Y + j * alto
            pygame.draw.rect(pantalla, BLACK, (x, y, ancho, alto), 1)

        # Extender las dos líneas largas (i = 1 e i = 2) hasta el cuadrado pequeño central
        if i == 1 or i == 2:
            i_x = OFFSET_X + tamanioc + i * ancho
            ini_y = OFFSET_Y
            final_x = i_x
            final_y = OFFSET_Y + CELL_SIZE + (CELL_SIZE // 3.7)  # Extender hasta el cuadrado pequeño central
            pygame.draw.line(pantalla, BLACK, (i_x, ini_y), (final_x, final_y), 1)

    # Cuadrado derecho (entre cárcel azul y amarilla) - Líneas extendidas
    for i in range(7):  # 7 columnas (base)
        for j in range(3):  # 3 filas (alto)
            x = OFFSET_X + BOARD_SIZE - tamanioc + i * (CELL_SIZE // 7)
            y = OFFSET_Y + tamanioc + j * (CELL_SIZE // 3)
            pygame.draw.rect(pantalla, BLACK, (x, y, CELL_SIZE // 7, CELL_SIZE // 3), 1)

    # Extender las dos líneas largas (j = 1 y j = 2) hasta el cuadrado pequeño central
    for j in [1, 2]:  # Solo para j = 1 y j = 2
        i_x = OFFSET_X + BOARD_SIZE - tamanioc
        ini_y = OFFSET_Y + tamanioc + j * (CELL_SIZE // 3)
        final_x = OFFSET_X + CELL_SIZE + (CELL_SIZE // 1.35)  # Extender hasta el borde del cuadrado pequeño central
        final_y = ini_y
        pygame.draw.line(pantalla, BLACK, (i_x, ini_y), (final_x, final_y), 1)

    # Cuadrado inferior (entre cárcel amarilla y verde) - Líneas extendidas
    for i in range(3):  # 3 columnas
        for j in range(7):  # 7 filas
            x = OFFSET_X + tamanioc + i * ancho
            y = OFFSET_Y + BOARD_SIZE - tamanioc + j * alto
            pygame.draw.rect(pantalla, BLACK, (x, y, ancho, alto), 1)

        # Extender las dos líneas largas (i = 1 e i = 2) hasta el cuadrado pequeño central
        if i == 1 or i == 2:
            i_x = OFFSET_X + tamanioc + i * ancho
            ini_y = OFFSET_Y + BOARD_SIZE - tamanioc
            final_x = i_x
            final_y = OFFSET_Y + BOARD_SIZE - CELL_SIZE - (CELL_SIZE // 3.7)  # Extender hasta el borde del cuadrado pequeño central
            pygame.draw.line(pantalla, BLACK, (i_x, ini_y), (final_x, final_y), 1)

    # Cuadrado izquierdo (entre cárcel verde y roja) - Líneas extendidas
    for i in range(7):  # 7 columnas (base)
        for j in range(3):  # 3 filas (alto)
            x = OFFSET_X + i * (CELL_SIZE // 7)
            y = OFFSET_Y + tamanioc + j * (CELL_SIZE // 3)
            pygame.draw.rect(pantalla, BLACK, (x, y, CELL_SIZE // 7, CELL_SIZE // 3), 1)

    # Extender las dos líneas largas (j = 1 y j = 2) hasta el cuadrado pequeño central
    for j in [1, 2]:  # Solo para j = 1 y j = 2
        i_x = OFFSET_X
        ini_y = OFFSET_Y + tamanioc + j * (CELL_SIZE // 3)
        final_x = OFFSET_X + CELL_SIZE - (CELL_SIZE // -3.8)  # Extender hasta el borde del cuadrado pequeño central
        final_y = ini_y
        pygame.draw.line(pantalla, BLACK, (i_x, ini_y), (final_x, final_y), 1)

    # Dibujar las casillas de meta en el cuadrado central
    center_square_size = CELL_SIZE  # Tamaño del cuadrado central
    cuadrado_central_x = OFFSET_X + CELL_SIZE
    cuadrado_central_y = OFFSET_Y + CELL_SIZE

    # Dibujar las líneas diagonales (formando una "X")
    pygame.draw.line(pantalla, BLACK, (cuadrado_central_x, cuadrado_central_y),
                     (cuadrado_central_x + center_square_size, cuadrado_central_y + center_square_size), THICKNESS)
    pygame.draw.line(pantalla, BLACK, (cuadrado_central_x + center_square_size, cuadrado_central_y),
                     (cuadrado_central_x, cuadrado_central_y + center_square_size), THICKNESS)

    # Dibujar un cuadrado más pequeño dentro del cuadrado central
    tamanio_cuadro_p = center_square_size // 2
    cuadrado_c_x = cuadrado_central_x + (center_square_size - tamanio_cuadro_p) // 2
    cuadrado_c_y = cuadrado_central_y + (center_square_size - tamanio_cuadro_p) // 2
    pygame.draw.rect(pantalla, BLACK, (cuadrado_c_x, cuadrado_c_y, tamanio_cuadro_p, tamanio_cuadro_p), THICKNESS)

# Definir las posiciones iniciales de las fichas en las cárceles
fichas = {
    "rojo": [],
    "azul": [],
    "verde": [],
    "amarillo": []
}

# Tamaño de las fichas
FICHA_RADIO = 14.5

# Espaciado entre las fichas en la cárcel
ESPACIADO = CELL_SIZE // 3  # Ajusta el espaciado para que las fichas quepan en la cárcel

# Posiciones iniciales de las fichas en las cárceles
for color in fichas:
    if color == "rojo":
        base_x = OFFSET_X + (CELL_SIZE // 3)  # Esquina superior izquierda de la cárcel roja
        base_y = OFFSET_Y + (CELL_SIZE // 3)
    elif color == "azul":
        base_x = OFFSET_X + BOARD_SIZE - (CELL_SIZE // 4.5 * 3)  # Esquina superior derecha de la cárcel azul
        base_y = OFFSET_Y + (CELL_SIZE // 3)
    elif color == "verde":
        base_x = OFFSET_X + (CELL_SIZE // 3)  # Esquina inferior izquierda de la cárcel verde
        base_y = OFFSET_Y + BOARD_SIZE - (CELL_SIZE // 4.5 * 3)
    elif color == "amarillo":
        base_x = OFFSET_X + BOARD_SIZE - (CELL_SIZE // 4.5 * 3)  # Esquina inferior derecha de la cárcel amarilla
        base_y = OFFSET_Y + BOARD_SIZE - (CELL_SIZE // 4.5 * 3)

    # Crear 4 fichas para cada jugador, distribuidas en una cuadrícula 2x2
    for i in range(2):  # Filas
        for j in range(2):  # Columnas
            x = base_x + j * ESPACIADO
            y = base_y + i * ESPACIADO
            fichas[color].append((x, y))  # Guardar la posición de cada ficha

# Función para dibujar las fichas
def dibujar_fichas(pantalla):
    for color, posiciones in fichas.items():
        for pos in posiciones:
            if color == "rojo":
                pygame.draw.circle(pantalla, RED, pos, FICHA_RADIO)
            elif color == "azul":
                pygame.draw.circle(pantalla, BLUE, pos, FICHA_RADIO)
            elif color == "verde":
                pygame.draw.circle(pantalla, GREEN, pos, FICHA_RADIO)
            elif color == "amarillo":
                pygame.draw.circle(pantalla, YELLOW, pos, FICHA_RADIO)

# Bucle principal del juego
def main():
    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuar = False

        # Limpiar la pantalla
        pantalla.fill(WHITE)

        # Dibujar el tablero
        dibujar_tabl(pantalla)

        # Dibujar las fichas
        dibujar_fichas(pantalla)

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
def draw_board(screen):
    # Dibujar el cuadrado grande (tablero principal)
    pygame.draw.rect(screen, BLACK, (OFFSET_X, OFFSET_Y, BOARD_SIZE, BOARD_SIZE), THICKNESS)

    # Dibujar las cárceles en cada esquina
    jail_size = CELL_SIZE  # Tamaño de cada cárcel
    jail_colors = [RED, BLUE, GREEN, YELLOW]  # Colores de las cárceles

    # Cárcel roja (esquina superior izquierda)
    pygame.draw.rect(screen, jail_colors[0], (OFFSET_X, OFFSET_Y, jail_size, jail_size), THICKNESS)
    # Cárcel azul (esquina superior derecha)
    pygame.draw.rect(screen, jail_colors[1], (OFFSET_X + BOARD_SIZE - jail_size, OFFSET_Y, jail_size, jail_size), THICKNESS)
    # Cárcel verde (esquina inferior izquierda)
    pygame.draw.rect(screen, jail_colors[2], (OFFSET_X, OFFSET_Y + BOARD_SIZE - jail_size, jail_size, jail_size), THICKNESS)
    # Cárcel amarilla (esquina inferior derecha)
    pygame.draw.rect(screen, jail_colors[3], (OFFSET_X + BOARD_SIZE - jail_size, OFFSET_Y + BOARD_SIZE - jail_size, jail_size, jail_size), THICKNESS)

    # Dibujar los cuadrados entre las cárceles (divididos en rectángulos)
    rect_width = CELL_SIZE // 3  # Ancho de cada rectángulo
    rect_height = CELL_SIZE // 7  # Alto de cada rectángulo

    # Cuadrado superior (entre cárcel roja y azul) - Líneas extendidas
    for i in range(3):  # 3 columnas
        for j in range(7):  # 7 filas
            x = OFFSET_X + jail_size + i * rect_width
            y = OFFSET_Y + j * rect_height
            pygame.draw.rect(screen, BLACK, (x, y, rect_width, rect_height), 1)

        # Extender las dos líneas largas (i = 1 e i = 2) hasta el cuadrado pequeño central
        if i == 1 or i == 2:
            start_x = OFFSET_X + jail_size + i * rect_width
            start_y = OFFSET_Y
            end_x = start_x
            end_y = OFFSET_Y + CELL_SIZE + (CELL_SIZE // 3.7)  # Extender hasta el cuadrado pequeño central
            pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 1)

    # Cuadrado derecho (entre cárcel azul y amarilla) - Líneas extendidas
    for i in range(7):  # 7 columnas (base)
        for j in range(3):  # 3 filas (alto)
            x = OFFSET_X + BOARD_SIZE - jail_size + i * (CELL_SIZE // 7)
            y = OFFSET_Y + jail_size + j * (CELL_SIZE // 3)
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE // 7, CELL_SIZE // 3), 1)

    # Extender las dos líneas largas (j = 1 y j = 2) hasta el cuadrado pequeño central
    for j in [1, 2]:  # Solo para j = 1 y j = 2
        start_x = OFFSET_X + BOARD_SIZE - jail_size
        start_y = OFFSET_Y + jail_size + j * (CELL_SIZE // 3)
        end_x = OFFSET_X + CELL_SIZE + (CELL_SIZE // 1.35)  # Extender hasta el borde del cuadrado pequeño central
        end_y = start_y
        pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 1)

    # Cuadrado inferior (entre cárcel amarilla y verde) - Líneas extendidas
    for i in range(3):  # 3 columnas
        for j in range(7):  # 7 filas
            x = OFFSET_X + jail_size + i * rect_width
            y = OFFSET_Y + BOARD_SIZE - jail_size + j * rect_height
            pygame.draw.rect(screen, BLACK, (x, y, rect_width, rect_height), 1)

        # Extender las dos líneas largas (i = 1 e i = 2) hasta el cuadrado pequeño central
        if i == 1 or i == 2:
            start_x = OFFSET_X + jail_size + i * rect_width
            start_y = OFFSET_Y + BOARD_SIZE - jail_size
            end_x = start_x
            end_y = OFFSET_Y + BOARD_SIZE - CELL_SIZE - (CELL_SIZE // 3.7)  # Extender hasta el borde del cuadrado pequeño central
            pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 1)

    # Cuadrado izquierdo (entre cárcel verde y roja) - Líneas extendidas
    for i in range(7):  # 7 columnas (base)
        for j in range(3):  # 3 filas (alto)
            x = OFFSET_X + i * (CELL_SIZE // 7)
            y = OFFSET_Y + jail_size + j * (CELL_SIZE // 3)
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE // 7, CELL_SIZE // 3), 1)

    # Extender las dos líneas largas (j = 1 y j = 2) hasta el cuadrado pequeño central
    for j in [1, 2]:  # Solo para j = 1 y j = 2
        start_x = OFFSET_X
        start_y = OFFSET_Y + jail_size + j * (CELL_SIZE // 3)
        end_x = OFFSET_X + CELL_SIZE - (CELL_SIZE // -3.8)  # Extender hasta el borde del cuadrado pequeño central
        end_y = start_y
        pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 1)

    # Dibujar las casillas de meta en el cuadrado central
    center_square_size = CELL_SIZE  # Tamaño del cuadrado central
    center_square_x = OFFSET_X + CELL_SIZE
    center_square_y = OFFSET_Y + CELL_SIZE

    # Dibujar las líneas diagonales (formando una "X")
    pygame.draw.line(screen, BLACK, (center_square_x, center_square_y), 
                     (center_square_x + center_square_size, center_square_y + center_square_size), THICKNESS)
    pygame.draw.line(screen, BLACK, (center_square_x + center_square_size, center_square_y), 
                     (center_square_x, center_square_y + center_square_size), THICKNESS)

    # Dibujar un cuadrado más pequeño dentro del cuadrado central
    inner_square_size = center_square_size // 2
    inner_square_x = center_square_x + (center_square_size - inner_square_size) // 2
    inner_square_y = center_square_y + (center_square_size - inner_square_size) // 2
    pygame.draw.rect(screen, BLACK, (inner_square_x, inner_square_y, inner_square_size, inner_square_size), THICKNESS)

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

def calcular_posicion(posicion):
    """
    Convierte la posición de la ficha en coordenadas (x, y) en la pantalla.
    """
    if posicion == "carcel":
        # Si la ficha está en la cárcel, devuelve una posición fuera del tablero o no la dibujes.
        return -100, -100  # Fuera de la pantalla

    # Definir las coordenadas base del tablero
    tablero_x = OFFSET_X  # Coordenada x inicial del tablero
    tablero_y = OFFSET_Y  # Coordenada y inicial del tablero

    # Definir el tamaño de cada casilla
    casilla_size = CELL_SIZE // 10  # Ajusta según el tamaño de tu tablero

    # Mapear la posición a coordenadas (x, y)
    # Esto depende de cómo esté estructurado tu tablero.
    # Aquí te doy un ejemplo básico para un tablero cuadrado.
    if 0 <= posicion < 10:
        # Primera fila (de izquierda a derecha)
        x = tablero_x + posicion * casilla_size
        y = tablero_y
    elif 10 <= posicion < 20:
        # Segunda fila (de derecha a izquierda)
        x = tablero_x + (19 - posicion) * casilla_size
        y = tablero_y + casilla_size
    elif 20 <= posicion < 30:
        # Tercera fila (de izquierda a derecha)
        x = tablero_x + (posicion - 20) * casilla_size
        y = tablero_y + 2 * casilla_size
    elif 30 <= posicion < 40:
        # Cuarta fila (de derecha a izquierda)
        x = tablero_x + (39 - posicion) * casilla_size
        y = tablero_y + 3 * casilla_size
    else:
        # Casillas adicionales (ajusta según tu tablero)
        x = tablero_x
        y = tablero_y

    return x, y

# Función para dibujar las fichas
def draw_fichas(screen, fichas):
    """
    Dibuja las fichas en la pantalla.
    """
    for color, lista_fichas in fichas.items():
        for ficha in lista_fichas:
            if ficha["posicion"] != "carcel":  # Solo dibujar fichas que no están en la cárcel
                x, y = calcular_posicion(ficha["posicion"])  # Convertir la posición en coordenadas (x, y)
                if color == "rojo":
                    pygame.draw.circle(screen, RED, (x, y), FICHA_RADIO)
                elif color == "azul":
                    pygame.draw.circle(screen, BLUE, (x, y), FICHA_RADIO)
                elif color == "verde":
                    pygame.draw.circle(screen, GREEN, (x, y), FICHA_RADIO)
                elif color == "amarillo":
                    pygame.draw.circle(screen, YELLOW, (x, y), FICHA_RADIO)

# Bucle principal del juego
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpiar la pantalla
        screen.fill(WHITE)

        # Dibujar el tablero
        draw_board(screen)

        # Dibujar las fichas
        draw_fichas(screen)

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
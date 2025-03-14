# -*- coding: utf-8 -*-
"""tablerov4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SvVtNIAgCniI1KnSkGg6F9xTwd2hMz17
"""

import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Parchís")

# columnaces y fuentes
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 36)

# Tamaño de las celdas
tcelda = 40

def dibujar_tabl(pantalla):
    for fila in range(15):
        for columna in range(15):
            x = columna * tcelda
            y = fila * tcelda
            pygame.draw.rect(pantalla, (200, 200, 200), (x, y, tcelda, tcelda), 1)
            # Dibujar propiedades especiales (ej: salidas)
            if Tablero[fila][columna]["tipo"] == "salida":
                pygame.draw.circle(pantalla, (255, 255, 0), (x + tcelda//2, y + tcelda//2), 10)

def dibujar_fichas(pantalla):
    for ficha in Fichas:
        fila, columna = ficha["pos"]
        x = columna * tcelda + tcelda // 2
        y = fila * tcelda + tcelda // 2
        columnac = {
            "Rojo": RED,
            "Verde": GREEN,
            "Azul": BLUE,
            "Naranja": ORANGE
        }[ficha["columnac"]]
        pygame.draw.circle(pantalla, columnac, (x, y), tcelda // 3)

def mostrar_mensaje(texto, pos=(10, 10)):
    """
    Muestra un mensaje en la pantalla.

    Parámetros:
        texto: El mensaje a mostrar.
        pos: La posición (x, y) donde se mostrará el mensaje.
    """
    mensaje = font.render(texto, True, BLACK)
    pantalla.blit(mensaje, pos)
    pygame.display.flip()

def Dados(columnac, Modo):
    """
    Realiza el lanzamiento de dados de manera gráfica.

    Parámetros:
        columnac: El columnac que está lanzando los dados.
        Modo: Indica si se seleccionó modo jugador (1) o desarrollador (2).

    Retorna:
        Una lista con los resultados de los dados y la regla de la cárcel.
    """
    global pantalla, font  # Asegúrate de que pantalla y font estén definidos globalmente

    Dado_1, Dado_2 = 0, 0
    Fcarcel = []

    # Buscar fichas en la cárcel
    for i in Fichas:
        if columnac in i:
            Fcarcel.append(i)

    if Modo == 1:  # Modo Jugador (dados aleatorios)
        # Botón para lanzar dados
        btn_rect = pygame.Rect(300, 500, 200, 50)  # Posición y tamaño del botón
        lanzado = False

        while not lanzado:
            for evento in pygame.evento.get():
                if evento.type == pygame.MOUSEBUTTONDOWN and btn_rect.columnalidepoint(evento.pos):
                    Dado_1 = random.randint(1, 6)
                    Dado_2 = random.randint(1, 6)
                    lanzado = True

            # Dibujar el botón
            pygame.draw.rect(pantalla, (0, 150, 0), btn_rect)  # columnac verde
            texto = font.render("Lanzar dados", True, WHITE)
            pantalla.blit(texto, (310, 510))

            # Mostrar mensaje de espera
            mostrar_mensaje(f"Turno de {columnac}. Presiona 'Lanzar dados'", (10, 10))
            pygame.display.flip()

    elif Modo == 2:  # Modo Desarrollador (ingresar valores manualmente)
        # Cuadros de texto para ingresar dados
        input_rect1 = pygame.Rect(300, 400, 100, 50)  # Primer dado
        input_rect2 = pygame.Rect(450, 400, 100, 50)  # Segundo dado
        btn_rect = pygame.Rect(300, 500, 250, 50)  # Botón de confirmación
        input_text1 = ""
        input_text2 = ""
        activo1 = True  # Indica si el primer cuadro de texto está activo
        confirmado = False

        while not confirmado:
            for evento in pygame.evento.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect1.columnalidepoint(evento.pos):
                        activo1 = True
                    elif input_rect2.columnalidepoint(evento.pos):
                        activo1 = False
                    elif btn_rect.columnalidepoint(evento.pos):
                        try:
                            Dado_1 = int(input_text1)
                            Dado_2 = int(input_text2)
                            if 1 <= Dado_1 <= 6 and 1 <= Dado_2 <= 6:
                                confirmado = True
                            else:
                                mostrar_mensaje("Los dados deben estar entre 1 y 6", (10, 100))
                        except ValueError:
                            mostrar_mensaje("Ingresa números válidos", (10, 100))

                if evento.type == pygame.KEYDOWN:
                    if activo1:
                        if evento.key == pygame.K_BACKSPACE:
                            input_text1 = input_text1[:-1]
                        else:
                            input_text1 += evento.unicode
                    else:
                        if evento.key == pygame.K_BACKSPACE:
                            input_text2 = input_text2[:-1]
                        else:
                            input_text2 += evento.unicode

            # Dibujar cuadros de texto y botón
            pygame.draw.rect(pantalla, WHITE, input_rect1)
            pygame.draw.rect(pantalla, WHITE, input_rect2)
            pygame.draw.rect(pantalla, (0, 150, 0), btn_rect)

            texto1 = font.render(input_text1, True, BLACK)
            texto2 = font.render(input_text2, True, BLACK)
            texto_btn = font.render("Confirmar", True, WHITE)

            pantalla.blit(texto1, (input_rect1.x + 10, input_rect1.y + 10))
            pantalla.blit(texto2, (input_rect2.x + 10, input_rect2.y + 10))
            pantalla.blit(texto_btn, (btn_rect.x + 10, btn_rect.y + 10))

            # Mostrar instrucciones
            mostrar_mensaje(f"Turno de {columnac}. Ingresa los valores de los dados:", (10, 10))
            pygame.display.flip()

    # Regla 1: Sacar ficha de la cárcel si hay un 5
    if (Dado_1 == 5 or Dado_2 == 5 or Dado_1 + Dado_2 == 5) and len(Fcarcel) != 0:
        Regla_1 = [True, Fcarcel]
        if Dado_1 == 5 and Dado_2 == 5:
            Regla_1.append(2)
        elif Dado_2 == 5:
            Regla_1.append(1)
        elif Dado_1 == 5:
            Regla_1.append(0)
        else:
            Regla_1.append(3)
    else:
        Regla_1 = [False, Fcarcel, 4]

    # Mostrar resultado de los dados
    mostrar_mensaje(f"Resultado: Dado 1 = {Dado_1}, Dado 2 = {Dado_2}", (10, 50))

    return [Dado_1, Dado_2, Regla_1, columnac]

#VERIFICAR BLOQUEO
def bloq ():
  """
    Esta función recorre las casillas del tablero y retorna una lista con los indices de las casillas que tienen un bloqueo
  """
  Bloqueos=[]
  for n in Tablero:
    if len(n[2])!=0 and len(n[3])!=0:
      Bloqueos.append(Tablero.index(n))
  return Bloqueos   #Retorna las casillas en las que hay bloqueos

#CASILLAS DESOCUPADAS
def C_vacia (Casilla):
  """
  Esta función recibe el indice de una casilla y retorna el puesto en el que se puede columnaocar la pieza
  """
  if len(Tablero[Casilla][2])==0 and len(Tablero[Casilla][3])==0:
    return 2
  elif len(Tablero[Casilla][2])==0:
    return 2
  else:
    return 3

#MOVIMIENTO FICHAS
def mov_f (Turno, Dobles, UF):
  """
  Esta función maneja todo lo relacionado al movimiento de las piezas:

  Analiza los siguientes casos para saber si se pueden hacer movimientos:
    - Si se han lanzado 3 pares seguidos
    - Si hay por lo menos una ficha en el tablero

  Al momento de realizar los movimientos, realiza lo siguiente:
    - Pide un input que indique el dado que se quiere utilizar y la ficha que se quiere mover
    - Se revisa que la casilla que está después de la ficha no tenga un bloqueo con al función bloq()
    - Se mueve la ficha 1 paso
    - Se repite el proceso hasta terminar los pasos que indica el dado
    - Pide un input de la ficha que se quiere mover con el otro dado
    - Cuando la ficha llega a su posición final se llama a la función Cap_Fichas

  Parámetros:
    Turno: La lista que retornó la función dados al iniciar el turno
    Dobles: El número de dados pares consecutivos que han ocurrido
    UF: Ultima ficha movida (Para llevarla a la carcel si ocurren 3 pares seguidos)

  Retorno:
    Ultima ficha movida
  """

  if Dobles==3:
    for i in Tablero:
      if UF in i:
        Fichas.append(i.pop(i.index(UF)))
        print("Sacaste 3 pares seguidos, la ultima ficha que moviste va a la carcel")
        i.append([])
        return []
  F=0
  for i in Fichas:
    if Turno[-1] in i:
      F+=1
      if F==4:
        print(f"Todas las fichas del columnac {Turno[-1]}, están en la carcel")
        return []
  if len(Turno)<=2:
    return []
  if Turno[0]==0 and Turno[1]==0:
    print("No hay movimientos disponibles")
    return []
  T=True
  while T:
    Num=3
    if len(Turno)==4:
      while Num not in (0,1):
        Num=int(input(f"¿Qué resultado del dado quiere utilizar?¿{Turno[0]} (Escribe 0) o {Turno[1]} (Escribe 1)?"))
      dado=Turno.pop(Num)
    elif len(Turno)==3:
      dado=Turno.pop(0)
    elif len(Turno)==2:
      return DicF[f"Ficha {F} {Turno[-1]}"]

    F=int(input(f"¿Qué ficha desea mover {dado} pasos? (1, 2, 3 o 4)"))
    while F not in (1, 2, 3, 4) or (DicF[f"Ficha {F} {Turno[-1]}"] in Fichas):
      F=int(input(f"La Ficha {F} no está en el tablero o no existe. Ingrese otro número"))
    Ficha=DicF[f"Ficha {F} {Turno[-1]}"]

    for i in Tablero:
      if (Ficha in i):
        C0Ficha=Tablero.index(i)
        CFFicha=Tablero.index(i)+dado
        PRestantes=dado
        for n in range(C0Ficha,(CFFicha)):
          if n+1 not in bloq():
            if Tablero[n][Tablero[n].index(Ficha)]==(17*(columnaces.index(columnac))):
              Tablero[n][0][0]=Tablero.pop(Tablero[n][Tablero[n].index(Ficha)])
              Tablero[n].append([])
              for a in range(1,PRestantes):
                Tablero[n][0].insert(Tablero[n][0].index(Ficha),[])
                Tablero[n][0][a]=Tablero[n].pop(Tablero[n][0].index(Ficha))
              break
            else:
              if n==67:
                b=n
                n=0
                Tablero[n][C_vacia(n)]=Tablero[b].pop(Tablero[b].index(Ficha))
                Tablero[b].append([])
                #Actualizar pantalla
              elif n>67:
                n-=67
                Tablero[n+1][C_vacia(n+1)]=Tablero[n].pop(Tablero[n].index(Ficha))
                Tablero[n].append([])
                #Actualizar pantalla
              else:
                Tablero[n+1][C_vacia(n+1)]=Tablero[n].pop(Tablero[n].index(Ficha))
                Tablero[n].append([])
                #Actualizar pantalla
              PRestantes-=1
          else:
            print(f"Hay un bloqueo en la casilla {Tablero.index(i)}")
            T=False
            break
        print(f"La ficha {Ficha} ha avanzado {dado} pasos")
        Cap_Fichas(Ficha, CFFicha)
        break
      else:
        for n in Tablero[17*(columnaces.index(columnac))][0]:
          if Ficha in n:
            C0Ficha=Tablero[17*(columnaces.index(columnac))][0].index(n)
            CFFicha=C0Ficha+dado
            if CFFicha<=7:
              Tablero[17*(columnaces.index(columnac))][0][CFFicha]=Tablero[17*(columnaces.index(columnac))][0].pop(C0Ficha)
              Tablero[17*(columnaces.index(columnac))][0].insert(C0Ficha,[])
              if CFFicha==7:
                print(f"La ficha {Ficha} ha coronado!")
                mov_f([10,0,False,columnac])
            elif CFFicha>7:
              print("Para coronar, necesita tener el número exacto de pasos")
              Turno.insert(0,dado)

#CAPTURA DE FICHAS
def Cap_Fichas(Ficha, c, s=False):
  """
  Esta función analiza si puede haber una captura en una casilla

  Parámetros:
    Ficha: La ficha que se movió (La que puede que vaya a capturar)
    c: La casilla que se va a analizar
    s: Un booleano que indica si la casilla es una salida y la ficha *Ficha* salió de su carcel (por defecto False)

  Retorno:
    - La función no arroja ninguna variable como retorno, sin embargo, cambia la lista Tablero removiendo la ficha capturada y añadiendola a la lista Fichas
  """
  for x in range (3,5):
    if s==True:
      if (Ficha[0] != Tablero[c][x][0]):
        FichaF=Tablero[c][x]
        Fichas.append(Tablero[c].pop([x]))
        print(f"La ficha {Ficha} ha capturado a la ficha {FichaF}")
        #ACTUALIZAR TABLERO
        mov_f([20,0,False,columnac])
    else:
      if (type(Tablero[c][0])!=int) and (c in bloq()) and (Ficha[0] != Tablero[c][x][0]):
        FichaF=Tablero[c][x]
        Fichas.append(Tablero[c].pop([x]))
        print(f"La ficha {Ficha} ha capturado a la ficha {FichaF}")
        #ACTUALIZAR TABLERO
        mov_f([20,0,False,columnac])
  return

#SACAR FICHA DE LA CARCEL
def SFCarcel (n, Turno):
  """
  Esta función saca las fichas de la carcel dependiendo del caso que se obtuvo con los dados:

  Parámetros:
    n: El número que creó la función dados para indicar qué dado es=5 o si fue la suma o ambos fueron 5
    Turno: El resultado que dió la función dados() en el turno actual

  Retorno:
    La función no retorna ninguna variable, sin embargo:
    - Revisa si hay un bloqueo en la salida
    - Revisa si hay fichas de otros equipos y llama a la función Cap_Fichas para removerlas
    - columnaoca a las fichas que se puedan sacar de la carcel en su salida
  """
  if n==0:
    print("Debe sacar una ficha de la carcel")
    for i in range(6,68,17):
      print(Tablero[i][-3]==Turno[-1])
      if Tablero[i][-3]==Turno[-1]:
        print(i in bloq())
        if i in bloq():
          if Tablero[i][2][0]!=Turno[-1] and Tablero[i][3][0]!=Turno[-1]:
            Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
          else:
            break
        if ((len(Tablero[i][2])>0) and Tablero[i][2][0]!=Turno[-1]) or (len(Tablero[i][3])>0 and Tablero[i][3][0]!=Turno[-1]):
          Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
        Tablero[i][C_vacia(i)]=Fichas.pop(Fichas.index(Turno[-2][1][0]))
        print(f"La ficha {Turno[-2][1][0]} ha salido de la carcel")
        Turno[0]=0
        #FICHA Turno[-2][1][0] SALE DE LA CARCEL

  elif n==1:
    print("Debe sacar una ficha de la carcel")
    for i in range(6,68,17):
      if Tablero[i][-3]==Turno[-1]:
        if i in bloq():
          if Tablero[i][2][0]!=Turno[-1] and Tablero[i][3][0]!=Turno[-1]:
            Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
          else:
            break
        if ((len(Tablero[i][2])>0) and Tablero[i][2][0]!=Turno[-1]) or (len(Tablero[i][3])>0 and Tablero[i][3][0]!=Turno[-1]):
          Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
        Tablero[i][C_vacia(i)]=Fichas.pop(Fichas.index(Turno[-2][1][0]))
        print(f"La ficha {Turno[-2][1][0]} ha salido de la carcel")
        Turno[1]=0
        #FICHA Turno[-2][1][0] SALE DE LA CARCEL

  elif n==2:
    print("Puede sacar dos fichas de la carcel (Debe sacar por lo menos 1)")
    for i in range(6,68,17):
      if Tablero[i][-3]==Turno[-1]:
        for n in range(2):
          if i in bloq():
            if Tablero[i][2][0]!=Turno[-1] and Tablero[i][3][0]!=Turno[-1]:
              Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
            else:
              break
          if ((len(Tablero[i][2])>0) and Tablero[i][2][0]!=Turno[-1]) or (len(Tablero[i][3])>0 and Tablero[i][3][0]!=Turno[-1]):
            Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
          Tablero[i][C_vacia(i)]=Fichas.pop(Fichas.index(Turno[-2][1][n]))
          print(f"La ficha {Turno[-2][1][n]} ha salido de la carcel")
          Turno[0]=0
          Turno[1]=0
          #FICHA Turno[-2][1][0] SALE DE LA CARCEL (PUEDE OCURRIR DOS VECES (SALEN 2))
  elif n==3:
    print("Debe sacar una ficha de la carcel")
    for i in range(6,68,17):
      if Tablero[i][-3]==Turno[-1]:
        if i in bloq():
          if Tablero[i][2][0]!=Turno[-1] and Tablero[i][3][0]!=Turno[-1]:
            Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
          else:
            break
        if ((len(Tablero[i][2])>0) and Tablero[i][2][0]!=Turno[-1]) or (len(Tablero[i][3])>0 and Tablero[i][3][0]!=Turno[-1]):
          Cap_Fichas(Fichas[Fichas.index(Turno[-2][1][0])], i, True)
        Tablero[i][C_vacia(i)]=Fichas.pop(Fichas.index(Turno[-2][1][0]))
        print(f"La ficha {Turno[-2][1][0]} ha salido de la carcel")
        Turno[0]=0
        Turno[1]=0


# Variables globales
Tablero = []
columnaces = ["Rojo", "Verde", "Azul", "Naranja"]
Fichas = []
DicF = {}
Modo = None
columnac = None
tcelda = 40

# Función para mostrar la pantalla de selección de modo
def seleccionar_modo():
    global Modo
    text_jugador = font.render("Modo Jugador (Dados Aleatorios)", True, BLACK)
    text_desarrollador = font.render("Modo Desarrollador (Ingresar Dados)", True, BLACK)
    rect_jugador = text_jugador.get_rect(center=(ancho//2, alto//2 - 50))
    rect_desarrollador = text_desarrollador.get_rect(center=(ancho//2, alto//2 + 50))

    while True:
        for evento in pygame.evento.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_jugador.columnalidepoint(evento.pos):
                    return 1
                elif rect_desarrollador.columnalidepoint(evento.pos):
                    return 2

        pantalla.fill(WHITE)
        pygame.draw.rect(pantalla, GRAY, rect_jugador)
        pygame.draw.rect(pantalla, GRAY, rect_desarrollador)
        pantalla.blit(text_jugador, rect_jugador)
        pantalla.blit(text_desarrollador, rect_desarrollador)
        pygame.display.flip()

# Función principal del juego
# En la función main():
def main():
    global Tablero, columnaces, Fichas, DicF, Modo, columnac

    # Crear tablero de 15x15 (ajustable)
    Tablero = []
    for fila in range(15):
        Tablero.append([])
        for columna in range(15):
            # Asignar propiedades según posición (ejemplo: esquinas son salidas)
            if (fila, columna) in [(0, 0), (0, 14), (14, 0), (14, 14)]:
                Tablero[fila].append({"tipo": "salida", "columnac": columnaces[fila//4], "fichas": []})
            else:
                Tablero[fila].append({"tipo": "normal", "columnac": None, "fichas": []})

    global Fichas
    global DicF
    Fichas=[]
    DicF={}
# En main():
    for columnac in columnaces:
        for i in range(4):  # 4 fichas por jugador
            Fichas.append({
                "columnac": columnac,
                "id": i,
                "pos": (0, 0)  # Posición inicial (cárcel)
            })

    Modo = seleccionar_modo()
    if Modo is None:
        return

    # Bucle principal del juego
    running = True
    while running:
        for evento in pygame.evento.get():
            if evento.type == pygame.QUIT:
                running = False

        # Lógica del juego
        for columnac in columnaces:
            # ... (tu código de manejo de turnos aquí)

            # Actualizar gráficos
            pantalla.fill(WHITE)
            dibujar_tabl(pantalla)
            dibujar_fichas(pantalla)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
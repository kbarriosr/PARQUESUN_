import random  # Importamos el módulo random para crear números aleatorios


class Dados:
    def __init__(self):
        self.contador_dobles = 0  # Inicializamos el contador de dobles seguidos


    def lanzar_dados(self, modo="real"):
        """
        Lanza los dados según el modo de juego.
        
        :param modo: "real" para lanzar aleatorio, "manual" para elegir valores.
        :return: (dado1, dado2)
        """
        
        if modo == "real":
            # Crear números aleatorios entre 1 y 6 para los dados
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            
        elif modo == "manual":
            while True:
                try:
                    # El jugador debe ingresar valores para los dados
                    dado1 = int(input("Ingrese el valor del primer dado (1-6): "))
                    dado2 = int(input("Ingrese el valor del segundo dado (1-6): "))
                    
                    # Valores deben estar en el rango válido
                    if 1 <= dado1 <= 6 and 1 <= dado2 <= 6:
                        break  # Si son válidos, salimos del bucle
                    else:
                        print(" !! Los valores deben estar entre 1 y 6.")
                except ValueError:
                    print("!! Entrada inválida, ingrese números entre 1 y 6.")


        print(f"🎲 Dados: {dado1}, {dado2}")


        # Verificar si los dos dados son iguales (los dobles)
        if dado1 == dado2:
            self.contador_dobles += 1  # Aumentamos el contador de dobles
            print(" Sacaste dobles, vuelves a lanzar.")


            # Si sacamos tres dobles seguidos hay penalización
            if self.contador_dobles == 3:
                print("!! Tres dobles seguidos, la última ficha movida vuelve a la cárcel.")
                self.contador_dobles = 0  # Reiniciamos el contador tras la penalización
        else:
            self.contador_dobles = 0  # Reiniciamos si no son dobles


        return dado1, dado2  # Devolvemos los valores de los dados
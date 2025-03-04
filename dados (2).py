import random

def lanzar_dados():
    """
    Lanza dos dados y devuelve los resultados.
    """
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    return dado_1, dado_2

def verificar_sacar_ficha(dado_1, dado_2, fichas_en_carcel):
    """
    Verifica si se debe sacar una ficha de la cárcel.
    - Si hay un 5 en los dados y hay fichas en la cárcel, se debe sacar una ficha.
    """
    if (dado_1 == 5 or dado_2 == 5 or dado_1 + dado_2 == 5) and fichas_en_carcel:
        return True
    else:
        return False
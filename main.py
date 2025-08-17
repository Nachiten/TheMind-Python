import random
import os
import time

def limpiar_pantalla():
    # Intenta limpiar consola, si no, imprime muchos saltos
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" * 5)

def mostrar_cartas(jugador, cartas):
    limpiar_pantalla()
    print(f"=== Cartas del Jugador {jugador} ===")
    print(" ".join(map(str, sorted(cartas))))
    input("\nPresiona ENTER cuando termines de ver tus cartas...")

def repartir_cartas(num_jugadores, nivel):
    mazo = list(range(1, 101))
    random.shuffle(mazo)
    manos = []
    for i in range(num_jugadores):
        cartas = [mazo.pop() for _ in range(nivel)]
        manos.append(cartas)
    return manos

def main():
    print("=== THE MIND (versión offline) ===\n")

    # Número de jugadores
    while True:
        try:
            num_jugadores = int(input("¿Cuántos jugadores? (2-4): "))
            if num_jugadores in [2, 3, 4]:
                break
        except ValueError:
            pass
        print("Opción inválida, intenta de nuevo.\n")

    # Nivel
    while True:
        try:
            nivel = int(input("¿Nivel? (1-12): "))
            if nivel >= 1:
                break
        except ValueError:
            pass
        print("Opción inválida, intenta de nuevo.\n")

    # Repartir
    manos = repartir_cartas(num_jugadores, nivel)

    # Mostrar cartas jugador por jugador
    for i, cartas in enumerate(manos, start=1):
        mostrar_cartas(i, cartas)

    limpiar_pantalla()
    print("=== Todas las manos fueron repartidas. ===")
    print("Ya pueden jugar offline en la mesa :)")

if __name__ == "__main__":
    main()

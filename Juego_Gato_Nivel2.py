# Nombre: ________
# Sección: _______

partidas = 0
victorias_j1 = 0
victorias_j2 = 0
empates = 0

seguir = "S"

while seguir == "S":

    c1 = "1"
    c2 = "2"
    c3 = "3"
    c4 = "4"
    c5 = "5"
    c6 = "6"
    c7 = "7"
    c8 = "8"
    c9 = "9"

    jugador = 1
    ficha = "X"

    jugadas = 0
    ganador = False

    print("\n===== JUEGO DEL GATO =====")
    print("Jugador 1: X | Jugador 2: O")

    while jugadas < 9 and ganador == False:

        print("\n")
        print(c1 + " | " + c2 + " | " + c3)
        print("--+---+--")
        print(c4 + " | " + c5 + " | " + c6)
        print("--+---+--")
        print(c7 + " | " + c8 + " | " + c9)

        valido = False

        while valido == False:

            try:

                pos = int(input("\nJugador " + str(jugador) +
                                " (" + ficha + "), ingrese casilla (1-9): "))

                if pos < 1 or pos > 9:
                    print("Error: la casilla debe estar entre 1 y 9.")

                else:

                    libre = False

                    if pos == 1 and c1 == "1":
                        c1 = ficha
                        libre = True

                    elif pos == 2 and c2 == "2":
                        c2 = ficha
                        libre = True

                    elif pos == 3 and c3 == "3":
                        c3 = ficha
                        libre = True

                    elif pos == 4 and c4 == "4":
                        c4 = ficha
                        libre = True

                    elif pos == 5 and c5 == "5":
                        c5 = ficha
                        libre = True

                    elif pos == 6 and c6 == "6":
                        c6 = ficha
                        libre = True

                    elif pos == 7 and c7 == "7":
                        c7 = ficha
                        libre = True

                    elif pos == 8 and c8 == "8":
                        c8 = ficha
                        libre = True

                    elif pos == 9 and c9 == "9":
                        c9 = ficha
                        libre = True

                    if libre:
                        valido = True
                    else:
                        print("Error: casilla ocupada.")

            except:
                print("Error: debe ingresar un número.")

        jugadas += 1

        # FILAS
        if c1 == c2 and c2 == c3:
            ganador = True
            tipo = "Fila 1"

        elif c4 == c5 and c5 == c6:
            ganador = True
            tipo = "Fila 2"

        elif c7 == c8 and c8 == c9:
            ganador = True
            tipo = "Fila 3"

        # COLUMNAS
        elif c1 == c4 and c4 == c7:
            ganador = True
            tipo = "Columna 1"

        elif c2 == c5 and c5 == c8:
            ganador = True
            tipo = "Columna 2"

        elif c3 == c6 and c6 == c9:
            ganador = True
            tipo = "Columna 3"

        # DIAGONALES
        elif c1 == c5 and c5 == c9:
            ganador = True
            tipo = "Diagonal principal"

        elif c3 == c5 and c5 == c7:
            ganador = True
            tipo = "Diagonal secundaria"

        if ganador:

            print("\n")
            print(c1 + " | " + c2 + " | " + c3)
            print("--+---+--")
            print(c4 + " | " + c5 + " | " + c6)
            print("--+---+--")
            print(c7 + " | " + c8 + " | " + c9)

            print("\n¡Jugador " + str(jugador) +
                  " (" + ficha + ") gana! - " + tipo)

            partidas += 1

            if jugador == 1:
                victorias_j1 += 1
            else:
                victorias_j2 += 1

        elif jugadas == 9:

            print("\n")
            print(c1 + " | " + c2 + " | " + c3)
            print("--+---+--")
            print(c4 + " | " + c5 + " | " + c6)
            print("--+---+--")
            print(c7 + " | " + c8 + " | " + c9)

            print("\n¡Empate!")

            partidas += 1
            empates += 1

        else:

            if jugador == 1:
                jugador = 2
                ficha = "O"
            else:
                jugador = 1
                ficha = "X"

    print("\n===== ESTADÍSTICAS DE SESIÓN =====")
    print("Partidas jugadas :", partidas)
    print("Victorias J1     :", victorias_j1)
    print("Victorias J2     :", victorias_j2)
    print("Empates          :", empates)

    seguir = input("\n¿Desea jugar otra partida? (S/N): ").upper()

print("\n===== ESTADÍSTICAS FINALES =====")
print("Partidas jugadas :", partidas)
print("Victorias J1     :", victorias_j1)
print("Victorias J2     :", victorias_j2)
print("Empates          :", empates)

print("\nGracias por jugar.")
# Nombre: ________
# Sección: _______

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
                    print("Casilla fuera de rango.")
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
                        print("La casilla ya está ocupada.")

            except:
                print("Debe ingresar un número.")

        jugadas += 1

        # Verificar filas
        if c1 == c2 and c2 == c3:
            ganador = True
            tipo = "Fila 1"
        elif c4 == c5 and c5 == c6:
            ganador = True
            tipo = "Fila 2"
        elif c7 == c8 and c8 == c9:
            ganador = True
            tipo = "Fila 3"

        # Verificar columnas
        elif c1 == c4 and c4 == c7:
            ganador = True
            tipo = "Columna 1"
        elif c2 == c5 and c5 == c8:
            ganador = True
            tipo = "Columna 2"
        elif c3 == c6 and c6 == c9:
            ganador = True
            tipo = "Columna 3"

        # Verificar diagonales
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

        elif jugadas == 9:

            print("\n")
            print(c1 + " | " + c2 + " | " + c3)
            print("--+---+--")
            print(c4 + " | " + c5 + " | " + c6)
            print("--+---+--")
            print(c7 + " | " + c8 + " | " + c9)

            print("\nEmpate.")

        else:

            if jugador == 1:
                jugador = 2
                ficha = "O"
            else:
                jugador = 1
                ficha = "X"

    seguir = input("\n¿Desea jugar otra partida? (S/N): ").upper()

print("\nGracias por jugar.")
''' Name 
    Rock paper scissors.
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que simula un juego de piedra papel o tijera.
    
Usage
    Python src/Rock_paper_scissors.py
    El programa se detiene cuando uno de los dos jugadores completa dos puntos, 
    el usuario debe ingresar cualquiera de las opciones permitidas para jugar: piedra, papel 
    o tijera. 
    Este programa considera como juggador 1 al usuario y jugador 2 a la computadora.
    Las reglas del juego son simples:
    Tijera le gana a papel, papel le gana a piedra y piedra le gana a tijera. 
    Si existe empate entre jugadores, ninguno obtiene el punto.

Category
    Recreational
    
Arguments
    None
    
See also
    None
    
'''

# Importar la libreria random
# Pedir al usuario que ingrese alguna opcion
# Hacer una lista con todas las opciones validas del juego
# Generar aleatoreamente la opcion de juego de la computadora
# Inicializar variables que cuentan los puntos para cada jugador

import random

print("El juego termina hasta que uno de los dos jugadores complete dos puntos")
user_name = input("Ingresa tu nombre: ")
computer = ['piedra', 'papel', 'tijera']
computer_points = 0
user_points = 0

# El programa se repite hasta que uno de los dos jugadores complete 2 puntos.

while computer_points < 2 and user_points < 2:

    user_choice = input(
        "Ingresa alguna opcion para jugar: piedra, papel o tijera \n").lower()
    computer_choice = random.choice(computer)

    # Si el usuario elige tijera

    #   Si la computadora elije papel
    #   Si la computadora elije piedra
    #  Almacenar el conteo de puntos para cada jugador
    
    # Empate
 
    if user_choice == computer_choice:
        print(f"La computadora elije {computer_choice}, ¡Empate!")
        
    if user_choice == 'tijera':
        
        if computer_choice == 'papel':
            print(f"La computadora elije {computer_choice}, ¡Ganaste!")
            user_points += 1

        if computer_choice == 'piedra':
            print(f"La computadora elije {computer_choice}, ¡Perdiste!")
            computer_points += 1

    # Si el usuario elije papel

    #   Si la computadora elije tijera
    #   Si la computadora elije piedra

    if user_choice == 'papel':

        if computer_choice == 'tijera':
            print(f"La computadora elije {computer_choice}, ¡Perdiste!")
            computer_points += 1

        if computer_choice == 'piedra':
            print(f"La computadora elije {computer_choice}, ¡Ganaste!")
            user_points += 1

    # Si el usuario elije piedra

    #   Si la computadora elije tijera
    #   Si la computadora elije papel

    if user_choice == 'piedra':

        if computer_choice == 'tijera':
            print(f"La computadora elije {computer_choice}, ¡Ganaste!")
            user_points += 1

        if computer_choice == 'papel':
            print(f"La computadora elije {computer_choice}, ¡Perdiste!")
            computer_points += 1

# Imprimir los puntos de cada jugador
# Se asigna el ganador segun el puntaje de cada jugador

if user_points > computer_points:
    print(f"Ganaste {user_name}, con {user_points} contra {computer_points} puntos")

else:
    print(f"Perdiste {user_name}, con {user_points} contra {computer_points} puntos")

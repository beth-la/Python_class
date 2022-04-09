''' Name 
    Rock paper scissors.
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que simula un juego de piedra papel o tijera.
    
Usage
    El programa se detiene cuando uno de los dos jugadores completa dos puntos, 
    el usuario debe ingresar cualquiera de las opciones permitidas para jugar: piedra, papel 
    o tijera. 
    Este programa considera como juggador 1 al usuario y jugador 2 a la computadora.

Category
    Recreational
    
Arguments
    None
    
See also
    None
    
'''
# Pedir al usuario que ingrese alguna opcion
# Elegir la opcion de la computadora
# Importar libreria random
# Inicializar variables que cuentan los puntos para cada jugador

import random

print("El juego termina hasta que uno de los dos jugadores complete dos puntos")
computer = ['piedra', 'papel', 'tijera']
computer_points = 0
user_points = 0

# El programa se repite hasta que uno de los dos jugadores complete 2 puntos.

while computer_points < 2 and user_points < 2:

    user_choice = input(
        "Ingresa alguna opcion para jugar: piedra, papel o tijera \n").lower()
    computer_choice = random.choice(computer)

    print(f"La computadora elije {computer_choice}")

    # Si el usuario elige tijera

    #   Si la computadora elije tijera
    #   Si la computadora elije papel
    #   Si la computadora elije piedra
    
    #  Almacenar el conteo de puntos para cada jugador 

    if user_choice == 'tijera':

        if computer_choice == 'tijera':
            print(f"{user_choice} empata con {computer_choice}, ¡Empate!")

        if computer_choice == 'papel':
            print(f"{user_choice} le gana a {computer_choice}, ¡Ganaste!")
            user_points += 1

        if computer_choice == 'piedra':
            print(f"{user_choice} pierde contra {computer_choice}, ¡Perdiste!")
            computer_points += 1

    # Si el usuario elije papel

    #   Si la computadora elije tijera
    #   Si la computadora elije papel
    #   Si la computadora elije piedra

    if user_choice == 'papel':

        if computer_choice == 'tijera':
            print(f"{user_choice} pierde contra {computer_choice}, ¡Perdiste!")
            computer_points += 1

        if computer_choice == 'papel':
            print(f"{user_choice} empata con {computer_choice}, ¡Empate!")

        if computer_choice == 'piedra':
            print(f"{user_choice} le gana a {computer_choice}, ¡Ganaste!")
            user_points += 1

    # Si el usuario elije piedra

    #   Si la computadora elije tijera
    #   Si la computadora elije papel
    #   Si la computadora elije piedra

    if user_choice == 'piedra':

        if computer_choice == 'tijera':
            print(f"{user_choice} le gana a {computer_choice}, ¡Ganaste!")
            user_points += 1

        if computer_choice == 'papel':
            print(f"{user_choice} pierde contra {computer_choice}, ¡Perdiste!")
            computer_points += 1

        if computer_choice == 'piedra':
            print(f"{user_choice} empata con {computer_choice}, ¡Empate!")

# Imprimir los puntos de cada jugador 
# 
if user_points > computer_points:
    print(f"Ganaste con {user_points} contra {computer_points} puntos")

else:
    print(f"Perdiste con {user_points} contra {computer_points} puntos")
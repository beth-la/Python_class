# Name: Generador de secuencia de ARN
# Version:
# Author: Lopez A. Brenda E.
# Descripcion: Programa que dada una secuencia de ADN, genera una de ARN
# Category: 
# Usage:
# Arguments:
# See also:

# Pedimos la secuencia de ADN al usuario.

ADN= input("Introduce la cadena de ADN de la cual desees obtener el ARN, no mayor a 100 nucleotidos")

# Nos aseguramos de que la secuencia ingresada no sea mayor a 100 nucleotidos. 
# Con el metodo replace sustituimos las T por U e imprimimos el resutado 

if len(ADN) <= 100:
    print(f"La secuencia de ARN es {ADN.replace('T','U')}")
else:
    print("La secuencia de nucleotidos debe ser menor a 100 nucleotidos")

# Name: Contador de nucleotidos 
# Version:
# Author: Lopez A. Brenda E.
# Descripcion: Programa que dada una secuencia de ADN, cuenta la frecuencia de los nucleotidos.
# Category: 
# Usage:
# Arguments:
# See also:

# Guardamos la secuencia de interes en una variable: 

ADN= 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# Tomando la secuencia guardada en la variable ADN, utilizamos el metodo count para contar la aparicion de cada letra dentro de la secuencia. 

print(f"La secuencia tiene estos nucleotidos: A:{ADN.count('A')} C:{ADN.count('C')} T:{ADN.count('T')} G:{ADN.count('G')}")

''' Name 
    Contador de nucleotidos con input.
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que dada una secuencia de ADN mediante un input, cuenta la frecuencia de los nucleotidos.
    
Category
    DNA sequence
    
Usage
    Python Contador_nucleotidos_input.py
    
Arguments
    None
    
See also
    None
    
'''
# Pedimos al usuario ingrese una secuencia de ADN 
# La secuencia  solicitada será guaradada en la variable ADN

ADN = input("Introduce una secuencia de ADN: ").upper()

# Obtenemos la frecuencia de aparicion de cad aletra.

print(f"El total por base es: A:{ADN.count('A')} C:{ADN.count('C')} T:{ADN.count('T')} G:{ADN.count('G')}")

# En este caso no necesitamos poner bloques de try-except ya que ninguna entrada tiene el potencial de romper el codigo 
# Aun si se trata de una entrada erronea, el programa seguira corriendo correctamente.
# Por lo que no se amerita utilizar un bloque try-except

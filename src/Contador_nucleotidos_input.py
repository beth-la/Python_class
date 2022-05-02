''' Name 
    Contador de nucleotidos con input.
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que dada una secuencia de ADN mediante un input, cuenta la frecuencia de los nucleotidos.
    
Category
    DNA sequence
    
Usage
    El programa nos permite obtener la frecuencia de aparición de cada nucleotido 
    de una secuencia de ADN.
    
Arguments
    None
    
See also
    None
    
'''
# Pedimos al usuario ingrese una secuencia de ADN 
# La secuencia  solicitada será guaradada en la variable ADN

ADN= input("Introduce una secuencia de ADN: ").upper()

# Obtenemos la frecuencia de aparicion de cad aletra.

print(f"El total por base es: A:{ADN.count('A')} C:{ADN.count('C')} T:{ADN.count('T')} G:{ADN.count('G')}")

''' 
Name 
    module_program 
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que llama a funciones de los modulos: ADN module y aminoacid modile
    
Category
    Aminoacid and ADN
    
Usage
    Python src/module_program 
    
Arguments
    None
     
See also
    None
'''

import ADN_module
import aminoacids_module

# Eliminando adaptadores del archivo 4_input_adapters 
# Guardar la ruta del archivo que contiene las secuencias sin adaptadores 

path_in = "data/4_input_adapters.txt"
path_out = (ADN_module.delete_adapters(path_in))

# Obteniendo las secuencias contenidas en el archivo 
# Contando el contenido de nucleotidos en las secuencias 

with open (path_out,'r') as archivo:
    secuencias = [line.replace("\n","") for line in archivo]
    
nucleotide_count = [ADN_module.count_dna(secuencia) for secuencia in secuencias]

for i in range (0, len(secuencias)):
    print(f"La cantidad de nucleotidos [A, T, G, C] en la secuencia {secuencias[i]} es: {nucleotide_count[i]}")
    
# llamando a funciones del modulo aminoacids

protein = "MSRSLLLRFLLFLLLLPPLP"
hidrofilic_aminoacids = aminoacids_module.aminoacid_per(protein)

print(f"El porcentage de aminoacidos hidrofilicos en la secuencia {protein} es {hidrofilic_aminoacids}%")


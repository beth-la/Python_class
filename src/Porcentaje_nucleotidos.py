''' Name 
    Calculo de porcentaje de nucleotidos 
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que calcula el procentaje de nucleotidos de una cadena de ADN almacenada en un archivo con formato .txt
    
Category
    DNA sequence
    
Usage
    Python src/Porcentaje_nucleotidos.py -i path/to/file
    
Arguments
    -h --help
    -i --input 
    
See also
    None
    
'''

import argparse

# Agregar paso de argumentos

arg_parser = argparse.ArgumentParser(description="Calcula el porcentaje de nucleotidos: AT y CG")

arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with ADN sequences",
                    required=True)

arguments = arg_parser.parse_args()

# Pedimos la ruta del archivo al usuario, esto se guardara en la variable my_file.   

# Con with open no es necesario cerrar el archivo al final
# Del archivo obtenemos la longitud de la secuencia y la secuencia.

# Se agrega la estructura try-except para avisar al usuario si su ruta no es valida 

try:
    with open(arguments.input) as archivo:
        secuencia_adn  = archivo.read()
        longitud_secuencia = len(secuencia_adn)
        
except IOError as io_error: 
    print(f"La ruta {io_error.filename} no es valida, el archivo no fue encontrado. \n")
    
    # Calculamos el porcentaje de AT con una regla de tres:

else:
      
    porcentaje_AT = ((secuencia_adn.count('A') + secuencia_adn.count('T')) * 100 )/(longitud_secuencia)

    # El porcentaje de CG es el complemento: 

    porcentaje_GC = (100 - porcentaje_AT)
    
    # Imprimimos los resultados obtenidos: 

    print(f"La proporción de AT y GC de la secuencia {secuencia_adn} es AT: {porcentaje_AT} % GC: {porcentaje_GC} %") 

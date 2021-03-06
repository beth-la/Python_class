''' Name 
    remove_adapters.py
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que elimina adaptadores de secuencias de ADN contenidas en un archivo.
    
Category
    DNA sequence
    
Usage
    Python src/generador_fasta.py -i path/to/file [-o OUTPUT]

Arguments
    -h --help
    -i --input 
    -o --output 
    
See also
    None
    
'''

# Abrir el archivo que contiene las secuencias deseadas
# Asignar las secuencias a una lista
# Agregamos estructura try-except para avisar al usuario si es que su archivo no se encuentra.

import argparse

arg_parser = argparse.ArgumentParser(description="Generador de archivo con secuencia de ADN")
arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with ADN sequences",
                    required=True)

arg_parser.add_argument("-o", "--output",
                    help="Flag argument, prints the path of the output file",
                    required=False)

arguments = arg_parser.parse_args()

# Arhivo con el que se probo el codigo: data/4_input_adapters.txt

try:  
    with open(arguments.input,'r') as archivo:
        secuencias= [line for line in archivo]
        sin_adaptadores= []
        
except IOError as io_error: 
    print(f"El archivo {io_error.filename} no se encuentra. \n")
    
# Excluimos la parte de la secuencia que contiene a los adaptadores
# Estas nuevas secuencias las almacenamos en una lista nueva 

else:
    
    for i in range(0,len(secuencias)):
        sin_adaptadores.append(secuencias[i][14:])

# Abrimos un nuevo archivo que sera el output 
# Ecribimos la lista con las secuencias en el archivo 

    my_file= open('results/Sec_sin_adaptadores.txt','w')
    my_file.write(''.join(sin_adaptadores))
    my_file.close()
    
    if arguments.output:
        print("La ruta del archivo final es: results/Sec_sin_adaptadores.txt")




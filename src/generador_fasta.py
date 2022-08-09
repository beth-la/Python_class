''' Name 
    Generador de archivo fasta
    
Version
    1.5
    
Author 
    Lopez A. Brenda.
    
Descripcion
    Programa que genera un archivo fasta apartir de un archivo que contiene una secuencia de ADN.
    
Category
    DNA sequence
    
Usage
    Python generador_fasta.py -i path/to/file [-o OUTPUT] 
        
Arguments
    -h --help
    -i --input 
    -o --output 
    
See also
    None
    
'''

import argparse

# Declarando argumentos para pasarlos por teclado:

arg_parser = argparse.ArgumentParser(description="Genera archivos en formato fasta")
arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with ADN sequences",
                    required=True)

arg_parser.add_argument("-o", "--output",
                    help="Flag argument, prints the path of the output file",
                    required=False)

arguments = arg_parser.parse_args()

# Archivo con el que se probó el codigo: data/dna.txt

try:
    with open(arguments.input,'r') as archivo:
        ADN= archivo.read()
        
except IOError as io_error: 
    print(f"El archivo {io_error.filename} no se encuentra. \n")

# Creamos un nuevo archivo que tendra el formato fasta:
# Escribimos el encabezado y la secuencia.

else:
    my_file= open("results/dna.fasta","w")
    my_file.write(">sequence_name \n")
    my_file.write(ADN)
    my_file.close()

# Si el usuario pide ruta del archivo fasta:
    
    if arguments.output:
        print("El archivo fasta se encuentra en la ruta: results/dna.fasta")
    

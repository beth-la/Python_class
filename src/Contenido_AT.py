''' Name 
    Contenido_AT.
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que dada una secuencia de ADN calcula el contenido de AT.
    
Category
    DNA sequence
    
Usage
    Python src/Contenido_AT.py -i INPUT -o OUTPUT -r ROUND
    
Arguments
    -h --help
    -i --input 
    -o --output 
    -r --round
    
See also
    None
    '''
    
# Creando el paso de argumentos:

import argparse

arg_parser = argparse.ArgumentParser(description="Calcula el contenido de AT")
arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)

arg_parser.add_argument("-o", "--output",
                    help="Flag argument, prints the path of the output file",
                    required=False)
         
arg_parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)

args = arg_parser.parse_args()

# Abrir el archivo con el argumento pasado por el usuario.
# Leer el archivo de entrada y guardar su contenido
# Calcular el contenido de AT 

with open(args.input, "r") as seq_file:
    my_dna = seq_file.read()
    
length = len(my_dna) 
a_count = my_dna.count('A') 
t_count = my_dna.count('T')

# Si el usuario pide redondear el contenido de AT

if args.round:
    at_content = round((a_count + t_count) / length, args.round)
    
# Si el usuario no pide redondear
    
else:
    at_content = (a_count + t_count) / length

# Escribir en un archivo nuevo

with open("results/output_final.txt","w") as archivo_final:
    archivo_final.write(f"AT content is {str(at_content)}")
    
# Imprimir la ruta del archivo final si el usuario la solicita

if args.output:
    print("La ruta del archivo final es: results/output_final.txt")

    
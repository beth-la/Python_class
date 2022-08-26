''' Name 
    search AT rich regions
    
Version
    1.0
    
Author 
    Lopez Angeles Brenda Elizabeth.
    
Descripcion
    Programa que busca regiones ricas en AT
    
Category
    DNA sequence
    
Usage
    Python rich_at.py -f path/to/file [-s ] 
    py .\src\rich_at.py -f data/ADN_at.txt -s 4
        
Arguments
    -h --help
    -f --file 
    -s --search
    
See also
    None
'''
# Importamos librerias
import argparse
import re 

# Paso de argumentos mediante argparse
arg_parser = argparse.ArgumentParser(description="Search AT rich regions")
arg_parser.add_argument("-f", "--file",
                    metavar="path/to/file",
                    help="Archivo con secuencia de ADN",
                    required=True)
         
arg_parser.add_argument("-s", "--search",
                    help="cantidad minima de AT a buscar",
                    type=int,
                    required=False)

args = arg_parser.parse_args()

# Abrimos el archivo y extraemos su contenido
with open(args.file, "r") as seq_file:
    dna = seq_file.read().upper()

def evaluate(dna):
    '''
    Evalua si el archivo contienealgun caracter diferente a los permitidos [ATGC].
        Parameters:
            dna (str): secuencia de ADN a procesar.
        Returns:
            0 (int): si encuentra caracteres invalidos.
            1 (int): si no encuentra caracteres invalidos. 
    '''
    not_dna = re.finditer("[^ATGC]+", dna)
    matches = len([*re.finditer("[^ATGC]+", dna)])
    if matches:
        for invalid in not_dna:
            print(f"Existen caracteres invalidos en tu archivo: {invalid.group()} en las coordenadas: {invalid.span()}")
        return(0)
    else:
        return(1)

def find_regions(dna, at=2):
    '''
    Evalua la existencia de regiones ricas en AT en una cadena de ADN.
        Parameters:
            dna (str): secuencia de ADN a procesar.
            at (int): tamaño minimo de las regiones ricas en AT a buscar, por default 2.
        Returns:
            0 (int): Termina la evaluacion de la secuencia. 
    '''
    at_rich = re.finditer("A+|T+",dna)
    matches = len([*re.finditer("A+|T+", dna)])
    if matches:
        for islas in at_rich:
            if len(islas.group()) >= at:
                print(f"Se encontro esta region rica en AT: {islas.group()} en la posicion {islas.span()}")
    else:
        print("No se encontraron regiones ricas en AT")
    return(0)

# Llamamos a nuestras funciones.
if evaluate(dna):
    if args.search:
        ans = find_regions(dna,args.search)
    else:
        ans = find_regions(dna)
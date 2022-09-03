''' Name 
    ADN/ARN to protein
    
Version
    1.0
    
Author 
    Lopez Angeles Brenda Elizabeth.
    
Descripcion
    Programa que convierte una secuencia de ADN o ARN en una secuencia peptidica.
    Por default, el programa convierte secuencias de ARN. 
    
Category
    Aminoacid sequence
    
Usage
    Python ARN_toPro.py [-h] [-f path/to/file] [-s SEQUENCE] [-o OUTPUT] [-p PRINT] [-c CHANGETODNA]
        
Arguments
    -h, --help
    -f --file, --file path/to/file 
    -s SEQUENCE, --SEQUENCE 
    -o OUTPUT, --OUTPUT 
    -p PRINT, --PRINT
    -c CHANCETODNA, --CHANGETODNA
    
See also
    None
'''
# Importamos librerias
import argparse
from aminoacids_module import evaluate_rna
from aminoacids_module import translate_dna
from ADN_module import evaluate_dna

# Paso de argumentos mediante argparse
arg_parser = argparse.ArgumentParser(description="Translating ARN to protein")
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo con la secuencia de ARN o ADN",
                    required=False)
                    
arg_parser.add_argument("-s", "--SEQUENCE",
                    help="Secuencia de ARN o ADN",
                    type=str,
                    required=False)
                    
arg_parser.add_argument("-o", "--OUTPUT",
                    help="Archivo de salida",
                    required=False)

arg_parser.add_argument("-p","--PRINT",
                    help = "Imprimir a pantalla la secuencia peptidica",
                    required= False)

arg_parser.add_argument("-c","--CHANGEtoDNA",
                    help = "Si la secuencia es de ADN",
                    required= False)

args = arg_parser.parse_args()

# Abrimos el archivo y extraemos su contenido.
# Si el usuario ingresa una secuencia de ADN, la convertimos a ARN llamando a la funcion del modulo creado.

if args.FILE:
    with open(args.FILE, "r") as seq_file:
        if args.CHANGEtoDNA:
            ADN = seq_file.read().upper()
            if evaluate_dna(ADN):
                ARN = translate_dna(ADN)
        else:
            ARN = seq_file.read().upper()

# Si el usurio ingresa una secuencia por teclado
# Si el usuario ingresa una secuencia de ADN, llamamos a la funcion translate_dna
            
if args.SEQUENCE:
    if args.CHANGEtoDNA:
        ADN = args.SEQUENCE
        ARN = translate_dna(ADN)
    else:
        ARN = args.SEQUENCE

def arn_to_peptid(ARN):
    '''
    Funcion que convierte una secuencia de ARN a proteina.
        Parameters:
            ARN (str): secuencia de ARN a procesar.
        Returns:
            peptide (str): secuencia peptidica generada. 
    '''
    gencode = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACU':'T', 'AAC':'N', 'AAU':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGU':'S', 'AGA':'R',
    'AGG':'R', 'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 'CAC':'H',
    'CAU':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGU':'R', 'GUA':'V', 'GUC':'V', 'GUG':'V',
    'GUU':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGU':'G', 'UCA':'S', 'UCC':'S',
    'UCG':'S', 'UCU':'S', 'UUC':'F', 'UUU':'F', 'UUA':'L',
    'UUG':'L', 'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}
 
    codon_sequence = [ARN[i:i+3] for i in range(0,len(ARN),3)]
    peptid = [gencode.get(codon, "*") for codon in codon_sequence]
    return(peptid)

# Evaluamos si la secuencia contiene algun caracter incorrecto.
# Si el usuario quiere un archivo como formato de salida. 
# Si el usurio quiere imprimir la secuencia a pantalla.

if evaluate_rna(ARN):
    peptid = arn_to_peptid(ARN)
    if args.OUTPUT:
        output_file = open(args.OUTPUT,'w')
        output_file.write(f"La secuencia proteica obtenida fue:\n{''.join(peptid)}")
        output_file.close()
        
    if args.PRINT:
        print(f"La secuencia proteica obtenida fue:\n{''.join(peptid)}")
''' Name 
    ARN to protein
    
Version
    1.0
    
Author 
    Lopez Angeles Brenda Elizabeth.
    
Descripcion
    Programa que busca regiones ricas en AT
    
Category
    Aminoacid sequence
    
Usage

        
Arguments
    -h, --help
    -f --file, --file path/to/file 

    
See also
    None
'''
# Importamos librerias
import argparse
from posixpath import split
import re 
from aminoacids_module import evaluate_rna

# Paso de argumentos mediante argparse
arg_parser = argparse.ArgumentParser(description="Translating ARN to protein")
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo con secuencia de ARN",
                    required=False)
                    
arg_parser.add_argument("-s", "--SEQUENCE",
                    help="Secuencia de ARN",
                    type=str,
                    required=False)
                    
arg_parser.add_argument("-o", "--OUTPUT",
                    help="Archivo de salida",
                    required=False)

arg_parser.add_argument("-p","--PRINT",
                    help = "Imprimir a pantalla la secuencia peptidica",
                    required= False)

args = arg_parser.parse_args()

# Abrimos el archivo y extraemos su contenido
if args.FILE:
    with open(args.FILE, "r") as seq_file:
        ARN = seq_file.read().upper()

if args.SEQUENCE:
    ARN = args.SEQUENCE

def arn_to_peptid(ARN):
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

if evaluate_rna(ARN):
    peptid = arn_to_peptid(ARN)
    if args.OUTPUT:
        output_file = open(args.OUTPUT,'w')
        output_file.write(f"La secuencia proteica obtenida fue:\n{''.join(peptid)}")
        output_file.close()
        
    if args.PRINT:
        print(f"La secuencia proteica obtenida fue:\n{''.join(peptid)}")








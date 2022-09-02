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
from aminoacids_module import evaluate

# Paso de argumentos mediante argparse
arg_parser = argparse.ArgumentParser(description="Translating ARN to protein")
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo con secuencia de ARN",
                    required=True)
                    
arg_parser.add_argument("-o", "--OUTPUT",
                    help="Archivo de salida",
                    type=int,
                    required=False)

arg_parser.add_argument("-p","--PRINT",
                    help = "Imprimir a pantalla",
                    required= False)

args = arg_parser.parse_args()

# Abrimos el archivo y extraemos su contenido
with open(args.FILE, "r") as seq_file:
    ARN = seq_file.read().upper()
    
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def codon_format(ARN):    
    codon_seq = [ARN[i:i+3] for i in range(0,len(ARN),3)]
    return(codon_seq)

if evaluate(ARN):
    print()

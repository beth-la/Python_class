''' Name 
    search AT rich regions
    
Version
    1.0
    
Author 
    Lopez Angeles Brenda E. 
    
Descripcion
    Programa que busca regiones ricas en AT
    
Category
    DNA sequence
    
Usage
    Python rich_at.py -f path/to/file [-n ] 
        
Arguments
    -h --help
    -f --file 
    -r --region
    
See also
    None
    phy
'''

import argparse
import re 

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

with open(args.file, "r") as seq_file:
    dna = seq_file.read().upper()
    
def evaluate(dna):
    not_dna = re.search("[^ATGC]+", dna)
    if(not_dna):
        print(f"Existen caracteres no validos en tu archivo, en las coordenadas: {not_dna.span()}")
        return(0)
    else:
        return(1)

def find(dna, at=2):
    at_rich = re.findall("A+|T+",dna)
    at_regions = [islas for islas in at_rich if len(islas) >= at]
    print(at_regions)
            
go_on = evaluate(dna)

if go_on:
    if args.search:
        ans = find(dna,args.search)
    else:
        ans = find(dna)
        
''' 
Name 
    ARN to peptid and aminoacid percentage.
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que calcula el porcentaje de aminoacidos en una secuencia peptidica, dada una secuencia 
    de tripletes de ARN.
    
Category
    Aminoacid sequence
    
Usage
    Python src/ARNto_peptid.py -s ARNsequence [-a AMINOACIDS]
    Python src/ARNto_peptid.py -s AUG UCU CGU UCC UUA UUG CUU CGA UUU UUA UUG UUC UUG CUC CUA CUG CCU CCC CUG CCA -a M
Arguments

    -h --help
    -s --sequence
    -a --aminoacids 
    
See also
    None
'''

# Importando argparse 
# Importando aminoacids_module
# Asignando los argumentos que recibe el programa

import argparse
from aminoacids_module import traducction

arg_parser = argparse.ArgumentParser(description="Obtener el contenido de aminoacidos")
arg_parser.add_argument("-s", "--sequence",
                    help="sequence of ARN triplets separated by blank space",
                    type= str,
                    nargs= '+',
                    required=True)

arg_parser.add_argument("-a", "--aminoacids",
                    help="Aminoacidos a buscar",
                    type = str,
                    nargs = '+',
                    required=False) 
           
arguments = arg_parser.parse_args() 

# Definiendo la funcion que calcula el porcentaje de aminoacidos 
# Como default se calcula el porcentaje de aminoacidos hidrofilicos 
# Si el usuario da una lista de aminoacidos, el contenido de estos se calcula recorriendo la lista 
# La suma de los aminoacidos a buscar se guarda en una variable 
# Se obtiene el porcentaje de aminoacidos

def aminoacid_per(aminoacid_sequence, aminoacid_list = ['A','I','L','M','F','W','Y','V']):
    
    '''
    Returns the percentage of aminoacids in a sequence 
        Parameters:
            aminoacid_sequence (str): sequence of aminoacids given by the user 
            aminoacid_list (list): aminoacids to calculate the percentage, by default ['A','I','L','M','F','W','Y','V']
        
        Returns:
            percentage (float): aminoacids percentage 
    '''
    
    length = len(aminoacid_sequence)
    aminoacid_count = 0
    
    for i in range(0,len(aminoacid_list)):
        aminoacid_count += str(aminoacid_sequence).count(str(aminoacid_list[i]).upper())
        
    percentage = (aminoacid_count * 100)/ length
    
    return(percentage)
    
# Nos aseguramos de que la funcion devuelva los resultados correctos 
# Bloque try-except nos permite saber si algo ocurrio mal con la prueba de la funcion

try:
    assert aminoacid_per("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert aminoacid_per("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
    assert aminoacid_per("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    assert aminoacid_per("MSRSLLLRFLLFLLLLPPLP") == 65
    
except AssertionError as AssertionError:
    print("Algo salio mal :( \n")

# Obtenemos la secuencia de aminoacidos llamando a la funcion traducction del modulo: 
    
aminoacid_seq = traducction(arguments.sequence)

# Si el usuario da la lista de aminoacidos a buscar
# Se imprime un mensaje con el porcentaje obtenido 

if arguments.aminoacids:  
    total = aminoacid_per(aminoacid_sequence = aminoacid_seq, aminoacid_list = arguments.aminoacids)
    print(f"El porcentaje de los aminoacidos: {' '.join(arguments.aminoacids).upper()} en la secuencia {aminoacid_seq} es: {total} %")
    
# Si el usuario no da la lista de aminoacidos 
# Se imprime el contenido de aminoacidos hidrofilicos en la secuencia dada

else:
    total = aminoacid_per(aminoacid_sequence = aminoacid_seq)
    print(f"El porcentaje de los aminoacidos hidrofilicos: A, I, L, M, F, W, Y, V en la secuencia {aminoacid_seq} es: {total} %")

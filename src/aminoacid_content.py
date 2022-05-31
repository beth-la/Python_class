''' Name 
    Aminoacid content 
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que calcula el porcentaje de un aminoacido en una secuencia dada
    
Category
    Aminoacid sequence
    
Usage
    Python src/aminoacid_content.py -s sequence/aminoacids -a aminoacid
    
Arguments
    -h --help
    -s --sequence
    -a --aminoacid
    
See also
    None
    '''

# Importar argparse
# Asignar argumentos que recibira el programa

import argparse

arg_parser = argparse.ArgumentParser(description="Obtener el contenido de aminoacidos")
arg_parser.add_argument("-s", "--sequence",
                    help="sequence of aminoacids",
                    required=True)

arg_parser.add_argument("-a", "--aminoacid",
                    help="Aminoacido a buscar",
                    required=True) 
           
arguments = arg_parser.parse_args() 

# Definir funcion que obtiene el porcentaje del aminoacido en la secuencia 
# Se obtiene la longitud de la secuencia 
# Se obtiene el total de apariciones del aminoacido 
# Se calcula el porcentaje y se devuelve el valor

def aminoacid_per(aminoacid_sequence, aminoacid):
    
    '''
    Returns the percentage of aminoacids in a sequence 
        Parameters:
            aminoacid_sequence (str): sequence of aminoacids given by the user 
            aminoacid_list (str): aminoacid to calculate the percentage
        
        Returns:
            percentage (float): aminoacid percentage 
    '''
    
    sequence_length = len(aminoacid_sequence)
    percentage = (aminoacid_sequence.upper().count(aminoacid.upper()) * 100)/ sequence_length
    return(percentage)
    
# Assert nos permite evaluar nuestra funcion para saber que obtiene los resultados correctos 
# El bloque try-except nos dice si hubo un error al evaluar la funcion
    
try:
    assert aminoacid_per("MSRSLLLRFLLFLLLLPPLP", "M") == 5
    assert aminoacid_per("MSRSLLLRFLLFLLLLPPLP", "r") == 10
    assert aminoacid_per("msrslllrfllfllllpplp", "L") == 50
    assert aminoacid_per("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

except AssertionError as AssertionError:
    print("Algo salio mal :( \n")
    

# Se llama a la funcion y se imprimen los resultados para el usuario: 

total = aminoacid_per(arguments.sequence, arguments.aminoacid)
print(f"El porcentaje del aminoacido {str(arguments.aminoacid).upper()} en la secuencia es: {total}")

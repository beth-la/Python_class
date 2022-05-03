''' Name 
    Generador de archivo fasta
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que genera un archivo fasta apartir de un archivo que contiene una secuencia de ADN.
    
Category
    DNA sequence
    
Usage
    Python generador_fasta.py
        
Arguments
    None
    
See also
    None
    
'''

try:
    with open('data/dna.txt','r') as archivo:
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
    

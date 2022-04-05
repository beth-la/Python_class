''' Name 
    Generador de archivo fasta
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que genera un archivo fasta apartir de un archivo que contiene una secuencia de ADN 
    y su encabezado.
    
Category
    DNA sequence
    
Usage
    A partir de archivos que contengan una secuencia de ADN y su encabezado, podemos generar un archivo 
    con formato fasta.
    
Arguments
    None
    
See also
    None
    
'''

# Abrir el archivo con with open.
# La variable ADN guarda el contenido del archivo dna.txt

with open('data/dna.txt','r') as archivo:
    ADN= archivo.read()

# Creamos un nuevo archivo que tendra el formato fasta:
# Escribimos el encabezado y la secuencia.

my_file= open("data/dna.fasta","w")
my_file.write(">sequence_name \n")
my_file.write(ADN)
my_file.close()
    

''' Name 
    Fasta files program generator
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que dado un archivo en formato .txt con secuencias de ADN, las transforma en 
    archivos con formato fasta.
    
Category
    DNA sequence
    
Usage
    El programa nos permite generar archivos con formato fasta a partir de un primer archivo 
    que contiene las secuencias, el archivo dado puede sustituirse por otro siempre y cuando 
    cuenten con el mismo formato.
    
Arguments
    None
    
See also
    None
    
'''
# Abrir el archivo en donde se encuentran las secuencias.
# Guardar este contenido en una lista.
# Darle el formato deseado
# Insertar el caracter '>' y un salto de linea en la posicion 2

with open ('data/dna_sequences.txt','r') as archivo:
    secuencias= [line.split('\t') for line in archivo]    
for secuencia in secuencias:
    secuencia.insert(0,'>')
    secuencia.insert(2,'\n')

# Generar el archivo output 
# Escribir el contenido de la lista "secuencia" en el archivo 
# cerrar el archivo

my_file= open('data/secuencias.fasta','w')
for secuencia in secuencias:
    my_file.write(' '.join(secuencia))
my_file.close()
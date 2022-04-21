''' Name 
    fasta_files_program.py
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que dado un archivo en formato .txt con secuencias de ADN, las transforma en 
    archivos con formato fasta.
    
Category
    DNA sequence
    
Usage
    python fasta_files_program.py
    
Arguments
    None
    
See also
    None
    
'''
# Abrir el archivo en donde se encuentran las secuencias.
# Guardar este contenido en una lista.
# Darle el formato deseado
# Insertar el caracter '>' y un salto de linea en la posicion 2
# La secuencia de ADN queda en la posicion 3 de la lista, si esta tiene algun guion "-", susituirlo por cadena vacia ''
# Convertir las minusculas a mayusculas

with open('data/dna_sequences.txt', 'r') as archivo:
    secuencias = [line.split('\t') for line in archivo]
    # Te genera esto:
    # >> [['seq_1   ATCGTACGATCGATCGATCGCTAGACGTATCG\n'], ['seq_2   actgatcgacgatcgatcgatcacgact\n'], ['seq_3   ACTGAC-ACTGT-ACTGTA----CATGTG']]
    
    
    # secuencias = [line.split('   ') for line in archivo]
    
#secuencias[2][1] = secuencias[2][1].replace('-', '').upper()

for secuencia in secuencias:
    secuencia.insert(0, '>')
    secuencia.insert(2, '\n')

# Generar el archivo output
# Escribir el contenido de la lista "secuencia" en el archivo
# cerrar el archivo
my_file = open('data/secuencias.fasta', 'w')
for secuencia in secuencias:
    my_file.write(''.join(secuencia)) # Los strings vacios tambien existen
my_file.close()

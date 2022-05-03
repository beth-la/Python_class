''' Name 
    Fasta files program generator
    
Version
    2.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que dado un archivo en formato .txt con secuencias de ADN, las transforma en 
    archivos con formato fasta.
    
Category
    DNA sequence
    
Usage
    Python src/fasta_files_program.py
    
Arguments
    None
    
See also
    None
    
'''
# Abrir el archivo en donde se encuentran las secuencias.
# Guardar este contenido en una lista.
# Generar una lista que contendra las secuencias sin  guiones y en mayusculas 
# Las secuencias se encuentran a partir de la posicion 5 del string 

# Agregar try y except para notificar al usuario si el archivo no existe:

try:
    with open('data/dna_sequences.txt', 'r') as archivo:
        secuencias = [line for line in archivo]

except IOError as io_error: 
    print(f"El archivo {io_error.filename} no se encuentra. \n")
    
else:
    
    format_seq = [secuencia[5:].upper().replace('-','') for secuencia in secuencias]
    
# Generar el archivo output
# Escribir el encabezado de cada lista "> seq_" y con un contador generar los numeros.
# Escribir el contenido de la lista "format_seq" en el archivo
# cerrar el archivo

    my_file = open('results/secuencias.fasta', 'w')
    
    for i in range(0,len(format_seq)):
        my_file.write(" > seq_" + str(i+1) + "\n" + format_seq[i])
    my_file.close()

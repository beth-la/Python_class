# Name: Generador archivo fasta
# Version:
# Author: Lopez A. Brenda E.
# Descripcion: Programa que genera un archivo fasta a partir de un archivo de ADN.
# Category: 
# Usage:
# Arguments:
# See also:

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
    
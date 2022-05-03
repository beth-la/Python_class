''' Name 
    remove_adapters.py
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que elimina adaptadores de secuencias de ADN contenidas en un archivo.
    
Category
    DNA sequence
    
Usage
    Python src/generador_fasta.py

Arguments
    None
    
See also
    None
    
'''

# Abrir el archivo que contiene las secuencias deseadas
# Asignar las secuencias a una lista
# Agregamos estructura try-except para avisar al usuario si es que su archivo no se encuentra.

try:  
    with open('data/4_input_adapters.txt','r') as archivo:
        secuencias= [line for line in archivo]
        sin_adaptadores= []
        
except IOError as io_error: 
    print(f"El archivo {io_error.filename} no se encuentra. \n")
    
# Excluimos la parte de la secuencia que contiene a los adaptadores
# Estas nuevas secuencias las almacenamos en una lista nueva 

else:
    
    for i in range(0,len(secuencias)):
        sin_adaptadores.append(secuencias[i][14:])

# Abrimos un nuevo archivo que sera el output 
# Ecribimos la lista con las secuencias en el archivo 

    my_file= open('results/Sec_sin_adaptadores.txt','w')
    my_file.write('\n'.join(sin_adaptadores))
    my_file.close()




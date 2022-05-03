''' Name 
    remove_adapters.py
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que elimina adaptadores de secuencias de ADN contenidas en un archivo.
    
Category
    DNA sequence
    
Usage
    python remove_adapters.py
    
Arguments
    None
    
See also
    None
    
'''

# Abrir el archivo que contiene las secuencias deseadas
# Asignar las secuencias a una lista
with open('data/4_input_adapters.txt','r') as archivo:
    secuencias = [line for line in archivo]
    sin_adaptadores = []
    
# Excluimos la parte de la secuencia que contiene a los adaptadores
# Estas nuevas secuencias las almacenamos en una lista nueva 
for secuencia in secuencias:
    sin_adaptadores.append(secuencia[14:])
# Hasta podrias hacerlo en una comprehension
# sin_adaptadores = [secuencia[14:] for secuencia in secuencias]

# Abrimos un nuevo archivo que sera el output 
# Escribimos la lista con las secuencias en el archivo 
my_file= open('data/Sec_sin_adaptadores.txt','w')
my_file.write('\n'.join(sin_adaptadores))
my_file.close()

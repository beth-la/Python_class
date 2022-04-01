''' Name 
    Trimming.
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que elimina adaptadores de secuencias de ADN contenidas en un archivo.
    
Category
    DNA sequence
    
Usage
    El programa nos permite obtener las secuencias de ADN eliminando las secuencias 
    que corresponden a adaptadores.
    
Arguments
    None
    
See also
    None
    
'''

with open('data/4_input_adapters.txt','r') as archivo:
    secuencias= [line.split("\n") for line in archivo]
    sin_adaptadores= []
for i in range(0,len(secuencias)):
    sin_adaptadores.append(secuencias[i][0][14:])

my_file= open('data/Sec_sin_adaptadores.txt','w')
my_file.write('\n'.join(sin_adaptadores))
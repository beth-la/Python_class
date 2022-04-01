with open('data/4_input_adapters.txt','r') as archivo:
    secuencias= [line.split("\n") for line in archivo]
    sin_adaptadores= []
for i in range(0,len(secuencias)):
    sin_adaptadores.append(secuencias[i][0][14:])
print(sin_adaptadores)

my_file= open('data/Sec_sin_adaptadores.txt','w')
my_file.write('\n'.join(sin_adaptadores))
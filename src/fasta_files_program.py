with open ('data/dna_sequences.txt','r') as archivo:
    secuencias= [line.split('\t') for line in archivo]

for secuencia in secuencias:
    secuencia.insert(0,'>')
print(secuencias) 

my_file= open('data/secuencias.fasta','w')
for secuencia in secuencias:
    my_file.write(' '.join(secuencia))
my_file.close()
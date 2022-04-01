with open ('data/dna_sequences.txt','r') as archivo:
    secuencias= [line.split('\t') for line in archivo]
for i in range (0, len(secuencias)):
    secuencias[i][0] = '>'
    secuencias[i].append('\n')
my_file= open('data/secuencias.fasta','w')
my_file.write('\n'.join(secuencias))
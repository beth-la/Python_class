with open ('data/dna_sequences.txt','r') as archivo:
    secuencias= [line.split('\t') for line in archivo]
print(secuencias)